HEURISTICS ?= JeroslowWangOneSidedSolver
FILENAME ?= input.cnf
.SILENT:

run:
	python3 main.py --heuristics $(HEURISTICS) --filename $(FILENAME)

dynamic:
	make run HEURISTICS=DynamicLargestIndividualSumSolver FILENAME=$(FILENAME)

jeroslow:
	make run HEURISTICS=JeroslowWangOneSidedSolver FILENAME=$(FILENAME)

clean:
	rm -f *.pyc
	rm -rf __pycache__

help:
	@echo "Usage:"
	@echo "  make <heuristic> FILENAME=<filename>"
	@echo "Heuristic shortcuts:"
	@echo "  dynamic  - DynamicLargestIndividualSumSolver"
	@echo "  jeroslow - JeroslowWangOneSidedSolver"
	@echo "Example:"
	@echo "  make random FILENAME=test.cnf"
