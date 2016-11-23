import node
import stack

NONE = 0
INCLUDED = 1
EXCLUDED = 2

def knapsack(target,weights):
	NONE = 0
	INCLUDED = 1
	EXCLUDED = 2

#        print("start")
	candidate = 0
	winflag = False
	Stack = stack.stack()
	Stack.push(node.node(NONE))
 #       print(str(NONE))
	total = 0
	while(not Stack.empty()):
        	if winflag:
                        #print(Stack.pop().get_val())
                        if Stack.top().get_val() == INCLUDED:
				#total = total + weights[candidate]
				print(weights[candidate])#Stack.print_stack()
                        candidate = candidate - 1
                        Stack.pop()
                     #   print("winflag hit")
               	elif target == 0:
                       	winflag = True
                        candidate = candidate - 1
       	                Stack.pop()
               	      #  print("target == 0")
                elif (((target < 0) and (Stack.top().get_val() == NONE)) or (candidate >= len(weights))):
			candidate = candidate - 1
               	        Stack.pop()
                       #	print(target)
#			print("(((target < 0) and (Stack.top() == NONE)) or (candidate > target))")
                else:	
			if Stack.top().get_val() == NONE:
                                target = target - weights[candidate]
                                candidate = candidate + 1
                                Stack.pop()
                                Stack.push(node.node(INCLUDED))
                                Stack.push(node.node(NONE))
                        #        print("first else if")
                        elif Stack.top().get_val() == INCLUDED:
                                target = target + weights[candidate]
                                candidate = candidate + 1
                                Stack.pop()
                                Stack.push(node.node(EXCLUDED))
				Stack.push(node.node(NONE))
                         #       print("second if in else")
			else:
                                #if stack.top() == EXCLUDED:
                                Stack.pop()
                                candidate = candidate - 1
                          #      print("else in else")
                   #     print("Else")
               # if Stack.empty():
                #        print("break")
       	         #       break
               # print("Candidate Number: " + str(candidate) + "\n")
	#	print(str(target))
#	print(total)
#uIn = [1,5,2,9,4]
#uIn2 = [90,73, 34, 50, 67, 18, 81, 24, 55, 50, 74, 61] 
#stack = stack.stack(node.node(uIn[0]))
#for i in range(0,len(uIn)):
#	stack.push(node.node(uIn[i]))
#stack.print_stack()
#knapsack(366,uIn2)

#stack.print_stack()
print("Welcome to Knapsack Solver\nTo quit, give an empty list of weights.")
while True:
	next_entry = raw_input("Give a list of weights seperated by commas: ").replace(" ","")
	if next_entry == "":
		break;
	
	next_entry_set = next_entry.split(",",next_entry.count(","))
	entry_int_array = []
	index = 0
	for entry in next_entry_set:
		#print(int(entry))
		entry_int_array.append(int(entry))
	#for entry in entry_int_array:
		#print(entry)
	next_entry = int(raw_input("Give the target number to reach: "))
	print("Attempting to fill knapsack: ")
	knapsack(next_entry,entry_int_array)

