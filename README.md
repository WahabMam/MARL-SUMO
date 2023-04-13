Date : 13/04/2023
MARL with Qlearning and Sumo.

Current scenario uses two agents to perform qlearn in an sumo environment.

### Steps to run the experiment
1. Clone the repository
```
git clone https://github.com/nclabteam/sumo-marl.git
```
2. Open the cloned repo in terminal
```
cd sumo-marl
```
3. Open the config.yaml file and change the server_ip to your systems ip address.

4. This exp is done using virtual env so create a virtual env using python as:
```
python -m venv venv-marl
```
5.  Activate the virtual env as in linux as:
``` 
source venv-marl/bin/activate
```
6. Install the required packages from req.txt
```
pip install req.txt
```
7. Run the 'run.sh' file :
```
./run.sh
```
if the bash file shows some permission denied error change the permissions as:

```
sudo chmod +x ./run.sh
```
8. The results generated can be seen in output dir.
