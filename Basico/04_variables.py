#Las variables sirven para almacenar datos, y estos datos pueden ser de diferentes tipos, como números, texto, listas, etc.
#Y para asignarlo seria algo asi:
My_name = "Kafa" #aca estoy asignando un texto a la variable My_name
My_age = 25 #aca estoy asignando un numero entero a la variable My_age
My_height = 1.79 #aca estoy asignando un numero decimal a la variable My_height

#y aca abajo puedo ejecutar print y mostrar  el contenido de las variables ya hechas
print(My_name)
print(My_age)
print(My_height)

#Se pueden asignar variables con el mismo nombres y diferente valor 
#Python es de tipado dinamico: el tipo de dato se determina en tiempo de ejecucion, y no es necesario declarar el tipo
#un ejemplo seria:
name = "Kafa"
print(type(name))

name=500
print(type(name))
#Cuando se ejecute, me va a mostrar que primero es un str y luego un int, a esto se le llama tipado dinamico
#Tambien es de tipado fuerte, osea no reliza conversiones automaticas
#Por ejemplo, si yo hago esto:
#print("Hola" + 5) #aca me va a dar error, porque no puedo sumar un str con un int, y no hace conversiones automaticas   
#Si quiero hacer eso tengo que convertirlo o escribirlo de otra manera, por ejemplo:
print("Hola" + str(5)) #aca me va a mostrar "Hola5", ya que se juntan al ser ambos str, y no hace conversiones automaticas

#Ahora se van a mostrar ejemplos de f-strings(literal de cadena de formato), que son una forma de formatear strings en Python
#Se pueden usar para mostrar variables dentro de un string
print(f"Hola soy {name} y tengo {My_age} años") #aca me va a mostrar "Hola soy Kafa y tengo 25 años", ya que se reemplaza 
#En este caso name tendria el valor de 500, ya que se ejecuta despues de la primera asignacion. Yo le puse 500 debajo de mi nombre(15 y 18)
print(f"Hola soy {name} y tengo {My_age + 40}  años")
#Aca me va a mostrar "Hola soy 500 y tengo 65 años", ya que se reemplaza name por 500 y My_age por 25, y se le suma 40 a My_age
#Esto existe desde la 3.6 de python, y en versiones anteriores no se podia hacer asi como esta aca
#Dicho esto, por lo que entiendo no es la mejor forma de mostrar variables

#Aca hay un ejemplo de como asignar rapido variables, tampoco es la mas recomendable, pero se puede hacer
city, country, continent = "Buenos Aires", "Argentina", "America"
print(f"Hola soy de {city}, {country}, {continent}") #aca me va a mostrar "Hola soy de Buenos Aires, Argentina, America"
#No se puede recomendar pero se puede econtrar en algunas lineas de codigo con este formato

#La forma mas recomendada es en convensiones de nombres de variables
#Ejemplo de convension de nombres de variables:
mi_nueva_variable = "Version correcta" #snake_case, es la mas recomendada
#Se pueden crear variables con mayusculas, pero no es recomendable, ya que se usan para constantes
#Y tampoco hace falta hacer la snake case con este simbolo: _ (si es que la variable tiene un nombre facil y rapido de escribir)
#Algunos ejemplos de nombres de variables que no es comun verlos:
MiNuevaVariable = "Version no recomendada" #camelCase, no es la mas recomendada tampoco, si bien tiene sentido, no es la mas comun de ver
minuevavariable = "Version no recomendada" #Todo el nombre en minusculas y todo junto, no es la mas recomendada

mi_nueva_variable123 = "Version correcta" #snake_case, es la mas recomendada, y se puede usar numeros al final del nombre de la variable

#Ojo con este dato!!!
#Python no tiene constantes (Ejemplo: Pi = 3.14159, etc), pero se puede simular una constante con una variable en mayusculas
#Una constante es un valor que no cambia, y una variable es un valor que puede cambiar, pero en python no hay constantes reales
#No se puede usar por ejemplo el formato const como en otros lenguajes
#Como dije antes se puede simular poniendo todo en mayusculas, pero no es recomendable, ya que no es una constante real
#Un ejemplo seria asi:
PI = 3.14159 #aca estoy simulando una constante, pero no es recomendable hacerlo

#Nombres no validos para variables:
#1. No puede empezar con un numero, por ejemplo: 1variable = "no valido" #esto daria error, ya que no puede empezar con un numero
#2. No puede tener espacios, por ejemplo: mi variable = "no valido" #esto daria error, ya que no puede tener espacios
#3. Tambien simplemente no se pueden usar palabras de python en si, como true, print, etc, ya que son palabras reservadas del lenguaje

Is_user_logged_in: bool = True #aca estoy asignando un valor booleano a la variable Is_user_logged_in, osea true
print(Is_user_logged_in) #aca me va a mostrar True, ya que es un valor booleano

#Que pasa si escribo lo mismo pero le asigno un numero? Bueno, en python no hay problema, ya que es de tipado dinamico
Is_user_logged_in: bool = 20 #aca estoy asignando un valor entero a la variable Is_user_logged_in, osea 20
print(Is_user_logged_in) #aca me va a mostrar 20, ya que es un valor entero y no genera problemas

#Pyhton se salta la declaracion de tipo de variable, y no genera error, ya que es de tipado dinamico, pero no es recomendable hacerlo
#La buena noticia es que python puede chequearlo dependiendo de como configures el IDE, como en este caso VS code
#Normalmente no lo tengo puesto en strict, pero si lo pongo en strict me va a mostrar un error
#Por que un numero no puede ser algo booleano (Osea true o false)
#Tambien sirve con variables que creaste antes y luego la quieres cambiar, todo depende de que tan estricto sea tu codigo o como escribas
















