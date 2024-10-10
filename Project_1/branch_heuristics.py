import operator
import random
from solver import SATSolver
from constants import TRUE, FALSE, UNASSIGN


class OrderedChoiceSolver(SATSolver):
    def select_decision_variable(self):
        var = random.choice(list(self.unassigned_vars()))
        # print(f"OrderedChoiceSolver picked variable: {var}")
        return var, random.sample([TRUE, FALSE], 1)[0]


class RandomChoiceSolver(SATSolver):
    def select_decision_variable(self):
        var = random.choice(list(self.unassigned_vars()))
        # print(f"RandomChoiceSolver picked variable: {var}")
        return var, random.sample([TRUE, FALSE], 1)[0]


class FrequentVarsFirstSolver(SATSolver):
    def preprocess(self):
        vs = {x: 0 for x in self.variables}
        for clause in self.clauses:
            for v in clause:
                vs[abs(v)] += 1
        self.vars_order_frequency = [
            t[0] for t in
            sorted(vs.items(), key=operator.itemgetter(1), reverse=True)]

    def select_decision_variable(self):
        var = next(filter(lambda v: self.assignments[v] == UNASSIGN, self.vars_order_frequency))
        # print(f"FrequentVarsFirstSolver picked variable: {var}")
        return var, random.sample([TRUE, FALSE], 1)[0]


class DynamicLargestIndividualSumSolver(SATSolver):
    def all_unresolved_clauses(self):
        return filter(lambda c: self.evaluate_clause(c) == UNASSIGN, self.clauses)

    def select_decision_variable(self):
        v_pos = {x: 0 for x in self.variables if self.assignments[x] == UNASSIGN}
        v_neg= {x: 0 for x in self.variables if self.assignments[x] == UNASSIGN}
        for clause in self.all_unresolved_clauses():
            for v in clause:
                try:
                    if v > 0:
                        v_pos[v] += 1
                    else:
                        v_neg[abs(v)] += 1
                except KeyError:
                    pass

        pos_count = max(v_pos.items(), key=operator.itemgetter(1))
        neg_count = max(v_neg.items(), key=operator.itemgetter(1))
        if pos_count[1] > neg_count[1]:
            # print(f"DynamicLargestIndividualSumSolver picked variable: {pos_count[0]}")
            return pos_count[0], TRUE
        else:
            # print(f"DynamicLargestIndividualSumSolver picked variable: {neg_count[0]}")
            return neg_count[0], FALSE


class JeroslowWangOneSidedSolver(SATSolver):
    def preprocess(self):
        self.jw_scores = {x: 0 for x in self.variables}
        for clause in self.clauses:
            for v in clause:
                self.jw_scores[abs(v)] += 2 ** -len(clause)

    def select_decision_variable(self):
        unassigned_vars = filter(lambda v: self.assignments[v] == UNASSIGN, self.variables)
        best_var = max(unassigned_vars, key=lambda v: self.jw_scores[v])
        # print(f"JeroslowWangOneSidedSolver picked variable: {best_var}")
        return best_var, random.sample([TRUE, FALSE], 1)[0]


class VSIDSSolver(SATSolver):
    def __init__(self, cnf):
        super().__init__(cnf)
        self.vsids_scores = {x: 0 for x in self.variables}
        self.decay_factor = 0.95

    def bump_variable(self, var):
        self.vsids_scores[var] += 1

    def decay_scores(self):
        for var in self.vsids_scores:
            self.vsids_scores[var] *= self.decay_factor

    def select_decision_variable(self):
        self.decay_scores()
        unassigned_vars = filter(lambda v: self.assignments[v] == UNASSIGN, self.variables)
        best_var = max(unassigned_vars, key=lambda v: self.vsids_scores[v])
        # print(f"VSIDSSolver picked variable: {best_var}")
        return best_var, random.sample([TRUE, FALSE], 1)[0]