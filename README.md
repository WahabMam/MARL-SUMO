Date : 26/04/2023

## Project Title: MultiVehiOpt: Multi-Agent Vehicle Routing Optimization.

**Project Objective:** Current scenario uses  multiple agents to perform q-learning in an SUMO environment for route optimization.

## Prerequisites (Software)
This repository uses SUMO (Simulation of Urban Mobility) version(1.14.1), an open source, highly portable, microscopic and continuous multi-modal traffic simulator, which can be downloaded from https://www.eclipse.org/sumo/ based on your operating system.

This repository requires an environment variable named `SUMO_HOME`, so, after installation ensure `SUMO_HOME` environemnt variable is set to the installed location of SUMO.

The experimentation is carried out using **python v3.6**
<!-- 
## We stronlgy recommend to create Virtual environment and then clone the repository as follow:
- **Linux:** Create a new virtual environment inside the project directory as ` python -m venv venv-marl` where venv-marl is the given name to the virtual environment.
- **Windows:** Create a new virtual env as `virtualenv venv-marl`. -->



### Steps to run the experiment
1. Clone the repository
    ```
    git clone https://github.com/nclabteam/sumo-marl.git
    ```
2. Open the cloned repo in terminal or if you have already have it
    ```
    cd sumo-marl
    ```
3. Open the config.yaml file and change the server_ip to your systems ip address. **(Description about config.yaml is given below)**

4. This exp is done using virtual env so create a virtual env using python as (for **linux** users):
    ```
    python -m venv venv-marl
    ```
- **Windows** users can create virtual env as
    ```
    virtualenv venv-marl
    ```
5.  Activate the virtual env as in **linux** as:
    ``` 
    source venv-marl/bin/activate
    ```
 - Activate the virtual env as in **Windows** as:
    ``` 
    venv-marl\Scripts\activate
    ```
6. Install the required packages from req.txt
    ```
    pip install -r req.txt
    ```
7. Run the 'run.sh' file (**linux** users) :
    ```
    ./run.sh
    ```
- if the bash file shows some permission denied error change the permissions as:

    ```
     sudo chmod +x ./run.sh
    ```
- Run the 'run.bat' file (**windows** users) :
    ```
    run.bat
    ```
8. The results generated can be seen in output dir.

9. For generating the figures, use the scripts provided inside `gen_figures` directory.


### Before running the experiment we need to make changes in 'config.yaml' and 'run.bat' file as per our need.

### Desciption about `config.yaml` file:
- **Scenario** : It’s the directory where our sumo configuration and OSM map files are located.
- **cfg_file**: Specifies the name of the SUMO configuration file.
- **net_file**: Specifies the name of the SUMO network file.
- **det_file**: Specifies the name of the SUMO detector file.
- **port**: Specifies the port number to be used for communication with the 
- **server_ip**: Specifies the IP address of the SUMO server( change as per your need).
- **total_episodes**: Specifies the total number of episodes to run( change as per your need)
- **start**: Specifies whether to start the SUMO simulation (True/False) if you chose ‘True’ then you don’t need to manually start the simulation otherwise you need.
- **quit_on_end**: Specifies whether to quit the SUMO simulation automatically when it ends (True/False).
- **num_clients**: Specifies the number of SUMO clients to be used (0 for one agent, or number of desired clients for multiple agents).
- **use_gui**: Specifies whether to use the SUMO GUI for visualization (True/False).
- **endpoints**: Specifies the list of valid endpoints for the simulation.
- **badpoints**: Specifies the list of edges which are congested and for which we have a negative reward.
- **successend**: Specifies the list of successful endpoint for the simulation which has highest positive reward.
- **start_edges**: Specifies the list of valid start edges for the simulation, where the length of start_edges should be equal to ‘num_clients’.
## Description about 'run.bat' and 'run.sh' file:
“run.bat” file is a batch file used to run the Python script `agent.py` with specific configurations.
- **num_agents** variable is used to specify the number of agents to be started by the batch file (0 for one agent, or number of desired clients for multiple agents).
num_agents variable is used in the loop structure to determine the number of iterations.

# Additional Files:
For generating the figures, use the scripts provided inside `gen_figures` directory.

`find_all_routes.py` file is used to calculate all the possible non congested routes from start to destination.
We only need to specify start point, dest point and number of routes that we want to be printed.
This file can be used as

```
python find_all_routes.py --config config.yaml --start E19 --dest E20 --nr 10
```
Where: 
```
--start // start edge
--dest // destination edge
--nr // number of routes to be printed
--nr : remove if we want to print all possible routes whithout facing congested roads
```






