class Node:
    def __init__(self,data):
       self.data=data
       self.next=None


class List:
    def __init__(self):
       self.head=None



def insert_at_beginning(self,data):
    new_node=Node(data)
    new_node.next=self.head
    self.head=new_node



