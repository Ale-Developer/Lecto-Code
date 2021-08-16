import parser
import math
from tkinter import*
from tkinter import messagebox as MB
import tkinter
from tkinter import ttk
import sqlite3

conexion = sqlite3.connect("database.db")


#Ventana principal
root = tkinter.Tk()
root.title("Lecto-Code")
'''root.iconbitmap("icono.ico")'''
root.geometry("670x400")

#Menu

menubar = Menu(root)
root.config(menu=menubar)

#Funciones de menu
def helpm():
    MB.showinfo("Bienvenido","Gracias por elejir Lecto-Code, brindamos nuestro servicio para que su negocio sea más organizado.")

def about():
    MB.showinfo("Acerca de...", "Propiedad intelectual: Alejandro Espinosa / Version: 1.0 / Date: 25/10/20 / Python: 3.8 ")

def contact():
    MB.showinfo("Contacto", "Contacto: miguel.espinosa77696@gmail.com")

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Salir", command=root.quit)


helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Bienvenido", command=helpm)
helpmenu.add_command(label="Contacto", command=contact)
helpmenu.add_separator()
helpmenu.add_command(label="Acerca de...", command=about)

#Menus en pantalla
menubar.add_cascade(label="Archivo", menu=filemenu)
menubar.add_cascade(label="Ayuda", menu=helpmenu)

#Panel de pestañas
nb = ttk.Notebook(root)
nb.pack(fill='both',expand='yes')

#Pestañas
p1 = ttk.Frame(nb)
p2 = ttk.Frame(nb)
p3 = ttk.Frame(nb)

#Elemento pestaña agregar
labelframe = LabelFrame(p1, text="Agregar Producto")
labelframe.config(width=390, height=300)
labelframe.place(x=10, y=10)

labelEAN = Label(labelframe, text="Código EAN: ")
labelEAN.place(x=30,y=30)
EANEntry = Entry(labelframe)
EANEntry.place(x=200,y=30)

labelDescripcion = Label(labelframe, text="Descripción: ")
labelDescripcion.place(x=30,y=80)
DescripcionEntry = Entry(labelframe)
DescripcionEntry.place(x=200,y=80)

labelPrecio = Label(labelframe, text="Precio: ")
labelPrecio.place(x=30,y=130)
PrecioEntry = Entry(labelframe)
PrecioEntry.place(x=200,y=130)

labelRubro = Label(labelframe, text="Rubro: ")
labelRubro.place(x=30,y=180)

#Lista desplegable

ListaRubro = ttk.Combobox(labelframe)
ListaRubro.place(x=200,y=180)

opciones = ["Limpieza", "Almacén","Librería","Bazar", "Bebidas", "Perecederos"]
ListaRubro["values"]=opciones

#Save
def save():
    if(EANEntry.get() == "" or DescripcionEntry.get() == "" or PrecioEntry.get() == "" or ListaRubro.get() == ""):
        MB.showwarning("Lecto-Code","Complete todos los datos")
    else:
        data = (EANEntry.get(),DescripcionEntry.get(),PrecioEntry.get(),ListaRubro.get())
        print(data)
        tabla = conexion.cursor()
        tabla.execute("INSERT INTO almacen(EAN,Descripcion,Precio,Rubro) VALUES(?,?,?,?)",data)
        conexion.commit()
        tabla.close
        MB.showinfo("Lecto-Code","Se ha guardado correctamente!!!")
        DescripcionEntry.delete(0,END)
        EANEntry.delete(0,END)
        PrecioEntry.delete(0,END)
        ListaRubro.delete(0,END)

#Boton agregar
BotonAgregar = Button(labelframe, text="Agregar", command=save)
BotonAgregar.place(x=160,y=230)

#Calculator

labelCalculadora = LabelFrame(p1, text="Calculadora")
labelCalculadora.config(width=250, height=300)
labelCalculadora.place(x=410, y=10)

#Functions
i = 0

def get_numbers(n):
    global i
    display.insert(i, n)
    i += 1

def get_operation(operator):
    global i
    opertor_length = len(operator)
    display.insert(i, operator)
    i+=opertor_length

def calculate():
    display_state = display.get()
    try:
        math_expression = parser.expr(display_state).compile()
        result = eval(math_expression)
        clear_display()
        display.insert(0, result)
    except Exception:
        clear_display()
        display.insert(0, 'Error')

def clear_display():
    display.delete(0, END)


