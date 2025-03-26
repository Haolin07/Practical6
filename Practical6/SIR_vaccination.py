import numpy as np
import matplotlib.pyplot as plt

vaccination_percentages = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
beta = 0.3
gamma = 0.05
total_population = 10000
time_steps = 1000

plt.figure(figsize=(10, 6), dpi=150)

for vp in vaccination_percentages:
    vaccinated = int(total_population * vp)
    S = total_population - vaccinated - 1  
    I = 1
    R = vaccinated  
    
    I_history = [I] 
    
    for _ in range(time_steps):
        if S <= 0 or I <= 0:
            I_history.append(0)
            continue
        
        infection_prob = beta * (I / (S + I + R))  
        new_infections = np.random.binomial(S, infection_prob)
        
        new_recoveries = np.random.binomial(I, gamma)
        
        S = max(S - new_infections, 0)
        I = max(I + new_infections - new_recoveries, 0)
        R += new_recoveries
        
        I_history.append(I)
    
    plt.plot(I_history, label=f"{vp*100:.0f}% Vaccinated")

plt.xlabel("Time")
plt.ylabel("Number of Infected People")
plt.title("SIR Model with Vaccination")
plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")  
plt.tight_layout()
plt.show()