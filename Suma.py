#Programa en Python para sumar dos numeros 
#Si no se declara el tipo de dato lo toma como string
x = input("Ingrese el valor de x: ")
y = input("Ingrese el valor de y: ")
resultado = x + y
print("El rsultado de la suma es: ", resultado)

#Si se declara el tipo del dato, lo toma como int
x = int(input("Ingrese el valor de x: "))
y = int(input("Ingrese el valor de y: "))
resultado = x+ y
print("El resultado de la suma es: ", resultado)

#Si se declara el tipo de dato, lo toma como float
#Con este tipo de dato se pueden sumaro enteros (int) y flotantes (float)
x = float(input("Ingrese el valor de x: "))
y = float(input("Ingrese el valor de y: "))
resultado = x + y
print("El resultado de la suma es: ", resultado)