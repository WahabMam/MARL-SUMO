@echo on
set num_agents=4
FOR /l %%i IN (0,1,%num_agents%) DO (
    echo Starting Agent : %%i
    start python agent.py --config="config.yaml" --vehicle=%%i
)