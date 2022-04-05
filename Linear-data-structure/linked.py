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

   def delbeg(self):
      if self.headval is None:
         print("ll is empty")
      else: self.headval=self.headval.nextval
   def delend(self):
      if self.headval is None:
       print("ll is empty")
      elif self.headval is None:
         self.headval=None
      else:
         n=self.headval
      while n.nextval.nextval is not None:
         n=n.nextval
      n.nextval=None

list = LinkedList()

list.headval = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)
e5 = Node(5)
e6 = Node(6)
# Link first Node to second node
list.headval.nextval = e2
# Link second Node to third node
e2.nextval = e3
# Link third Node to fourth node 
e3.nextval = e4
# Link four Node to five node
e4.nextval = e5
e5.nextval = e6
list.delbeg()
list.delend()
list.listprint()

