import maniArchivos
def funcionEnpriptacion():
    AlfabetoMin =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
    Alfabetomin2 = ['ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '-']


    AlfabetoMayus =  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
    AlfabetoMayus2 = ['Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '-']

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

    if opcion==1:

        archivo = str(input("Ingrese la ruta de su archivo: "))
        f = open(archivo, "r+")
        print(" \nEl contenido del archivo es: \n")
        contenido = f.read()
        print(contenido)
        f.close()
    elif opcion ==2:
        archivo = str(input("Ingrese la ruta de su archivo: "))
        f = open(archivo, "r+")
        linea = input("\nIntroduce el texto que deseas agregar: ")
        maniArchivos.escribirArchivo(linea, archivo)
        contenido = f.read()
        print("\n",contenido)
        f.close()
    elif opcion==3:
        archivo = str(input("Ingrese la ruta de su archivo: "))
        f = open(archivo, "r+")

        for linea in f:#accedo a cada linea
            for palabra in  linea.split():#accedo a las palabras
                cadena.append([])
                for i in range(len(palabra)):#Accedo a cada letra
                    cadena[b].append(palabra[i])#guardo cada letra en el arreglo de arreglo
                b+=1
        
        cadena.pop()
        d=0
        for a in range(len(cadena)):
            d=d+len(cadena[a])
            for b in range(len(cadena[a])):
                for c in range(len(AlfabetoMin)):
                    if cadena[a][b] == AlfabetoMin[c]:
                        Alfabetomin2= Alfabetomin2[-d:] + Alfabetomin2[:-d]
                        cadena[a][b]=Alfabetomin2[c]
                        Alfabetomin2= Alfabetomin2[d:] + Alfabetomin2[:d]
                        break
                    elif cadena[a][b] == Alfabetomin2[c]:
                        Alfabetomin2= Alfabetomin2[-d:] + Alfabetomin2[:-d]
                        for e in range(len(Alfabetomin2)):
                            if cadena[a][b] == Alfabetomin2[e]:
                                cadena[a][b] = AlfabetoMin[e]
                                break
                        Alfabetomin2= Alfabetomin2[d:] + Alfabetomin2[:d]
                        break
                    elif cadena[a][b] == AlfabetoMayus[c]:
                        AlfabetoMayus2= AlfabetoMayus2[-d:] + AlfabetoMayus2[:-d]
                        cadena[a][b]=AlfabetoMayus2[c]
                        AlfabetoMayus2= AlfabetoMayus2[d:] + AlfabetoMayus2[:d]
                        break
                    elif cadena[a][b] == AlfabetoMayus2[c]:
                        AlfabetoMayus2= AlfabetoMayus2[-d:] + AlfabetoMayus2[:-d]
                        for e in range(len(AlfabetoMayus2)):
                            if cadena[a][b]==AlfabetoMayus2[e]:
                                cadena[a][b] = AlfabetoMayus[e]
                                break
                        AlfabetoMayus2= AlfabetoMayus2[d:] + AlfabetoMayus2[:d]
                        break
                    else:
                        None
        encriptado = ""
        for a in range(len(cadena)):
            for b in range(len(cadena[a])):
                encriptado = encriptado + cadena[a][b]
            encriptado = encriptado+" "

        t = open("encriptadoEj2.txt", "w")
        t.write(encriptado)
        t.close()
        
        print("\n",encriptado,"\n")
        f.close()
    
    elif opcion==4:
        archivo = str(input("Ingrese la ruta de su archivo: "))
        
        t=open(archivo, "r+")
    
        for linea in t:#accedo a cada linea
            for palabra in  linea.split():#accedo a las palabras
                cadena.append([])
                for i in range(len(palabra)):#Accedo a cada letra
                    cadena[b].append(palabra[i])#guardo cada letra en el arreglo de arreglo
                b+=1
        cadena.pop()
        d=0
        for a in range(len(cadena)):
            d=d+len(cadena[a])
            for b in range(len(cadena[a])):
                for c in range(len(AlfabetoMin)):
                    if cadena[a][b] == AlfabetoMin[c]:
                        Alfabetomin2= Alfabetomin2[-d:] + Alfabetomin2[:-d]
                        cadena[a][b]=Alfabetomin2[c]
                        Alfabetomin2= Alfabetomin2[d:] + Alfabetomin2[:d]
                        break
                    elif cadena[a][b] == Alfabetomin2[c]:
                        Alfabetomin2= Alfabetomin2[-d:] + Alfabetomin2[:-d]
                        for e in range(len(Alfabetomin2)):
                            if cadena[a][b] == Alfabetomin2[e]:
                                cadena[a][b] = AlfabetoMin[e]
                                break
                        Alfabetomin2= Alfabetomin2[d:] + Alfabetomin2[:d]
                        break
                    elif cadena[a][b] == AlfabetoMayus[c]:
                        AlfabetoMayus2= AlfabetoMayus2[-d:] + AlfabetoMayus2[:-d]
                        cadena[a][b]=AlfabetoMayus2[c]
                        AlfabetoMayus2= AlfabetoMayus2[d:] + AlfabetoMayus2[:d]
                        break
                    elif cadena[a][b] == AlfabetoMayus2[c]:
                        AlfabetoMayus2= AlfabetoMayus2[-d:] + AlfabetoMayus2[:-d]
                        for e in range(len(AlfabetoMayus2)):
                            if cadena[a][b]==AlfabetoMayus2[e]:
                                cadena[a][b] = AlfabetoMayus[e]
                                break
                        AlfabetoMayus2= AlfabetoMayus2[d:] + AlfabetoMayus2[:d]
                        break
                    else:
                        None
        desencriptado=""
        for a in range(len(cadena)):
            for b in range(len(cadena[a])):
                desencriptado = desencriptado + cadena[a][b]
            desencriptado=desencriptado+" "
        t=open("desencriptado.txt", "w")
        t.write(desencriptado)
        print("\nTexto Encriptado: ", linea)
        print("texto desenciptado: ",desencriptado, "\n")
        t.close()
    else:
        print("Adios!!")
        None

i=0
while i==0:
    funcionEnpriptacion()
    print("\nVolver a ejecutar: 0")
    print("Ingrese un numero mayor a cero para salir")
    i=int(input("ingrese la opcion: "))