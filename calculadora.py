# calculadora.py - Versión Estable
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

if __name__ == "__main__":
    print("--- Calculadora Básica ---")
    print("Suma (5 + 3):", sumar(5, 3))
    print("Resta (5 - 3):", restar(5, 3))
    #Version dañada
    print("Multiplicación (5 * 3):", multiplicar(5, 3))  # Esta línea causará un error porque la función multiplicar no está definida
    print("División (5 / 3):", dividir(5, 3))  # Esta línea también causará un error porque la función dividir no está definida