def undo():
    display_state = display.get()
    if len(display_state):
        display_new_state = display_state[:-1]
        clear_display()
        display.insert(0, display_new_state)
    else:
        clear_display()
        display.insert(0, 'Error')

def square_root(n):
    display_state = int(n) / 2
    for i in range(20):
        if x * x == n:
            return x
        else:
            x = (x + (n/x)) / 2
    return x

#Frames Calculator

frameDisplay = Frame(labelCalculadora)
frameDisplay.config(width=220, height=40)
frameDisplay.place(x=0,y=4)

frameBotones = Frame(labelCalculadora)
frameBotones.config(bg="gray",width=320, height=400)
frameBotones.place(x=3,y=40)

#Display Calculator

display = Entry(frameDisplay, font=("Arial Black",12),width=40)
display.place(x=3, y=0)

#Numeric button Calculator

Button(frameBotones, text="  7  ", command=lambda: get_numbers(7),font=("Arial Black",12)).grid(row=2, column=0, sticky=W+E)
Button(frameBotones, text="  8  ", command=lambda: get_numbers(8),font=("Arial Black",12)).grid(row=2, column=1, sticky=W+E)
Button(frameBotones, text="  9  ", command=lambda: get_numbers(9),font=("Arial Black",12)).grid(row=2, column=2, sticky=W+E)

Button(frameBotones, text="  4  ", command=lambda: get_numbers(4),font=("Arial Black",12)).grid(row=3, column=0, sticky=W+E)
Button(frameBotones, text="  5  ", command=lambda: get_numbers(5),font=("Arial Black",12)).grid(row=3, column=1, sticky=W+E)
Button(frameBotones, text="  6  ", command=lambda: get_numbers(6),font=("Arial Black",12)).grid(row=3, column=2, sticky=W+E)

Button(frameBotones, text="  1  ", command=lambda: get_numbers(1),font=("Arial Black",12)).grid(row=4, column=0, sticky=W+E)
Button(frameBotones, text="  2  ", command=lambda: get_numbers(2),font=("Arial Black",12)).grid(row=4, column=1, sticky=W+E)
Button(frameBotones, text="  3  ", command=lambda: get_numbers(3),font=("Arial Black",12)).grid(row=4, column=2, sticky=W+E)

#Operative buttons Calculator

Button(frameBotones, text=" x² ", command=lambda: get_operation("**2"),bg="snow3",font=("Arial Black",12)).grid(row=1, column=0, sticky=W+E)
Button(frameBotones, text="  0  ", command=lambda: get_numbers(0),font=("Arial Black",12)).grid(row=5, column=0, columnspan=2,sticky=W+E)
Button(frameBotones, text="  ,  ", command=lambda: get_operation("."),font=("Arial Black",12)).grid(row=5, column=2, sticky=W+E)
Button(frameBotones, text="  =  ", command=lambda: calculate(),bg="powder blue",font=("Arial Black",12)).grid(row=5, column=3, sticky=W+E)

Button(frameBotones, text="  +  ", command=lambda: get_operation("+"),bg="snow3",font=("Arial Black",12)).grid(row=4, column=3, sticky=W+E)
Button(frameBotones, text="  ─  ", command=lambda: get_operation("-"),bg="snow3",font=("Arial Black",12)).grid(row=3, column=3, sticky=W+E)
Button(frameBotones, text="  x  ", command=lambda: get_operation("*"),bg="snow3",font=("Arial Black",12)).grid(row=2, column=3, sticky=W+E)
Button(frameBotones, text="  ÷  ", command=lambda: get_operation("/"),bg="snow3",font=("Arial Black",12)).grid(row=1, column=3, sticky=W+E)

Button(frameBotones, text="  CE  ", command=lambda: clear_display(),bg="gray27",font=("Arial Black",12)).grid(row=0, column=0, columnspan=2, sticky=W+E)

Button(frameBotones, text="  ‹  ", command=lambda: undo(),bg="gray27",font=("Arial Black",12)).grid(row=0, column=2,columnspan=2, sticky=W+E)
Button(frameBotones, text="  )  ", command=lambda: get_operation(")"),bg="snow3",font=("Arial Black",12)).grid(row=1, column=2, sticky=W+E)
Button(frameBotones, text="  (  ", command=lambda: get_operation("("),bg="snow3",font=("Arial Black",12)).grid(row=1, column=1, sticky=W+E)



#Elemento pestaña modificar.
labelframeModificar = LabelFrame(p2, text="Modificar Producto")
labelframeModificar.config(width=390, height=300)
labelframeModificar.place(x=10, y=10)

