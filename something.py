import itertools 
import copy

import pandas as pd
import networkx as nx 
  
def degree_centrality(G, nodes): 
    r"""Compute the degree centrality for nodes in a bipartite network. 
  
    The degree centrality for a node `v` is the fraction of nodes  
    connected to it. 
  
    Parameters 
    ---------- 
    G : graph 
       A bipartite network 
  
    nodes : list or container 
      Container with all nodes in one bipartite node set. 
  
    Returns 
    ------- 
    centrality : dictionary 
       Dictionary keyed by node with bipartite degree centrality as the value. 
  
    Notes 
    ----- 
    The nodes input parameter must contain all nodes in one bipartite node set, 
    but the dictionary returned contains all nodes from both bipartite node 
    sets. 
  
    For unipartite networks, the degree centrality values are  
    normalized by dividing by the maximum possible degree (which is  
    `n-1` where `n` is the number of nodes in G).  
  
    In the bipartite case, the maximum possible degree of a node in a 
    bipartite node set is the number of nodes in the opposite node set 
    [1]_.  The degree centrality for a node `v` in the bipartite 
    sets `U` with `n` nodes and `V` with `m` nodes is 
  
    .. math:: 
  
        d_{v} = \frac{deg(v)}{m}, \mbox{for} v \in U , 
  
        d_{v} = \frac{deg(v)}{n}, \mbox{for} v \in V , 
  
  
    where `deg(v)` is the degree of node `v`.         
  
      
    """
    top = set(nodes) 
    bottom = set(G) - top 
    s = 1.0/len(bottom) 
    centrality = dict((n,d*s) for n,d in G.degree_iter(top)) 
    s = 1.0/len(top) 
    centrality.update(dict((n,d*s) for n,d in G.degree_iter(bottom))) 
    return centrality 



import networkx as nx 
G=nx.erdos_renyi_graph(100,0.5) 
d=nx.degree_centrality(G) 
print(d) 


E=nx.Graph()
nx.path_graph()
