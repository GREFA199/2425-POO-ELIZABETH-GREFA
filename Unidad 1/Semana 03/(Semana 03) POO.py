class ClimaDiario:
    def __init__(self):
        self.temperaturas = []

    # Método para ingresar las temperaturas
    def ingresar_temperaturas(self):
        print("Ingrese las temperaturas diarias (en °C):")
        for i in range(7):
            temp = float(input(f"Día {i + 1}: "))
            self.temperaturas.append(temp)

    # Método para calcular el promedio semanal
    def calcular_promedio(self):
        if not self.temperaturas:
            return 0
        return sum(self.temperaturas) / len(self.temperaturas)

# Programa principal
if __name__ == "__main__":
    clima = ClimaDiario()
    clima.ingresar_temperaturas()
    promedio = clima.calcular_promedio()
    print(f"El promedio semanal de temperatura es: {promedio:.2f}°C")