labelEAN = Label(labelframeModificar, text="Código interno: ")
labelEAN.place(x=30,y=10)
InternoEntryModificar = Entry(labelframeModificar)
InternoEntryModificar.place(x=200,y=10)

labelEAN = Label(labelframeModificar, text="Código EAN: ")
labelEAN.place(x=30,y=50)
EANEntryModificar = Entry(labelframeModificar)
EANEntryModificar.place(x=200,y=50)

labelDescripcion = Label(labelframeModificar, text="Descripción: ")
labelDescripcion.place(x=30,y=90)
DescripcionEntryModificar = Entry(labelframeModificar)
DescripcionEntryModificar.place(x=200,y=90)

labelPrecio = Label(labelframeModificar, text="Precio: ")
labelPrecio.place(x=30,y=130)
PrecioEntryModificar = Entry(labelframeModificar)
PrecioEntryModificar.place(x=200,y=130)

labelRubro = Label(labelframeModificar, text="Rubro: ")
labelRubro.place(x=30,y=170)

#Lista desplegable

ListaRubroModificar = ttk.Combobox(labelframeModificar)
ListaRubroModificar.place(x=200,y=170)

opciones = ["Limpieza", "Almacén","Librería","Bazar", "Bebidas", "Perecederos"]
ListaRubroModificar["values"]=opciones

def Modificar():
    if(InternoEntryModificar.get()== "" or EANEntryModificar.get()=="" or  DescripcionEntryModificar.get()== "" or PrecioEntryModificar.get()=="" or  ListaRubroModificar.get()== ""):
        MB.showwarning("Lecto-Code","Complete todos los datos")
    else:
        InternoEntryModificar.config(state="normal")
        dataModificar = (InternoEntryModificar.get(),EANEntryModificar.get(),DescripcionEntryModificar.get(),PrecioEntryModificar.get(),ListaRubroModificar.get())
        InternoEntryModificar.config(state="disabled")
        tabla = conexion.cursor()
        tabla.execute("UPDATE almacen SET Interno=?,EAN=?,Descripcion=?,Precio=?,Rubro=?" ,dataModificar)
        conexion.commit()
        tabla.close()
        MB.showinfo("Lecto-Code","Se ha modificado correctamente")


#Boton Modificar
BotonModificar = Button(labelframeModificar, text="Modificar",command=Modificar)
BotonModificar.place(x=160,y=230)

#Label buscar Modificar
labelBuscarModificar = LabelFrame(p2, text="Buscar Producto")
labelBuscarModificar.config(width=250, height=300)
labelBuscarModificar.place(x=410, y=10)

#Label buscar EAN

def buscarEANModificar():
    buscoEANModificar = (EANEntryBuscarModificar.get(),)
    tabla = conexion.cursor()
    tabla.execute("SELECT * FROM almacen WHERE EAN=?",buscoEANModificar)
    dataBuscados = tabla.fetchall()
    InternoEntryModificar.config(state="normal")
    InternoEntryModificar.delete(0,END)
    EANEntryModificar.delete(0,END)
    DescripcionEntryModificar.delete(0,END)
    PrecioEntryModificar.delete(0,END)
    ListaRubroModificar.delete(0,END)
    if(len(dataBuscados) > 0):
        for dato in dataBuscados:
            InternoEntryModificar.insert(0,dato[0])
            InternoEntryModificar.config(state="disable")
            EANEntryModificar.insert(0,dato[1])
            DescripcionEntryModificar.insert(0,dato[2])
            PrecioEntryModificar.insert(0,dato[3])
            ListaRubroModificar.insert(0,dato[4])
    else:
        MB.showwarning("Lecto-Code","No se ha encontrado el EAN")

labelSearch = Label(labelBuscarModificar, text="EAN: ")
labelSearch.place(x=10,y=30)
EANEntryBuscarModificar = Entry(labelBuscarModificar)
EANEntryBuscarModificar.place(x=100,y=30)

#Boton buscar EAN Modificar 
BotonBuscarModificar = Button(labelBuscarModificar, text="Buscar",command=buscarEANModificar)
BotonBuscarModificar.place(x=100,y=70)

#Label buscar Interno Modificar

