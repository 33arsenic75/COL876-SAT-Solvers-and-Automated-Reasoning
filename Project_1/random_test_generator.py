import random
import math
import os
import subprocess

def generate_3sat_instance(N, L):
    clauses = []
    for _ in range(L):
        clause = []
        while len(clause) < 3:
            literal = random.randint(1, N)
            if literal not in clause and -literal not in clause:
                if random.random() < 0.5:
                    literal = -literal
                clause.append(literal)
        clauses.append(clause)
    return clauses

def write_dimacs(clauses, N, filename):
    with open(filename, 'w') as f:
        f.write(f"p cnf {N} {len(clauses)}\n")
        for clause in clauses:
            f.write(" ".join(map(str, clause)) + " 0\n")


def main():
    N = 150
    r_values = [i * 0.2 for i in range(1, 31)]
    os.makedirs('testcases', exist_ok=True)
    for r in r_values:
        L = math.ceil(r * N)
        for i in range(10):  
            clauses = generate_3sat_instance(N, L)
            filename = f"testcases/3sat_r{r:.1f}_{i}.cnf"
            write_dimacs(clauses, N, filename)

if __name__ == "__main__":
    main()