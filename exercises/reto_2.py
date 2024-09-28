lado = 10
# Línea superior
print("*" * lado)

# Líneas intermedias (con el centro hueco)
for i in range(5):
    print("*" + " " * (lado - 2) + "*")

# Línea inferior
print("*" * lado)

