def login(username: str,passwd: str):
    if username == "usuario1" and passwd == "asdasd":
        return True
    else:
        return False
        
        
intentos = 0
while intentos < 3:
    user = input("Ingrese su nombre de usuario: ")
    pwd = input("Ingrese su contraseña: ")
    auth = login(username=user, passwd= pwd)
    if auth:
        print("Inicio de sesion con exito!!!\n")
    else:
        intentos += 1
        print("Error de inicio de sesion\n")
    