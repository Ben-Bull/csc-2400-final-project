f# Algorithmic Optimization of The Farmer Was Replaced()
Group project for CSC2400 (Design of Algorithms)

### Project Overview
Briefly describe the computational problem, its inputs and outputs, and what makes
a solution optimal.
The problem we are trying to solve is how to most efficiently complete the game "The Farmer Was Replaced()" using a "Full Reset" run of the game. To summarize, the game gives you a shell to work with and you are tasked to completely code and automate a robot to harvest crops to upgrade itself and eventually win by unlocking a leaderboard node. Initially, this was an NP-hard problem, as there were way too many moving parts and most of us were not familiar with the game. Ultimately, our problem was simplified down to just the upgrade tree, which will be represented by a weighted undirected graph, with weights being dynamically adjusted based on prior upgrades.

An input looks like a set of valid upgrades in the tree. If an input skips a node, it is an invalid upgrade. There are fourteen required nodes and twenty optional nodes for completion, so an input is between lengths 14 and 34.

An output will look like the time it takes to complete the game using a predefined set of code within the game. An optimized solution will have the best possible time, and that will be found using our algorithms.

### In-Progress Documents
In-game Optimization Spreadsheet: https://docs.google.com/spreadsheets/d/1PI8f8Hs-sWApmiEnL6VNyektc-77cWffpSFwHtN0xAE/edit?usp=sharing

### Team Members
- Ben Bull:
- Jackson Phibbs:
- Caelum Pitts: 
- Hayden Queener: 

### Algorithms
Explain all three required algorithms:
1. **Brute Force:** How does it systematically explore possible solutions?
2. **Genetic Algorithm:** How are candidate solutions represented and evolved?
3. **A\*:** What algorithm did you choose, and how does it work on your
problem?

### Building and Running
List dependencies and exact commands necessary to compile and execute the project.
For example, for a C++ implementation:
```bash
g++ -std=c++17 src/brute_force/main.cpp -o brute_force
./brute_force
```
Your instructions must match your actual files and operating environment.

### Example Input and Output
Show at least one small example of a successful run.

### Experimental Results
Explain how algorithms are evaluated, and link to results in the repository. This
section may say *work in progress* during development, but must be completed by
final submission.

### Generative AI Statement:
Your `README.md` must include a statement on if and how generative AI models were
used within the project. It should list the model/company used, and the scope of
the assistance.