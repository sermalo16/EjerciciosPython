from pickle import NONE
import maniArchivos
f = open("ejemplo.txt", "r+")
archivo = "ejemplo.txt"

AlfabetoMin =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
Affabetomin2 = ['ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '-']


AlfabetoMayus =  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
Alfabetomayus2 = ['Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '-']

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

if opcion==1:
    print(" \nEl contenido del archivo es: \n")
    contenido = f.read()
    print(contenido)
elif opcion ==2:
    linea = input("Introduce el texto que deseas agregar: ")
    maniArchivos.escribirArchivo(linea, archivo)
    contenido = f.read()
    print("\n",contenido)
elif opcion==3:
    for linea in f:#accedo a cada linea
        for palabra in  linea.split():#accedo a las palabras
            cadena.append([])
            for i in range(len(palabra)):#Accedo a cada letra
                cadena[b].append(palabra[i])#guardo cada letra en el arreglo de arreglo
            b+=1
        
    cadena.pop()
    d=1
    print(cadena)
    d=1
    for a in range(len(cadena)):
        for b in range(len(cadena[a])):
            for c in range(len(AlfabetoMin)):
                
                NONE
    encriptado = ""
elif opcion==4:
    None
else:
    None