import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np 

files=["C:\\Users\\nclab\\Desktop\\New Update\\sumo-marl\\output\\2023-04-20_11-18-42_veh0.csv","C:\\Users\\nclab\\Desktop\\New Update\\sumo-marl\\output\\2023-04-20_11-18-42_veh1.csv",
       'C:\\Users\\nclab\\Desktop\\New Update\\sumo-marl\\output\\2023-04-20_11-18-42_veh2.csv','C:\\Users\\nclab\\Desktop\\New Update\\sumo-marl\\output\\2023-04-20_11-18-43_veh3.csv',
       'C:\\Users\\nclab\\Desktop\\New Update\\sumo-marl\\output\\2023-04-20_11-18-43_veh4.csv']
avg={}
rewards=[]
for file in files:
    df=pd.read_csv(file)
    reward=df['reward']
    rewards.append(reward)
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
array=[np.array(x) for x in rewards]
avg_hops=[np.mean(k) for k in zip(*array)]
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot( avg_hops, color=colors[0], linewidth=2,marker='o')
ax.set_xticks(np.arange(0,101,5))
# Add a title and axis labels
ax.set_title('Avg Reward vs. Number of Episodes', fontsize=15)
ax.set_xlabel('Episodes', fontsize=12)
ax.set_ylabel('Avg Reward', fontsize=12)

# Customize the ticks and gridlines
ax.tick_params(axis='both', which='major', labelsize=12, length=6)
ax.tick_params(axis='both', which='minor', labelsize=10, length=4)
ax.grid(color='lightgray', linestyle='--')

# Show the plot
plt.show()