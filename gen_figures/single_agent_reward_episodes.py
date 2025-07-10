import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Create save directory
save_dir = "D:\\Sumo\\sumo-marl\\Results_Figures"
os.makedirs(save_dir, exist_ok=True)

# Load the data
data = pd.read_csv("D:\\Sumo\\sumo-marl\\output\\2025-07-10_10-49-10_veh0.csv")
episodes = data['episode']
rewards = data['reward']

# Color
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

# Plotting
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(episodes, rewards, color=colors[0], linewidth=2, marker='o')
ax.set_xticks(np.arange(0, 101, 5))
ax.set_title('Reward vs. Number of Episodes', fontsize=18)
ax.set_xlabel('Episodes', fontsize=12)
ax.set_ylabel('Reward', fontsize=12)

# Ticks & grid
ax.tick_params(axis='both', which='major', labelsize=10, length=6)
ax.tick_params(axis='both', which='minor', labelsize=10, length=4)
ax.grid(color='lightgray', linestyle='--')

# Save
png_path = os.path.join(save_dir, "reward_single_agent_plot.png")
pdf_path = os.path.join(save_dir, "reward_single_agent_plot.pdf")
plt.savefig(png_path, dpi=300, bbox_inches='tight')
plt.savefig(pdf_path, dpi=300, bbox_inches='tight')

# Show
plt.show()
