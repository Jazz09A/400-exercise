#Metodo euclides MCD

def mcd(a, b):
    """Calcula el máximo común divisor (MCD) de dos números utilizando el algoritmo de Euclides.

    Args:
        a: Primer número.
        b: Segundo número.

    Returns:
        El máximo común divisor de a y b.
    """

    while b != 0:
        a, b = b, a % b
    return a

# Ejemplo de uso:
resultado = mcd(180, 150)
print(f"El MCD es: {resultado}")
    
        
        