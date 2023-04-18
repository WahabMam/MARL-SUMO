from utils import checkSumo, getRandomRoute
import random

# traci, sumolib = checkSumo()

class qlEnv():
    def __init__(self, sumoBinary, traci, logger, net_file: str,det_file: str, cfg_file: str, alldets: list, edgelists: list, dict_connection, 
                 veh:str, endpoint: list,config:dict, begin_time: int =0, num_seconds:int = 2000, max_depart_delay:int = 10000):
        
        self.sumoBinary = sumoBinary
        self.net = net_file
        self.det = det_file
        self.sumocfg = cfg_file
        self.alldets = alldets
        self.edgelists = edgelists
        self.config = config
        self.use_gui = config['use_gui']

        self.veh = veh
        self.endpoint = endpoint

        self.episode = 0 # # of run time 
        self.begin_time = begin_time
        self.num_seconds = num_seconds
        self.max_depart_delay = max_depart_delay

        self.action_space = [0,1,2]
        self.n_actions = len(self.action_space)
        self.dict_connection = dict_connection

        self.sumo =traci
        self.logger = logger
        
    def start_simulation(self):
        veh_id = int(self.config['veh_id'])
        if veh_id == 0:
            self.start_simulation_server()
        else:
            self.start_simulation_client()


    def start_simulation_client(self):
        self.sumo.init(port=int(self.config['port']),host = str(self.config['server_ip']))
        self.sumo.setOrder(int(self.config['veh_id'])+1)


    def start_simulation_server(self):
        PORT = self.config['port']
        sumo_cmd = [self.sumoBinary,
            '-c', self.sumocfg,
            '--max-depart-delay', str(self.max_depart_delay)]
        if self.config['num_clients'] != 0:
            sumo_cmd.extend(['--num-clients',str(self.config['num_clients'])])
        if self.use_gui:
            if self.config['start']:
                sumo_cmd.extend(['--start'])
            if self.config['quit_on_end']:
                sumo_cmd.extend(['--quit-on-end'])
            self.sumo.start(sumo_cmd,PORT)
            self.sumo.setOrder(int(self.config['veh_id'])+1)
            self.sumo.gui.setSchema(self.sumo.gui.DEFAULT_VIEW, "real world")
        else:
            self.sumo.start(sumo_cmd,PORT)
            self.sumo.setOrder(self.config['veh_id']+1)

        self.logger.warn("Sumo Started for Veh {} at: {}".format(self.config['veh_id'],sumo_cmd))
        '''
        if self.begin_time > 0:
            sumo_cmd.append('-b {}'.format(self.begin_time))
        
        '''

        
    def reset(self):
        if self.episode!=0: 
            self.sumo.close()

        self.episode+=1
        self.start_simulation()

        #vehicle  생성
        route_id = "rou"+self.veh[3:]
        id = int(self.veh[3:])
        route = self.config['start_edges']
        route = route[id]
        # route = getRandomRoute(dictconnection=self.dict_connection,sumo = self.sumo)
        # print("Veh  : {} route : ++++++++++++++ {}".format(self.veh,route))
        self.sumo.route.add(route_id, route) #default route
        self.sumo.vehicle.add(self.veh, route_id,departLane='best')
        # self.sumo.vehicle.setParameter(self.veh,'depart',str(id*10))
        self.sumo.simulationStep()
        curedge = self.get_curedge(self.veh)
        return curedge

    def get_curedge(self,veh):
        curedge = self.sumo.vehicle.getRoadID(veh)
        # curlane = self.sumo.vehicle.getLaneID(veh)
        # curedge = self.sumo.lane.getEdgeID(curlane)
        return curedge

    def get_done(self,curedge):
        done = False
        if curedge in self.endpoint:
            done = True
        return done
    
    def get_reward(self, nextedge):
        reward = 0
        if nextedge=='E6' or nextedge=='E2' or nextedge=='E13' or nextedge=='-E19':
            reward = -100
        elif nextedge=='E20':
            reward = 500
        return reward
    
    def get_nextedge(self,curedge, action):
        nextedge = self.dict_connection[curedge][action]
        return nextedge

    def get_vehiclecount(self):
        return self.sumo.vehicle.getIDCount()
  
    def step(self, curedge, nextedge):
        
        beforeedge = curedge #비교해서 변하면 고를려고!

        done = self.get_done(curedge)
        reward = self.get_reward(nextedge)

        if done:
            return reward, done
        
        self.sumo.vehicle.changeTarget(self.veh,nextedge) #차량 움직여!

        # curedge = self.get_curedge(self.veh)
        # done = self.get_done(curedge)
        # if done:
        #     return reward,done  
        # self.sumo.simulationStep() 
        # if curedge in self.edgelists and curedge !=beforeedge : #변했네!! 그럼 이제 다음 꺼 고르러 가야지
        #     return reward,done  
        
        while self.sumo.simulation.getMinExpectedNumber() > 0:
            if self.veh in self.sumo.vehicle.getIDList():
                curedge = self.get_curedge(self.veh)
                done = self.get_done(curedge)
                if done:
                    break  
                if curedge in self.edgelists and curedge !=beforeedge : #변했네!! 그럼 이제 다음 꺼 고르러 가야지
                    break
            self.sumo.simulationStep() 

        return reward, done    

    
    
    