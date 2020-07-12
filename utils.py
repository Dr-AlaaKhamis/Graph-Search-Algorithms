from inspect import getsource
import networkx as nx
import matplotlib.pyplot as plt
from pygments.formatters import HtmlFormatter
from pygments.lexers import PythonLexer
from IPython.display import HTML
from IPython.display import display
from pygments import highlight

#
# prints the source code of a list of functions
# in the jupyter notebook
#

def source(*functions):
    source_code = '\n\n'.join(getsource(fn) for fn in functions)        
    display(HTML(highlight(source_code, PythonLexer(), HtmlFormatter(full=True))))

#
# the following classes are meant for
# drawing graphs and manipulate them on jupyter notebook
#


class Graph:
    def __init__(self, graph_dict=None, directed=True):
        self.graph_dict = graph_dict or {}
        self.directed = directed
        if not directed:
            self.make_undirected()

    def make_undirected(self):
        for a in list(self.graph_dict.keys()):
            for (b, dist) in self.graph_dict[a].items():
                self.connect1(b, a, dist)
    
    def connect(self, A, B, distance = 1):
        self.connect1(A, B, distance)
        if not self.directed:
            self.connect1(B, A, distance)
    
    def connect1(self, A, B, distance):
        self.graph_dict.setdefault(A, {})[B] = distance

    def get(self, a, b=None):
        links = self.graph_dict.setdefault(a, {})
        if b is None:
            return links
        else:
            return links.get(b)

    def nodes(self):
        s1 = set([k for k in self.graph_dict.keys()])
        s2 = set([k2 for v in self.graph_dict.values() for k2, v2 in v.items()])
        nodes = s1.union(s2)
        return list(nodes)

def UndirectedGraph(graph_dict=None):
    return Graph(graph_dict=graph_dict, directed=False)



#
# hardcoded examples generating the figures in the notebooks 
# it has no value of its own
#


def disjoint_forest():
    MAP = UndirectedGraph(dict(
        _0=dict(_1=10, _2=5),
        _3=dict(_4=2),
        _5=dict(_6=11, _7=3, _8=2),
        _9=dict(_10=3),
        _11=dict()))
    MAP.locations = dict(
        _0=(50, 650), _1=(30, 400), _2=(70, 400),
        _3=(90, 550), _4=(110, 550), _5=(130, 650),
        _6=(150, 650), _7=(130, 400), _8=(150, 400),
        _9=(170, 550), _10=(190, 550), _11=(210, 550))
    node_colors = {node : 'black' for node in MAP.locations.keys()}
    node_positions = MAP.locations
    node_labels = {k:(v[0], v[1] - 3) for k, v in MAP.locations.items()}
    edges = {(k, k2) : v2 for k, v in MAP.graph_dict.items() for k2, v2 in v.items()}
    graph_data = {
        'graph_dict' : MAP.graph_dict,
        'node_colors': node_colors,
        'node_positions': node_positions,
        'node_label_positions': node_labels,
        'edge_weights': edges
    }
    G = nx.Graph(graph_data['graph_dict'])
    node_colors = node_colors or graph_data['node_colors']
    node_positions = graph_data['node_positions']
    node_label_pos = graph_data['node_label_positions']
    edge_weights = graph_data['edge_weights']
    plt.figure(figsize=(18, 3))
    nx.draw(G, pos={k : node_positions[k] for k in G.nodes()}, node_color=[node_colors[node] for node in G.nodes()], linewidths=2, edgecolors='k', node_size = 500)
    node_label_handles = nx.draw_networkx_labels(G, pos=node_label_pos, font_size=15)
    [label.set_bbox(dict(facecolor='white', edgecolor='none')) for label in node_label_handles.values()]
    # nx.draw_networkx_edge_labels(G, pos=node_positions, edge_labels=edge_weights, font_size=14)
    plt.show()