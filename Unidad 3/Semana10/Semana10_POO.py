import os

class Producto:
    def __init__(self, codigo, nombre, cantidad, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"Código: {self.codigo}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = {}
        self.cargar_inventario()

    def cargar_inventario(self):
        """Carga el inventario desde un archivo de texto."""
        try:
            if os.path.exists(self.archivo):
                with open(self.archivo, "r") as file:
                    for line in file:
                        # Leer cada línea y crear objetos Producto
                        codigo, nombre, cantidad, precio = line.strip().split(",")
                        self.productos[codigo] = Producto(codigo, nombre, int(cantidad), float(precio))
                print("Inventario cargado exitosamente desde el archivo.")
            else:
                print("El archivo de inventario no existe. Se creará uno nuevo al guardar datos.")
        except Exception as e:
            print(f"Error al cargar el inventario desde el archivo: {e}")

    def guardar_inventario(self):
        """Guarda el inventario actual en un archivo de texto."""
        try:
            with open(self.archivo, "w") as file:
                for producto in self.productos.values():
                    file.write(f"{producto.codigo},{producto.nombre},{producto.cantidad},{producto.precio}\n")
            print("Inventario guardado exitosamente en el archivo.")
        except PermissionError:
            print("Error: No se tienen permisos para escribir en el archivo.")
        except Exception as e:
            print(f"Error al guardar el inventario en el archivo: {e}")

    def agregar_producto(self, codigo, nombre, cantidad, precio):
        """Agrega un nuevo producto al inventario."""
        if codigo in self.productos:
            print("Error: Ya existe un producto con ese código.")
        else:
            self.productos[codigo] = Producto(codigo, nombre, cantidad, precio)
            self.guardar_inventario()
            print(f"Producto '{nombre}' agregado exitosamente.")

    def actualizar_producto(self, codigo, cantidad=None, precio=None):
        """Actualiza la cantidad o el precio de un producto existente."""
        if codigo not in self.productos:
            print("Error: No existe un producto con ese código.")
        else:
            producto = self.productos[codigo]
            if cantidad is not None:
                producto.cantidad = cantidad
            if precio is not None:
                producto.precio = precio
            self.guardar_inventario()
            print(f"Producto '{producto.nombre}' actualizado exitosamente.")

    def eliminar_producto(self, codigo):
        """Elimina un producto del inventario."""
        if codigo not in self.productos:
            print("Error: No existe un producto con ese código.")
        else:
            nombre = self.productos[codigo].nombre
            del self.productos[codigo]
            self.guardar_inventario()
            print(f"Producto '{nombre}' eliminado exitosamente.")

    def mostrar_inventario(self):
        """Muestra todos los productos en el inventario."""
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("Inventario:")
            for producto in self.productos.values():
                print(producto)

def menu():
    inventario = Inventario()

    while True:
        print("\n--- MENÚ DE GESTIÓN DE INVENTARIO ---")
        print("1. Mostrar inventario")
        print("2. Agregar producto")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            inventario.mostrar_inventario()
        elif opcion == "2":
            try:
                codigo = input("Ingrese el código del producto: ")
                nombre = input("Ingrese el nombre del producto: ")
                cantidad = int(input("Ingrese la cantidad: "))
                precio = float(input("Ingrese el precio: "))
                inventario.agregar_producto(codigo, nombre, cantidad, precio)
            except ValueError:
                print("Error: La cantidad y el precio deben ser números válidos.")
        elif opcion == "3":
            try:
                codigo = input("Ingrese el código del producto a actualizar: ")
                cantidad = input("Ingrese la nueva cantidad (deje en blanco para no cambiar): ")
                precio = input("Ingrese el nuevo precio (deje en blanco para no cambiar): ")
                cantidad = int(cantidad) if cantidad else None
                precio = float(precio) if precio else None
                inventario.actualizar_producto(codigo, cantidad, precio)
            except ValueError:
                print("Error: La cantidad y el precio deben ser números válidos.")
        elif opcion == "4":
            codigo = input("Ingrese el código del producto a eliminar: ")
            inventario.eliminar_producto(codigo)
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
