import os
import time
from collections import deque
TRUE = 1
FALSE = 0
UNASSIGN = -1



class SATSolver:
    def __init__(self, file_path):
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"No such file or directory: '{file_path}'")
        self.file_path = file_path
        self.clauses, self.variables = self.parse_cnf(file_path)
        self.learned_clauses = set()
        self.assignments = {var: UNASSIGN for var in self.variables}
        self.decision_level = 0
        self.implication_graph = {var: ImplicationNode(var, UNASSIGN) for var in self.variables}
        self.decision_vars = set()
        self.decision_history = {}
        self.propagation_history = {}
        self.decision_count = 0
    
    def execute(self):
        start_time = time.time()
        is_satisfiable = self.solve()
        elapsed_time = time.time() - start_time
        result = self.format_output(is_satisfiable, elapsed_time)
        return {
            'satisfiable': "SAT" if is_satisfiable else "UNSAT",
            'time': elapsed_time,
            'assignment': result,
            'decisions': self.decision_count
        }

    def format_output(self, is_satisfiable, elapsed_time):
        output = {}
        output['file'] = self.file_path
        output['satisfiable'] = "SAT" if is_satisfiable else "UNSAT"
        output['time'] = elapsed_time
        output['decisions'] = self.decision_count
        output['assignment'] = ' '.join(['{}{}'.format('' if val == 1 else '-', var)
                                      for var, val in self.assignments.items()])
        return output

    def preprocess(self):
        """ Preprocessing steps before solving """
        pass

    def solve(self):
        """
        Determines if the CNF is satisfiable.
        :return: True if SAT, False if UNSAT
        """
        self.preprocess()
        while not self.all_vars_assigned():
            conflict_clause = self.unit_propagation()
            if conflict_clause is not None:
                # Conflict detected during unit propagation
                backtrack_level, learned_clause = self.analyze_conflict(conflict_clause)
                if backtrack_level < 0:
                    return False
                self.learned_clauses.add(learned_clause)
                self.backtrack(backtrack_level)
                self.decision_level = backtrack_level
            elif self.all_vars_assigned():
                break
            else:
                # Decision making
                self.decision_level += 1
                self.decision_count += 1
                decision_var, decision_val = self.select_decision_variable()
                self.assignments[decision_var] = decision_val
                self.decision_vars.add(decision_var)
                self.decision_history[self.decision_level] = decision_var
                self.propagation_history[self.decision_level] = deque()
                self.update_implication_graph(decision_var)
        return True

    def pick_branching_variable(self):
        """
        Selects the first unassigned variable in the natural order.
        :return: variable, assigned value
        """
        for var in self.variables:
            if self.assignments[var] == UNASSIGN:
                return var, TRUE
                
    def parse_cnf(self, file_path):
        """
        Parses a DIMACS CNF file, returns clauses and literals.
        :param file_path: the file path
        :raises OSError: if file format is incorrect
        :returns: (clauses, literals)
        """
        with open(file_path) as file:
            lines = [
                line.strip().split() for line in file.readlines()
                if not (line.startswith('c') or line.startswith('%') or line.startswith('0')) and line != '\n'
            ]

        if lines[0][:2] == ['p', 'cnf']:
            num_literals, num_clauses = map(int, lines[0][-2:])
        else:
            raise OSError('Invalid CNF file format.')

        literals = set()
        clauses = set()
        for line in lines[1:]:
            if line[-1] != '0':
                raise OSError('Each clause line must end with 0.')
            clause = frozenset(map(int, line[:-1]))
            literals.update(map(abs, clause))
            clauses.add(clause)

        return clauses, literals

    def evaluate_literal(self, literal):
        value = self.assignments[abs(literal)]
        return value if value == UNASSIGN else value ^ (literal < 0)

    def evaluate_clause(self, clause):
        if not clause:
            return TRUE
        values = list(map(self.evaluate_literal, clause))
        return UNASSIGN if UNASSIGN in values else max(values)

    def evaluate_cnf(self):
        return min(map(self.evaluate_clause, self.clauses))

    def is_unit_clause(self, clause):
        values = []
        unassigned_literal = None

        for literal in clause:
            value = self.evaluate_literal(literal)
            values.append(value)
            unassigned_literal = literal if value == UNASSIGN else unassigned_literal

        is_unit = ((values.count(FALSE) == len(clause) - 1 and values.count(UNASSIGN) == 1) or
                   (len(clause) == 1 and values.count(UNASSIGN) == 1))
        return is_unit, unassigned_literal

    def update_implication_graph(self, var, clause=None):
        node = self.implication_graph[var]
        node.value = self.assignments[var]
        node.level = self.decision_level

        if clause:
            for v in [abs(lit) for lit in clause if abs(lit) != var]:
                node.parents.append(self.implication_graph[v])
                self.implication_graph[v].children.append(node)
            node.clause = clause

    def unit_propagation(self):
        while True:
            propagation_queue = deque()
            for clause in self.clauses.union(self.learned_clauses):
                clause_value = self.evaluate_clause(clause)
                if clause_value == TRUE:
                    continue
                if clause_value == FALSE:
                    return clause
                else:
                    is_unit, unit_literal = self.is_unit_clause(clause)
                    if not is_unit:
                        continue
                    propagation_pair = (unit_literal, clause)
                    if propagation_pair not in propagation_queue:
                        propagation_queue.append(propagation_pair)
            if not propagation_queue:
                return None

            for prop_literal, clause in propagation_queue:
                prop_var = abs(prop_literal)
                self.assignments[prop_var] = TRUE if prop_literal > 0 else FALSE
                self.update_implication_graph(prop_var, clause=clause)
                try:
                    self.propagation_history[self.decision_level].append(prop_literal)
                except KeyError:
                    pass  # propagated at level 0

    def get_unit_clauses(self):
        return list(filter(lambda x: x[0], map(self.is_unit_clause, self.clauses)))

    def all_vars_assigned(self):
        return all(var in self.assignments for var in self.variables) and \
               not any(var for var in self.variables if self.assignments[var] == UNASSIGN)

    def unassigned_vars(self):
        return filter(lambda v: v in self.assignments and self.assignments[v] == UNASSIGN, self.variables)
            
    def select_decision_variable(self):
        var = next(self.unassigned_vars())
        return var, TRUE

    def analyze_conflict(self, conflict_clause):
        def latest_assigned_var(clause):
            for var in reversed(assign_history):
                if var in clause or -var in clause:
                    return var, [x for x in clause if abs(x) != abs(var)]

        if self.decision_level == 0:
            return -1, None

        assign_history = [self.decision_history[self.decision_level]] + list(self.propagation_history[self.decision_level])

        pool_literals = conflict_clause
        processed_literals = set()
        current_level_literals = set()
        previous_level_literals = set()
        while True:
            for lit in pool_literals:
                if self.implication_graph[abs(lit)].level == self.decision_level:
                    current_level_literals.add(lit)
                else:
                    previous_level_literals.add(lit)

            if len(current_level_literals) == 1:
                break

            last_assigned, others = latest_assigned_var(current_level_literals)

            processed_literals.add(abs(last_assigned))
            current_level_literals = set(others)

            pool_clause = self.implication_graph[abs(last_assigned)].clause
            pool_literals = [l for l in pool_clause if abs(l) not in processed_literals] if pool_clause else []
        
        learned_clause = frozenset(current_level_literals.union(previous_level_literals))
        backtrack_level = max([self.implication_graph[abs(x)].level for x in previous_level_literals]) if previous_level_literals else self.decision_level - 1

        return backtrack_level, learned_clause
    
    def backtrack(self, level):
        for var, node in self.implication_graph.items():
            if node.level <= level:
                node.children[:] = [child for child in node.children if child.level <= level]
            else:
                node.value = UNASSIGN
                node.level = -1
                node.parents = []
                node.children = []
                node.clause = None
                self.assignments[node.variable] = UNASSIGN

        self.decision_vars = {var for var in self.variables if self.assignments[var] != UNASSIGN and not self.implication_graph[var].parents}

        for k in list(self.propagation_history.keys()):
            if k > level:
                del self.decision_history[k]
                del self.propagation_history[k]

class ImplicationNode:
    def __init__(self, variable, value):
        self.variable = variable
        self.value = value
        self.level = -1
        self.parents = []
        self.children = []
        self.clause = None

    def all_parents(self):
        parents = set(self.parents)
        for parent in self.parents:
            parents.update(parent.all_parents())
        return list(parents)

