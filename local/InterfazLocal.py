from tkinter import *
from tkinter import messagebox
import threading
from clases.Local import *
from clases.SimularLocal import *
from clases.BD import *
from os import system

local1 = Local()
bd = BD() 

#Metodo para guardar la informacion en la base de datos
def guardar_info():
    #Aqui verifica si están vacios los campos del formulario, si estan vacios, da el mensaje
    if ((not id.get())  or (not nombre.get()) or (not en_servicio.get()) or (not hora_entrada.get()) or (not hora_salida.get()) or (not num_clientes.get()) or (not num_productos_vendidos.get())):
        system("cls")
        if (not bd.consultaLocal()):
            print("\n\n  ************************************")
            print("  No hay registros en la base de datos")
            print("  ************************************")
        else:
            print("\n\n  ************************************")
            print("  Ya hay registros en la base de datos")
            print("  ************************************")
        messagebox.showinfo("Accion Necesaria","Por favor llena todos los campos")
    else: #Si no están vacios obtenemos los valores de la variables para guardarlas en un objeto
        local1.setId(id.get()) 
        local1.setNombre(nombre.get())
        local1.setEn_servicio(en_servicio.get())
        local1.setHora_entrada(hora_entrada.get())
        local1.setHora_salida(hora_salida.get())
        local1.setNumero_Clientes(num_clientes.get())
        local1.setNumero_ProductosVendidos(num_productos_vendidos.get())
        bd.insertarLocal(local1) #llamamos al metodo para insertar en la base de datos y pasamos como parametreo el objeto
        id_entry.delete(0, END) #borramos los valores solo en el formulario
        nombre_entry.delete(0, END)
        en_servicio_entry.delete(0, END)
        hora_entrada_entry.delete(0, END)
        hora_salida_entry.delete(0, END)
        num_clientes_entry.delete(0, END)
        num_productos_vendidos_entry.delete(0, END)
        system("cls")
        print("\n\n  ************************************")
        print("  Ya hay registros en la base de datos")
        print("  ************************************")
        messagebox.showinfo("Notificacion","Los datos se insertaron correctamente en la Base de datos")

#definimos el metodo para hacer la consulta hacia la base de datos
def consulta():
    
    if (not bd.consultaLocal()):
        system("cls")
        print("\n\n  ************************************")
        print("  No hay registros en la base de datos")
        print("  ************************************")
    else:
        system("cls")
        for local1 in bd.consultaLocal():
            print("  Id: ",local1.getId())
            print("  Nombre: ",local1.getNombre())
            print("  En servicio: ",local1.getEn_servicio()) 
            print("  Hora entrada: ",local1.getHora_entrada()) 
            print("  Hora salida: ",local1.getHora_salida()) 
            print("  Numero de clientes: ",local1.getNumero_Clientes()) 
            print("  Numero de productos vendidos: ",local1.getNumero_ProductosVendidos()) 
            print(" ")

# Definimos el metodo para hacer la simulacion con hilos
def simular():
    hilo1 = threading.Thread(target = simularLocal, args=(21,"Lupita","Si", 9.45, 18.59, 40, 60))
    hilo2 = threading.Thread(target = simularLocal, args=(22,"Don Hipolito","Si", 10.15, 19.59, 34, 54))
    hilo3 = threading.Thread(target = simularLocal, args=(23,"La Teotiteca","Si", 10.00, 14.59, 20, 24))
    hilo4 = threading.Thread(target = simularLocal, args=(24,"Doña Rosa","Si", 7.50, 17.59, 41, 57))
    
    hilo1.start()
    hilo2.start() 
    hilo3.start()
    time.sleep(3)  
    hilo4.start()

mywindow = Tk()
mywindow.geometry("300x650")
mywindow.title("Local")
mywindow.resizable(False,False) 
mywindow.config(background = "#213141")
main_title = Label(text = "Ingrese los datos del local", font = ("Roboto", 16), bg = "#00CD63", fg = "#000000", width = "500", height = "2")
main_title.pack()

#creamos cada uno de los labels
id_label = Label(text = "Id: ", bg="#213141", fg = "#FFFFFF", font = ("Roboto", 12))
nombre_label = Label(text = "Nombre: ", bg="#213141", fg = "#FFFFFF", font = ("Roboto", 12))
en_servicio_label = Label(text = "En servicio (Si/No): ", bg="#213141", fg = "#FFFFFF", font = ("Roboto", 12))
hora_entrada_label = Label(text = "Hora entrada (HH:MM): ", bg="#213141", fg = "#FFFFFF", font = ("Roboto", 12))
hora_salida_label = Label(text = "Hora salida (HH:MM): ", bg="#213141", fg = "#FFFFFF", font = ("Roboto", 12))
num_clientes_label = Label(text = "Numero de clientes: ", bg="#213141", fg = "#FFFFFF", font = ("Roboto", 12))
num_productos_vendidos_label = Label(text = "Numero de productos vendidos: ", bg="#213141", fg = "#FFFFFF", font = ("Roboto", 12))
#Establecemos la ubiacacion de cada uno de los labels
id_label.place(x = 22, y = 70)
nombre_label.place(x = 22, y = 130)
en_servicio_label.place(x = 22, y = 190)
hora_entrada_label.place(x = 22, y = 250)
hora_salida_label.place(x = 22, y = 310)
num_clientes_label.place(x = 22, y = 370)
num_productos_vendidos_label.place(x = 22, y = 430)

# Estas variables serviran para almacenar los valores de los campos de texto del formulario
id = StringVar()
nombre = StringVar()
en_servicio = StringVar()
hora_entrada = StringVar()
hora_salida = StringVar()
num_clientes = StringVar()
num_productos_vendidos = StringVar()

#Creamos los entry(campos de textos del formulario)
id_entry = Entry(textvariable = id, width = "40", bd = "3")
nombre_entry = Entry(textvariable = nombre, width = "40", bd = "3")
en_servicio_entry = Entry(textvariable = en_servicio, width = "40", bd = "3")
hora_entrada_entry = Entry(textvariable = hora_entrada, width = "40", bd = "3")
hora_salida_entry = Entry(textvariable = hora_salida, width = "40", bd = "3")
num_clientes_entry = Entry(textvariable = num_clientes, width = "40", bd = "3")
num_productos_vendidos_entry = Entry(textvariable = num_productos_vendidos, width = "40", bd = "3")
#Establecemos la posicion de los entry
id_entry.place(x = 22, y = 100)
nombre_entry.place(x = 22, y = 160)
en_servicio_entry.place(x = 22, y = 220)
hora_entrada_entry.place(x = 22, y = 280)
hora_salida_entry.place(x = 22, y = 340)
num_clientes_entry.place(x = 22, y = 400)
num_productos_vendidos_entry.place(x = 22, y = 460)

#creamos los botones de Guardar, Consultar y simular
guardar_btn = Button(mywindow,text = "Guardar", width = "34", height = "2", command = guardar_info, bg = "#00CD63")
consultar_btn = Button(mywindow,text = "Consultar", width = "34", height = "2", command = consulta,bg = "#00CD63")
simular_btn = Button(mywindow,text = "Simular", width = "34", height = "2", command = simular,bg = "#00CD63")
#establecemos la posicion de los botones creados antes
guardar_btn.place(x = 22, y = 500)
consultar_btn.place(x = 22, y = 545)
simular_btn.place(x = 22, y = 590)

mywindow.mainloop()