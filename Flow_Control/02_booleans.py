#Los booleans basicamente son lo que vengo escribiendo hace rato
#Basicamente el True y el False
#Ahora viene un tema, antes yo habia escrito cosas como <= o >=
#Hay mas simbolos de estos y voy a tratar de printearlos y explicarlos

print("\n Operadores de Comparacion")
print("5 > 3:", 5 > 3) #True
print("5 < 3:", 5 < 3) #False
print("5 == 5:", 5 == 5) #True (Igualdad)
print("5 != 3:", 5 != 3) #True (Desigualdad)
print("5 >= 5:", 5 >= 5) # True (Mayor o igual que)
print("5 <= 3:", 5 <= 3) # False (Menor o igual que)

#Ahora vamos a comparar cadenas de texto, como escuche en un video son lexicograficas!
#En forma facil seria algo asi:

print("\n Comparacion de cadenas:")
print("manzana < pera:", "manzana" < "pera") #Aca va a tirar True xd, aunque el texto tenga mas caracteres no es por eso...
#Aca el dato es que analiza la primera letra, en base a cual va primero en el alfabeto por eso la M de manzana es menor y la P que viene despues es mayor

#Tambien el codigo es sensible a las mayusculas, ejemplo:

print(" 'hola' == 'Hola' ", "hola" == "Hola") #False

#Aca estan tambien una lista de Los operadores logicos que use antes:
print("\nOperadores lógicos:")
print("True and True:", True and True)   # True
print("True and False:", True and False)  # False
print("True or False:", True or False)    # True
print("False or False:", False or False)  # False
print("not True:", not True)             # False
print("not False:", not False)            # True


#Aca podemos hacer un ejercicio a mano para practicar los True, False y los operadores:

print("\n Tablas de la Verdad")
print("and:")
print("A     B     A and B")
print("True   True", True and True)
print("False   True", False and True)
print("True    False", True and False)
print("False   False", False and False)


print("\n or:")
print("A     B     A or B")
print("True  True ", True or True)
print("True  False", True or False)
print("False True ", False or True)
print("False False", False or False)

print("\n not:") 
print("A     not A")
print("True ", not True)
print("False", not False)

#Estos son ejemplos de como se comportarian, una vez que lo lees no es tan complejo
#Tengo en cuenta que solo el codigo procesa lo que hay fuera de las comillas, lo que esta entre comillas osea el texto es para representar
#El Verdadero calculo lo hace cuando le presentas un operador logico que lee las palabras que estan fuera de las comillas
