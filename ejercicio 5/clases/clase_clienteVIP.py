from clases.clase_cliente import Cliente

class ClienteVIP(Cliente):
    def obtenerDescuento(self):
        return 0.15 #15% de descuento por ser VIP