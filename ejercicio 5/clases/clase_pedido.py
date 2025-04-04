class Pedido:
    def __init__(self, cliente, productos):
        self.__cliente = cliente
        self.__productos = productos
        self.total = self.calculartotal()

def calculartotal(self):
    subtotal = sum(precio for _, precio in self.productos)
    descuento = subtotal * self.cliente.obtenerDescuento()
    return subtotal - descuento
    
def detalles(self):
    print(f"Cliente: {self.cliente.nombre}")
    print("Productos: ")
    for nombre, precio in self.productos:
        print(f" - {nombre}: ${precio:.2f}")
    print(f"Total con descuento aplicado: ${self.total:.2f}")