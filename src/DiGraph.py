from src import GraphInterface


class DiGraph(GraphInterface.GraphInteface):

    class NodeData:
        def __init__(self, key, pos):
            self.key = key
            self.pos = pos
            self.ingoing = {}
            self.outgoing = {}
            self.index = -1
            self.low_link = float('inf')
            self.on_stack = False
            self.dist = float('inf')
            self.prev = -1

        def get_key(self):
            return self.key

        def get_pos(self):
            return self.pos

        def add_outgoing_edge(self, node_id, weight):
            self.outgoing[node_id] = weight

        def add_ingoing_edge(self, node_id, weight):
            self.ingoing[node_id] = weight

        def remove_outgoing_edge(self, node_id):
            if node_id in self.outgoing:
                del self.outgoing[node_id]

        def remove_ingoing_edge(self, node_id):
            if node_id in self.ingoing:
                del self.ingoing[node_id]

        def get_ingoing_edges(self):
            return self.ingoing

        def get_outgoing_edges(self):
            return self.outgoing

        def set_ingoing_edges(self, ingoing):
            self.ingoing = ingoing

        def set_outgoing_edges(self, outgoing):
            self.outgoing = outgoing

        def get_index(self):
            return self.index

        def set_index(self, index):
            self.index = index

        def set_low_link(self, lowlink):
            self.lowlink = lowlink

        def get_low_link(self):
            return self.lowlink

        def is_on_stack(self):
            return self.on_stack

        def set_on_stack(self, boolean):
            self.on_stack = boolean

    def __init__(self):
        self.nodes = {}
        self.mc = 0
        self.nodeSize = 0
        self.edgeSize = 0

    def v_size(self) -> int:
        return len(self.nodes)

    def e_size(self) -> int:
        return self.edgeSize

    def get_all_v(self) -> dict:
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.nodes[id1].get_ingoing_edges()

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.nodes[id1].get_outgoing_edges()

    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 is id2:
            return False
        if id1 in self.nodes and id2 in self.nodes:
            self.nodes.get(id1).add_outgoing_edge(id2, weight)
            self.nodes.get(id2).add_ingoing_edge(id1, weight)
            self.edgeSize += 1
            self.mc += 1
            return True
        return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self.nodes:
            return False
        self.nodes[node_id] = self.NodeData(node_id, pos)
        self.mc += 1
        return True

    def remove_node(self, node_id: int) -> bool:
        if node_id not in self.nodes:
            return False

        # Remove all edges from src->dst
        for node in self.nodes[node_id].get_ingoing_edges():
            self.nodes[node].remove_outgoing_edge(node_id)
            self.edgeSize -= 1

        # Remove all edges from dst->src

        for node in self.nodes[node_id].get_outgoing_edges():
            self.nodes[node].remove_ingoing_edge(node_id)
            self.edgeSize -= 1

        del self.nodes[node_id]
        self.mc += 1

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 in self.nodes and node_id2 in self.nodes:
            self.nodes[node_id1].remove_outgoing_edge(node_id1)
            self.nodes[node_id2].remove_ingoing_edge(node_id1)
            self.edgeSize -= 1
            self.mc += 1
            return True
        return False

    def get_node(self, node_id):
        if node_id in self.nodes:
            return self.nodes[node_id]


