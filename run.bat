@echo on
set num_agents=5
FOR /L %%i IN (1,1,%num_agents%) DO (
    echo Starting Agent : %%i
    start python agent.py --config="config.yaml" --vehicle=%%i
)