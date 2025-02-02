class Personaje:

    def __init__(self, nombre, fuerza, agilidad, resistencia, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.agilidad = agilidad
        self.resistencia = resistencia
        self.vida = vida

    def mostrar_atributos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Fuerza: {self.fuerza}")
        print(f"Agilidad: {self.agilidad}")
        print(f"Resistencia: {self.resistencia}")
        print(f"Vida: {self.vida}")

    def recibir_ataque(self, daño):
        daño_real = max(daño - self.resistencia, 0)
        self.vida -= daño_real
        print(f"{self.nombre} ha recibido {daño_real} puntos de daño.")
        if self.vida <= 0:
            self.vida = 0
            print(f"{self.nombre} ha caído en combate.")

    def atacar(self, enemigo):
        print(f"{self.nombre} ataca a {enemigo.nombre}.")
        enemigo.recibir_ataque(self.fuerza)


class Guerrero(Personaje):

    def __init__(self, nombre, fuerza, agilidad, resistencia, vida, arma):
        super().__init__(nombre, fuerza, agilidad, resistencia, vida)
        self.arma = arma

    def mostrar_atributos(self):
        super().mostrar_atributos()
        print(f"Arma: {self.arma}")

    def atacar(self, enemigo):
        print(f"{self.nombre} utiliza su arma {self.arma} para atacar.")
        daño = self.fuerza + 5  # Bonus de daño por arma
        enemigo.recibir_ataque(daño)


class Mago(Personaje):

    def __init__(self, nombre, fuerza, agilidad, resistencia, vida, hechizo):
        super().__init__(nombre, fuerza, agilidad, resistencia, vida)
        self.hechizo = hechizo

    def mostrar_atributos(self):
        super().mostrar_atributos()
        print(f"Hechizo: {self.hechizo}")

    def atacar(self, enemigo):
        print(f"{self.nombre} lanza un hechizo {self.hechizo} para atacar.")
        daño = self.agilidad * 2  # Los magos usan agilidad para atacar
        enemigo.recibir_ataque(daño)


# Simulación de combate
def iniciar_combate(jugador1, jugador2):
    ronda = 1
    while jugador1.vida > 0 and jugador2.vida > 0:
        print(f"\n--- Ronda {ronda} ---")
        jugador1.atacar(jugador2)
        if jugador2.vida > 0:
            jugador2.atacar(jugador1)
        ronda += 1
    print("\n¡El combate ha terminado!")
    if jugador1.vida > 0:
        print(f"El ganador es {jugador1.nombre}.")
    elif jugador2.vida > 0:
        print(f"El ganador es {jugador2.nombre}.")
    else:
        print("Es un empate.")


# Creación de personajes
guerrero = Guerrero("Ragnar", 15, 8, 10, 100, "Espada de Acero")
mago = Mago("Merlín", 5, 12, 5, 80, "Rayo Arcano")

# Mostrar atributos
guerrero.mostrar_atributos()
mago.mostrar_atributos()

# Iniciar combate
iniciar_combate(guerrero, mago)
