import numpy as np
import matplotlib.pyplot as plt
#set the basic variable
N = 10000
S = 9999
I = 1
R = 0
time = 1000
#establish the arrays
S_history = [S]
R_history = [R]
I_history = [I]
#caculate the number of SIR
for i in range(time) :
    #num of I
    Infect_probility = 0.3 * (I/N)
    new_infections = np.random.choice(range(2), S,p=[1-Infect_probility,Infect_probility])
    sum_new_infections = np.sum(new_infections)
    #num of R
    Recover_probility = 0.05
    new_recoveries = np.random.choice(range(2), I, p=[1-Recover_probility, Recover_probility])
    sum_new_recoveies = np.sum(new_recoveries)
    #show the new SIR
    S =S - sum_new_infections
    I=I + sum_new_infections - sum_new_recoveies
    R = R + sum_new_recoveies
    #add it to the arrays
    S_history.append(S)
    R_history.append(R)
    I_history.append(I)
#show the figure
plt.figure(figsize=(6,4), dpi=150)
plt.plot(S_history,label="Susceptible")
plt.plot(R_history,label="Recovered")    
plt.plot(I_history,label="Infected")
plt.xlabel('Time')
plt.ylabel('Number of People')
plt.title('SIR Model') 
plt.legend()
plt.show()   
