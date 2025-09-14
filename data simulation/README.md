# Disease Spread Simulation (SIR Model)

This project simulates the spread of a disease in a population using a simple SIR (Susceptible-Infected-Recovered) model.

## Files

- `simulation.py`: Main script that runs the simulation, saves results, and generates plots.
- `requirements.txt`: Lists required Python packages (`pandas`, `matplotlib`).
- `results/simulation_output.csv`: Output CSV file with daily counts of healthy, infected, and recovered individuals.
- `results/plots.png`: Line plot showing the simulation results over time.

## How to Run

1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
2. Run the simulation:
   ```sh
   python simulation.py
   ```
   (or use `py -3 simulation.py` on Windows)

## Output

- The simulation results are saved to `results/simulation_output.csv`.
- A plot of the simulation is saved as `results/plots.png`.

## Example Output

| Day | Healthy | Infected | Recovered |
|-----|---------|----------|-----------|
| 1   |   920   |    80    |     0     |
| 2   |    15   |   985    |     0     |
| 3   |     0   |  1000    |     0     |

## Notes
- The simulation parameters (population size, infection probability, etc.) can be adjusted in `simulation.py`.
- The simulation uses Python's built-in `random` module (no installation needed).
