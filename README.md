# Dynamic Epistemic Logic via Clue(Cluedo)

This package is my final project submission for COSI-112A-1 : Modal, Temporal, and Spatial Logic for Language at Brandeis University, fall 2025 semester.

---

## Features
- Command line arguments for number of players, number of simulations.
- Kripke model tracks accessibility relations for each agent from the actual world 
to possible worlds that the agent cannot distinguish between.
- Script outputs logs for Dynamic Epistemic Logic update tracing, optional argument
for whether accessibility relations should be recorded in log.

---
## Hopes & Dreams for the Future

- Ability to add any number of random characters, weapons, and rooms
- Returning animated visualizations of the Kripke model as the simulation progresses.
- Lying/bluffing mechanic that allows for more subtle knowledge updates
- LLM agents that play against each other??
- Potential capstone???
---
## Installation:

# Clone the repository
git clone https://github.com/travislitke/dynamic_epistemic_logic_Cluedo.git

---
## Operation 

Run the script from the project directory with the following command line statement:

$ python main.py -p <int,number of players> -r <int,number of simulations> -a <y/n, log accessibility relations>

