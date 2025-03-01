import json
import os

class Producto:
    def __init__(self, id_producto, nombre, stock, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.stock = stock
        self.precio = precio
    
    def actualizar_stock(self, cantidad):
        self.stock = cantidad
    
    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio
    
    def to_dict(self):
        return {"id": self.id_producto, "nombre": self.nombre, "stock": self.stock, "precio": self.precio}
    
    @staticmethod
    def from_dict(data):
        return Producto(data["id"], data["nombre"], data["stock"], data["precio"])

class Inventario:
    def __init__(self, archivo="datos_inventario.json"):
        self.archivo = archivo
        self.productos = {}
        self.cargar_datos()
    
    def guardar_datos(self):
        with open(self.archivo, "w") as f:
            json.dump({k: v.to_dict() for k, v in self.productos.items()}, f, indent=4)
    
    def cargar_datos(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, "r") as f:
                datos = json.load(f)
                self.productos = {k: Producto.from_dict(v) for k, v in datos.items()}
    
    def agregar_producto(self, producto):
        if producto.id_producto in self.productos:
            print("El ID ya existe en el inventario.")
        else:
            self.productos[producto.id_producto] = producto
            self.guardar_datos()
            print("Producto agregado correctamente.")
    
    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_datos()
            print("Producto eliminado.")
        else:
            print("El producto no existe.")
    
    def actualizar_producto(self, id_producto, stock=None, precio=None):
        if id_producto in self.productos:
            if stock is not None:
                self.productos[id_producto].actualizar_stock(stock)
            if precio is not None:
                self.productos[id_producto].actualizar_precio(precio)
            self.guardar_datos()
            print("Producto actualizado.")
        else:
            print("No se encontró el producto.")
    
    def buscar_producto(self, nombre):
        encontrados = [p for p in self.productos.values() if nombre.lower() in p.nombre.lower()]
        for p in encontrados:
            print(f"ID: {p.id_producto} | Nombre: {p.nombre} | Stock: {p.stock} | Precio: ${p.precio:.2f}")
        if not encontrados:
            print("No se encontró ningún producto.")
    
    def mostrar_productos(self):
        if self.productos:
            for p in self.productos.values():
                print(f"ID: {p.id_producto} | Nombre: {p.nombre} | Stock: {p.stock} | Precio: ${p.precio:.2f}")
        else:
            print("Inventario vacío.")

def menu():
    inventario = Inventario()
    while True:
        print("\n1. Agregar producto\n2. Eliminar producto\n3. Actualizar producto\n4. Buscar producto\n5. Mostrar inventario\n6. Salir")
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            id_p = input("ID: ")
            nombre_p = input("Nombre: ")
            stock_p = int(input("Stock: "))
            precio_p = float(input("Precio: "))
            inventario.agregar_producto(Producto(id_p, nombre_p, stock_p, precio_p))
        elif opcion == "2":
            id_p = input("ID a eliminar: ")
            inventario.eliminar_producto(id_p)
        elif opcion == "3":
            id_p = input("ID a actualizar: ")
            stock_p = input("Nuevo stock (dejar en blanco para no cambiar): ")
            precio_p = input("Nuevo precio (dejar en blanco para no cambiar): ")
            inventario.actualizar_producto(id_p, int(stock_p) if stock_p else None, float(precio_p) if precio_p else None)
        elif opcion == "4":
            nombre_p = input("Nombre del producto: ")
            inventario.buscar_producto(nombre_p)
        elif opcion == "5":
            inventario.mostrar_productos()
        elif opcion == "6":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()

