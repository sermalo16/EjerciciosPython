from re import I


f=open("ejemplo.txt", "r+")
#x=250
#f.write(str(x)) Escritura en el archivo
#cadena = f.readlines()
#cadena = f.readline()

#for linea in f:
#    print(linea,end='') imprime sin enter

#for linea in f:        #Imprimer letras
#   for letra in linea:
#      print(letra, end=' ')

#for linea in f:  #Imprimir palabras
#    for palabra in linea.split():
#        print(palabra)

#l = [1, 4, 6, 7 , 2]
#l.pop()#elimina el ultimo elemento o el elmento que indiquemos
#l.insert(0,15)#inseta un elemento en la posicionindicada
#l= l[3:]+ l[:3]

#AlfabetoMin =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
#Alfabetomin2 = ['ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '-']

#Alfabetomin2=Alfabetomin2[-6:] + Alfabetomin2[:-6]
#print(AlfabetoMin, "\n", Alfabetomin2)

texto = ["hola","mundo"]

texto2= "koala"
for a in range(len(texto)):
    for b in range(len(texto[a])):
        print(texto[a][b])
print(e)
