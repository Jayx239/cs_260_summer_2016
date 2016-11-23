import node
import stack
# Node Tests ---------------------------
#Initialize a new node with value of 17
print("aNode = node.node(17)")
aNode = node.node(17)

# print function and get_val function
print("aNode.print_val()")
aNode.print_val()
print("aNode.get_val()")
print(aNode.get_val())

# Set val method
aNode.set_val(12)
print("aNode.set_val(12)")

# Verification
print("aNode.print_val()")
aNode.print_val()
print("aNode.get_val()")

print(aNode.get_val())

# set_next node
print("aNode.set_next(node.node(19))")
aNode.set_next(node.node(19))

#print values
print("aNode.get_next().print_val()")
aNode.get_next().print_val()
print("print(aNode.get_next().get_val())")
print(aNode.get_next().get_val())

# Stack Tests ---------------------------
# Create new stack with base node being aNode
print("aStack = stack.stack(aNode)")
aStack = stack.stack()

print("aStack.push(aNode)")
aStack.push(aNode)

print("aStack.top().get_val()")
print(aStack.top().get_val())

print("aStack.top().get_next().get_val()")
print(aStack.top().get_next().get_val())

print("aStack.pop().get_val()")
print(aStack.pop().get_val())

print("aStack.top().get_val()")
print(aStack.top().get_val())

print("aStack.push(aNode)")
aStack.push(aNode)

print("aStack.top().get_val()")
print(aStack.top().get_val())

print("aStack.top().get_next().get_val()")
print(aStack.top().get_next().get_val())
