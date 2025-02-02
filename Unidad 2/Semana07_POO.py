# Programa: Conexión a Base de Datos
# Descripción: Clase que simula conectar y desconectar una base de datos usando constructores y destructores.
# Autora: Elizabeth Francisca Grefa Dahua
# Fecha: 24 de enero de 2025

class DatabaseConnection:
    # Simula una conexión a una base de datos.

    def __init__(self, db_name):
        # Constructor: Inicializa el nombre de la base de datos y establece la conexión.
        self.db_name = db_name
        self.connection = None
        self.connect()

    def connect(self):
        # Establece la conexión simulada.
        if not self.connection:
            print(f"Conectando a la base de datos {self.db_name}...")
            self.connection = True
            print("Conexión establecida.")
        else:
            print(f"Ya estás conectado a {self.db_name}.")

    def disconnect(self):
        # Cierra la conexión simulada.
        if self.connection:
            print(f"Desconectando de la base de datos {self.db_name}...")
            self.connection = None
            print("Conexión cerrada.")

    def __del__(self):
        # Destructor: Cierra la conexión automáticamente.
        self.disconnect()

# Ejemplo de uso
if __name__ == "__main__":
    db_conn = DatabaseConnection("MyDatabase")  # Crear conexión
    print("Realizando operaciones en la base de datos...")  # Simular operaciones
    db_conn.disconnect()  # Cerrar conexión manualmente (opcional)
