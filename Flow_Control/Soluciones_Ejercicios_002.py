#1
print("\nEjercicio 1")
mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
secreto = mensaje[7:]
print(secreto)


#2
print("\nEjercicio 2")
numeros = [10, 20, 30, 40, 50]
numeros[0], numeros[-1] = numeros[-1], numeros[0] # Intercambio en una sola línea
print(numeros)


#3
print("\nEjercicio 3")
pan = ["pan arriba"]
ingredientes = ["jamón", "queso", "tomate"]
pan_abajo = ["pan abajo"]
sandwich = pan + ingredientes + pan_abajo
print(sandwich)

#4
print("\nEjercicio 4")
lista = [1, 2, 3]
lista_duplicada = lista + lista
print(lista_duplicada)


#5
print("\nEjercicio 5")
lista = [10, 20, 30, 40, 50]
print(lista[2])
#Segun la IA este es una version mas corta y mas eficiente usando un simple slicing. solo si se quiere mostrar cierto valor en una lista controlada y mas corta
#A continuacion muestro el ejemplo de alguien que dejo la solucion en Github (Midudev)

lista = [10, 20, 30, 40, 50]
centro = len(lista) // 2
print(lista[centro])
#Ambos ejemplos cumplen su funcion, pero el primero es mas corto y para algo mas controlado
#este se basa en el comando para medir longitud (len) y hacer un calculo por la mitad
#luego perdir que la lista llamada centro que ya hizo el calculo muestre el resultado en pantalla, osea justo el medio de la lista



#6
print("\nEjercicio 6")
lista1 = [1, 2, 3, 4, 5, 6]
mitad = len(lista1)//2
lista_invertida = lista1[:mitad][::-1] + lista1[mitad:] # Ojo aca, me costo entenderlo y necesite ayuda
#Aca lo que hacen es dividir por la mitad la lista y luego aplicarle un "salto" pero invertido, que esto genera que en vez de saltar numeros y los lea diferente
#los lee de forma invertida hacia el otro lado, luego se suma de nuevo para unir la parte de la lista que faltaba, pero esta vez los : empiezan del lado derecho
#Dando a entender que no se modifica y que esa mitad se sigue leyendo igual
