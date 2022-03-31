f=open("ejemplo.txt", "r+")

AlfabetoMin =   ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l' ,'m', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
AlfabetoMayus = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
cadena = [[]]


b=0
for linea in f:#accedo a cada linea
    for palabra in  linea.split():#accedo a las palabras
        cadena.append([])
        for i in range(len(palabra)):#Accedo a cada letra
            cadena[b].append(palabra[i])#guardo cada letra en el arreglo de arreglo
        b+=1
        
cadena.pop()
d=1
print(cadena)


for a in range(len(cadena)):
    for b in range(len(cadena[a])):
        for c in range(len(AlfabetoMin)):
            if cadena[a][b] == AlfabetoMayus[c]:
                d=b+c+1
                cadena[a][b]=AlfabetoMayus[d]
                break
            if cadena[a][b] == AlfabetoMin[c]:
                d=b+c+1
                cadena[a][b] = AlfabetoMin[d]
                break

encriptado=""
for a in range(len(cadena)):
    for b in range(len(cadena[a])):
        encriptado = encriptado + cadena[a][b]
    encriptado=encriptado+" "

t=open("encriptadoEj1.txt", "w")

t.write(encriptado)
#print(AlfabetoMayus[26])
print(cadena)