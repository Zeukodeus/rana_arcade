from tkinter import *
import random

# Variables globales
base = 460
altura = 470
radio = 50
carretera_speed = 2

# Función para el botón arriba
def arriba():
    x, y = c.coords(rana)
    if y - 10 >= 10:
        c.move(rana, 0, -10)
    else:
        c.move(rana, 0, initial_position[1] - y)

# Función para el botón abajo
def abajo():
    x, y = c.coords(rana)
    if y + 10 <= altura - 10:
        c.move(rana, 0, 10)
    else:
        c.move(rana, 0, initial_position[1] - y)

# Función para el botón de izquierda
def izquierda():
    x, y = c.coords(rana)
    if x - 10 >= 10:
        c.move(rana, -10, 0)
    else:
        c.move(rana, initial_position[0] - x, 0)

# Función para el botón de derecha
def derecha():
    x, y = c.coords(rana)
    if x + 10 <= base - 10:
        c.move(rana, 10, 0)
    else:
        c.move(rana, initial_position[0] - x, 0)

# Ventana principal
ventana_principal = Tk()
ventana_principal.title("GameArcade - La Rana Insana")
ventana_principal.geometry("500x800")
ventana_principal.resizable(False, False)
ventana_principal.config(bg="Blue")

# Frame de graficación
frame_graficacion = Frame(ventana_principal, bg="yellow", width=480, height=500)
frame_graficacion.place(x=10, y=10)

# Creación del lienzo (canvas)
c = Canvas(frame_graficacion, width=base, height=altura, bg="green")
c.place(x=10, y=10)
c.create_rectangle(0, 70, base, 140, fill="black", outline="white", width=2)
c.create_rectangle(0, 200, base, 265, fill="black", outline="white", width=2)
c.create_rectangle(0, 320, base, 390, fill="black", outline="white", width=2)

# Load road image
road_image = PhotoImage(file="img/carro.png")

# Carretera superior
carretera_sup = c.create_image(base//2, 107, image=road_image)

# Carretera del medio
carretera_med = c.create_image(base//2, 235, image=road_image)

# Carretera Inferior
carretera_inf = c.create_image(base//2, 357, image=road_image)

# Diseño de la rana
rana_image = PhotoImage(file="img/rana.png")

# Dibujar la imagen de la rana en el lienzo
initial_position = (base//2, 435)
rana = c.create_image(initial_position[0], initial_position[1], image=rana_image)

# Animating the rectangles
def move_rectangles():
    global carretera_speed

    if carretera_sup:
        if c.coords(carretera_sup)[0] <= -base:
            c.move(carretera_sup, base*2, 0)
        else:
            c.move(carretera_sup, -carretera_speed, 0)
    if carretera_med:
        if c.coords(carretera_med)[0] <= -base:
            c.move(carretera_med, base*2, 0)
        else:
            c.move(carretera_med, -carretera_speed, 0)
    if carretera_inf:
        if c.coords(carretera_inf)[0] <= -base:
            c.move(carretera_inf, base*2, 0)
        else:
            c.move(carretera_inf, -carretera_speed, 0)
    
    # Aumentar la velocidad de los autos cuando la rana llegue arriba
    if c.coords(rana)[1] <= 10:
        carretera_speed += 1
    
    # Schedule the next move
    ventana_principal.after(5, move_rectangles)

# Start the animation
move_rectangles()

# Frame de controles
frame_controles = Frame(ventana_principal, bg="Yellow", width=480, height=290)
frame_controles.place(x=10, y=500)

# Botón para mover hacia arriba
arriba_icon = PhotoImage(file="img/arriba.png")
bt_arriba = Button(frame_controles, image=arriba_icon, command=arriba)
bt_arriba.place(x=210, y=30, width=60, height=60)

# Botón para mover hacia abajo
abajo_icon = PhotoImage(file="img/abajo.png")
bt_abajo = Button(frame_controles, image=abajo_icon, command=abajo)
bt_abajo.place(x=210, y=170, width=60, height=60)

# Botón para mover hacia la izquierda
izquierda_icon = PhotoImage(file="img/izq.png")
bt_izquierda = Button(frame_controles, image=izquierda_icon, command=izquierda)
bt_izquierda.place(x=135, y=100, width=60, height=60)

# Botón para mover hacia la derecha
derecha_icon = PhotoImage(file="img/derecha.png")
bt_derecha = Button(frame_controles, image=derecha_icon, command=derecha)
bt_derecha.place(x=285, y=100, width=60, height=60)

# Run
ventana_principal.mainloop()

