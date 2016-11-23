import heap




heap = heap.Heap()

commands = {"deletemin": 0,"insert": 1, "makenull": 2, "inorder":3,"preorder":4,"postorder":5,"min": 6, "sort":7,"help":8}

helpText = "help - Prints this list\nmakenull - Clears the heap\ninsert  - Inserts the number into the heap\nmin - Prints the current min on the heap\ninorder - Prints heap in inorder\npreorder - Prints heap in preorder\npostorder - Prints heap in postorder\ndeletemin - Removes min from the heap\nsort - Calls deletemin repeatedly to print out sorted numbers\nexit - Exits the program (also Crtl-D exits)"

print("Welcome to the Heap\nThe List of Commands is below, type help to see them again.")
print(helpText)
command = raw_input()
while command != "":
	
	inputSplit = command.split(" ")
	if inputSplit[0] not in commands:
		print("Bad Command - type help for commands")
		command = raw_input()
		continue
	print(inputSplit[0])
	cmd = commands[inputSplit[0]]
	if cmd == 0:
		heap.deletemin()
	if cmd == 1:
		heap.insert(int(inputSplit[1]))
	if cmd == 2:
		heap.makenull()
	if cmd == 3:
		heap.inorder()
	if cmd == 4:
		heap.preorder()
	if cmd == 5:
		heap.postorder()
	if cmd == 6:
		heap.min()
	if cmd == 7:
		size = 1
		while(size > 0):
			size = heap.deletemin()
	if cmd == 8:
		heap.help()
	command = raw_input()

