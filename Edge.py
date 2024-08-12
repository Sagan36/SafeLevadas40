# 2023-2024 Programacao 2 LTI
# Grupo 40
# 62269 Dinis Garcia
# 62238 Afonso Paulo

class Edge(object):
    """
    Class of Edges
    """
    
    def __init__(self, src, dest, weight):
        """
        Constructs an Edge
        
        Requires:
        src and dst are Nodes
        and weight is a int.
        Ensures:
        Edge such that src == self.getSource() and dest == self.getDestination() 
        and weight == self.getValue() 
        """
        self._src = src
        self._dest = dest
        self._weight = weight

        
    def getSource(self):
        """
        Gets the source Node
        """
        return self._src

    
    def getDestination(self):
        """
        Gets the destination Node
        """
        return self._dest
    
    def getValue(self):
        """
        Gets the time of the Node
        """
        return self._weight
    


    def __str__(self):
        """
        String representation
        """
        return self._src.getName() + '->' + self._dest.getName()\
        + '=' +str(self.getValue())
