import os
import csv
from pysat.formula import CNF
from pysat.solvers import Solver
import re

def test_satisfiability(folder_path):
    with open('results.csv', mode='w', newline='') as csvfile:
        result_writer = csv.writer(csvfile)
        result_writer.writerow(['r', 'Satisfiability', 'Conflicts', 'Decisions', 'Propagations', 'Time'])
        for filename in sorted(os.listdir(folder_path)):
            if filename.endswith('.cnf'):
                file_path = os.path.join(folder_path, filename)
                formula = CNF(from_file=file_path)
                with Solver(name='g3', use_timer = True) as solver:
                    solver.append_formula(formula.clauses)
                    is_satisfiable = solver.solve()
                    data = solver.accum_stats()
                    conflicts = data['conflicts']
                    decisions = data['decisions']
                    propagations = data['propagations']
                    time_taken = '{0:.6f}'.format(solver.time())
                    # r = re.search(r'3sat_r(\d+\.\d+)_\d+\.cnf', filename)
                    r = re.search(r'3sat_r(\d+\.\d+)_\d+\.cnf', filename)
                    if r:
                        r_value = r.group(1)
                    else:
                        r_value = 'N/A'
                    result = 'SAT' if is_satisfiable else 'UNSAT'
                    result_writer.writerow([r_value, result, conflicts, decisions, propagations, time_taken])
                    print(f"Solved {filename}")

# Specify the folder containing the DIMACS files
folder_path = 'testcases'
test_satisfiability(folder_path)
