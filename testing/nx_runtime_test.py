import json
import networkx as nx
from typing import List
from timeit import default_timer as timer
from DiGraph import DiGraph
from GraphAlgo import GraphAlgo
from datetime import timedelta
import random



def load_from_json(file_name: str):
    file = open(file_name, "r+")
    data = json.load(file)

    for node in data['Nodes']:
        posList = node['pos'].split(',')
        graph.add_node(node['id'], id = node['id'], pos=tuple(posList), low_link = float('inf'), is_on_stack = False, index = -1 )

    for edge in data['Edges']:
        graph.add_edge(edge['src'], edge['dest'], weight=edge['w'])

    file.close()
    return True

print()
graph = nx.DiGraph()
path = '../data/G_10_80_1.json'
print("testing ", path)
start = timer()
load_from_json(path)
end = timer() - start
print("Load time: ", end)
start = timer()
nx.strongly_connected_components(graph)
end = timer() - start
print("Connected components: ", end)
g = nx.to_undirected(graph)
start = timer()
nx.node_connected_component(g, 3)
end = timer() - start
print("Connected component: ", end)
start = timer() - start
nx.shortest_path(graph, 1, 2)
end = timer() - start
print("Shortest path :", end)

print()
graph = nx.DiGraph()
path = '../data/G_100_800_1.json'
print("testing ", path)
start = timer()
load_from_json(path)
end = timer() - start
print("Load time: ", end)
start = timer()
nx.strongly_connected_components(graph)
end = timer() - start
print("Connected components: ", end)
g = nx.to_undirected(graph)
start = timer()
nx.node_connected_component(g, 3)
end = timer() - start
print("Connected component: ", end)
start = timer() - start
nx.shortest_path(graph, 1, 2)
end = timer() - start
print("Shortest path :", end)

print()
graph = nx.DiGraph()
path = '../data/G_1000_8000_1.json'
print("testing ", path)
start = timer()
load_from_json(path)
end = timer() - start
print("Load time: ", end)
start = timer()
nx.strongly_connected_components(graph)
end = timer() - start
print("Connected components: ", end)
g = nx.to_undirected(graph)
start = timer()
nx.node_connected_component(g, 3)
end = timer() - start
print("Connected component: ", end)
start = timer() - start
nx.shortest_path(graph, 1, 2)
end = timer() - start
print("Shortest path :", end)

print()
graph = nx.DiGraph()
path = '../data/G_10000_80000_1.json'
print("testing ", path)
start = timer()
load_from_json(path)
end = timer() - start
print("Load time: ", end)
start = timer()
nx.strongly_connected_components(graph)
end = timer() - start
print("Connected components: ", end)
g = nx.to_undirected(graph)
start = timer()
nx.node_connected_component(g, 3)
end = timer() - start
print("Connected component: ", end)
start = timer() - start
nx.shortest_path(graph, 1, 2)
end = timer() - start
print("Shortest path :", end)

print()
graph = nx.DiGraph()
path = '../data/G_20000_160000_1.json'
print("testing ", path)
start = timer()
load_from_json(path)
end = timer() - start
print("Load time: ", end)
start = timer()
nx.strongly_connected_components(graph)
end = timer() - start
print("Connected components: ", end)
g = nx.to_undirected(graph)
start = timer()
nx.node_connected_component(g, 3)
end = timer() - start
print("Connected component: ", end)
start = timer() - start
nx.shortest_path(graph, 1, 2)
end = timer() - start
print("Shortest path :", end)

print()
graph = nx.DiGraph()
path = '../data/G_30000_240000_1.json'
print("testing ", path)
start = timer()
load_from_json(path)
end = timer() - start
print("Load time: ", end)
start = timer()
nx.strongly_connected_components(graph)
end = timer() - start
print("Connected components: ", end)
g = nx.to_undirected(graph)
start = timer()
nx.node_connected_component(g, 3)
end = timer() - start
print("Connected component: ", end)
start = timer() - start
nx.shortest_path(graph, 1, 2)
end = timer() - start
print("Shortest path :", end)