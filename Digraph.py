# 2023-2024 Programacao 2 LTI
# Grupo 40
# 62269 Dinis Garcia
# 62238 Afonso Paulo

class Digraph(object):
    """
    Class of Directed Graphs
    """

    def __init__(self):
        """
        Constructs a Directed Graph
        
        Ensures:
        empty Digraph, i.e.
        Digraph such that [] == self.getNodes() and {} == self.getEdges() 
        """
        self._nodes = []
        self._edges = {}

        
    def addNode(self, node):
        """
        Adds a Node
        
        Requires:
        node is Node not in the digraph yet
        Ensures:
        getNodes() == getNodes()@pre.append(node)
        getEdges[node] == [] 
        """
        if node in self._nodes:
            raise ValueError('Duplicate node')
        else:
            self._nodes.append(node)
            self._edges[node] = []

            
    def addEdge(self, edge):
        """
        Adds an Edge to the Digraph

        Requires:
        edge is an Edge object
        edge.getSource() and edge.getDestination() are Node objects in the graph
        Ensures:
        The edge is added to the graph, i.e. 
        edge.getSource() -> edge.getDestination() is a valid edge in the graph
        self._edges[edge.getSource()] contains edge.getDestination()
        """
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self._nodes and dest in self._nodes):
            raise ValueError('Node not in graph')
        self._edges[src].append(edge)

        
    def childrenOf(self, node):
        """
        Returns a list of nodes that are children of a given node in the graph

        Requires:
        node is a Node object in the graph
        Ensures:
        A list of nodes that are children of the given node is returned
        """
        return self._edges[node]

    
    def hasNode(self, node):
        """
        Checks if a node is in the graph

        Requires:
        node is a Node object
        Ensures:
        True if the node is in the graph, False otherwise
        """
        return node in self._nodes

    
    def __str__(self):
        """
        Returns a string representation of the directed graph

        Requires:
        The directed graph has been initialized
        Ensures:
        A string representation of the directed graph is returned
        """
        result = ''
        for src in self._nodes:
            for dest in self._edges[src]:
                result = result + src.getName() + '->' + dest.getName() + '\n'




