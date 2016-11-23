import math
ADDITIONS=0
CLASSIC_CALC=0
memory= {None:None}

def fib_mem(n):
	if(memory.has_key(n)):
		return memory[n]
	if n == 0:
                return 0
        if n == 1:
                return 1
        return add(fib_classic(n-1),fib_classic(n-2))

	memory[n]=fib_mem(n-1)+fib_mem(n-2)
	return memory[n]
def add(a,b):
	global ADDITIONS
	ADDITIONS+=1
	return a+b

def fib_closed(n):
        out = ((math.pow(1+math.sqrt(5),n)-math.pow(1-math.sqrt(5),n))/(math.pow(2,n)*math.sqrt(5)))
	return out

def fib_classic(n):
        if n == 0:
                return 0
        if n == 1:
                return 1
        return add(fib_classic(n-1),fib_classic(n-2))

def fib_loops(n):
	if n==0:
		return 0
	if n==1:
		return 1
	a=0
	b=1
	fib_num=0
	for i in range(1,n-1):
		fib_num += add(a,b)
		temp = a
		a = add(a,b)
		b = temp
	add(fib_num,1)
	return fib_num



for i in range(0,10):
	print("Computing the " +str(i) + "th Fibonacci Number:")
	print("The closed form finds: " + str(fib_closed(i)))
	print("The recursive definition finds: " + str(fib_classic(i)))
	print("Additions needed for recursive definition : " + str(ADDITIONS))
	ADDITIONS=0
	print("The loop definition finds: " + str(fib_loops(i)))
	print("Additions needed for loop definition : " + str(ADDITIONS))