def buscarInternoModificar():
    buscoInternoModificar = (InternoEntryBuscarModificar.get(),)
    tabla = conexion.cursor()
    tabla.execute("SELECT * FROM almacen WHERE Interno=?",buscoInternoModificar)
    dataBuscadosModificar = tabla.fetchall()
    InternoEntryModificar.config(state="normal")
    InternoEntryModificar.delete(0,END)
    EANEntryModificar.delete(0,END)
    DescripcionEntryModificar.delete(0,END)
    PrecioEntryModificar.delete(0,END)
    ListaRubroModificar.delete(0,END)
    if(len(dataBuscadosModificar) > 0):
        for dato in dataBuscadosModificar:
            InternoEntryModificar.insert(0,dato[0])
            InternoEntryModificar.config(state="disable")
            EANEntryModificar.insert(0,dato[1])
            DescripcionEntryModificar.insert(0,dato[2])
            PrecioEntryModificar.insert(0,dato[3])
            ListaRubroModificar.insert(0,dato[4])
    else:
        MB.showwarning("Lecto-Code","No se ha encontrado el Interno")

labelSearch = Label(labelBuscarModificar, text="Interno: ")
labelSearch.place(x=10,y=110)
InternoEntryBuscarModificar = Entry(labelBuscarModificar)
InternoEntryBuscarModificar.place(x=100,y=110)

#Boton buscar Interno Modificar
BotonBuscarModificar2 = Button(labelBuscarModificar, text="Buscar",comman=buscarInternoModificar)
BotonBuscarModificar2.place(x=100,y=150)

#Elemento pestaña eliminar

labelframeEliminar = LabelFrame(p3, text="Eliminar Producto")
labelframeEliminar.config(width=390, height=300)
labelframeEliminar.place(x=10, y=10)

labelEANEliminar = Label(labelframeEliminar, text="Código EAN: ")
labelEANEliminar.place(x=30,y=10)
EANEntryEliminar = Entry(labelframeEliminar)
EANEntryEliminar.place(x=200,y=10)

labelEANEliminar = Label(labelframeEliminar, text="Código interno: ")
labelEANEliminar.place(x=30,y=50)
InternoEntryEliminar = Entry(labelframeEliminar)
InternoEntryEliminar.place(x=200,y=50)

labelDescripcionEliminar = Label(labelframeEliminar, text="Descripción: ")
labelDescripcionEliminar.place(x=30,y=90)
DescripcionEntryEliminar = Entry(labelframeEliminar)
DescripcionEntryEliminar.place(x=200,y=90)

labelPrecioEliminar = Label(labelframeEliminar, text="Precio: ")
labelPrecioEliminar.place(x=30,y=130)
PrecioEntryEliminar = Entry(labelframeEliminar)
PrecioEntryEliminar.place(x=200,y=130)

labelRubroEliminar = Label(labelframeEliminar, text="Rubro: ")
labelRubroEliminar.place(x=30,y=170)

#Lista desplegable

ListaRubroEliminar = ttk.Combobox(labelframeEliminar)
ListaRubroEliminar.place(x=200,y=170)

opciones = ["Limpieza", "Almacén","Librería","Bazar", "Bebidas", "Perecederos"]
ListaRubroEliminar["values"]=opciones

#Boton Eliminar
def BDEliminar():
    InternoEntryEliminar.config(state="normal")
    EANEntryEliminar.config(state="normal")
    DescripcionEntryEliminar.config(state="normal")
    PrecioEntryEliminar.config(state="normal")
    ListaRubroEliminar.config(state="normal")
    dataEliminar = (InternoEntryEliminar.get(),)
    tabla = conexion.cursor()
    tabla.execute("DELETE FROM almacen WHERE Interno=?",dataEliminar)
    conexion.commit()
    tabla.close()
    MB.showwarning("Lecto-Code","Se ha eliminado el Producto")
    InternoEntryEliminar.delete(0,END)
    EANEntryEliminar.delete(0,END)
    DescripcionEntryEliminar.delete(0,END)
    PrecioEntryEliminar.delete(0,END)
    ListaRubroEliminar.delete(0,END)
    InternoEntryEliminar.config(state="disabled")
    EANEntryEliminar.config(state="disabled")
    DescripcionEntryEliminar.config(state="disabled")
    PrecioEntryEliminar.config(state="disabled")
    ListaRubroEliminar.config(state="disable")

BotonEliminar = Button(labelframeEliminar, text="Eliminar",command=BDEliminar)
BotonEliminar.place(x=160,y=230)

#Label buscar Eliminar
labelBuscarEliminar = LabelFrame(p3, text="Buscar Producto")
labelBuscarEliminar.config(width=250, height=300)
labelBuscarEliminar.place(x=410, y=10)

