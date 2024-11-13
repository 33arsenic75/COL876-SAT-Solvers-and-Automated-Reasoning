# COL-876: SAT Solvers and Automated Reasoning

This repository contains resources, notes, and solutions for **COL-876: SAT Solvers and Boolean Encodings**, a course taught by Dr. Priyanka Golia at IITD. The course provides an in-depth look into SAT solving, Boolean satisfiability problems, and encoding techniques and Applications of SAT Solver used to represent various computational problems as SAT instances.

## Course Overview

**Instructor:** Dr. Priyanka Golia  
**Institute:** Indian Institute of Technology Delhi (IITD)  
**Course Topics:** The course centers on SAT solvers, Boolean encodings, satisfiability problems, and strategies for effective SAT formulation and solving.
**Course Webpage:** https://priyanka-golia.github.io/COL-876/index.html

## Course Structure

### 1. Lectures
   - Topics covered include:
     - **Basic Introduction to Course**
     - **Basic Introduction to Propositional Logic and CNF**
     - **CNF Encodings (part 1)**
     - **CNF Encodings (part 2)**
     - **CNF Encodings (part 3)**
     - **SAT Solving DP (part 1)**
     - **SAT Solving DPLL (part 1)**
     - **SAT Solving CDCL (part 2)**
     - **SAT Solving CDCL (part 3)**
     - **SAT Solving Heuristics**
     - **UNSATcore**
     - **MaxSAT**
     - **Model Counting**
     - **QBF**


### 2. Project 1
   - **Objective**: Design a SAT solver to check the satisfiability of CNF formulas, with inputs in DIMACS format. The solver should output "UNSAT" if the formula is unsatisfiable, otherwise output a satisfying assignment.
   - **CDCL Procedure**: Implement a solver based on the Conflict-Driven Clause Learning (CDCL) procedure. Develop heuristics for:
     - **PickBranchingVariable**: Choose branching variables and truth values using custom heuristics. Compare your approach to both random choice and 2-clause heuristics.
     - **ConflictAnalysis**: Implement a more advanced heuristic than the basic conflict analysis covered in class.
   - **Testing**: Evaluate your solver using randomly generated 3-SAT formulas with various parameters for variables and clauses. Use CryptoMiniSAT to confirm satisfiability of test formulas and analyze performance.
   - **Submission Requirements**:
     - Source code, CNF formulas, and a report of findings, including:
       - Analysis of solver performance
       - Plots of compute time vs. varying formula parameters

### 3. Project 2
   - **Objective**: Apply course concepts to a complex, real-world problem using SAT solvers.
   - **Paper Presentation**: As part of this project, each student was required to present a paper on an application of SAT solvers in class, exploring real-world uses and highlighting innovative applications.

## Repository Contents

- **`COL876_Minor.pdf`**: Minor Exam Paper.
- **`COL876_Project1.pdf`**: Graded Copy for Project 1.
- **`COL876_Project2.pdf`**: Graded Copy for Project 2.
- **`COL876_Quiz1.pdf`**: Quiz 1 paper for the course.
- **`COL876_Quiz1_Paper.pdf`**: Quiz 1 solution paper or reference.
- **`COL876_Quiz2.pdf`**: Quiz 2 paper for the course.
- **`Project_1/`**: Code, DIMACS format files, and report for Project 1.
- **`Project_2/`**: Code, report, and presentation materials for Project 2.
- **`Slides/`**: Lecture slides and additional presentation materials.
