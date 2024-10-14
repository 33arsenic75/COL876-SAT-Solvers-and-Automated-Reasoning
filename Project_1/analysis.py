import os
import subprocess
import time
import csv
import re
from time import sleep
heuristics_list = [
    # 'dynamic',   
    # 'jeroslow',  
    'twoclause',
    'random',    
]
testcases_folder = 'testcases'
start_r = 4.2
start_n = 1
test_files = [f for f in os.listdir(testcases_folder) if f.endswith('.cnf')]
test_files.sort(reverse=True)

with open('benchmark_results.csv', mode='a', newline='') as csv_file:  # Change mode to 'a' for appending
    fieldnames = ['r', 'FileName'] + [f'{heuristic}_time' for heuristic in heuristics_list] + [f'{heuristic}_satisfiability' for heuristic in heuristics_list] + [f'{heuristic}_decision' for heuristic in heuristics_list]  # Added value to fieldnames
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    if csv_file.tell() == 0: 
        writer.writeheader() 
    for test_file in test_files:
        test_file_path = os.path.join(testcases_folder, test_file)
        r = re.search(r'3sat_r(\d+\.\d+)_(\d+)\.cnf', test_file)
        if r:
            r_value = float(r.group(1))
            n_value = int(r.group(2))
            # if r_value < start_r or (r_value == start_r and (n_value < start_n or n_value == 10)):
            #     continue
            if r_value < start_r or (n_value != 1):
                continue
        else:
            r_value = 'N/A'
        
        result_row = {'r': r_value}
        for heuristic in heuristics_list:
            print("Starting ", test_file_path, heuristic)
            start_time = time.time()
            try:
                result = subprocess.run(
                    ['make', '-s', heuristic, f'FILENAME={test_file_path}'],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    timeout=1200
                )
                end_time = time.time()
                time_taken = end_time - start_time
                output = result.stdout.decode('utf-8')
                satisfiability, value = output.split()
            except subprocess.TimeoutExpired:
                time_taken = 1800
                satisfiability = 'TIMEOUT'
                value = 'TIMEOUT'
            result_row['FileName'] = test_file
            result_row[f'{heuristic}_time'] = round(time_taken, 4)  # Corrected rounding method
            result_row[f'{heuristic}_satisfiability'] = satisfiability
            result_row[f'{heuristic}_decision'] = value  # Added value to result_row
        print("Done with ", test_file_path)
        writer.writerow(result_row)
        csv_file.flush()
        sleep(0.1)


print("Benchmarking completed. Results saved to benchmark_results.csv.")