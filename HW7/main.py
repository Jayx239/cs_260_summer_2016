#Flags
Python3 = False	#Modifys input method, Tux runs 2.7.6, Autogradr runs 3.0
DEBUG = False#True

#Globals
DistinctNodes = None
Graph = [[None]]

def prim(Graph,start_node):
	G = Graph
	global DistinctNodes
	distance = [float("inf")for i in range(0,len(G))]
	distance[start_node] = 0
	dNodes = DistinctNodes
	dNodes.remove(start_node)
	numNodes = len(dNodes);
	lastNode = start_node

	while len(dNodes) > 0:
		smallestWeight = float("inf")
		newNode = -1
		smallI = -1
		smallJ = -1
		for i in range(0,len(G)):
			for j in range(0,len(G)):
				if i not in  dNodes or j in dNodes:
					continue
				if G[j][i] < smallestWeight:
					smallestWeight = G[j][i]
					newNode = i
					smallestI = j
					smallestJ = i
				if G[i][j] < smallestWeight:
					smallestWeight = G[i][j]
					newNode = i
					smallestI = i
					smallestJ = j
		if smallestWeight == float("inf"):
			break
		G[smallestI][smallestJ] = float("inf")
		G[smallestJ][smallestI] = float("inf")
		print("Added " + str(newNode))
		print("Using Edge ["+str(smallestI) + "," + str(smallestJ) + "," + str(smallestWeight)+ "]")
		dNodes.remove(newNode)
		lastNode = smallestI
#		smallest[-1,-1,float("inf")]
#		for i in range(0,len(dNodes)):
#			for j in range(0,len(dNodes)):
#				Di = dNodes[i]
#				Dj = dNodes[j]
#				if G[Di][Dj] < smallest[2]:
#					smallest = [Di,Dj,float(G[Di][Dj])]
#		smallNode = smallest[0]
#		smallestNode2 =
#		for i in range(0,len(dNodes)):
#			if G[smallNode][i] > G[smallestNode2

def kruskal(Graph):
	G = Graph
	global DistinctNodes
	distance = [float("inf")for i in range(0,len(G))]
	dNodes = DistinctNodes
	numNodes = len(dNodes);
	distinctEdges = None

	while len(dNodes) > 0:
		smallestWeight = float("inf")
		newNode = -1
		smallI = -1
		smallJ = -1
		for i in range(0,numNodes):
			for j in range(0,numNodes):
				if j not in dNodes and i not in dNodes:
					continue
				if G[j][i] < smallestWeight:
					smallestWeight = G[j][i]
					newNode = i
					smallestI = j
					smallestJ = i
				if G[i][j] < smallestWeight:
					smallestWeight = G[i][j]
					newNode = i
					smallestI = i
					smallestJ = j
		if smallestWeight == float("inf"):
			break
		G[smallestI][smallestJ] = float("inf")
		G[smallestJ][smallestI] = float("inf")
		if distinctEdges is None or not(smallestI in distinctEdges[0] and smallestJ in distinctEdges[0]):
			print("Select Edge ["+str(smallestI) + "," + str(smallestJ) + "," + str(smallestWeight)+ "]")

		if distinctEdges is None:
			distinctEdges = [[smallestI,smallestJ]]
		else:
			distinctEdges.append([smallestI,smallestJ])


		lastIndex = len(distinctEdges) -1	
		for i in range(len(distinctEdges)-1,0,-1):
			if (smallestI in distinctEdges[i-1] or smallestJ in distinctEdges[i-1]) and (smallestI in distinctEdges[lastIndex] or smallestJ in distinctEdges[lastIndex]):
				for node in distinctEdges[lastIndex]:
					distinctEdges[i-1].append(node)
			#	lastIndex = i-1
			#	if len(distinctEdges[i]) != 0:
				#	distinctEdges[i-1].append(nodes in distinctEdges[i])
				distinctEdges.remove(distinctEdges[lastIndex])
				lastIndex = i-1
		count = 0
		for i in range(0,numNodes):
			if i in distinctEdges[0]:
				count+=1
#		if count >= numNodes:
#			break
#		print(str(distinctEdges) + "\n")	
		if len(distinctEdges) == 1 and count >= numNodes:
			break
		#if smallestI in dNodes:
		#	dNodes.remove(smallestI)
	#	if smallestJ in dNodes:
	#		dNodes.remove(smallestJ)
	#	lastNode = smallestI

	

#def makeSet(v):
	
#def findSet(u):
	
#def union(u,v):
	


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
#	print("Possible Commands are: \ndijkstra x - Runs Dijkstra starting at node X. X must be an integer\nfloyd - Runs Floyd's algorithm\nhelp - prints this menu\nexit or ctrl-D - Exits the program")
	print("Commands: \nexit or ctrl-d - quits the program\nhelp - prints this menu\nprim integer_value - run's Prim's algorithm starting at node given\nkruskal - runs Kruskal's algorithm")
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

print("Welcome to Minimum Spanning Tree Finder")
inputFileName = ""
if DEBUG:
	inputFileName = "input1.txt"
else:
	if Python3:
		inputFileName = input("Give the file name graph is in: ")
	else:
		inputFileName = raw_input("Give the file name graph is in: ")

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
		break
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
	elif inputCommand.find("prim") != -1:
		param = int(inputCommand.split(" ",2)[1])
		prim(Graph,param)
	elif inputCommand.find("kruskal") != -1:
		print("Running Kruskal's Algorithm")
		kruskal(Graph)	
	elif inputCommand == "help":
		printHelp()
	elif inputCommand == "pg":
		printGraph()
