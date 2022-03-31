import maniArchivos


texto = str(input("ingrese la ruta del archivo: "))

def funcionEnpriptacion(texto):
    f = open(texto, "r+")
    AlfabetoMin = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                   'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    AlfabetoMayus = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    cadena = [[]]
    b = 0
    opcion = 0

    print("\nSeleccione una opcion: ")
    print("1. Leer archivo")
    print("2. Agregar Texto al archivo")
    print("3. Encriptar archivo")
    print("4. Desencriptar Acrchivo")
    print("Presione cualquier tecla para salir")
    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        print(" \nEl contenido del archivo es: \n")
        contenido = f.read()
        print(contenido, "\n")
    elif opcion == 2:
        linea = input("\nIntroduce el texto que deseas agregar: ")
        maniArchivos.escribirArchivo(linea, texto)
        contenido = f.read()
        print(contenido, "\n")
    elif opcion == 3:
        for linea in f:#accedo a cada linea
            for palabra in  linea.split():#accedo a las palabras
                for i in range(len(palabra)):#Accedo a cada letra
                    cadena[b].append(palabra[i])#guardo cada letra en el arreglo de arreglo
                b+=1
                cadena.append([])
        
        cadena.pop()
        d=1
        for a in range(len(cadena)):
            for b in range(len(cadena[a])):
                for c in range(len(AlfabetoMin)):
                    if cadena[a][b] == AlfabetoMayus[c]:
                        d = b+c+1
                        if d>26:
                            d=(d-26)-1
                        cadena[a][b] = AlfabetoMayus[d]
                        break
                    if cadena[a][b] == AlfabetoMin[c]:
                        d = b+c+1
                        if d>26:
                            d=(d-26)-1
                        cadena[a][b] = AlfabetoMin[d]
                        break
        encriptado = ""
        for a in range(len(cadena)):
            for b in range(len(cadena[a])):
                encriptado = encriptado + cadena[a][b]
            encriptado = encriptado+" "

        t = open("encriptadoEj1.txt", "w")

        t.write(encriptado)
        # print(AlfabetoMayus[26])
        print("\n",encriptado,"\n")
    elif opcion==4:

        t=open("encriptadoEj1.txt", "r+")
    
        for linea in t:#accedo a cada linea
            for palabra in  linea.split():#accedo a las palabras
                cadena.append([])
                for i in range(len(palabra)):#Accedo a cada letra
                    cadena[b].append(palabra[i])#guardo cada letra en el arreglo de arreglo
                b+=1
        cadena.pop()
        d=1
    
    
        for a in range(len(cadena)):
            for b in range(len(cadena[a])):
                for c in range(len(AlfabetoMin)):
                    if cadena[a][b] == AlfabetoMayus[c]:
                        d=(c-b)-1
                        cadena[a][b]=AlfabetoMayus[d]
                        break
                    if cadena[a][b] == AlfabetoMin[c]:
                        d=(c-b)-1
                        cadena[a][b] = AlfabetoMin[d]
                        break

        desencriptado=""
        for a in range(len(cadena)):
            for b in range(len(cadena[a])):
                desencriptado = desencriptado + cadena[a][b]
            desencriptado=desencriptado+" "
    

        t=open("desencriptado.txt", "w")
        t.write(desencriptado)
        print("\nTexto Encriptado: ", linea)
        print("texto desenciptado: ",desencriptado, "\n")

    
    else:
        print("\n")
        None

i=0
while i<=0:
    funcionEnpriptacion(texto)
    print("0. Volver a ejecutar")
    print("1. salir")
    i=int(input("ingrese la opcion: "))
