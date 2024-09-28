def calculo_temp_media(temp_max, temp_min):
    suma = temp_max + temp_min
    media = suma / 2
    return media

#parte 2
dias = int(input("Ingrese el numero de dias: "))
for i in range(dias + 1):
    temp_max = float(input("Ingrese la temperatura maxima: "))
    temp_min = float(input("Ingrese la temperatura minima: "))
    media = calculo_temp_media(temp_max, temp_min)
    print(f"La temperatura media para el dia {i+1}: ", media)