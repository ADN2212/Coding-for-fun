"""
Como lo dice el titulo, ordena una liked list creada de forma aleatoria usando el algoritmo de ordenamiento Quick Sort.
"""

from random import randint

class Node:
	"""
	An object for storing a single node of a linked list.
	Models two attributes- data and the link to the next node in the list.

	"""
	data = None
	next_node = None

	def __init__(self, data):
		self.data = data

	def __repr__(self):#cuando se mustre un objeto de esta clase de manera directa, aparecera esta representacion, de ahi __repr__
		return "<Node data: %s>" % self.data
#		return "Node data: {}".format(self.data)#tambiense puede usar format()


class LinkedList:
	"""
	Single linked list
	"""
	def __init__(self):
		self.head = None

	def is_empty(self):
		return self.head == None

	def size(self):
		"""
		returns the number of nodes in the lsit
		takes linear time.
		"""
		current = self.head
		count = 0

		while current != None:
			count += 1
			current = current.next_node

		return count	

	def add(self, data):
		"""
		Adds new Node containing data at head of the list
		Takes O(1) (constant) time.
		"""
		next_node = Node(data) 
		next_node.next_node = self.head#the firts node will be the next of the one that we are adding, it means the new will be the firts.
		self.head = next_node


	def search(self, key):
		"""
		Searcho for the firts node containing data that mactches they key
		returns the node or 'None' if not found.
		Takes O(n) (Linear) time. 
		"""
		current = self.head#this is a node

		while current != None:

			if current.data == key:
				return current

			else:
				current = current.next_node

		return None

	def insert(self, data, index):
		"""
		insert a new node containing data at the index position.
		insertion takes constant time --> O(1), but finding the node takes linear time --> O(n)

		takes overall O(n)
		"""
		if index == 0:
			self.add(data)#if index is equeal to 0 it (the new node) will be the head. 	

		if index > 0:
			new = Node(data)
			position = index
			current = self.head

			while position > 1:
				current = current.next_node
				position -= 1

			#Once we have got the node in the position we want to insert our new node, we chage the references:	
			prev = current
			next_node = current.next_node
			prev.next_node = new
			new.next_node = next_node	

	def remove(self, key):
		"""
		Removes Node containing data that matches the key 
		Returns the node or None if key does not exist
		Takes O(n) time.
		"""

		current = self.head
		previous = None
		found = False

		while current and not found:
			if current.data == key and current is self.head:
				found = True# stops the loop
				self.head = current.next_node#the next node in the linked list will be the new head.	

			elif current.data == key:
				found = True
				previous.next_node = current.next_node

			else:
				previous = current
				current = current.next_node

		return current		

	def node_at_index(self, index):

		if index == 0:
			return self.head

		else:
			current = self.head	
			position = 0

			while position < index:
				current = current.next_node
				position += 1

			return current#the node that is at the index that we wanted.	

	def revertida(self):
		"""
		Este metodo sirve para inverir el orden de una linked_list
		retorna una linked list invertida dejando la original sin cambios.
		"""
		if self.is_empty() == True or self.size() == 1:
			return self

		Linked_List_reverted = LinkedList()

		actual = self.head

		while actual:
			Linked_List_reverted.add(actual.data)
			actual = actual.next_node

		return Linked_List_reverted	



	def __repr__(self):
		"""
		Return a string representation of the list
		takes O(n) (linear) time.
		"""
		if self.is_empty():
			return "Linked List Vacia"

		nodes = []
		current = self.head

		while current != None:
			
			if current is self.head:
				nodes.append("[Head: %s]" % current.data)#esto queda mas claro con format()(at least to me).

			elif current.next_node is None:
				nodes.append("[Tail: %s]" % current.data)

			else:
				nodes.append("[%s]" % current.data)

			current = current.next_node

		return "-->".join(nodes)#yo lo hubiera hecho con un ciclo.		

def random_linked_list(longitud):
	"""
	Esta funcion crea una linked list con valores aleatorios en sus nodos, servirá para poner a prueba el Algoritmo.
	"""
	nodes = []
	lkl = LinkedList()

	if longitud <= 0:
		return lkl

	if longitud == 1:
		lkl.head = Node(randint(0, 1000))
		return lkl
	
	else:
		
		for i in range(longitud):
			nodes.append(Node(randint(0, 1000)))#Solo trabajar con enteros positivos para simplificar las cosas XD

		lkl.head = nodes[0]#Hacer el primer nodo creado la cabeza de la linked list.
		lkl.head.next_node = nodes[1]

		for i in range(1, len(nodes) - 1):
			nodes[i].next_node = nodes[i + 1]#Conectar los nodos.

		return lkl



