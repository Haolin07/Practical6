import numpy as np
import matplotlib.pyplot as plt

# set variables
beta = 0.3    
gamma = 0.05  
size = 100    
timesteps = 100  

# set the net
population = np.zeros((size, size), dtype=int)
#choice first point
outbreak = np.random.choice(size, 2)
population[outbreak[0], outbreak[1]] = 1


plt.figure(figsize=(6, 4), dpi=150)

for t in range(timesteps):
    #find infected
    infected = np.where(population == 1)
    rows, cols = infected[0], infected[1]
    
    new_infections = []
    for i in range(len(rows)):
        r, c = rows[i], cols[i]
        #exam their surrounding
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue  # 跳过自身
                nr, nc = r+dr, c+dc
                if 0 <= nr < size and 0 <= nc < size:
                    if population[nr, nc] == 0 and np.random.rand() < beta:
                        new_infections.append((nr, nc))
    
    for (r, c) in new_infections:
        population[r, c] = 1
    
    # recover
    recovery_mask = np.random.rand(len(rows)) < gamma
    population[rows[recovery_mask], cols[recovery_mask]] = 2
    
    # draw the picture
    plt.clf()
    plt.imshow(population, cmap='viridis', vmin=0, vmax=2, interpolation='nearest')
    plt.title(f'Time Step {t+1} | Infected: {len(rows)}')
    plt.colorbar(ticks=[0, 1, 2], label='State (0:S, 1:I, 2:R)')
    plt.pause(0.1)

plt.show()