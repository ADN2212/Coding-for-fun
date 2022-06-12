import tkinter as tk
from random import choice, randint
from tkinter import messagebox#para poder sacar ventanas emergentes.
#from time import sleep

#--------------------------------------------------------variables---------------------------------------------------------------------------
ventana = tk.Tk()
ventana.geometry("550x500")
ventana.title("Random Walks")
ventana.resizable(False, False)

lienzo = tk.Canvas(ventana, width = 450, height = 450, bg = "black")
lienzo.pack()#si no lo ponia asi el metodo create_line no me funcionba (por que?)

numero_pasos = tk.StringVar()

cuadro_pasos = tk.Entry(ventana, textvariable = numero_pasos).pack()

numero_pasos.set("Cuantos pasos?")

start_point = [225, 225]

end_point = [0, 0]

color = ""

#proceso = 0
#--------------------------------------------------------Funciones-----------------------------------------------------------------------------------------------------------
def crear_circulo(lista_centro, radio):
	global lienzo
	lienzo.create_oval(lista_centro[0]-radio, lista_centro[1] + radio, lista_centro[0] + radio, lista_centro[1] - radio, fill="blue")#Ver el funcionamiento del metodo create_oval

#crear_circulo(start_point, 5)#Fijar el punto de partida en la pantalla.

def color_aleatorio():
	return choice(["green", "red", "gold", "silver", "brown", "purple"])



def dar_un_paso():
	global start_point
	global end_point
	global lienzo
	direccion = choice([1, 2])#para elejir si se movera en sentido vertical u horizontal

	if direccion == 1:
		end_point[0] = start_point[0] + choice([-10, 10])#Aumenta o disminuye la coordenada X del punto
		end_point[1] = start_point[1]

	elif direccion == 2:
		end_point[0] = start_point[0]
		end_point[1] = start_point[1] + choice([-10, 10])#Aumenta o disminuye la coordenada Y del punto

#Para que las coordenadas no se salgan del canvas
	if end_point[0] > 450:
		end_point[0] = end_point[0] - 10
	
	if end_point[0] < 0:
		end_point[0] = end_point[0] + 10

	if end_point[1] > 450:
		end_point[1] = end_point[1] - 10

	if end_point[1] < 0:
		end_point[1] = end_point[1] + 10
		
	lienzo.create_line(start_point[0], start_point[1], end_point[0], end_point[1], fill = color)	
	print("Desde {} hasta {}".format(start_point, end_point))
	start_point = end_point
	end_point = [0, 0]


def caminar():
	global numero_pasos
	global start_point
	global color
	color = color_aleatorio()
	crear_circulo(start_point, 5)
	try:
		n = int(numero_pasos.get())
		for i in range(n):
			dar_un_paso()
			#sleep(0.5)
		crear_circulo(start_point, 5)	
	except:
		messagebox.showwarning("Error !!", "Por favor introdusca un numero entero")


def ejecutar():
	global numero_pasos
	global color
#	color = color_aleatorio()#si lo hago aqui tendra un unico color todo el camino. 
	global start_point
	
	try:
		n = int(numero_pasos.get())#Esta todo dentro del bloque del try-except, pero esta es la linea que esta supuesta a lazar el error.
		start_point = [randint(0, 450), randint(0, 450)]#Para que el punto de partida sea aleatorio.
		crear_circulo(start_point, 5)
		caminar_2(n)
				
	except:
		messagebox.showwarning("Error !!", "Por favor introdusca un numero entero")


def caminar_2(pasos):
#	global proceso
	global lienzo
	global start_point
	global color
	color = color_aleatorio()#Si la activo aqui cambia de color a cada paso.

	if pasos > 0: 
		dar_un_paso()
		lienzo.after(10, caminar_2, pasos-1)#aqui hay recursividad, ya que la funcion se llamara a si misma despues de 10 milisegundos.
#														el tercer argumento de el metodo affter es el argumento que sesivira la funcion caminar_2 despues de que pase el tiempo.
	else:
#		lienzo.after_cancel(proceso)
		crear_circulo(start_point, 5)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

boton = tk.Button(ventana, text = "¡Go Walk!", command = ejecutar)
boton.pack()

ventana.mainloop()


























