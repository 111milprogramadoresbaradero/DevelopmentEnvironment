"""Este codigo calcula el maximo de 
    un listado de numeros."""

n = eval(input("¿Cantidad de valores? "))
valores = []
for i in range(0,n):
    v1 = eval(input())
    valores.append(v1)
maximo = -1000000
for valor in valores:
    if (valor > maximo):
        maximo = valor
print(maximo) 

