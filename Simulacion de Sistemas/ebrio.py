
# Actividad #3 Simulacion de Sistemas
# Nombre: Carlos Ferrer
# C.I: 28.326.446
# Seccion: N1113

# Librerias necesarias
from tkinter import *
from tkinter import messagebox
from random import random
import tkinter.ttk as ttk

# Función que realizo los calculos para determinar la posicion del ebrio
def ebrioFunction():
    # Variables globales a utilizar en la función
    global output_treeview, result_label, count_label, count, countEbrio, count_label_ebrio, label_probabilidad


    # Contador con la cantidad de intentos realizados
    count += 1
    count_label.config(text=f"N-Intentos: {count}")

    x = 0 # representa al movimiento en el eje x (Este, Oeste)
    y = 0 # representa al movimiento en el eje y (Norte, Sur)
    ncuadras = 0 # numero de calles caminadas
    direccion = "" # representa la dirección a la que se mueve el ebrio
    valorAbsX = 0 # Suma de los Valores en X
    valorAbsY = 0 # Suma de los Valores en Y

    output_treeview.delete(*output_treeview.get_children())

    # Ciclo While para repetir el proceso 10 veces (10 Calles)
    while ncuadras < 10:
        r = random() # Numeros Aleatorios
        #Norte
        if r <= 0.25:
            direccion = "Norte"
            if direccion == "Norte":
                x = 0
                y = 1
        # Sur
        elif r > 0.25 and r <= 0.5:
            direccion = "Sur"
            if direccion == "Sur":
                x = 0
                y = -1
        # Este
        elif r > 0.5 and r <= 0.75:
            direccion = "Este"
            if direccion == "Este":
                x = 1
                y = 0
        # Oeste
        elif r > 0.75 and r <= 1:
            direccion = "Oeste"
            if direccion == "Oeste":
                x = -1
                y = 0

        # Contador cantidad de cantidad de calles caminadas
        ncuadras += 1
        output_treeview.insert("", END, values=(ncuadras, f"{r:.4f}", x, y))

        # Suma de los valores Absolutos
        valorAbsX += x
        valorAbsY += y

    resultado = abs(valorAbsX) + abs(valorAbsY)


    # Funcion para calcular la probabilidad
    def calcularProbabilidad(nobservaciones, n2calles):
        probabilidad = n2calles / nobservaciones
        probabilidad_final = probabilidad * 100
        resultado_string = str(probabilidad_final)
        return resultado_string
    # Mostramos el label de la probabilidad
    label_probabilidad.config(text="La probabilidad de que termine su recorrido a 2 calles segun los datos actuales es de: "+ calcularProbabilidad(count, countEbrio) + "%")

    # Condicionales para mostrar si termino o no su recorrido a 2 calles de donde estaba inicialmente        
    if resultado == 2:
        countEbrio += 1 # Contador de las veces que el ebrio termino a 2 calles
        count_label_ebrio.config(text=f"N-Ebrio\n a 2 Calles: {countEbrio}")
        result_label.config(text="Resultado: El borracho terminó a 2 calles de donde estaba inicialmente")
        opcion2 = messagebox.askquestion("Repetir Simulación", "¿Deseas repetir la simulación?")
        if opcion2 == 'yes':
            ebrioFunction()
    else:
        result_label.config(text="Resultado: El borracho no terminó a 2 calles de donde estaba inicialmente")
        opcion2 = messagebox.askquestion("Repetir Simulación", "¿Deseas repetir la simulación?")
        if opcion2 == 'yes':
            ebrioFunction()


# Funcion principal que muestra la interfaz grafica
def functionCalculo():
    global output_treeview, result_label, count_label, count, countEbrio, count_label_ebrio, label_probabilidad
    # Reiniciamos contadores
    count = 0 
    countEbrio = 0

    # Configuramos tkinter
    root = Tk()
    root.title("Simulación de Sistemas")
    root.geometry("1000x420")  # Ajusta el tamaño de la ventana principal

    # Paleta de colores
    colores = ["#d8f3dc", "#b7e4c7", "#95d5b2", "#74c69d", "#52b788", "#40916c", "#2d6a4f", "#1b4332", "#081c15"]

    # Label superior para dar bienvenida a la aplicacion
    label = Label(root, text="Bienvenido al programa para calcular la trayectoria del ebrio", padx=10, pady=10, bg=colores[0], fg=colores[8], font=("Arial", 12, "bold"))
    label.pack()

    frame = Frame(root, bg=colores[1])
    frame.pack(pady=10)

    # Configuraciones de la interfaz grafica (labels, buttons)
    count_label = Label(frame, text="N-Intentos: 0", bg=colores[1], fg=colores[8], font=("Arial", 10, "bold"))
    count_label.pack(side=RIGHT)
    count_label_ebrio = Label(frame, text="N-Ebrio\n a 2 Calles: 0", bg=colores[1], fg=colores[8], font=("Arial", 10, "bold"))
    count_label_ebrio.pack(side=LEFT)

    header_label = Label(frame, text="------ Tabla de Información ------", bg=colores[1], fg=colores[8], font=("Arial", 10, "bold"))
    header_label.pack()

    output_treeview = ttk.Treeview(frame, columns=("calles", "aleatorios", "x", "y"), show="headings")
    output_treeview.heading("calles", text="# Calles Recorridas", anchor=CENTER)
    output_treeview.column("calles", anchor=CENTER)
    output_treeview.heading("aleatorios", text="# Aleatorios", anchor=CENTER)
    output_treeview.column("aleatorios", anchor=CENTER)
    output_treeview.heading("x", text="X", anchor=CENTER)
    output_treeview.column("x", anchor=CENTER)
    output_treeview.heading("y", text="Y", anchor=CENTER)
    output_treeview.column("y", anchor=CENTER)
    output_treeview.pack()

    result_label = Label(root, text="", bg=colores[1], fg=colores[8], font=("Arial", 10, "bold"))
    result_label.pack()

    label_probabilidad = Label(root, text="", bg=colores[1], fg=colores[8], font=("Arial", 10, "bold"))
    label_probabilidad.pack()

    button_frame = Frame(root, bg=colores[1])
    button_frame.pack(pady=10)

    button = Button(button_frame, text="Realizar Cálculos", command=ebrioFunction, bg=colores[4], fg=colores[8], font=("Arial", 10, "bold"))
    button.pack(side=LEFT, padx=10)

    exit_button = Button(button_frame, text="Salir", command=root.quit, bg=colores[3], fg=colores[8], font=("Arial", 10, "bold"))
    exit_button.pack(side=LEFT, padx=10)

    root.mainloop()
# Llamamos la funcion que ejecuta el programa
functionCalculo()
