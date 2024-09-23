import argparse
import os
from solver import SATSolver
from branch_heuristics import OrderedChoiceSolver, RandomChoiceSolver, FrequentVarsFirstSolver, DynamicLargestIndividualSumSolver, JeroslowWangOneSidedSolver, VSIDSSolver
import csv
import pandas as pd
import time


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Choose heuristics and input file for SAT Solver.')
    parser.add_argument('--heuristics', type=str, required=True, help='Heuristics to use for the solver')
    parser.add_argument('--filename', type=str, required=True, help='Input file for the solver')
    args = parser.parse_args()

    heuristics = args.heuristics
    filename = args.filename

    if heuristics == 'OrderedChoiceSolver':
        solver = OrderedChoiceSolver(filename)
    elif heuristics == 'RandomChoiceSolver':
        solver = RandomChoiceSolver(filename)
    elif heuristics == 'FrequentVarsFirstSolver':
        solver = FrequentVarsFirstSolver(filename)
    elif heuristics == 'DynamicLargestIndividualSumSolver':
        solver = DynamicLargestIndividualSumSolver(filename)
    elif heuristics == 'JeroslowWangOneSidedSolver':
        solver = JeroslowWangOneSidedSolver(filename)
    elif heuristics == 'VSIDSSolver':
        solver = VSIDSSolver(filename)
    else:
        raise ValueError(f"Unknown heuristics: {heuristics}")

    answer = solver.execute()
    # print(answer)
    print(answer['satisfiable'])