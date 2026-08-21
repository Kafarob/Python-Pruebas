#Ahora voy a mostrar el formato input, que recopila datos del usuario, y los guarda en una variable, para luego poder usarlos
#Ejemplos:

print("Hola, como te llamas?") #aca le pregunto al usuario su nombre
nombre = input() #aca guardo el nombre del usuario en la variable nombre

#print(nombre) #aca muestro el nombre del usuario que guardamos en la variable nombre
#otro ejemplo para mostrar el nombre del usuario en una frase, usando f-string
print(f"Hola {nombre}, un gusto hablar!") #aca muestro el nombre del usuario
#otra forma seria tambien esta:
Nombre = input("Perdona, pero como te llamas?\n") #aca le pregunto al usuario su nombre y lo guardo en la variable Noombre
#Aca uso \n para hacer un salto de linea, y que el usuario escriba su nombre en la siguiente linea y no sea todo junto
print(f"Hola {Nombre}, un gusto hablar contigo de nuevo!") #aca muestro el nombre

age = input("cuantos años tenes?\n") #aca le pregunto al usuario su edad y lo guardo en la variable age
print(f"Hola {Nombre}, un gusto hablar contigo de nuevo! y tenes {age} años") #aca muestro el nombre y la edad del usuario
#Ojo aca, si quiero sumarle algun numero a la edad para decirle algo, no puedo ya que la edad esta en srt en realidad
#Un ejemplo para intentar arreglarlo o que se muestre la suma sin error seria asi:

age = input ("Escribe tu edad y te dire un dato curioso jaja\n") #aca le pregunto al usuario su edad y lo guardo en la variable age
#aca le sumo 5 a la edad del usuario, pero como age es un str, tengo que convertirlo a int para poder sumarle 5
age = int(age)#aca convierto la edad a int
print(f"Hola {Nombre}, un gusto hablar contigo de nuevo! y tenes {age} años, y en 5 años vas a tener {age + 5} años") 
#Todo esto es posible ya que python se ejecuta de arriba hacia abajo, y primero se ejecuta la linea 20, luego la 21, y asi sucesivamente
#Una vez ingresado y que se muestren los datos, antes de terminar la linea se cambia a una variable entera para poder hacer la suma

print("Ahora vamos a obtener multiples valores al mismo tiempo")

Pais, Ciudad = input("En que pais y ciudad vives?\n").split()# split() divide el texto ingresado en varias partes, usando los espacios
print(f"Tu entonces vives en {Pais}, {Ciudad}")