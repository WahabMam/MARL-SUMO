import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np 
import os

# Output directory
save_dir = "D:\\Sumo\\sumo-marl\\Results_Figures"
os.makedirs(save_dir, exist_ok=True)

# File paths
files = [
    "D:\\Sumo\\sumo-marl\\output\\2025-07-10_10-49-10_veh0.csv",
    "D:\\Sumo\\sumo-marl\\output\\2025-07-10_10-49-10_veh1.csv",
    "D:\\Sumo\\sumo-marl\\output\\2025-07-10_10-49-10_veh2.csv",
    "D:\\Sumo\\sumo-marl\\output\\2025-07-10_10-49-11_veh3.csv",
    "D:\\Sumo\\sumo-marl\\output\\2025-07-10_10-49-11_veh4.csv"
]

# Read hops
hops = []
for file in files:
    df = pd.read_csv(file)
    hops.append(df['hops'])

# Plot
colors = ['#1f77b4', "#1b1816", '#2ca02c', '#d62728', '#9467bd', '#8c564b']
array = [np.array(x) for x in hops]
avg_hops = [np.mean(k) for k in zip(*array)]

fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(avg_hops, color=colors[0], linewidth=2, marker='o')
ax.set_xticks(np.arange(0, 101, 5))
ax.set_title('Route Length vs. Number of Episodes', fontsize=15)
ax.set_xlabel('Episodes', fontsize=12)
ax.set_ylabel('Average Route Length', fontsize=12)

# Style
ax.tick_params(axis='both', which='major', labelsize=12, length=6)
ax.tick_params(axis='both', which='minor', labelsize=10, length=4)
ax.grid(color='lightgray', linestyle='--')

# Save
png_path = os.path.join(save_dir, "avg_route_length_plot.png")
pdf_path = os.path.join(save_dir, "avg_route_length_plot.pdf")
plt.savefig(png_path, dpi=300, bbox_inches='tight')
plt.savefig(pdf_path, dpi=300, bbox_inches='tight')

# Show

plt.show()
