# 2023-2024 Programacao 2 LTI
# Grupo 40
# 62269 Dinis Garcia
# 62238 Afonso Paulo

from WritingFile import WritingFile
import sys
def printPath(path):
    """
    String representation of a path

    Requires:
    path a list of nodes
    Ensures:
    string whith nodes' names concatenated by '->'
    """
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + ' -> '
    return result 
    
def BestOf3(Shortest , Lightest , Best = []):
    '''
    It makes a list with the best 3 possible,
    paths.

    Requires:
    Shortest is a list of nodes.
    Lightest is the value of each Node added
    on the Shortest List.
    Ensures:
    Best list with the 3 lightest paths.
    '''
    if Shortest == None:#The first case is always a None, 
    #this prevents that a list with none is added
        return 
    if [Shortest, Lightest] in Best:#To avoid repetition when adding the paths
        return Best
    if len(Best) < 3 :#If there isnt 3 Paths 
        Best.append([Shortest, Lightest])
        Best.sort(key=lambda weight: (weight[1],-len(weight[0])\
        ,[node.getName() for node in weight[0]])) 
        return Best 
        #Sees if there is a heavier path
        #in the current Best than the current path   
    if Lightest < (Best[2])[1]:
        Best.pop()
        Best.append([Shortest, Lightest])
    Best.sort(key=lambda weight: (weight[1],-len(weight[0])\
    ,[node.getName() for node in weight[0]]) )
    return Best   
def DFS(graph, start, end, path, shortest, TotalWeight, Lighest, NoNoPaths = []):
    """
    Depth first search in a directed graph

    Requires:
    graph a Digraph;
    start and end nodes;
    path and shortest lists of nodes 
    TotalWeight and Lighest are ints
    NoNoPaths is a list that when its made the recursive
    adds the paths that were already explored.
    Ensures:
    a shortest path from start to end in graph.
    """
    path = path + [start]
    if start == end:
        return path, TotalWeight, 0
    for edge in graph.childrenOf(start):
        node = edge.getDestination()
        weight = edge.getValue()
        if node not in path:
            if shortest == None or TotalWeight + weight < Lighest or path not in NoNoPaths:
                #It checks if the current path is the lighest it can be and 
                #checks if the path is currently on wasnt already explored.
                newPath,CurrentWeight,Answer = DFS(graph, node, end, path, shortest\
                , TotalWeight + weight, Lighest)#Total weight is always being updated
                if newPath != None :
                    shortest = newPath
                    Lighest = CurrentWeight
            NoNoPaths.append(BestOf3(shortest,Lighest))
    Answer = BestOf3(shortest,Lighest)           
    return shortest, Lighest, Answer

def search(graph, start, end):
    """
    Wrapper function to initialize DFS function

    Requires:
    graph a Digraph;
    start and end are nodes
    Ensures:
    shortest path from start to end in graph
    """
    if type(end) == str :
        return [end + ' ' +'out of the network']
    elif type(start) == str:
         return [start + ' ' +'out of the network']
    _,_,DFSdone = DFS(graph, start, end, [], None, 0,0) #The function is used 
    #in a recursive way so there needs to be returning other aspects but for 
    #the answer we only want the third elemnt which is the best3 paths.
    if DFSdone == None:
        return [start.getName() + ' and ' + end.getName()+''+  ' do not communicate']

    End = []
    for nodes,weight in DFSdone:#Transform the nodes into str using .getName()
        NodesName = []
        for node in nodes:
            NodesName.append(node.getName())
        End.append([weight,NodesName])
    DFSdone.clear()#This is need so when we calling safeLevadas1 it doesnt add
    #values that were already added.
    return End

def safeLevadas1(LevadasNetworkFile, StationsFile,OutputFile):
    """
    Starts the Function with the Files we want.

    Requires:
    LevadasNetworkFile is a string representing the path to 
    the file containing the levadas network data.
    StationsFile is a string representing the path 
    to the file containing the stations data.
    OutputFile is a string that has the name of the OutPutFile.
    Ensures:
    A file that has the best 3 paths from a station to another.
    """
    Content = {}
    f = WritingFile(LevadasNetworkFile, StationsFile)
    f.ReadsFilesLevadas()
    Stations = f.ReadsFileStations()
    for i in Stations:
        Start, end = f.StationToNode(i[0],i[1])
        Content['# '+ i[0] + ' - ' + i[1]] = search(f,Start,end)
    f.WritingOutPutFile(OutputFile,Content)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)
        
    LevadasNetworkFile = sys.argv[1]
    StationsFile = sys.argv[2]
    OutputFile = sys.argv[3]
    
    safeLevadas1(LevadasNetworkFile, StationsFile, OutputFile)

