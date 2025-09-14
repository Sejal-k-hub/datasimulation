import random
import pandas as pd
import matplotlib.pyplot as plt

# Parameters
N = 1000
days = 100
infection_prob = 0.05
recovery_time = 7

def run_simulation():
    # States: 0=Healthy, 1=Infected, 2=Recovered
    population = [0] * N
    population[0] = population[1] = 1
    infected_days = [0] * N
    results = []

    for day in range(1, days+1):
        new_infections = []
        for i in range(N):
            if population[i] == 1:
                for j in range(N):
                    if population[j] == 0 and random.random() < infection_prob:
                        new_infections.append(j)
                infected_days[i] += 1
                if infected_days[i] >= recovery_time:
                    population[i] = 2

        for j in new_infections:
            population[j] = 1
            infected_days[j] = 0

        results.append([
            day,
            population.count(0),
            population.count(1),
            population.count(2)
        ])

    df = pd.DataFrame(results, columns=["Day", "Healthy", "Infected", "Recovered"])
    df.to_csv("results/simulation_output.csv", index=False)
    return df

if __name__ == "__main__":
    df = run_simulation()
    print(df.head())
    df.plot(x="Day", y=["Healthy","Infected","Recovered"], figsize=(10,6))
    plt.xlabel("Day")
    plt.ylabel("Number of Individuals")
    plt.title("Disease Spread Simulation (SIR Model)")
    plt.legend()
    plt.savefig("results/plots.png")
    plt.show()
