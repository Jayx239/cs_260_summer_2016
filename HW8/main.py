import math

def print_approx(length):
    print( "Approx Min: " + str(math.ceil(math.log(math.factorial(length),2))))

def swap(values,index1,index2):
    temp = values[index1]
    values[index1] = values[index2]
    values[index2] = temp


def print_values(values):
    out = "["
    for i in range(0,len(values)-1):
        out +=  str(values[i]) + ", "
    out += str(values[len(values)-1]) + "]"
    print(out)

def bubble_sort(values):
    list_len = len(values)
    num_comps = 0 
    swapped = 1
  #  for i in range(len(values)-1,0,-1):
    while swapped != 0:
        swapped = 0
        for j in range(1,list_len):
            num_comps+=1
            if int(values[j-1]) > int(values[j]):
                swapped = 1
                swap(values,j-1,j)
            #    num_comps+=1 
           # if swapped ==  0 and j == i:
                #break
            #num_comps+=1
    print_values(values)
    print("Comparisons: " + str(num_comps))
    print_approx(len(values))

def insert_sort(values):
    num_comps = 0
    for i in range(1,len(values)):
        j = i
        while j > 0 and int(values[j-1]) > int(values[j]):
            num_comps+=1
            swap(values,j-1,j)
            j -= 1
        if j > 0:
            num_comps+=1
    print_values(values)
    print("Comparisons: " + str(num_comps))
    print_approx(len(values))
merge_comp_count = 0
def merge_sort(A):
    global merge_comp_count
    merge_comp_count = 0
    m_sort(A,0,len(A)-1);
    print_values(A)
    print("Comparisons: " + str(merge_comp_count))
    print_approx(len(A))
def m_sort(a,start,stop):
    global merge_comp_count
    if start >= stop:
        #merge_comp_count += 1
        return
    middle = start + int(math.floor((stop-start)/2))
    m_sort(a,start,middle)
    m_sort(a,middle+1,stop)
    merge(a,start,middle,stop)

def merge(A,start,middle,stop):
    global merge_comp_count
    i = start
    j = middle+1
    Aux = A[:]
    for k in range(start,stop+1):
        if i > middle:
            A[k] = Aux[j]
            j += 1
            #merge_comp_count+=1
        elif j > stop:
            A[k] = Aux[i]
            i +=1
            #merge_comp_count+=2
        elif int(Aux[j]) > int(Aux[i]):
            A[k] = Aux[i]
            i +=1
            merge_comp_count+=1
        else:
            A[k] = Aux[j]
            j +=1
            merge_comp_count+=1
quick_num_comps = 0

def quick_sort(A):
    global quick_num_comps
    quick_num_comps = 0
    qsort(A,0,len(A)-1)
    print_values(A)
    print("Comparisons: " + str(quick_num_comps))
    print_approx(len(A))
def qsort(A,start,stop):
    global quick_num_comps
    if start < stop:
        p = partition(A,start,stop)
        qsort(A,start,p-1)
        qsort(A,p+1,stop)

def partition(A,start,stop):
    global quick_num_comps
    pivot = A[stop]
    i = start
    for j in range(start,stop):
        if not(int(A[j]) > int(pivot)):
            swap(A,i,j)
            i+=1
        quick_num_comps +=1

    swap(A,i,stop)
    return i

def printHelp():
    print("Commands:\nhelp - Prints this menu\nexit or CTRL-D - Exits the program\nsort_method int_list - Enter a sort method followed by a list of space sperated integers to sort them\nPossible Sort Methods: bubblesort insertion mergesort quicksort")

print("Welcome to the sorting thunderdome\nThis program is used to compare sorting methods")

printHelp()
while True:
    inputCommand = ""
    #if Python3:
    inputCommand = raw_input("Command: ")
    #else:
     #   inputCommand = raw_input("Enter command: ")                               
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
        print("Running Prim's Algorithm\nStarting Node: " + str(param))
        prim(Graph,param)
    elif inputCommand.find("kruskal") != -1:
        print("Running Kruskal's Algorithm")
        kruskal(Graph)
    elif inputCommand.find("bubblesort") != -1:
        print("Using Bubble Sort:")
        numbers = inputCommand.split(" ",inputCommand.count(" "))
        numbers.remove("bubblesort")
        bubble_sort(numbers)
    elif inputCommand.find("insertion") != -1:
        print("Using Insertion Sort:")
        numbers = inputCommand.split(" ", inputCommand.count(" "))
        numbers.remove("insertion")
        insert_sort(numbers)
    elif inputCommand.find("mergesort") != -1:
        print("Using Merge Sort:")
        numbers = inputCommand.split(" ", inputCommand.count(" "))
        numbers.remove("mergesort")
        merge_sort(numbers)
    elif inputCommand.find("quicksort") != -1:
        print("Using Quick Sort:")
        numbers = inputCommand.split(" ", inputCommand.count(" "))
        numbers.remove("quicksort")
        quick_sort(numbers)
    elif inputCommand == "help":
        printHelp()
    elif inputCommand == "pg":
        printGraph()
