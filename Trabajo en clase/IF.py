x = int(input("ingrese un entero: "))
y = int(input("ingrese otro: "))
op = input("Seleccione la operacion: (+,-,*,/): ")

if op=='+' :
    print(x+y)
elif op== '-' :
    print(x-y)
elif op== '*' :
    print(x*y)
elif op == '/' :
    print(x/y)
else :
    print("operador no valido")