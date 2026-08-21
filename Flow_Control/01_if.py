#Aca vamos a ver las sentencias condicionales
#Osea bloques que se ejecutan cuando se cumplen ciertas condiciones establecidas

print("\n Sentencia Simple Condicional")

edad = 20 #Asigno el valor 20 a la edad

if edad >= 20: #Aca Aplico la condicion de que si es mayor o igual a 20 va a mostrar lo que Dice el Print de abajo
    print("Tienes o eres mayor a 20 años")#Los dos puntos : luego del 20 serian como un "entonces", para dar pie al print
#La sangria es siempre necesaria, ya que si se separa no contaria para la condicion establecida y nos tiraria error nuestro IDE

#Ahora vamos a agregar otra condicional importante, que seria el "Else" y tambien el mas raro que seria el "Elif"

if edad >= 20:
    print("Sos mayor de edad")
    #Ahora viene el asunto para disponer de otro print segun la condicion
else:
    print("Sos un wachin")#En caso de contar con un input si ingresa numeros menores y mayores al 20 le dara su respectivo mensaje
#El tema es este, aveces no se pueden evitar, pero tampoco hay que llenar de bifurcaciones el codigo si no es 100% necesario

print("\n Sentencia condicional con elif")#Pongo de ejemplo una nota de un examen o algo similar    
nota = 9
if nota >= 9:
    print("Buenisima Nota!!")
elif nota >= 7:
    print("Buena nota!")#En este caso los elif sirve bastante por si la nota esta entre Buenisima nota y desaprobado, sin saltar de un extremo al otro
elif nota >= 5:
    print("Aprobado pero podria ser mejor!")
else:
    print("Desaprobado!")#El Else no es obligatorio, en este caso si, pero en otros casos no hace falta dar info extra por si no se cumplen
#Tener en cuenta que Dependiendo de la nota o valor que tenga la variable, solo mostrara el texto de la cual "Active" primero
#Si ponemos 9 entonces pondra la primera, y las demas seran ignoradas y no se revisan
#Se toma solo un camino, y se revisa desde arriba hacia abajo, hasta que se cumpla la condicion

#Voy con otro tipo de condiciones

print("\n Condiciones multiples")
edad = 25
tiene_registro = True

if edad >= 18 and tiene_registro: #El And en este caso revisa que ambas condiciones se cumplan, en caso de que alguna sea false no se "activa"
    print("Estas en condiciones para Manejar un auto🛻)")
else:
    print("Usted no esta apto para Conducir este auto")#Y tira el else, en este caso todo es true y la edad esta bien
#Pero en caso de un input que sea False y no cumpla la condicion directamente se manda al Else


#Antes use el And, que se denomina operador logico, pero hay otros tambien

#Supongamos que estamos en otro pais o con otras leyes y...
if edad >= 18 or tiene_registro:
    print("Estas en condiciones para Manejar un auto🛻)")#Aca estamos con el Or, que solo necesita una de las condiciones para que se "active"
else:
    print("Si paga una coima lo dejamos ir sin problema")

#Ahora voy a usar otro tipo que seria el if not

es_sabado = False
if not es_sabado:
    print("Falso sabado, pero nos juntamos igual")#Aca estariamos negando la variable para revisarla al reves y confirmar un False


#Ahora vamos con La anidacion de condicionales

edad = 20
lleno_de_guita = True

if edad <= 15:
    if lleno_de_guita:
        print("Podes entrar al boliche y salir de joda")#Esto si bien funciona, no es tan recomendable, ya que estamos metiendo muchas condiciones
    else:
        print("Salen esos mates")#Osea estamos anidando y generando esa Sangria que marca que hay una condicion adentro de otra
else:
    print("Los wachines no entran")#Si bien esto es algo cortito, si disponemos de mas datos lo mejor seria hacerlo lo mas corto posible
#Mientras mas anidadas o condiciones adentro de otras esten presentes, mas complejo sera el codigo

#Podemos darle la vuelta de esta forma:
if edad < 15:
    print("Los wachines no entran")
elif lleno_de_guita:
    print("Vamos de joda pero no podes entrar al boliche")
else:
    print("Salen esos mates y no salimos xd")

#Aca damos vuelta la tortilla y vamos con otras opciones
#Obvio cada uno lo resuelve teniendo en cuenta cuanta cantidad de variables y datos necesita revisan con las condiciones!


#Un ejemplo con los booleanos osea los True y False son los numeros, como hice bien al principio, cualquier numero da como resultado True
#Ya sea negativo, par inpar etc. Pero si el valor es 0 entocnes siempre mostrara un False como resultado

#Ejemplo:

numero = 1
if numero:
    print("El numero no es cero")

numero = 0
if numero:
    print("Aca no entra nunca la revision de codigo")#Por que? por que ya el numero uno es True y activa el primer if



nombre = "Juan"
if nombre:
    print("El nombre no esta vacio") #En este caso los textos cuando estan vacios se mantienen como False pero en este caso Dice Juan
#Entonces cuando se ejecute mostrara el texto del print ya que siempre da True en la condicion if