import os
import subprocess
import time
import csv

# Define the heuristics to test
heuristics_list = [
    'ordered',
    'random',
    'frequent',
    'dynamic',
    'jeroslow',
    'vsids'
]

# Define the test cases folder
testcases_folder = 'testcases'

# Get all test files in the testcases folder
test_files = [f for f in os.listdir(testcases_folder) if f.endswith('.cnf')]
test_files.sort()

# Create a CSV file to store the results
with open('benchmark_results.csv', mode='w', newline='') as csv_file:
    fieldnames = ['test_file'] + [f'{heuristic}_time' for heuristic in heuristics_list] + [f'{heuristic}_satisfiability' for heuristic in heuristics_list]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    # Iterate over each test file
    for test_file in test_files:
        test_file_path = os.path.join(testcases_folder, test_file)
        result_row = {'test_file': test_file}
        # Iterate over each heuristic
        for heuristic in heuristics_list:
            print("Starting ", test_file_path, heuristic)
            start_time = time.time()
            try:
                # Run the make command with a timeout of 120 seconds
                result = subprocess.run(
                    ['make', heuristic, f'FILENAME={test_file_path}'],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    timeout=120
                )
                end_time = time.time()
                time_taken = end_time - start_time

                # Check the output for satisfiability result
                output = result.stdout.decode('utf-8')
                satisfiability = output if 'TIMEOUT' not in output else 'UNKNOWN'

            except subprocess.TimeoutExpired:
                time_taken = 120
                satisfiability = 'TIMEOUT'

            # Store the result in the row
            result_row[f'{heuristic}_time'] = time_taken
            result_row[f'{heuristic}_satisfiability'] = satisfiability

        # Write the result row to the CSV file
        print("Done with ", test_file_path)
        writer.writerow(result_row)
        csv_file.flush()


print("Benchmarking completed. Results saved to benchmark_results.csv.")
