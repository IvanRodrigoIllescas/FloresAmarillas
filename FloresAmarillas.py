import turtle as tur
import tkinter as tk
# funciona para windows, para otro S.O como android pueden dar las lineas que ponen la ventana en "zomed"
def dibujar_flor():
    tur.penup()
    tur.left(90)
    tur.fd(200)
    tur.pendown()
    tur.right(90)
    tur.fillcolor("yellow")
    tur.begin_fill()
    tur.circle(10, 180)
    tur.circle(25, 110)
    tur.left(50)
    tur.circle(60, 45)
    tur.circle(20, 170)
    tur.right(24)
    tur.fd(30)
    tur.left(10)
    tur.circle(30, 110)
    tur.fd(20)
    tur.left(40)
    tur.circle(90, 70)
    tur.circle(30, 150)
    tur.right(30)
    tur.fd(15)
    tur.circle(80, 90)
    tur.left(15)
    tur.fd(45)
    tur.right(165)
    tur.fd(20)
    tur.left(155)
    tur.circle(150, 80)
    tur.left(50)
    tur.circle(150, 90)
    tur.end_fill()
    tur.left(150)
    tur.circle(-90, 70)
    tur.left(20)
    tur.circle(75, 105)
    
    #input(tur.heading())
    
    tur.left(-261)  # Cambio a tur.left(60) en lugar de tur.setheading(60)
    tur.circle(80, 98)
    tur.circle(-90, 40)
    tur.left(180)
    tur.circle(90, 40)
    tur.circle(-80, 98)
    
    #input(tur.heading())
    
    tur.left(23)  # Cambio a tur.left(97) en lugar de tur.setheading(-83)
    tur.fd(30)
    tur.left(90)
    tur.fd(25)
    tur.left(45)
    tur.fillcolor("dark green")
    tur.begin_fill()
    tur.circle(-80, 90)
    tur.right(90)
    tur.circle(-80, 90)
    tur.end_fill()
    tur.right(135)
    tur.fd(60)
    tur.left(180)
    tur.fd(85)
    tur.left(90)
    tur.fd(80)
    tur.right(90)
    tur.right(45)
    tur.fillcolor("dark green")
    tur.begin_fill()
    tur.circle(80, 90)
    tur.left(90)
    tur.circle(80, 90)
    tur.end_fill()
    tur.left(135)
    tur.fd(60)
    tur.left(180)
    tur.fd(60)
    tur.right(90)
    tur.circle(200, 60)
    tur.penup()
    tur.goto(0, 0)
    tur.pendown()

ventana = tk.Tk()
ventana.state('zoomed')
ventana.state(tk.NORMAL)
ventana.resizable(False, False)
screen_width = ventana.winfo_screenwidth()
screen_height = ventana.winfo_screenheight()
ventana.geometry(f"{screen_width}x{screen_height}")
canvas = tur.ScrolledCanvas(ventana)
canvas.pack(fill=tk.BOTH, expand=tk.YES)
ventana.state('zoomed')
ventana.title("Flores Amarillas para Mi Amor")
tur = tur.RawTurtle(canvas)


tur.shape("turtle")

num_flores = 5

numTemp=[]
numDef =[]

num=290  #para que este centrado 290

for i in range(num_flores):
    numTemp.append(num)
    num += 175/num_flores
    
    
    
    
for i in range(num_flores):
    if numTemp:  # Verificar si numTemp no está vacía
        numDef.append(numTemp[-1])  # Agregar el último elemento de numTemp a numDef
        numTemp.pop()  # Eliminar el último elemento de numTemp
    if len(numTemp) >= 2:  # Verificar si numTemp tiene al menos dos elementos
        numDef.append(numTemp[0])  # Agregar el segundo elemento de numTemp a numDef
        numTemp.pop(0) 










#numeros=[430, 290, 395, 325, 360]


for i in numDef:
    
    tur.setheading(i)
    dibujar_flor()
    
    

#tur.setheading(70)
#dibujar_flor()

#tur.setheading(290)
#dibujar_flor()

#tur.setheading(395)
#dibujar_flor()

#tur.setheading(325)
#dibujar_flor()

#tur.setheading(0)
#dibujar_flor()



tur.hideturtle()




ventana.mainloop()

