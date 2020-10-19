class L(object):
	"""docstring for L"""
	def __init__(self, node):
		self.node=node
		self.next=None	


a=L(11)
b=L(52)
a.next=b
c=L(18)
b.next=c

# class Node(obj):

def traversal( head ):
	curNode = head
	while curNode is not None :
		print (curNode.node)
		curNode = curNode.next

traversal(a)

# 	def __init__(self, el,next_add):
# 		self.el=el
# 		self.next=next_add
# def add_first(L,e):
# 	newest=Node(e)
# 	newest.next=L.e
# 	L.head=newest
# 	L.size=L.size+1
# def add_last(L,e):
# 	newest=Node(e)
# 	newest.next=None
# 	L.tail.next=newest
# 	L.tail=newest
# 	L.size=L.size+1
# def remove_first(L):
# 	if L.head==None:
# 		assert 1>2,"head cannot empty"
# 	L.head=L.head.next
# 	L.size=L.size-1

		
# class linkedlist(object):
# 	"""docstring for linkedlist"""
# 	def __init__(self,Node,e):
# 		self.node=Node
# 		self.e=
# 	def add_first(self)
# 		