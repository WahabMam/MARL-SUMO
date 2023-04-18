import argparse
from utils import *
import os, sys

from rl.env.single_env import qlEnv
from rl.qlearning.qlagent import qlAgent


def ql_run(sumoBinary, traci, logger, total_episodes, net, det, sumocfg, alldets,edgelists,dict_connection,veh,endpoints,badpoints,config,file_path): 
    env = qlEnv(sumoBinary=sumoBinary,traci = traci,logger= logger,net_file=net,det_file=det,cfg_file=sumocfg,alldets=alldets,edgelists=edgelists,
                dict_connection=dict_connection,veh=veh,endpoint=endpoints,config = config)
    agent = qlAgent(id=veh, edgelists= edgelists, dict_connection = dict_connection)
    qtable = agent.set_qtable()
    cntSuccess=0
    lst_cntSuccess=[]
    idxSuccess=-1
    for episode in range(0,total_episodes):
        msg = "******** Episode {}/{} started ********".format(episode+1,total_episodes)
        logger.info(msg)
        #reset environment
        isSuccess=True
        routes = []
        rewards = 0
        agent.set_episilon()
        curedge = env.reset()
        routes.append(curedge)
        # logger.info("Current edge : {}".format(curedge))
        done = False
        cnt=0
        while not done: 
            block = True
            while block: #막힌 도로를 고름
                if curedge in endpoints:
                    break
                curedge = env.get_curedge(veh)
                # print(f"Current edge : {curedge}")
                action = agent.get_action(curedge) #현재 edge에서 가능한 (0,1,2) 중 선택 :e-greedy 방식으로
                
                nextedge = env.get_nextedge(curedge, action) #next edge 계산해서 env에 보냄.
                logger.info(f"Agent : {agent.id} Current edge : {curedge} Action : {action} nextedge : {nextedge}")
                if nextedge!="" : break
                agent.learn_block(curedge, action) #막힌 도로 선택시, blockreward 부여(blockreward - -100)
            
            if nextedge in badpoints: isSuccess=False
            routes.append(nextedge)

            reward, done = env.step(curedge, nextedge) #changeTarget to nextedge
            logger.info(f"Agent : {agent.id} Reward : {reward} done : {done} ")
            agent.learn(curedge, action, reward, nextedge)
            rewards += reward
            

            if done:
                if nextedge==endpoints[0]:
                    print('Arrived:) ')
                else:
                    isSuccess = False
                    print('Bad Arrived:( ')
                break
            
            curedge = nextedge
            cnt+=1

        #Consecutive Success 계산
        if isSuccess:
            if idxSuccess==-1: idxSuccess = episode
            cntSuccess+=1
        else:
            cntSuccess = 0
            idxSuccess=-1
        lst_cntSuccess.append(cntSuccess)
        data =[episode,len(routes),reward,str(routes)]
        save_data(file_path=file_path,data=data)
        print(f"Agent : {agent.id} Episode : {episode}, len : {len(routes)} route : {routes}, reward : {reward}")
        # logger.warn("+++++++++++++++++++++++++++++++++++++++")
        # logger.warn(f"Agent : {agent.id} Episode : {episode}, route : {routes}, reward : {reward}")
        # logger.warn("+++++++++++++++++++++++++++++++++++++++")
    print('Routing #{} => Consecutive Success: {} from episode #{}'.format(episode, cntSuccess,idxSuccess))
    # plot_result(episodenum,lst_cntSuccess)
    sys.stdout.flush()
  


def main():
    traci,sumolib = checkSumo()
    logger = setUpLogger()
    parser = argparse.ArgumentParser(description="Sumo Client Server")
    parser.add_argument("--config",type=str,default = "config.yaml")
    parser.add_argument("--vehicle",type=str)
    args = parser.parse_args()
    config = parseConfig(args)
    logger.info("Config : {}".format(config))
    cfg_path = os.path.abspath(os.path.join(config['scenario'],config['cfg_file']))

    OUT_DIR ='output'
    
    veh_id = f"veh{args.vehicle}"
    file_path = setup_csv(OUT_DIR,veh_id)
    
    if config['use_gui']:
        sumoBinary = sumolib.checkBinary('sumo-gui')
    else:
        sumoBinary = sumolib.checkBinary('sumo')
    logger.info("Sumo : {}".format(sumoBinary))

    net_file_path = os.path.abspath(os.path.join(config['scenario'],config['net_file']))
    det_file_path = os.path.abspath(os.path.join(config['scenario'],config['det_file']))

    all_dets = generate_detectionfile(net_file_path, det_file_path) #generate detector file
    edgelists = get_alledges(net_file_path)
    dict_connection = calculate_connections(edgelists, net_file_path)

    ql_run(sumoBinary=sumoBinary,traci = traci,logger = logger,total_episodes=config['total_episodes'],net=net_file_path,det=det_file_path,
           sumocfg=cfg_path,alldets=all_dets,edgelists=edgelists,dict_connection=dict_connection,veh=veh_id,
           endpoints=config['endpoints'],badpoints=config['badpoints'],config = config,file_path=file_path)


    # traci.close()
if __name__ == "__main__":
    main()