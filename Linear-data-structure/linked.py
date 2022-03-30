#prooggram to link the nodes an display
class Node:
   def __init__(self, dataval):
      self.dataval = dataval
      self.nextval = None

class LinkedList:
   def __init__(self):
      self.headval = None

   def listprint(self):
      printval = self.headval
      while printval is not None:
         print (printval.dataval)
         printval = printval.nextval

list = LinkedList()
list.headval = Node(1)
e2 = Node(2)
e3 = Node(3)

# Link first Node to second node
list.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3

list.listprint()



#proggram to 