from tkinter import *
from random import choice
from tkinter import messagebox


ventana = Tk()
ventana.title("El Ahorcado")
ventana.geometry("500x250")
ventana.config(bg = "blue")
#---------------------------------------------------------------Variables--------------------------------------------------------------------------------

palabras = [
"Abrir", "Boquilla", "Recolector", "Esmeralda", "Cuadra", "Molde", "Caballo", "Carro", "Espagueti", "Leon", "Africa",
"Unir", "Almohada", "Pariente", "Guardacostas", "Crema", "Notas", "Inundar", "Robo", "Asesinar", "Correo"
]#Deben ser muchas mas

palabra_mostrada = StringVar()

texto_mostrar = []

palabra_seleccionada = ""

letra_elegida = StringVar()

intentos_fallidos = 0

#-------------------------------------------------------------- Funciones-------------------------------------------------------------------------------------
"""
def prueba():
	global palabras
	p = choice(palabras)
	palabra_mostrada.set(p)
"""
def crear_circulo(lista_centro, radio):
	global lienzo
	lienzo.create_oval(lista_centro[0]-radio, lista_centro[1] + radio, lista_centro[0] + radio, lista_centro[1] - radio, fill= "red")#Ver el funcionamiento del metodo create_oval

def dibujar_meñeco(n):
	"""Como dice el nombre, se encarga de dibujar las partes del muñeco en funcion del numero que se le de"""
	global lienzo
	
	if n == 1:
		crear_circulo([120, 85], 10)#Cabeza

	if n == 2:
		lienzo.create_line(120, 85, 120, 140, fill = "red", width = 3)#Torzo
	
	if n == 3:
		lienzo.create_line(120, 100, 141, 121, fill = "red", width = 3)#brazo derecho	
	
	if n == 4:
		lienzo.create_line(120, 100, 99, 121, fill = "red", width = 3)#brazo izquierdo.	

	if n == 5:
		lienzo.create_line(120, 140, 92, 168, fill = "red", width = 3)#Pierna izquierda.

	if n == 6:
		lienzo.create_line(120, 140, 148, 168, fill = "red", width = 3)#Pierna derecha. 		


def hacer_str(lista_letras):
	cadena_texto = ""
	for l in lista_letras:
		cadena_texto += l

	return cadena_texto	

def seleccionar_y_mostrar():
	global palabra_mostrada
	global palabra_seleccionada
	global texto_mostrar

	palabra_seleccionada = choice(palabras).lower()
	#print(palabra_seleccionada)

	for i in range(len(palabra_seleccionada)):
		texto_mostrar.append("?")

	palabra_mostrada.set(hacer_str(texto_mostrar).upper())

seleccionar_y_mostrar()
		
def porbar_letra():
	"""Esta funcion prueba si la letra que el usuario esta insertando esta dentro de la palabra, ademas es la principal del programa."""
	global palabra_mostrada
	global palabra_seleccionada
	global letra_elegida
	global texto_mostrar
	global letra_elegida
	global intentos_fallidos
	posiciones = []

	L = letra_elegida.get().lower()

	if len(L)!= 1 or not L.isalpha():
		messagebox.showwarning(":(", "Solo puedes ingresar una letra por turno, ademas no puedes ingresar numeros")
		letra_elegida.set("")
		intentos_fallidos += 1
		dibujar_meñeco(intentos_fallidos)
		if intentos_fallidos == 6:
			etiqueta_4["text"] = "Has Perdido!"
			boton_ingresar.destroy()
			print("La palabra era: {}".format(palabra_seleccionada))
			
	else:	
		if L in palabra_seleccionada:
			etiqueta_4["text"] = "'{}' está".format(L.upper())			

			for i in range(len(palabra_seleccionada)):
				if palabra_seleccionada[i] == L:
					posiciones.append(i)

			print("La letra: '{}' esta en {}".format(L, posiciones))

			for i in range(len(texto_mostrar)):
				if i in posiciones:
					texto_mostrar[i] = L

			palabra_mostrada.set(hacer_str(texto_mostrar).upper())	
			letra_elegida.set("")

			if "?" not in texto_mostrar:
				etiqueta_4["text"] = "Has Ganado :-)"
				boton_ingresar.destroy()	
				
		else:	
#			print("La letra '{}' no esta".format(L))
			etiqueta_4["text"] = "'{}' no está".format(L.upper())
			letra_elegida.set("")
			intentos_fallidos += 1
			dibujar_meñeco(intentos_fallidos)
			if intentos_fallidos == 6:
				etiqueta_4["text"] = "Has Perdido :-("
				boton_ingresar.destroy()
				print("La palabra era: {}".format(palabra_seleccionada))
#---------------------------------------------------------------------------------------------------------------------------------------------------------------	

frame_1 = Frame(ventana)
frame_1.pack()
frame_1.config(bg = "black", width = "250", height= "250", relief = "sunken", bd = 15)
frame_1.pack(side = "left")

etiqueta_1 = Label(frame_1, text = "Tu Palabra: ")
etiqueta_1.place(x = 70, y = 10)
etiqueta_1.config(bg = "black", font = ("Times new roman", 11), fg = "yellow")

etiqueta_2 = Label(frame_1, textvariable = palabra_mostrada)
etiqueta_2.place(x = 0, y = 50)
etiqueta_2.config(width = "27", font = ("arial", 10), fg = "yellow", bg = "blue", justify = "center")

etiqueta_3 = Label(frame_1, text = "Elige Letra: ")
etiqueta_3.place(x = 0, y = 90)
etiqueta_3.config(font = ("Times new roman", 11), fg = "yellow", bg = "black", justify = "left")

caja_letra = Entry(frame_1, textvariable = letra_elegida)
caja_letra.place(x = 90, y = 90)
caja_letra.config(width = "5", font = ("Times new roman", 11), bg = "white", justify = "center", fg= "black")

boton_ingresar = Button(frame_1, text = "Probrar Letra", command = porbar_letra)
boton_ingresar.place(x = 70, y = 130)
boton_ingresar.config(bg = "blue", font = ("Times new roman", 11), fg = "yellow")

etiqueta_4 = Label(frame_1)
etiqueta_4.place(x = 0, y = 170)
etiqueta_4.config(width = "27", font = ("Times new roman", 11), fg = "yellow", bg = "black", justify = "center")

#---------------------------------------------------Parte del Grafico------------------------------------------------------------------------------

lienzo = Canvas(ventana, width = 250, height = 250, bg = "black")
lienzo.pack(side = "right")


def crear_circulo(lista_centro, radio):
	global lienzo
	lienzo.create_oval(lista_centro[0]-radio, lista_centro[1] + radio, lista_centro[0] + radio, lista_centro[1] - radio, fill= "red")#Ver el funcionamiento del metodo create_oval

lienzo.create_rectangle(10, 220, 150, 240, fill = "blue")#base de la ahorca 

lienzo.create_line(50, 220, 50, 50, fill = "blue", width = 4)#Hasta?

lienzo.create_line(50, 50, 120, 50, fill = "blue", width = 4)#linea horizontal

lienzo.create_line(120, 50, 120, 80, fill = "blue", width = 4)#Linea vertical


#help(porbar_letra)
#help(dibujar_meñeco)
#help(Canvas.create_line)

ventana.mainloop()

















































