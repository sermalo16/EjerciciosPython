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

l = [1,2,3,4,5,6,7,8,9,10]
#l.pop()#elimina el ultimo elemento o el elmento que indiquemos
#l.insert(0,15)#inseta un elemento en la posicionindicada
for i in range(0,4):
    l.insert(-2,l.pop())#rotacion de la lista
print(l)