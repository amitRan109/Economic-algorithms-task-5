from typing import List
import networkx as nx

class Agent:
    def __init__(self, _values, tag):
        self.values = _values
        self.tag = tag
    def item_value(self,item_index: int) -> float:
        return self.values[item_index]

def envy_graph(agents:List[Agent], bundles:List[List[int]]):
    G= nx.DiGraph()
    G.add_nodes_from(agents)
    for a in agents: #check if a envy of eneryone else
        sum_a = sum_values(a,bundles,a.tag) #sum value of a
        for b in agents:
            if (a != b):
                sum_b = sum_values(a,bundles,b.tag) #sum value of a if he had the part of b 
                if (sum_a < sum_b): #a envy on b
                    G.add_edge(a,b)
    return G

def sum_values(agent:Agent, bundles:List[int], tag:int)->float: #return the value of some part for a agent 
    _sum = 0
    for x in bundles[tag]:
        _sum += agent.item_value(x)
    return _sum


#----example 1----
print("----example 1----", end='\n\n')

Ami = Agent([1,2,3],0) 
Tami = Agent([3,1,2],1) 
 
G = envy_graph([Ami,Tami],[[1,2],[0]])
for e in G.edges:
    print("(", e[0].tag ," , ", e[1].tag, ")", end=' , ')
print('\n')

#----example 2----

print("----example 2----", end='\n\n')

Ami = Agent([1,2,3],0) 
Tami = Agent([3,1,2],1) 
Rami = Agent([2,3,1],2) 

G = envy_graph([Ami,Tami,Rami],[[0],[1],[2]])
for e in G.edges:
    print("(", e[0].tag ," , ", e[1].tag, ")", end=' , ')
print('\n')

#----example 3----

print("----example 3----", end='\n\n')

Ami = Agent([1,0,0,0],0) 
Tami = Agent([0,1,0,0],1) 
Rami = Agent([0,0,1,0],2) 
Hami = Agent([0,0,0,1],3)

G = envy_graph([Ami,Tami,Rami,Hami],[[3],[0],[1],[2]])
for e in G.edges:
    print("(", e[0].tag ," , ", e[1].tag, ")", end=' , ')
print('\n')
