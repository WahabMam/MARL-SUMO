from collections import defaultdict
import argparse
from utils import *
import os, sys

def dfs(graph, start, end, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = [start]
    if start == end:
        yield path
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            yield from dfs(graph, neighbor, end, visited, path + [neighbor])
    visited.remove(start)

def list_all_routes(graph, start, end, exclude :list =None):
    routes = []
    if exclude is not None:
        for route in dfs(graph, start, end):
            set1 = set(route)
            set2 = set(exclude)
            inter = set1.intersection(set2)
            if len(inter) == 0:
                routes.append(route)
    else:
        for route in dfs(graph, start, end):
            routes.append(route)
    return routes

def print_routes(routes,num = None):
    if num is None:
        num = len(routes)
    for el in routes[:num]:
        print(f"Length : {len(el)} Route : {el}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sumo Client Server")
    parser.add_argument("--config",type=str,default = "config.yaml")
    parser.add_argument("--vehicle",type=str, default='0')
    parser.add_argument("--start",type=str)
    parser.add_argument("--dest",type=str)
    parser.add_argument("--nr",type=int, default=11)
    args = parser.parse_args()
    config = parseConfig(args)
    cfg_path = os.path.abspath(os.path.join(config['scenario'],config['cfg_file']))
    conjusted = ['E6','-E6','E2','-E2','E13','-E13','-E19']
    OUT_DIR ='output'

    net_file_path = os.path.abspath(os.path.join(config['scenario'],config['net_file']))
    det_file_path = os.path.abspath(os.path.join(config['scenario'],config['det_file']))

    all_dets = generate_detectionfile(net_file_path, det_file_path) #generate detector file
    edgelists = get_alledges(net_file_path)
    dict_connection = calculate_connections(edgelists, net_file_path)

    start = args.start
    end = args.dest

    routes = list_all_routes(dict_connection,start=start,end=end,exclude=conjusted)
    print(f"The number of routes from {start} -> {end} = {len(routes)}")
    sorted_routes = sorted(routes, key=lambda x: len(x))
    print_routes(sorted_routes,args.nr)
    
    