#Pedimos el valor de kilometros que se corrieron, los convertimos a millas
#Si el valor de las millas es = 10 entonces imprimir "meta no cumplida"
#De otra forma imprimir "Meta cumplida"
#1 kilometro es = 0.621371 millas
#solicitar los kilometros
k=float(input("¿Cuantos Kilometros corriste?"))
#calcular las millas
factor = 0.621371 
millas= k*factor
if millas == 10:
    print("Meta cumplida")
else:
    print("Meta cumplida")
#imprimir una salida como esta: 1 kilometro(s) equivale a .621 millas
print("%.1f Kilometros(s) equivale a: %.2f millas" %(k, millas))