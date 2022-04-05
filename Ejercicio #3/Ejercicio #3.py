import random
import maniArchivos
def funcionEnpriptacion():
    cadena = [[]]
    opcion = 0
    b=0
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
        archivo=str(input("ingrese la ruta del archivo a encriptar: "))
        f=open(archivo,"r+")
        text=f.read()
        texto = text.lower().split(" ")

        palabras = [
            'murcielago',
            'hipotenusa',
            'escupitajo',
            'sudorienta',
            'suponieras',
            'riachuelos',
            'autenticos',
            'bisabuelos',
            'bufonerias',
            'questionar'
        ]

        dispo = []
        mayor = 0
        count = 0
        word = ""
        enc = ""
        indice = 0
        indexL =0
        for letra in texto:
            word = ""
            enc = ""
            indice = 0
            indexL =0
            mayor = 0
            for palabra in palabras:
                count = 0
                for i in range(len(letra)):
                    if(letra[i] in palabra):
                        count+=1
                if(count>mayor):
                    mayor = count
                    word = palabra

            for i in range(len(palabras)):
                if(word == palabras[i]):
                    indice = i
            
            # logica
            enc= str(indice)
            for l in letra:
                indexL=""
                for i in range(len(word)):
                    if(l == word[i]):
                        indexL+=str(i)
                if(l not in word):
                    indexL+=l.upper()
                enc+=indexL
            dispo.append(enc)

        t = open("encriptadoEj3.txt", "w")
        t.write(" ".join(dispo))
        t.close()
        print(" ".join(dispo))
        f.close()

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
        
    else:
        print("Adios!!")
        exit()

i=0
while i==0:
    funcionEnpriptacion()
    print("0. Volver a ejecutar")
    print("Ingrese un numero mayor a cero para salir")
    i=int(input("ingrese la opcion: "))
