'''Gestion de productos e inventario
Diseñar una clase Producto que incluya atributos como codigo, nombre, precio y cantidad en stock.
Ademas que administre una coleccion de objetos Productos, incorporando metodos para agregar, buscar, actualizar y eliminar productos.
Este ejercicio permite modelar situaciones reales de gestion de ventas y refuerza el concepto de encapsualimiento y manejo de colecciones en programacion orientiada a objetos.'''

class Producto:
    
    def __init__(self, codigo, nombre, precio, stock):
        self._codigo = codigo
        self._nombre = nombre
        self._precio = precio
        self._stock = stock

    def get_codigo(self):
        return self._codigo

    def get_nombre(self):
        return self._nombre

    def get_precio(self):
        return self._precio

    def get_stock(self):
        return self._stock

    def __repr__(self):
        return f"Producto (codigo = {self.codigo}, nombre {self.nombre}, precio {self.precio})"

