import maniArchivos

def funcionEnpriptacion():
    
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
    print("Presione cualquier tecla para salir\n")
    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        texto = str(input("ingrese la ruta del archivo a encriptar: "))
        f = open(texto, "r+")
        print(" \nEl contenido del archivo es: \n")
        contenido = f.read()
        print(contenido, "\n")
        f.close()
    elif opcion == 2:
        texto = str(input("ingrese la ruta del archivo a encriptar: "))
        f = open(texto, "r+")
        linea = input("\nIntroduce el texto que deseas agregar: ")
        maniArchivos.escribirArchivo(linea, texto)
        contenido = f.read()
        print(contenido, "\n")
        f.close()
    elif opcion == 3:
        texto = str(input("ingrese la ruta del archivo a encriptar: "))
        f = open(texto, "r+")
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
        print("\n",encriptado,"\n")
        f.close()
        t.close()

    elif opcion==4:
        texto = str(input("ingrese la ruta del archivo a desncriptar: "))
        
        t=open(texto, "r+")
    
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
        print("Adios!!")
        None

i=0
while i==0:
    funcionEnpriptacion()
    print("0. Volver a ejecutar")
    print("Ingrese un numero mayor a cero para salir")
    i=int(input("ingrese la opcion: "))
