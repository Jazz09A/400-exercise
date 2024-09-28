import math
def calcular_area(radio: int):
    area = round(math.pi * (radio ** 2),2)
    perimetro = round(2*math.pi*radio,2)
    
    print(f"El area de la circunferecia es: {area}")
    print(f"El perimetro de la circunferecia es: {perimetro}")
    
calcular_area(2)