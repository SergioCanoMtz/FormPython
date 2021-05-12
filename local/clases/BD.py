import mysql.connector
from .Local import *
from .PuntoDeVenta import *

class BD:
    def __init__(self):
        self.conexion = mysql.connector.connect(
            host="localhost", 
            user="root", 
            password="", 
            database="mercado")
        self.cursor = self.conexion.cursor()

    def insertarLocal(self, local):
        consulta = "Insert into local(id,nombre,en_servicio,hora_entrada,hora_salida,num_clientes,num_productos_vendidos) values (%s, %s, %s, %s, %s, %s, %s)"
        datos = [local.getId(), local.getNombre(), local.getEn_servicio(), local.getHora_entrada(), local.getHora_salida(), local.getNumero_Clientes(), local.getNumero_ProductosVendidos()]

        self.cursor.execute(consulta, datos)
        self.conexion.commit()

    def consultaLocal(self):
        listalocal = []
        consulta = "SELECT * FROM local"
        self.cursor.execute(consulta)

        datos = self.cursor.fetchall()
        for registro in datos:
            local = Local()
            local.setId(registro[0])
            local.setNombre(registro[1])
            local.setEn_servicio(registro[2])
            local.setHora_entrada(registro[3])
            local.setHora_salida(registro[4])
            local.setNumero_Clientes(registro[5])
            local.setNumero_ProductosVendidos(registro[6])

            listalocal.append(local)

        return listalocal