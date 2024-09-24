import itertools
import os  

def read_cnf_file(file_path):
    with open(file_path, 'r') as file:
        clauses = []
        for line in file:
            if line.startswith('p') or line.startswith('c'):
                continue
            clause = list(map(int, line.strip().split()))[:-1]
            clauses.append(clause)
    return clauses

def calculate_average_shared_literals(clauses):
    total_shared_literals = 0
    pair_count = 0

    for clause1, clause2 in itertools.combinations(clauses, 2):
        shared_literals = set(clause1).intersection(set(clause2))
        total_shared_literals += len(shared_literals)
        pair_count += 1

    if pair_count == 0:
        return 0

    return total_shared_literals / pair_count

if __name__ == "__main__":
    folder_path = 'testcases'
    total_files = len(os.listdir(folder_path))
    sum = 0
    for file_name in sorted(os.listdir(folder_path)):
        if file_name.endswith('.cnf'):
            file_path = os.path.join(folder_path, file_name)
            clauses = read_cnf_file(file_path)
            average_shared_literals = calculate_average_shared_literals(clauses)
            print(f"File: {file_name} : {average_shared_literals}")
            sum += average_shared_literals
    print(f"Average number of shared literals between pairs of clauses: {sum/total_files}")
