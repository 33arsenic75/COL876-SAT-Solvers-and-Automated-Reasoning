# Makefile for running the SAT Solver with specified heuristics and input file

# Default values for the arguments
HEURISTICS ?= OrderedChoiceSolver
FILENAME ?= input.cnf
.SILENT:
# Target to run the SAT Solver with specified heuristics and input file
run:
	python3 main.py --heuristics $(HEURISTICS) --filename $(FILENAME)

# Shortcuts for different heuristics
ordered:
	make run HEURISTICS=OrderedChoiceSolver FILENAME=$(FILENAME)

random:
	make run HEURISTICS=RandomChoiceSolver FILENAME=$(FILENAME)

frequent:
	make run HEURISTICS=FrequentVarsFirstSolver FILENAME=$(FILENAME)

dynamic:
	make run HEURISTICS=DynamicLargestIndividualSumSolver FILENAME=$(FILENAME)

jeroslow:
	make run HEURISTICS=JeroslowWangOneSidedSolver FILENAME=$(FILENAME)

vsids:
	make run HEURISTICS=VSIDSSolver FILENAME=$(FILENAME)


clean:
	rm -f *.pyc
	rm -rf __pycache__

help:
	@echo "Usage:"
	@echo "  make <heuristic> FILENAME=<filename>"
	@echo "Heuristic shortcuts:"
	@echo "  ordered  - OrderedChoiceSolver"
	@echo "  random   - RandomChoiceSolver"
	@echo "  frequent - FrequentVarsFirstSolver"
	@echo "  dynamic  - DynamicLargestIndividualSumSolver"
	@echo "  jeroslow - JeroslowWangOneSidedSolver"
	@echo "  vsids    - VSIDSSolver"
	@echo "Example:"
	@echo "  make random FILENAME=test.cnf"
