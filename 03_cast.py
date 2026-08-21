#Esto seria para transformar un tipo de valor a otro tipo diferente

print("conversion de tipos")
print(10 + int("100"))#aca sumo un numero normal con un numero que estaba en formato de texto, pero lo transformo a entero
print("100" + str(10))#aca sumo un numero en formato de texto con un numero entero, pero lo transformo a texto tambien(str y se juntan)

#Y ojo con esto, podes convertir un numero con decimal a uno entero y lo redondea hacia abajo sin excepcion
#Excepto por el comando Round, pero ojo que lo redondea al numero par mas cercano( por ejemplo de 3.5 a 4 y no a 3, y de 2.5 a 2 y no a 3)
#Solo si es justo en el medio, si es 3.6 o 3.4 lo redondea al mas cercano, pero si es 3.5 lo redondea al numero par mas cercano
print(int(10.9))#aca lo transformo a entero y lo redondea
print(float(10.9))#aca lo transformo a decimal normal
#Cada vez que el codigo lo muestre se va a ver la diferencia uno es 10 y el otro es 10.9


#Ojo con esto tambien, podes escribir un booleano en numeros negativos, pero solo el 0 dara como resultado False
print(bool(-1))#aca lo transformo a booleano y da True
print(bool(0))#aca lo transformo a booleano y da False 
print(bool(1))#aca lo transformo a booleano y da True, y no hay diferencia entre 1 y -1, ambos dan True, solo el 0 da False

#Algo parecido pasa aca
print(bool(""))#aca lo transformo a booleano y da False, porque es un texto vacio
print(bool(" "))#aca lo transformo a booleano y da True, porque es un texto con un espacio
print(bool("hola"))#aca lo transformo a booleano y da True, porque es un texto con contenido

#ojo tambien en transformar textos en enteros, si el texto no es un numero entero, va a dar error, por ejemplo el hola mundo y ponerle int
# print(int("hola mundo"))#esto va a dar error porque "hola mundo" no es un numero entero y no tiene sentido alguno
