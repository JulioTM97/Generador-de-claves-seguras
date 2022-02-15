import random

while 1 > 0:
    file = open("claves.txt", "r")
    pagina = str.upper(input("Inserte el nombre de la pagina: \n")+":")
    contenido = file.read()
    if contenido.find(pagina) > -1:
        print("Ya tienes una contraseña para esta pagina.")
        file.close()
        continue
    file.close()
    file = open("claves.txt", "a")
    longitud = int(input("Ingrese la longitud de la contraseña: \n"))
    clave = ""
    for i in range(longitud):
        tipoCaracter = int(random.randint(0, 2))
        if tipoCaracter == 0:
            #Mayusculas
            clave += chr(random.randint(65, 90))
        elif tipoCaracter == 1:
            #Minusculas
            clave += chr(random.randint(97, 122))
        else:
            #Numero
            clave += str(random.randint(0, 9))
    print("Su contraseña es: " + clave)
    file.writelines(pagina + "\n")
    file.writelines(clave + "\n\n")
    file.close()