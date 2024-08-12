# 2023-2024 Programacao 2 LTI
# Grupo 40
# 62269 Dinis Garcia
# 62238 Afonso Paulo

class Node(object):
    """
    Class of Nodes
    """

    def __init__(self, id, name):
        """
        Constructs a Node
        
        Requires:
        name is a string and id 
        is also a string
        Ensures:
        node such that name == self.getName()
        """
        self._name = name
        self._id  = id


        
    def getName(self):
        """
        Gets the name
        """
        return self._name

            
    def getID(self):
        """
        Gets the id
        """
        return self._id
        

    
    def __str__(self):
        """
        String representation
        """
        return self._name, ' - ' ,self.getID()
