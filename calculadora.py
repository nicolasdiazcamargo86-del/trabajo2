# calculadora.py - Versión Estable
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b

if __name__ == "__main__":
    print("--- Calculadora Básica ---")
    a = float(input("digite numero a "))
    b = float(input("digite numero b "))
    print("Suma (a + b):", sumar(a, b))
    print("Resta (a - b):", restar(a, b))
    #Correcion funciones de calculadora
    print("Multiplicación (a * b):", multiplicar(a, b))
    print("División (a / b):", dividir(a, b))