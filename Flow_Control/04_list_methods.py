#Listas Metodos

#Los metodos mas importantes para trabajar con listas
##
#Se llaman metodos ya que es propiedad de la lista la cual estamos modificando con el .append o el .insert,etc

lista1 = [1, 2, 3, 4, 5]

lista1.append(6)#Esto añade cierto elemento al final de la lista
#[1, 2, 3, 4, 5, 6]
print(lista1)

lista1.insert(1, 88)#Esto inserta el elemento en la posicion que indiquemos (El primer numero)
print(lista1)

lista1.extend(["aguante boca", "Chupala gordo", "wachin"]) #Esto agrega varios elementos al final de la lista
print(lista1)

#Ahora vamos a eliminar elementos de una lista
lista1.remove(2)#Esto solo elimina LA PRIMERA aparicion en la cadena de numeros del 2
print(lista1)#Si hubiera mas de un 2 solo elimina el primero que aparece en la lista, y los otros se quedan

lista1.pop()#Su valor por defecto seria -1, entonces si no ponemos nada elimina por defecto el ultimo elemento de la lista
#Pero podemos ultilizar indices normales y tambien negativos: lista1.pop(2) o tambien 1 y asi
#tambien lo que hace es "agarrarse" y te lo devuelve si es que le asignas ese valor a otra variable o lista y luego le das un print
#ejemplo
#ultimo = lista1.pop() y luego le damos print, ahi nos va a mostrar el elemento que .pop elimino

#Tambien si por algun motivo queres eliminar todos los elementos se puede aplicar un clear
lista1.clear()
print(lista1)

#Otra forma de eliminar mas agresiva seria el del

#del lista1[-1]
#print(lista1)
#aca eliminaria el ultimo al poner -1

#ahora vamos a eliminar un rango de elementos
lista2 = ['Hola','Chau','Villero','Wachines', 'Estigarribia']

del lista2[1:3]#Aca usamos el del con rangos para eliminar cierta parte de la lista y no toda o uno solo
print(lista2)


#Otros metodos muy utiles

print("Ordenar las listas")
numeros = [1, 1700, 5, 100, 9999]
numeros.sort()
print(numeros)
#Esto ordena los numeros en orden correcto del menor al mayor
#Un dato aca es que este metodo la modifica, no la guarda y la podemos asigan a otra lista que se llame por ej numeros_ordenados
#como pasaba en el caso del .pop

#Si queremos crear una lista ordenada y que se "guarde" para luego asigarla y darle un print:
print("Ordenar las listas pero esta vez creando una copia")
numeros2 = [80, 100, 5000, 4, 8, 55]
#Ahora si podemos darle el valor a otra lista poniendo este metodo que se parece
numeros2_ordenados = sorted(numeros2)
print(numeros2_ordenados)
#En este caso se crea una copia de la lista y la guarda con los numeros ordenados

#Ahora voy a ver un caso con cadenas de textos y datos para este tipo de listas
print("Ordenar una lista con cadenas de texto exclusivamente en minusculas")
autos =["ford", "peugeot", "fiat","ford", "peugeot", "mclaren", "fiat" ]
autos_ordenados = sorted(autos)
print(autos_ordenados)
#En este caso ordena las marcas por el nombre y las junta en la lista
#Ahora un ejemplo con mayusculas y minusculas mezcladas, aca viene el problema

print("Ordenar listas de texto pero esta vez con mayusculas y minusculas mezcladas")
empresas = ["sony","Samsung", "Mcdonalds","Sony","samsung","mcdonalds"]
empresas_ordenadas = sorted(empresas)
print(empresas_ordenadas)
#En este caso ordena las mayusculas primero y luego las minusculas, y no importa si estan bien ordenadas o no

#Ahora vamos a usar "key" para arreglar este problema
print("Ordenar listas de texto pero esta vez con mayusculas y minusculas mezcladas (Ahora con key)")
empresas2 = ["sony","Samsung", "Mcdonalds","Sony","samsung","mcdonalds"]
empresas2.sort(key=str.lower)
print(empresas2)
#Aca cito a la IA
#key=str.lower: Le dice a Python: "Oye, antes de comparar los nombres para ordenarlos, conviértelos en minúsculas en tu mente, pero no alteres el texto real".
#Por eso cuando se hace print se siguen mostrando en su formato original, pero python las vio como todas minusculas y pudo ordenarlas

#Coas utiles a tener en cuenta:

numeros3 = [1, 2, 5, 1, 8, 9, 1, 66, 1, 77]
print(numeros3.count(1))
#Este metodo .count, sirve para contar cuantas veces cierto elemento se encuentra en la lista, en este caso nos diria 4
#Tambien le podemos decir que nos verifique si sabe que hay cierto elemento en la lista y nos tire un booleano (True/False)
print(66 in numeros3)#En este caso como el 66 si esta nos daria True, en caso contrario si le decimos 500 nos daria False

