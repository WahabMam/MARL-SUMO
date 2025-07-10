# MultiVehiOpt: Multi-Agent Vehicle Routing Optimization

**Date:** 26/04/2023

**Project Objective:** The current scenario uses multiple agents to perform Q-learning in a SUMO environment for route optimization.

---

## Prerequisites (Software)

This repository uses **SUMO (Simulation of Urban Mobility)** version **1.14.1**, an open-source, highly portable, microscopic and continuous multi-modal traffic simulator. Download it from: https://www.eclipse.org/sumo/.  
⚠️ Make sure to set the environment variable `SUMO_HOME` to your SUMO installation directory.

---

## Python Version Compatibility

✅ This project was tested using **Python 3.6**. If your system uses a newer Python version (e.g., Python 3.12), create a virtual environment with Python 3.6 by running `py -3.6 -m venv venv-marl` on Windows or `python3.6 -m venv venv-marl` on Linux/macOS.

---

## How to run the experiment:

Clone the repository by running `git clone https://github.com/nclabteam/sumo-marl.git` and navigate to the project directory with `cd sumo-marl`. Next, edit the `config.yaml` file and update the `server_ip` field with your system’s IP address. Then create and activate a virtual environment by running `python -m venv venv-marl` and `source venv-marl/bin/activate` on Linux/macOS, or by running `virtualenv venv-marl` and `venv-marl\Scripts\activate` on Windows. Install dependencies by running `pip install -r req.txt`. Finally, run the experiment by executing `./run.sh` on Linux/macOS (if permission is denied, first run `sudo chmod +x ./run.sh`), or run `run.bat` on Windows.

---

## Results and outputs

Output logs and CSV files are saved in the `output/` directory, while generated plots are saved in the `Results_Figures/` directory. To generate result plots, use the scripts inside the `gen_figures/` directory.

---

## Configuration (`config.yaml`) overview

| Key            | Description                             |
|----------------|---------------------------------------|
| `Scenario`     | Directory containing SUMO config and OSM map files |
| `cfg_file`     | SUMO configuration file name          |
| `net_file`     | SUMO network file name                 |
| `det_file`     | SUMO detector file name                |
| `port`         | Communication port                     |
| `server_ip`    | IP of the SUMO server (edit as needed)|
| `total_episodes` | Total episodes to run                 |
| `start`        | Whether to auto-start SUMO (`True`/`False`) |
| `quit_on_end`  | Auto-quit SUMO on simulation end      |
| `num_clients`  | Number of SUMO clients (0 = single agent) |
| `use_gui`      | Use SUMO GUI (`True`/`False`)         |
| `endpoints`    | List of valid simulation endpoints    |
| `badpoints`    | List of congested roads (negative reward) |
| `successend`   | List of successful destination edges  |
| `start_edges`  | List of valid start edges (length = `num_clients`) |

---

## Windows batch file (`run.bat`) usage

The batch file starts the simulation with multiple agents. Modify the `num_agents` variable to set how many clients to spawn.

---

## Additional utility: Route discovery

To find non-congested routes, run `python find_all_routes.py --config config.yaml --start E19 --dest E20 --nr 10`.
