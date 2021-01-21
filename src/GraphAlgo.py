import threading
from typing import List
import threading
from src import GraphAlgoInterface, GraphInterface
import json
import os
from src.DiGraph import DiGraph
import matplotlib.pyplot as plt
import numpy as np
import random
from graphics import *
import sys

class GraphAlgo(GraphAlgoInterface.GraphAlgoInterface):

    def __init__(self, graph=None):
        sys.setrecursionlimit(10**6)

        if graph is None:
            self.graph = DiGraph()
        else:
            self.graph = graph
        self.index = 0
        self.S = []
        self.order = []
        self.x_max = float('-inf')
        self.y_max = float('-inf')
        self.x_min = float('inf')
        self.y_min = float('inf')
        self.fig = plt.figure()
        self.component = {}

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        self.graph = DiGraph()
        file = open(file_name, "r+")
        data = json.load(file)

        for node in data['Nodes']:
            posList = node['pos'].split(',')
            self.graph.add_node(node['id'], tuple(posList))

        for edge in data['Edges']:
            self.graph.add_edge(edge['src'], edge['dest'], edge['w'])

        file.close()
        return True

    def save_to_json(self, file_name: str) -> bool:

        file = open(file_name, "w+")

        n = []
        e = []

        # Save every node, and all the edges inside
        for node in self.graph.get_all_v().values():
            nodes_to_json = {
                'pos': " ".join(map(str , node.get_pos())),
                'id': node.get_key()
            }
            n.append(nodes_to_json)
            for edge, weight in node.get_outgoing_edges().items():
                edges_to_json = {
                    'src': node.get_key(),
                    'w': weight,
                    'dest': edge
                }
                e.append(edges_to_json)

        print("n is", n)
        print("e is", e)

        file.write("{\"Edges\":")
        file.write(json.dumps(e))
        file.write(",\"Nodes\":")
        file.write(json.dumps(n))
        file.write("}")
        file.close()

        return True

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        self.S = []
        for node in self.graph.get_all_v().values():
            node.dist = float('inf')
            node.prev = -1
            self.S.append(node)

        self.graph.get_node(id1).dist = 0

        while self.S:
            # getting the minimum here
            u = self.S[0]
            for m in self.S:
                if m.dist < u.dist:
                    u = m

            self.S.remove(u)

            for neighbor_id, weight in self.graph.all_out_edges_of_node(u.get_key()).items():
                neighbor = self.graph.get_node(neighbor_id)
                alt = u.dist + weight
                if alt < neighbor.dist:
                    neighbor.dist = alt
                    neighbor.prev = u.get_key()

        prev_list = []
        current_id = id2
        while current_id is not id1:
            prev_list.append(current_id)
            current_id = self.graph.get_node(current_id).prev

        prev_list.append(current_id)
        prev_list.reverse()
        return self.graph.get_node(id2).dist, prev_list

    def connected_component(self, id1: int) -> list:
        if self.graph.get_node(id1).get_outgoing_edges():
            return self.strong_connect(self.graph.get_node(id1))
        return [self.graph.get_node(id1)]

    def connected_components(self) -> List[list]:
        self.index = 0
        self.S = []

        # Reset nodes
        for node in self.graph.get_all_v().values():
            node.set_index(-1)

        connected_list = list()
        for node in self.graph.get_all_v().values():
            if node.get_index() is -1:
                component = self.strong_connect(node)
                if component is not None:
                    connected_list.append(component)
        return connected_list




    def plot_graph(self) -> None:
        self.fig.set_size_inches(15, 10.5, forward=True)
        skipped = True
        for node in self.graph.get_all_v().values():
            skipped = True
            if node.get_pos() is None:
                x = random.uniform(0, 1)
                y = random.uniform(0, 1)
            else:
                x, y, z = node.get_pos()
                x = float(x)
                y = float(y)
            if x < self.x_min:
                self.x_min = x
            if y < self.y_min:
                self.y_min = y
            if x > self.x_max:
                self.x_max = x
            if y > self.y_max:
                self.y_max = y

        res = 0.001

        if skipped:
            self.x_min = 0
            self.x_max = 1
            self.y_min = 0
            self.y_max = 1


        self.x_min -= res
        self.x_max += res
        self.y_min -= res
        self.y_max += res

        it = [self.x_min, self.x_max, self.y_min, self.y_max]

        plt.axis(it)
        for node in self.graph.get_all_v().values():
            if node.get_pos() is None:
                x = random.uniform(self.x_min, self.x_max)
                y = random.uniform(self.y_min, self.y_max)
            else:
                x, y, z = node.get_pos()
                x = float(x)
                y = float(y)
            circle = plt.Circle((x, y), .0001, color='r')
            text = plt.text(x, y, str(node.get_key()))
            plt.gcf().gca().add_artist(circle)
            plt.gcf().gca().add_artist(text)

            for neighbor_id in node.get_outgoing_edges().keys():
                neighbor = self.graph.get_node(neighbor_id)
                if neighbor is node:
                    continue
                if neighbor.get_pos() is not None:
                    x1, y1, z1 = neighbor.get_pos()
                else:
                    x1, y1 = None, None
                if x1 is None:
                    x1 = random.uniform(self.x_min, self.x_max)
                else:
                    x1 = float(x1)
                if y1 is None:
                    y1 = random.uniform(self.y_min, self.y_max)
                else:
                    y1 = float(y1)

                # plt.axline((x1, y1), (x, y))
                # if not (np.allclose(x1,x) and np.allclose(y1,y)):

                plt.plot((x1, x), (y1, y))

        try:
            plt.pause(9999)
        except:
            pass

    def strong_connect(self, node):
        node.set_index(self.index)
        node.set_low_link(self.index)
        self.index += 1
        self.S.append(node)
        node.set_on_stack(True)

        for neighbor_id in self.graph.all_out_edges_of_node(node.get_key()):
            neighbor = self.graph.get_node(neighbor_id)
            if neighbor.get_index() is -1:
                self.strong_connect(neighbor)
                node.set_low_link(min(node.get_low_link(), neighbor.get_low_link()))
            elif neighbor.is_on_stack():
                node.set_low_link(min(node.get_low_link(), neighbor.get_index()))

        if node.get_low_link() == node.get_index():
            # start a new strongly connected component
            component = list()
            neighbor = self.S.pop()
            neighbor.set_on_stack(False)

            while neighbor is not node:
                component.append(neighbor)
                neighbor = self.S.pop()
                neighbor.set_on_stack(False)
            return component



    def DFS_iterative(self, node):
        self.S.append(node)
        while self.S:
            node = self.S.pop()
            if node.get_index() == -1:
                node.set_index(1)
                for neighbor_id in self.graph.all_out_edges_of_node(node.get_key()):
                    neighbor = self.graph.get_node(neighbor_id)
                    self.S.append(neighbor)




    #reverses all edges in the graph
    def reverse(self):
        for node in self.graph.get_all_v().values():
            temp = node.get_outgoing_edges()
            node.set_outgoing_edges(node.get_ingoing_edges())
            node.set_ingoing_edges(temp)






