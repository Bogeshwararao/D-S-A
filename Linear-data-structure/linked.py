#linked list
class Node:
   def __init__(self, dataval):
      self.dataval = dataval
      self.nextval = None

class LinkedList:
   def __init__(self):
      self.headval = None
#up to here to craete a node 
   def listprint(self):
      while self.headval is not None:
         print (self.headval.dataval)
         self.headval= self.headval.nextval
#the above code is to display 
#proggram to add the node at the beginning
def add_begging(self, newdata):
       new_node=Node(newdata)

       
       new_node.nextval=self.headval
       self.headval=new_node




list = LinkedList()

list.headval = Node(1)
e2 = Node(2)
e3 = Node(3)
# Link first Node to second node
list.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3

list.listprint()