class Node:
	
	# Class to create nodes of linked list
	# constructor initializes node automatically
	def __init__(self,data):
		self.data = data
		self.next = None
	
class Stack:
	
	# head is default NULL
	def __init__(self):
		self.head = None
	
	# Checks if stack is empty
	def isempty(self):
		if self.head == None:
			return True
		else:
			return False
	
	# Method to add data to the stack
	# adds to the start of the stack
	def push(self,data):
		
		if self.head == None:
			self.head=Node(data)
			
		else:
			newnode = Node(data)
			newnode.next = self.head
			self.head = newnode
	
	# Remove element that is the current head (start of the stack)
	def pop(self):
		
		if self.isempty():
			return None
			
		else:
			# Removes the head node and makes
			#the preceding one the new head
			poppednode = self.head
			self.head = self.head.next
			poppednode.next = None
			return poppednode.data
	
	# Returns the head node data
	def peek(self):
		
		if self.isempty():
			return None
			
		else:
			return self.head.data
	
	# Prints out the stack	
	def display(self):
		
		iternode = self.head
		if self.isempty():
			print("Stack Underflow")
		
		else:
			
			while(iternode != None):
				
				print(iternode.data,"->",end = " ")
				iternode = iternode.next
			return
		
# Driver code
MyStack = Stack()

MyStack.push(11)
MyStack.push(22)
MyStack.push(33)
MyStack.push(44)

# Display stack elements
MyStack.display()

# Print top element of stack
print("\nTop element is ",MyStack.peek())
# Delete top elements of stack
MyStack.pop()
# Display stack elements
MyStack.display()

# Print top element of stack
print("\nTop element is ", MyStack.peek())








################################################################################################################################################################
def priorty(ch):
    if ch in "+-":
        return 1
    elif ch in "^":
        return 3
    elif ch in "*/":
        return 2
    else:
        return 0
def infix(inf):
    i = 0
    st = []
    pos = ""
    for ch in inf:
        ch == "("
        if (ch == "("):
            st.append(ch)
        elif(ch.isalpha()):
            pos += ch
        elif(ch == ")"):
             k=st.pop()
             while(k != ")"):
                pos += k
                k =st.pop()
        elif ch in "+-/%*^":
            if not st:
                st.append(ch)
            elif priorty(ch) <= priorty(st[-1]):
                pos += st.pop()
                while (st and priorty(ch) <= priorty(st[-1])):
                    pos += st.pop()
                st.append(ch)       
            
        else:
            st.append(ch)
    while(st):
        pos+= st.pop()
        
    print (pos)
inn = input("Enter: ")
print(inn)
infix(inn)


