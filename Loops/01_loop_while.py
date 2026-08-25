#Bucles (While)

#Permiten repetir un bloque de codigo mientras se cumpla alguna condicion
###

print("\nBucle While")

#Bucle con una simple condicion

contador = 0
while contador <= 5:
    print(contador)
    contador += 1 #Esto es muy importante para evitar lus bucles infinitos

while True:
    print("hola")
    break
#Al no poner una condicion de salida, no le damos ninguna instruccion o un acercamiento a lo que queremos llegar, por lo tanto es infinito
#Aca estaria mostrando holas hasta que nosotros lo paremos
#Hay que acordarse que eventualmente la condicion se tiene que cumplir para llegar al final, como por ejemplo del 1 al 5 como el anterior

#Ojo que tambien tenemos la palabra Break, para salir de un bucle

print("Contador 2 con un bucle infinito pero lo cortamos con un break al llegar a 20:")
contador2 = 0
while True:
    print(contador2)
    contador2 += 1
    if contador2 == 21:
        break

#No siempre tiene sentido un break pero por ejemplo si no sabes cual es la condicion de salida y hasta que no encuentres cierto valor o elemento no quieres terminarlo
#Un ejemplo para usar un break en un caso que quieras encontrar algo especifico

print("\nContador para buscar un numero mutiplo de 5")
contador3 = 0

while contador3 <=100:
    contador3 += 1
    print(contador3)
    if contador3 % 5 == 0: # Si una división tiene un resto de cero, significa que el primer número se puede dividir perfectamente por el segundo. Por lo tanto, ¡es uno de sus múltiplos!
        print("Este numero es multiplo de 5")
        break

#Ahora voy a ver el Continue, lo que hace es saltar con esa iteracion
#Y continua con el bucle

print("\nBucle con continue")
contador4 = 0
while contador4 < 10:
    contador4 +=1
    if contador4 % 2 == 0:
        continue #Aca lo que hace este continue es volver a inciar el bucle, si el numero no es par entonces si se activa el print, pero si es par lo ignora
    #Todo lo que este por debajo no se ejecutara cuando se cumpla el if, solo en caso de que el numero sea impar. Si es impar entonces si se activa el print
    print(contador4)



#Ahora voy con la condicion Else, la pregunta es, cuando se ejecuta?

print("\nBucle while con elese")
contador5 = 0
while contador5 <= 5:
    print(contador5)
    contador5 += 1
else:
     print("El bucle ha terminado en 5")
#la pregunta es, el bucle termino y podriamos poner print sin ningun problema y no pasaria nada
#Si se puede hacer normalmente, pero se puede usar para asegurarte al 100% que el bucle termino y se encontro la condicion falsa y termina
#Un else si hay un break directamente no se activa y nunca se muestra


#Ahora vamos a ver un ejemplo para pedirle a un usuario un numero que tiene que ser positivo
#Sino no pone algun numero positivo, el bucle no lo deja en paz