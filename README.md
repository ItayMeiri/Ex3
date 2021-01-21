# Ex 3

This project is part of an assignment for the Object Oriented Programming(OOP) course at Ariel University. You can check out the main github here: https://github.com/simon-pikalov/Ariel_OOP_2020/

In this project, we're implementing a directional weighted graph in Python. 



## DiGraph class
This class represents a simple directional weighted graph with following operations

* add nodes
* add edges
* remove node
* remove edge
* get node
* vertices size 
* edge size
* get all nodes

_The exact documentation is available in the Wiki_


### Example usage:
```python
    g = DiGraph()  # creates an empty directed graph
    for n in range(4):
        g.add_node(n) # create nodes with n as key
```

You can then connect these nodes through edges:
```python
g.add_edge(0, 1, 3) # adds an edge between 0 -> 1 with weight 3
```

## GraphAlgo class
The real power of the project is the algorithms class, this class suports the following algorithms:
* loading and saving a graph from json
* computing the shortest path
* finding the connected component of a node
* finding all strongly connected components
* plotting the graph

### Example usage:
```python
  
graph = DiGraph() # create a DiGraph
graph.add_node(0)
graph.add_node(1)
graph.add_node(2)

graph.add_edge(0, 1, 2)
graph.add_edge(0, 2, 4)
graph.add_edge(1, 2, 1)

algo = GraphAlgo(graph) # initialize the algorithms class

path = algo.shortest_path(0, 2) # compute the shortest path
print(path)
```

In this example, we're adding 3 nodes and adding edges, the **shortest_path()** function will return the weight of the shortest path and the actual path itself.
In this case, we're checking how to travel from 0 to 2 ( 0 -> 1 -> 2 is shortest)

```output: (3, [0, 1, 2])```



The algo function also allows the plot function:

![Image Graph](https://i.imgur.com/tnNokBt.jpg)
