class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo_autor = (titulo, autor)  # Tupla para garantizar inmutabilidad
        self.categoria = categoria
        self.isbn = isbn
    
    def __str__(self):
        return f"{self.titulo_autor[0]} de {self.titulo_autor[1]} (ISBN: {self.isbn})"


class Usuario:
    def __init__(self, nombre, usuario_id):
        self.nombre = nombre
        self.usuario_id = usuario_id  # ID único
        self.libros_prestados = []  # Lista para gestionar los libros prestados
    
    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.usuario_id})"


class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}  # Diccionario con ISBN como clave
        self.usuarios = set()  # Conjunto para manejar IDs de usuario únicos
        self.prestamos = {}  # Diccionario de préstamos usuario_id -> lista de libros

    def agregar_libro(self, libro):
        if libro.isbn not in self.libros_disponibles:
            self.libros_disponibles[libro.isbn] = libro
            print(f"Libro agregado: {libro}")
        else:
            print("Este libro ya está en la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
            print(f"Libro con ISBN {isbn} eliminado de la biblioteca.")
        else:
            print("El libro no existe en la biblioteca.")

    def registrar_usuario(self, usuario):
        if usuario.usuario_id not in self.usuarios:
            self.usuarios.add(usuario.usuario_id)
            self.prestamos[usuario.usuario_id] = []
            print(f"Usuario registrado: {usuario}")
        else:
            print("El usuario ya está registrado.")

    def dar_baja_usuario(self, usuario_id):
        if usuario_id in self.usuarios and not self.prestamos[usuario_id]:
            self.usuarios.remove(usuario_id)
            del self.prestamos[usuario_id]
            print(f"Usuario con ID {usuario_id} eliminado.")
        else:
            print("No se puede eliminar: usuario no existe o tiene libros prestados.")

    def prestar_libro(self, usuario_id, isbn):
        if usuario_id in self.usuarios and isbn in self.libros_disponibles:
            libro = self.libros_disponibles.pop(isbn)
            self.prestamos[usuario_id].append(libro)
            print(f"Libro prestado: {libro} a usuario {usuario_id}")
        else:
            print("No se puede prestar: libro o usuario no disponible.")

    def devolver_libro(self, usuario_id, isbn):
        if usuario_id in self.prestamos:
            for libro in self.prestamos[usuario_id]:
                if libro.isbn == isbn:
                    self.prestamos[usuario_id].remove(libro)
                    self.libros_disponibles[isbn] = libro
                    print(f"Libro devuelto: {libro}")
                    return
            print("El usuario no tiene este libro prestado.")
        else:
            print("Usuario no registrado.")

    def buscar_libro(self, titulo=None, autor=None, categoria=None):
        resultados = []
        for libro in self.libros_disponibles.values():
            if (titulo and titulo.lower() in libro.titulo_autor[0].lower()) or \
               (autor and autor.lower() in libro.titulo_autor[1].lower()) or \
               (categoria and categoria.lower() == libro.categoria.lower()):
                resultados.append(libro)
        
        if resultados:
            for libro in resultados:
                print(libro)
        else:
            print("No se encontraron libros con los criterios dados.")

    def listar_libros_prestados(self, usuario_id):
        if usuario_id in self.prestamos and self.prestamos[usuario_id]:
            print(f"Libros prestados a {usuario_id}:")
            for libro in self.prestamos[usuario_id]:
                print(libro)
        else:
            print("El usuario no tiene libros prestados.")


# Pruebas del sistema
biblioteca = Biblioteca()
libro1 = Libro("1984", "George Orwell", "Ficción", "123456789")
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", "Realismo mágico", "987654321")
usuario1 = Usuario("Juan Pérez", "U001")

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.registrar_usuario(usuario1)
biblioteca.prestar_libro("U001", "123456789")
biblioteca.listar_libros_prestados("U001")
biblioteca.devolver_libro("U001", "123456789")
biblioteca.listar_libros_prestados("U001")

