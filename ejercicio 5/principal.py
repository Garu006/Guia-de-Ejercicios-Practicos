'''Crear una clase Cliente con atributos básicos (por  ejemplo, ID, nombre y 
contacto) y una  clase Pedido que  contenga información sobre el cliente,  la lista 
de productos solicitados y el total de la venta. Se podrá incluir el uso de herencia 
para diferenciar entre tipos de clientes (por ejemplo, cliente regular y cliente VIP) 
y aplicar descuentos especiales, demostrando el uso de la herencia y el 
polimorfismo para adaptar el  comportamiento de  los  objetos según  el  tipo  de 
cliente.'''

from clases import Cliente, ClienteVIP, Pedido

def main():
    print("\n--Registro de Clientes--")
    id = int(input("\nIngrese el ID del cliente: "))
    nombre = input("\nIngrese el nombre del cliente: ")
    contacto = input("Ingrese el contacto del cliente: ")
    tipo_cliente = input("El cliente es VIP o no?: ")
    
    if tipo_cliente == 'si' or tipo_cliente == 'sí':
        cliente = ClienteVIP(id, nombre, contacto)
    else:
        cliente = Cliente(id, nombre, contacto)
