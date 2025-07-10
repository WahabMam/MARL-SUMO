Date : 26/04/2023

## Project Title: MultiVehiOpt: Multi-Agent Vehicle Routing Optimization.

**Project Objective:** The current scenario uses multiple agents to perform Q-learning in a SUMO environment for route optimization.

---

## Prerequisites (Software)

This repository uses **SUMO (Simulation of Urban Mobility)** version **1.14.1**, an open-source, highly portable, microscopic and continuous multi-modal traffic simulator, which can be downloaded from:

🔗 https://www.eclipse.org/sumo/

> ⚠️ Make sure to set the environment variable `SUMO_HOME` to the installed location of SUMO.

---

## Python Version Compatibility

✅ This project was tested using **Python 3.6**.

If your system uses a newer Python version (e.g., Python 3.12), we recommend creating a virtual environment using Python 3.6.

### To create a virtual environment using Python 3.6:

- **Windows:**
    ```bash
    py -3.6 -m venv venv-marl
    ```

- **Linux/macOS:**
    ```bash
    python3.6 -m venv venv-marl
    ```

---

## Steps to Run the Experiment

1. **Clone the repository**
    ```bash
    git clone https://github.com/nclabteam/sumo-marl.git
    ```

2. **Navigate to the project directory**
    ```bash
    cd sumo-marl
    ```

3. **Open the `config.yaml` file** and change the `server_ip` to your system’s IP address.  
   📌 *(See config.yaml details below)*

4. **Create a virtual environment**  
   - **Linux:**
     ```bash
     python -m venv venv-marl
     ```
   - **Windows:**
     ```bash
     virtualenv venv-marl
     ```

5. **Activate the virtual environment**  
   - **Linux:**
     ```bash
     source venv-marl/bin/activate
     ```
   - **Windows:**
     ```bash
     venv-marl\Scripts\activate
     ```

6. **Install dependencies**
    ```bash
    pip install -r req.txt
    ```

7. **Run the experiment**
   - **Linux:**
     ```bash
     ./run.sh
     ```
     > If permission is denied:
     ```bash
     sudo chmod +x ./run.sh
     ```
   - **Windows:**
     ```bash
     run.bat
     ```

8. **Results**
   - Output logs and CSVs are stored in the `output/` directory.
   - 📊 **Generated plots are saved in** `Results_Figures/`.

9. **To generate result plots**, use the scripts provided in the `gen_figures/` directory.

---

## Configuration Details: `config.yaml`

| Key | Description |
|-----|-------------|
| `Scenario` | Directory containing SUMO config and OSM map files |
| `cfg_file` | SUMO configuration file name |
| `net_file` | SUMO network file name |
| `det_file` | SUMO detector file name |
| `port` | Communication port |
| `server_ip` | IP of the SUMO server (edit as needed) |
| `total_episodes` | Total episodes to run |
| `start` | Whether to auto-start SUMO (`True`/`False`) |
| `quit_on_end` | Auto-quit SUMO on simulation end |
| `num_clients` | Number of SUMO clients (0 = single agent) |
| `use_gui` | Use SUMO GUI (`True`/`False`) |
| `endpoints` | List of valid simulation endpoints |
| `badpoints` | List of congested roads (negative reward) |
| `successend` | List of successful destination edges |
| `start_edges` | List of valid start edges (length = `num_clients`) |

---

## Batch File Explanation

`run.bat` (for Windows) is used to start the simulation with multiple agents.

- **`num_agents`**: Number of clients to start.
- The value is used in a loop to spawn the desired number of agents.

---

## Additional Utility

### Route Discovery

To find non-congested routes, use `find_all_routes.py`:

```bash
python find_all_routes.py --config config.yaml --start E19 --dest E20 --nr 10
