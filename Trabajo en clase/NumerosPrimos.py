numero= int(input("Ingrese un numero a evaluar: "))
valor= range(2,numero)
contador = 0
for n in valor:
  if numero % n == 0:
    contador +=1
if contador > 0 :
  print("El numero no es primo" )
else:
  print("El numero es primo")