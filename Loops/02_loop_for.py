#BLUCES FOR

#Estos bucles permiten ejecutar un bloque de codigo repetidamente mientras ITERA un iterable o una lista

print("\n Bucle For")

#Iterar una lista

frutas = ["manzana", "pera", "mandarina"]
for fruta in frutas:
    print(fruta)


#Se puede iterar sobre cualquier cosa iterable (Ser iterable significa que se pueden revisar sus varios sub-elementos, una sola letra o numero no lo es)

cadena = "kafa"
for caracteres in cadena:
    print(caracteres)
#En este caso revisa cada una de las letras y las muestra al ejectuar, en este caso esta iterando cadenas de textos

#Ahora voy a usar enumerate(), que sirve para enumar las prodiedades de la lista(como el indice y el valor)

frutas = ["manzana", "pera", "mandarina"]
for index, fruta in enumerate(frutas):
    print(f"El Indice es {index} y la fruta es {fruta}")
#
#Esto mostraria esto 
#El Indice es 0 y la fruta es manzana
#El Indice es 1 y la fruta es pera
#El Indice es 2 y la fruta es mandarina
#Cuando hay que enumerar los elementos de una lista siempre va primero el indice y luego el elemento (index, fruta)
#No hace falta nombrar las cosas como ahora, pero es una forma de mostrar que representa cada cosa. Se puede hacer de la forma mas comoda que nos quede
#Abreviar cosas y acortar nombres, solo improta la posicion, no el nombre

#PARA NO MAREARME MUCHO LA IA ME LO EXPLICO ASI

#for VARIABLE in HERRAMIENTA(COLECCION):
    # código...

#Variable se refiere a la variable que nosotros creamos para que temporalmente agarre un valor
#La herramienta es por que podemos usar sorted, enumerate etc para ordenar o enumerar si es que lo queremos los elementos de la lista
#Y coleccion es la variable o la lista que ya esta creada de la cual queremos sacar los elementos y aplicarle la herramienta/metodo para luego mostrarlo asi


print("\nOrden de los personajes ya jugables en gta 5")
pjgta5 = ["Michael Joven", "Michael Viejo", "Franklin", "Trevor"]
Orden5 = [ "primer", "segundo", "tercer", "cuarto"]
for indice5, pj in enumerate(pjgta5):
    print(f"El {Orden5[indice5]} personaje es {pj}")


#Bluces anidados
#Osea meter un for dentro de otro y otro y asi..
 
letras0 = ["A", "B", "C"]
numeros0 = [1, 2, 3]

for letra in letras0: #Aca se iteran cada letra de la lista de letras0
    for numero in numeros0: #Aca hace lo mismo y una vez que termina el primer bucle empieza a iterar el elemento que sigue
        print(f"{letra}{numero}")#Cuanto termina las primeras iteraciones vuelve a hacer el bucle hasta el ultimo elemento osea C



