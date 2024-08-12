# 2023-2024 Programacao 2 LTI
# Grupo 40
# 62269 Dinis Garcia
# 62238 Afonso Paulo

from Digraph import Digraph
from Edge import Edge
class Graph(Digraph):
    def addEdge(self, edge):
        """
        Adds an edge to the graph.

        edge: An Edge object representing the edge to add.

        Requires:
        edge must be an Edge object.

        Ensures:
        The edge is added to the graph.
        """
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource(), edge.getValue())
        Digraph.addEdge(self, rev)
