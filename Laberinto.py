"""

Juego del laberinto inspirado en maze.c del curso de seguridad informatica.

"""

#Variables:
pasos = 0

personaje = "$"

#posicion actual del personage.
f, c = 1, 1

#posicion anterior del personage.
f0, c0 = 1, 1

continua = True

laberinto = [  	['+', '-', '+', '-', '-', '-', '+', '-', '-', '-', '+'],
			   	['|', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', '#', '|'],
				['|', ' ', '|', ' ', '-', '-', '+', ' ', '|', ' ', '|'],
				['|', ' ', '|', ' ', ' ', ' ', '|', ' ', '|', ' ', '|'],
				['|', ' ', '+', '-', '-', ' ', '|', ' ', '|', ' ', '|'],
				['|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', '|'],
				['+', '-', '-', '-', '-', '-', '+', '-', '-', '-', '+'] ] 


#Funciones:

def show_maze(maze):
	"""
	Muestra el laberinto.
	"""
	global f, c, pasos

	str_maze = "Posición Actual: Fila = {}, Columna = {}, Número de Pasos: {} \n\n".format(f + 1, c + 1, pasos)

	for fila in maze:
		for ch in fila:
			str_maze += ch
		str_maze += "\n"				
	
	print(str_maze)


def mover(direccion):
	"""
	reposiciona el personaje en funcion de parametro que recibe.
	"""
	global laberinto, f, c, personaje, f0, c0

	f0, c0 = f, c

	laberinto[f0][c0] = "."#Da la impresión de que va dejando un rastro.

	if direccion == "w":
		f -= 1

	if direccion == "s":
		f += 1

	if direccion == "d":
		c += 1

	if direccion == "a":
		c -= 1			
	
	#laberinto[f][c] = personaje

	return None# is a void function.


def continue_or_not(f, c):
	"""
	Determina si el usuario puede seguir jugando o no.
	"""
	global laberinto

	if laberinto[f][c] in ["+", "-", "|", "#"]:
		return False
	
	else:
		return True

			


laberinto[f][c] = personaje 

print("Ay coñ*, estamos atrapados en un laberinto, busquemos la forma de salir!")
print("Usa las teclas: 'w', 's', 'd' y 'a' para mover hacia arriba, abajo, derecha y izquierda respectivamente")
show_maze(laberinto)

movimiento = ""

while continua:

	movimiento = input("Ir en dirección: ")

	if not (movimiento in ["w", "s", "d", "a"]):
		print("Whut? dirección no valida")
		show_maze(laberinto)

	else:
		pasos += 1
		mover(movimiento)
		continua = continue_or_not(f, c)
		
		#print(continua)

		if not(continua):
			if laberinto[f][c] == "#":

				laberinto[f][c] = "♥"
				show_maze(laberinto)			
				print("Has Ganado :)")
				
			else:
				laberinto[f][c] = "X"
				show_maze(laberinto)			
				print("Has Perdido :(")
		
		else:
			laberinto[f][c] = personaje
			show_maze(laberinto)
		


		












