def  copiar_lkl(lkl):
	"""
	Esta funcion sirve para copiar una lkl tomando sus nodos y creando nuevos para que al
	hacer cambios en esta no se cambie la lkl original.
	"""
	copia = LinkedList()

	cabeza = lkl.head

	while cabeza:
		copia.add(cabeza.data)
		cabeza = cabeza.next_node
	
	return copia.revertida()

def unir_linked_lists(menor_que_el_pivote, pivote, mayor_que_el_pivote):
	"""
	Esta funcion sirve para unir las listas conectadas que se van retornado recursivamente.
	"""

	merged_linked_list = LinkedList()

	menor_p = copiar_lkl(menor_que_el_pivote)#Esto para evitar cabiar las lkl que resive esta funcion como argumento. 
	mayor_p = copiar_lkl(mayor_que_el_pivote)	
	nuevo_pivote = pivote#Para no cambiar las propiedades del que se da como argumento.

	if menor_p.is_empty() and mayor_p.is_empty():
		merged_linked_list.head = nuevo_pivote
		return merged_linked_list

	elif menor_p.is_empty():
		merged_linked_list.head = nuevo_pivote
		nuevo_pivote.next_node = mayor_p.head
		return merged_linked_list
	
	elif mayor_p.is_empty():
		merged_linked_list.head = menor_p.head
		menor_p.node_at_index(menor_p.size()-1).next_node = nuevo_pivote#El nodo final sera el pivote.
		nuevo_pivote.next_node = None
		return merged_linked_list

	else:
		merged_linked_list.head = menor_p.head
		merged_linked_list.node_at_index(merged_linked_list.size()-1).next_node = nuevo_pivote		
		nuevo_pivote.next_node = mayor_p.head

		return merged_linked_list

def QSforLinkedList(Linked_List):

	"""
	Esta es la funcion principal que se encarga de aplicar el algoritmo Qucik_Sort a una likend_list.
	"""
	
	if Linked_List.size() == 1 or Linked_List.is_empty():
		return Linked_List# Esta es la 'Stopping Condition'

	menor_que_el_pivote = LinkedList()

	mayor_que_el_pivote = LinkedList()

	pivote = Linked_List.head# tomar el primer valor de la linked_list como pivote.
	
	actual = pivote.next_node# Este es el nodo que le sigue a la cabeza.

	while actual != None:
		if actual.data <= pivote.data:
			menor_que_el_pivote.add(actual.data)

		else:	
			mayor_que_el_pivote.add(actual.data)

		actual = actual.next_node

	menor_que_el_pivote = menor_que_el_pivote.revertida()#Esto es devido a como trabaja el metodo "add()"
	mayor_que_el_pivote = mayor_que_el_pivote.revertida()
#	print("Menores = {}, Pivote = {}, Moyores = {}".format(menor_que_el_pivote, pivote, mayor_que_el_pivote))

	return unir_linked_lists(QSforLinkedList(menor_que_el_pivote), pivote, QSforLinkedList(mayor_que_el_pivote))


def verificar_iterativa(linked_list):
	"""
	Verifica que la liked list esta ordenada de forma ascendente.
	retorna True o False 
	"""
#	print(linked_list)
	actual = linked_list.head
#	ascendente = True#supongo que esta ordenada de entrada
#	print("Actual node = {}, Next Node = {}".format(actual, actual.next_node))

	while actual != None and actual.next_node != None:
#		print("Entró")
		if not(actual.data <= actual.next_node.data):
			return False

		actual = actual.next_node

	return True


unsorted_lkl = random_linked_list(10)#Ojo: Con una linked list de 100,000 nodos se alcanza la "maximun recursion dethp" 
sorted_lkl = QSforLinkedList(copiar_lkl(unsorted_lkl))

print("A Linked List = {}\n\nHas been sorted = {}".format(unsorted_lkl, sorted_lkl))

#print(verificar_iterativa(unsorted_lkl))
#print(verificar_iterativa(sorted_lkl))


"""
lkl_normal = random_linked_list(15)
lkl_invertida = lkl_normal.revertida()

print("Una linked List = {}\n\nHa sido invertida = {}".format(lkl_normal, lkl_invertida))
"""




































	











