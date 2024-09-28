def esMultiplo(a,b):
    if a %b == 0:
        return True
    else:
        return False
    
    
num1 = 10
num2 = 5
multiplo = esMultiplo(num1,num2)    
if multiplo:
    print(num1,"es multiplo de",num2)
else:
    print(num1,"no es multiplo de",num2)