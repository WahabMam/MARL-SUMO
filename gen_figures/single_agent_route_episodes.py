import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

# Load the data
data = pd.read_csv('C:\\Users\\nclab\\Desktop\\New Update\\sumo-marl\\output\\2023-04-20_11-18-42_veh0.csv')

# Extract the values of the "reward" and "number of episodes" columns
# reward = data['reward']
hops=data['hops']
episodes = data['episode']
# Define a custom color scheme
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

# Create the plot
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(episodes, hops, color=colors[0], linewidth=2,marker='o')
ax.set_xticks(np.arange(0,101,5))
# ax.set_yticks(np.arange(0,20,1))
# ax.tick_params(axis='y', labelspacing=5)
# ytick_labels = ax.get_yticklabels()
# for label in ytick_labels:
#     label.set_y(label.get_position()[1] - 50)

# plt.scatter(episodes,hops)
plt.grid(axis='both')
plt.tick_params(axis='x', rotation=45)

# Add a title and axis labels
ax.set_title('Route Length vs. Number of Episodes', fontsize=18)
ax.set_xlabel('Episodes', fontsize=14)
ax.set_ylabel('Route Length', fontsize=14)

# Customize the ticks and gridlines
ax.tick_params(axis='both', which='major', labelsize=12, length=6)
ax.tick_params(axis='both', which='minor', labelsize=10, length=4)
ax.grid(color='lightgray', linestyle='--')

# Add a legend
# ax.legend(['Reward'], fontsize=12, loc='upper left')

# Show the plot
plt.show()
