from .Local import *
import threading
import time

def simularLocal(id, nombre, en_servicio, hora_entrada, hora_salida, numero_Clientes, numero_ProductosVendidos):
    local1=Local()
    local1.setId(id)
    local1.setNombre(nombre)
    local1.setEn_servicio(en_servicio)
    local1.setHora_entrada(hora_entrada)
    local1.setHora_salida(hora_entrada)
    local1.setNumero_Clientes(numero_Clientes)
    local1.setNumero_ProductosVendidos(numero_ProductosVendidos)

    print("\n")
    print("id Local: ", local1.getId())
    print("Nombre: ", local1.getNombre())
    print("En servicio: ", local1.getEn_servicio())
    print("Hora Entrada: ", local1.getHora_entrada())
    print("Hora salida: ", local1.getHora_salida())
    print("Numero de clientes: ", local1.getNumero_Clientes())
    print("Numero de productos vendidos: ", local1.getNumero_ProductosVendidos())
    time.sleep(3)  