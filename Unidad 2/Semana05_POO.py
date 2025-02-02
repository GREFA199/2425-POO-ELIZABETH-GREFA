# Programa para calcular el área de un rectángulo
# Autora: Elizabeth Francisca Grefa Dahua
# Fecha: 24 de enero de 2025
# Descripción: Este programa calcula el área de un rectángulo a partir de su largo y ancho ingresados por el usuario.

def calcular_area_rectangulo(largo, ancho):
    """
    Calcula el área de un rectángulo.

    Parámetros:
    largo (float): El largo del rectángulo.
    ancho (float): El ancho del rectángulo.

    Retorna:
    float: El área del rectángulo.
    """
    return largo * ancho

try:
    # Solicita al usuario el largo y el ancho del rectángulo
    largo = float(input("Ingrese el largo del rectángulo: "))
    ancho = float(input("Ingrese el ancho del rectángulo: "))

    if largo <= 0 or ancho <= 0:
        print("El largo y el ancho deben ser valores positivos.")
    else:
        # Calcula el área utilizando la función definida
        area = calcular_area_rectangulo(largo, ancho)

        # Muestra el resultado con dos decimales
        print(f"El área del rectángulo es {area:.2f} unidades cuadradas.")

except ValueError:
    print("Por favor, ingrese un número válido.")