#Label Buscar EAN Eliminar
labelSearchEliminar = Label(labelBuscarEliminar, text="EAN: ")
labelSearchEliminar.place(x=10,y=30)
EANEntryBuscarEliminar = Entry(labelBuscarEliminar)
EANEntryBuscarEliminar.place(x=100,y=30)

#Boton buscar EAN Eliminar
def buscaEANEliminar():
    buscarEANEliminar = (EANEntryBuscarEliminar.get(),)
    tabla = conexion.cursor()
    tabla.execute("SELECT * FROM almacen WHERE EAN=?",buscarEANEliminar)
    dataBuscadosEliminar = tabla.fetchall()
    InternoEntryEliminar.config(state="normal")
    EANEntryEliminar.config(state="normal")
    DescripcionEntryEliminar.config(state="normal")
    PrecioEntryEliminar.config(state="normal")
    ListaRubroEliminar.config(state="normal")
    InternoEntryEliminar.delete(0,END)
    EANEntryEliminar.delete(0,END)
    DescripcionEntryEliminar.delete(0,END)
    PrecioEntryEliminar.delete(0,END)
    ListaRubroEliminar.delete(0,END)
    if(len(dataBuscadosEliminar) > 0):
        for dato in dataBuscadosEliminar:
            InternoEntryEliminar.insert(0,dato[0])
            EANEntryEliminar.insert(0,dato[1])
            DescripcionEntryEliminar.insert(0,dato[2])
            PrecioEntryEliminar.insert(0,dato[3])
            ListaRubroEliminar.insert(0,dato[4])
    else:
        MB.showwarning("Lecto-Code","No se ha encontrado el EAN")
    InternoEntryEliminar.config(state="disabled")
    EANEntryEliminar.config(state="disabled")
    DescripcionEntryEliminar.config(state="disabled")
    PrecioEntryEliminar.config(state="disabled")
    ListaRubroEliminar.config(state="disabled")

BotonBuscarEliminar = Button(labelBuscarEliminar, text="Buscar",command=buscaEANEliminar)
BotonBuscarEliminar.place(x=100,y=70)

#Label Buscar Interno Eliminar
labelSearchEliminar = Label(labelBuscarEliminar, text="Interno: ")
labelSearchEliminar.place(x=10,y=110)
InternoEntryBuscarEliminar = Entry(labelBuscarEliminar)
InternoEntryBuscarEliminar.place(x=100,y=110)

#Boton buscar Interno Eliminar
def buscaInternoEliminar():
    buscarInternoEliminar = (InternoEntryBuscarEliminar.get(),)
    tabla = conexion.cursor()
    tabla.execute("SELECT * FROM almacen WHERE Interno=?",buscarInternoEliminar)
    dataBuscadosEliminar = tabla.fetchall()
    InternoEntryEliminar.config(state="normal")
    EANEntryEliminar.config(state="normal")
    DescripcionEntryEliminar.config(state="normal")
    PrecioEntryEliminar.config(state="normal")
    ListaRubroEliminar.config(state="normal")
    InternoEntryEliminar.delete(0,END)
    EANEntryEliminar.delete(0,END)
    DescripcionEntryEliminar.delete(0,END)
    PrecioEntryEliminar.delete(0,END)
    ListaRubroEliminar.delete(0,END)
    if(len(dataBuscadosEliminar) > 0):
        for data in dataBuscadosEliminar:
            InternoEntryEliminar.insert(0,data[0])
            EANEntryEliminar.insert(0,data[1])
            DescripcionEntryEliminar.insert(0,data[2])
            PrecioEntryEliminar.insert(0,data[3])
            ListaRubroEliminar.insert(0,data[4])            
    else:
        MB.showwarning("Lecto-Code","No se ha encontrado el Interno")
    InternoEntryEliminar.config(state="disabled")
    EANEntryEliminar.config(state="disabled")
    DescripcionEntryEliminar.config(state="disabled")
    PrecioEntryEliminar.config(state="disabled")
    ListaRubroEliminar.config(state="disabled")

BotonBuscarEliminar = Button(labelBuscarEliminar, text="Buscar",command=buscaInternoEliminar)
BotonBuscarEliminar.place(x=100,y=150)

#AGREGAMOS PESTAÑAS CREADAS
nb.add(p1,text="Agregar")
nb.add(p2,text="Modificar")
nb.add(p3,text="Eliminar")


#Bucle loop
root.mainloop()