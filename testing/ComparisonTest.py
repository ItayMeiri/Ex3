import threading
from timeit import default_timer as timer
from DiGraph import DiGraph
from GraphAlgo import GraphAlgo
from datetime import timedelta
import random
import sys



algo = GraphAlgo()

# Test comparing the runtime of various functions


sys.setrecursionlimit(10 ** 6)
def connected_component_test(id):
    start = timer()
    algo.connected_component(id)
    return timer() - start


def strong_connected_component():
    start = timer()
    algo.connected_components()
    return timer() - start


def shortest_path(id1, id2):
    start = timer()
    algo.shortest_path(id1, id2)
    return timer() - start


i = 0

connected_component_average = 0
strong_connected_component_average = 0
shortest_path_average = 0



test_amount = 2

def test_graph(test_amount, file):
    algo.load_from_json(file)
    i = 0
    connected_component_average = 0
    strong_connected_component_average = 0
    shortest_path_average = 0
    while i < test_amount:
        i += 1
        random.seed(i)
        r1 = random.randint(1, test_amount)
        r2 = random.randint(1, test_amount)

        # add up the total runtime
        connected_component_average += connected_component_test(r1)
        strong_connected_component_average += strong_connected_component()
        shortest_path_average += shortest_path(r1, r2)

    connected_component_average /= test_amount
    strong_connected_component_average /= test_amount
    shortest_path_average /= test_amount

    return connected_component_average, strong_connected_component(), shortest_path_average


def test_graph2(file, bol=False):
    start = timer()
    algo.load_from_json(file)
    load = timer() - start
    if bol:
        algo.plot_graph()

    start = timer()
    connected_component_test(3)
    con = timer() - start

    start = timer()
    strong_connected_component()
    st = timer() - start

    start = timer()
    shortest_path(1, 2)
    p = timer() - start

    return st, con, p, load



file = '../data/G_10_80_1.json'
st, con, p, load = test_graph2(file)
print("file: ", file)
print("load", load)
print("connected", con)
print("strongly", st)
print("path,", p)
print()


file = '../data/G_100_800_1.json'
st, con, p, load = test_graph2(file, True)
print("file: ", file)
print("load", load)
print("connected", con)
print("strongly", st)
print("path,", p)
print()

file = '../data/G_1000_8000_1.json'
st, con, p, load = test_graph2(file)
print("file: ", file)
print("load", load)
print("connected", con)
print("strongly", st)
print("path,", p)
print()


file = '../data/G_10000_80000_1.json'
st, con, p, load = test_graph2(file)
print("file: ", file)
print("load", load)
print("connected", con)
print("strongly", st)
print("path,", p)
print()

file = '../data/G_20000_160000_1.json'
st, con, p, load = test_graph2(file)
print("file: ", file)
print("load", load)
print("connected", con)
print("strongly", st)
print("path,", p)
print()

file = '../data/G_30000_240000_1.json'
st, con, p, load = test_graph2(file)
print("file: ", file)
print("load", load)
print("connected", con)
print("strongly", st)
print("path,", p)
print()

