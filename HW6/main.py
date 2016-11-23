
Python3 = True
DEBUG = False#True
DistinctNodes = None
Graph = [[None]]

def dijkstra(G,start_node):
	global DistinctNodes
	distance = [float("inf") for i in range(0,len(G))]
	prev = [None for i in range(0,len(G))]
	distance[start_node] = float(0)
	dNodes = DistinctNodes
	while len(dNodes) > 0:
		smallest = [-1,-1,float("inf")]
		for i in range(0,len(dNodes)):
			for j in range(0,len(dNodes)):
				Di = dNodes[i]
				Dj = dNodes[j]
				if G[Di][Dj] < smallest[2]:
					smallest = [Di,Dj,float(G[Di][Dj])]
		smallNode = smallest[0]
		
		if smallNode < 0:
			break
		dNodes.remove(smallNode)
		for j in range(0,len(G)):
			#if G[i][j] != float("inf"):
			alt = float(distance[smallNode] + G[smallNode][j])
			if alt < distance[j]:
				distance[j] = alt
				prev[j] = smallNode
				
	return distance
	
def floyd(inG):
	G = inG
	for i in range(0,len(G)):
		G[i][i] = float(0)
	for i in range(0,len(G)):
		for j in range(0,len(G)):
			for k in range(0,len(G)):
				if G[i][j] > (G[i][k] + G[k][j]):
					G[i][j] = G[i][k] + G[k][j]
	
	return G
	
def printHelp():
	print("Possible Commands are: \ndijkstra x - Runs Dijkstra starting at node X. X must be an integer\nfloyd - Runs Floyd's algorithm\nhelp - prints this menu\nexit or ctrl-D - Exits the program")

def makeGraph(inputFileName):
	try:
		inputFile = open(inputFileName,'r')
	except IOError:
		print("Invalid file name...\nexiting...")
		exit(-1)
	else:
		global Graph
		global DistinctNodes
		numNodes = int(inputFile.readline())
		Graph = [[float("inf") for i in range(0,numNodes)] for j in range(0,numNodes)] 
		DistinctNodes = [i for i in range(0,numNodes)]
	
		
		line = inputFile.readline()
		while line != "":
			fields = line.split(" ", line.count(" "))
			Graph[int(fields[0])][int(fields[1])] = float(fields[2])
			line=inputFile.readline()
	inputFile.close()
	
def printGraph():
	numNodes = len(Graph)
	for i in range(0,numNodes):
		for j in range(0,numNodes):
			print(i,j,Graph[i][j])

inputFileName = ""
if DEBUG:
	inputFileName = "input1.txt"
else:
	if Python3:
		inputFileName = input("File containing graph: ")
	else
		inputFileName = raw_input("File containing graph: ")

makeGraph(inputFileName)

if DEBUG:
	printGraph()
printHelp()

while True:
	makeGraph(inputFileName)
	
	inputCommand = ""
	if Python3:
		inputCommand = input("Enter command: ")
	else:
		inputCommand = raw_input("Enter command: ")
		
	if inputCommand == "exit":
		print("Bye")
		break;
	elif inputCommand.find("floyd") != -1:
		makeGraph(inputFileName)
		distances = floyd(Graph)
		for i in range(0,len(distances)):
			print(distances[i])
		if DEBUG:
			print("Floyd")
	elif inputCommand.find("dijkstra") != -1:
		param = int(inputCommand.split(" ",2)[1])
		result = dijkstra(Graph,param)
		print(result)
		if DEBUG:
			print("Dijkstra");
	elif inputCommand == "help":
		printHelp()
	elif inputCommand == "pg":
		printGraph()
