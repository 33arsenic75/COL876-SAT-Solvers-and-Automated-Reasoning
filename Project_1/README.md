# Project Setup and Usage Guide

## Setup Virtual Environment

1. **Create a virtual environment**:
    ```sh
    python3 -m venv venv
    ```

2. **Activate the virtual environment**:
    - On macOS and Linux:
        ```sh
        source venv/bin/activate
        ```
    - On Windows:
        ```sh
        .\venv\Scripts\activate
        ```

3. **Install the requirements**:
    ```sh
    pip install -r requirements.txt
    ```

## Benchmark Files

1. **Benchmark Files**:

The benchmark files are used to test the performance and accuracy of the solver. 

- **Test Cases**: The test cases are located in the `testcases` directory. Each file in this directory represents a different test case for the solver. The naming convention for the test files is as follows:
  - `3sat_r0.4_7.cnf`: Here, `r0.4` denotes the value of `r`, and `7` is the index number for a specific `r` value.
- **Results**: The results of the benchmarks are saved in the `benchmark_results.csv` file. 

2. **Benchmark Results Format**

The benchmark results are stored in a CSV file named `benchmark_results.csv`. Each row in the file represents the results of a benchmark test for a specific value of `r`. The columns in the file are as follows:

- **r**: The parameter value used in the benchmark test.
- **dynamic_time**: The time taken by the dynamic algorithm to complete the test.
- **jeroslow_time**: The time taken by the Jeroslow-Wang algorithm to complete the test.
- **dynamic_satisfiability**: The satisfiability result (SAT/UNSAT/TIMEOUT) of the dynamic algorithm.
- **jeroslow_satisfiability**: The satisfiability result (SAT/UNSAT/TIMEOUT) of the Jeroslow-Wang algorithm.
- **dynamic_decision**: The number of decisions made by the dynamic algorithm.
- **jeroslow_decision**: The number of decisions made by the Jeroslow-Wang algorithm.


## Using the Makefile

The Makefile contains several commands. Below are the available commands and their usage:

1. **Run the solver with default heuristics and filename**:
    ```sh
    make run
    ```
    This command will run the solver using the default heuristics (`JeroslowWangOneSidedSolver`) and filename (`input.cnf`).

2. **Run the solver with Dynamic Largest Individual Sum Solver heuristics**:
    ```sh
    make dynamic FILENAME=<your_input_file>
    ```
    Replace `<your_input_file>` with the path to your input file.

3. **Run the solver with Jeroslow Wang One Sided Solver heuristics**:
    ```sh
    make jeroslow FILENAME=<your_input_file>
    ```
    Replace `<your_input_file>` with the path to your input file.

4. **Clean the project**:
    ```sh
    make clean
    ```
    This command will remove temporary files and directories like `__pycache__`.

5. **Display help information**:
    ```sh
    make help
    ```
    This command will display usage information and examples.

