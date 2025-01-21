# Ecosystem Simulation

A Python-based ecosystem simulation featuring the interaction between grass, rabbits, and wolves. This simulation demonstrates basic predator-prey relationships and resource management in a controlled environment.

## Description

This program simulates a simple ecosystem with three main components:
- Grass (renewable resource)
- Rabbits (herbivores)
- Wolves (predators)

Each component follows specific rules for growth, reproduction, and survival, creating a dynamic ecosystem simulation.

## Parameters

### Grass
- Maximum capacity: 400 units
- Growth rate: 5 units per stage
- Food value: 10 units (when eaten by rabbits)

### Rabbits
- Maximum food capacity: 45 units
- Metabolism rate: 3 units/stage
- Reproduction age: 10 stages
- Reproduction probability: 50% (in suitable conditions)
- Minimum food for reproduction: 40 units
- Maximum age: 25 stages
- Food value: 10 units (when eaten by wolves)
- Survival without food: 3 stages

### Wolves
- Maximum food capacity: 200 units
- Metabolism rate: 2 units/stage (adjustable)
- Reproduction age: 10 stages
- Reproduction probability: 50% (in suitable conditions)
- Minimum food for reproduction: 120 units
- Maximum age: 50 stages
- Survival without food: 2 stages

## Initial State
- Grass: 400 blocks
- Rabbits: 20 units
- Wolves: 2 units (configurable)

## Features
- Stage-by-stage simulation
- Configurable wolf parameters (population, energy, metabolism rate)
- Detailed status display for each organism
- Interactive progression through stages
- Natural life cycles including reproduction and death
- Resource competition and predator-prey relationships

## How to Run

1. Ensure you have Python installed on your system
2. Run the simulation:
   ```
   python main.py
   ```
3. When prompted, configure the wolf parameters (or press Enter to use defaults):
   - Wolf population
   - Wolf energy
   - Wolf metabolism rate
4. Press Enter after each stage to progress through the simulation

## Simulation Rules

1. **Grass**
   - Grows by 5 units each stage
   - Cannot exceed maximum capacity of 400 units

2. **Rabbits**
   - Must eat to maintain energy
   - Can reproduce if conditions are met
   - Die if they reach maximum age or run out of food

3. **Wolves**
   - Hunt rabbits for food
   - Can reproduce if conditions are met
   - Die if they reach maximum age or run out of food

## Termination Condition
The simulation ends when both rabbit and wolf populations reach zero.

## Notes
- The simulation provides detailed information about each organism's status at every stage
- Parameters can be modified through the code to experiment with different ecosystem balances
- The randomized elements (reproduction, hunting success) create unique outcomes in each run

## Contributing
Feel free to fork this project and modify the parameters or add new features to explore different ecosystem dynamics.