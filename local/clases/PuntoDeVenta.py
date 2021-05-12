
class PuntoDeVenta():
    def __init__(self):
        self.en_servicio = ""
        self.hora_entrada = 0.0
        self.hora_salida = 0.0
        self.numero_Clientes = 0
        self.numero_ProductosVendidos = 0
     
        
    def setEn_servicio(self, en_servicio):
        self.en_servicio = en_servicio
    def getEn_servicio(self):
        return self.en_servicio

    def setHora_entrada(self, hora_entrada):
        self.hora_entrada = hora_entrada
    def getHora_entrada(self):
        return self.hora_entrada
    
    def setHora_salida(self, hora_salida):
        self.hora_salida = hora_salida
    def getHora_salida(self):
        return self.hora_salida

    def setNumero_Clientes(self, numero_Clientes):
        self.numero_Clientes = numero_Clientes
    def getNumero_Clientes(self):
        return self.numero_Clientes
    
    def setNumero_ProductosVendidos(self, numero_ProductosVendidos):
        self.numero_ProductosVendidos = numero_ProductosVendidos
    def getNumero_ProductosVendidos(self):
        return self.numero_ProductosVendidos