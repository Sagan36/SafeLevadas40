# 2023-2024 Programacao 2 LTI
# Grupo 40
# 62269 Dinis Garcia
# 62238 Afonso Paulo

from Graph import Graph
from Node import Node
from Edge import Edge

class File(Graph):
    '''
    This class reads the File and creates
    the Nodes and the Edges that will be used
    for the DFS later on the code. 
    '''
    
    def __init__(self, FileNameLevadas, FileNameStations):
        """
        Initializes the File object with the given file names.

        FileNameLevadas: File name for levadas.
        FileNameStations: File name for stations.

        Requires:
        Valid file paths.

        Ensures:
        File object is initialized.
        """
        super().__init__()
        self._FileLevadas = FileNameLevadas
        self._FileStations = FileNameStations

    def getFileLevadas(self):
        """
        Returns the file name for the levadas.

        Requires:
        The File object has been initialized with a valid file name for the levadas.

        Ensures:
        Returns the file name for the levadas as a string.
        """
        return self._FileLevadas
    
    def getFileStations(self):
        """
        Returns the file name for the stations.

        Requires:
        The File object has been initialized with a valid file name for the stations.

        Ensures:
        Returns the file name for the stations as a string.
        """
        return self._FileStations
    
    def LevadaFormating(self,LevadaList):
        """
        Formats the third element of each levada in the given list and 
        makes the Nodes and Edges that will be used in the DFS 
        function.

        Requires:
        LevadaList must be a list of lists, where each inner list has at 
        least three elements.
        The third element of each inner list must be a string that 
        can be formatted as a list of tuples.

        Ensures:
        The third element of each inner list in LevadaList is formatted 
        as a list of tuples and the Nodes and the Edges are made.
        """
        Finallist = []
        for Levada in LevadaList:#Creates the nodes
            self.addNode(Node(Levada[0], Levada[1]))
            
        
        for Levada in LevadaList:
            FormatedList = []    
            FormatingTrails = (Levada[2])[1:-1].split("), ")# These two lines of code
            #remove unecessary parentheses and brackets
            FormatingTrails[-1] = FormatingTrails[-1][:-1]
            
           
            for string in FormatingTrails:
                string = string + ")" 
                info = string.strip("()").split(",")
                if info[0] != '':
                    key = info[0].strip()#These three lines transform 
                    #the string into a tuple 
                    value = int(info[1].strip())
                    FormatedList.append((key, value))
                    
                    for node in self._nodes:
                        if node._id == Levada[0]:
                            startNode = node
                        if node._id == key:
                            endNode = node
                    
                    self.addEdge(Edge(startNode, endNode,value)) #Creates the Edges
            Finallist.append(FormatedList)   
        while len(Finallist) > 0:#It updates the third element of "Levada" with the new info
            for newLevada in LevadaList:
                newLevada[2] = Finallist[0]
                del Finallist[0] 
        return LevadaList
    
    def ReadsFilesLevadas(self):
        """
        Reads a text file and returns its content as a list of lists.

        Requires:
        FileName must be a string representing a valid file path.

        Ensures:
        Returns a list of lists containing the content of the file. Each element 
        in the list corresponds to a line in the file, 
        and each line is represented as a list of strings, 
        where elements are separated by ', '.
        If the file specified by FileName exists and is readable, it returns the 
        content as described above.
        """
        inFile = open(self.getFileLevadas(),"r", encoding = "utf-8")
        allLines = inFile.readlines()
        
        info = []
        
        for line in allLines[1:]: #removes the first line of the allLines cause its 
            #the specification of each value in each Levada
            inLines = line.rstrip().splitlines()#everything that has a white space is 
            #seperated by a ',' and put everyting in a list 
            info.append(inLines)
        newInfo = []
        for Levada in info:
            string_Levada = Levada[0]
            split_Levadas = [part.strip() for part in string_Levada.split(',')]
            if len(split_Levadas) > 2:
                split_Levadas[2] = ', '.join(split_Levadas[2:])
            split_Levadas = split_Levadas[:3]
            newInfo.append(split_Levadas)
        self.LevadaFormating(newInfo)
        return newInfo
  
    def ReadsFileStations(self):
        """
        Reads a text file and returns its content as a list of lists.

        Ensures:
        Returns a list of lists containing the content of the file. 
        Each element in the list corresponds to a line in the file, 
        and each line is represented as a list of strings, 
        where elements are separated by ', '.
        If the file specified by FileName exists and is readable, 
        it returns the content as described above.
        """
        inFile = open(self.getFileStations(),"r", encoding = "utf-8")
        allLines = inFile.readlines()
        
        info = []
        for line in allLines:
                inLines = line.rstrip().split(' - ')
                info.append(inLines)
        return info
    
    def StationToNode(self, Start, End):
        """
        Converts the given start and end station names to Node objects.

        Start: The name of the start station.
        End: The name of the end station.

        Requires:
        Start and End must be strings representing valid station names.

        Ensures:
        eturns a tuple of two Node objects representing the start and end stations.
        """
        NodeEnd = End
        NodeStart = Start
        for node in self._edges:
            if Start == str(node.getName()):
                NodeStart = node
            elif End == str(node.getName()):
                NodeEnd = node
        return NodeStart, NodeEnd 
    
    def __str__(self) -> str:
        """
        Returns a string representation of the File object.

        Requires:
        The File object has been initialized with valid file names 
        for levadas and stations.

        Ensures:
        Returns a string representation of the File object.
        """
        pass