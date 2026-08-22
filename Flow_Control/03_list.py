#Las listas son secuencias mutables de elementos
#Pueden contener elementos de varios tipos

print("\nCrear Listas")
lista1 = [1, 2, 3, 4, 5, 6, 7, 8] #Lista de enteros
lista2 = ["Autos","Aviones","Barcos"]#Lista de cadenas
lista3 = [1, "hola", 3.14, True] #Lista de tipos mixtos


lista_vacia = []
lista_de_listas = [[1, 2], [3, 4]]
lista_matrix = [[1, 2], [2, 3], [4, 5]]

print(lista1)
print(lista2)
print(lista3)
print(lista_vacia)
print(lista_de_listas)
print(lista_matrix)


#Acceso a elementos por indice
#Todas las listas empiezan con 0 y no con 1
#Tener en cuenta esto al elegir cada elemento y su posicion

print("\nAcceso a elementos por indice")

print(lista1[0])#1
print(lista3[2])#3.14
print(lista2[-1])
#Aca es un atajo para elegir el elemento ultimo, mientras mas vayamos restando va en sentido contrario, hasta llegar al primero
print(lista2[-2])

print(lista_de_listas[1][0])#Aca primero se especifica que lista interna quieres acceder y luego la posicion de adentro
#Aca deberia mostrar el numero 3


#TEMA IMPORTANTE ACA
#El Slicing de las listas (cortarlas)

print(lista1[1:4]) #Aca arranca desde la posicion 2 hasta la 4, pero el ultimo numero no estaria incorporado, se detiene uno antes
#En este caso deberia enseñar: 2, 3 y 4

#Tambien se puede hacer de esta forma para que nos de HASTA la posicion que nosotros queramos
print(lista1[:3]) #En este caso mostraria 1, 2, y 3
print(lista1[3:]) #En este caso serian el 4 y 5
print(lista1[:])#Este simbolo copia la lista y la representa de la misma forma que la original

#Este ultimo parametro se puede usar para generar otras variedades
print(lista1 [::2])#Con esto se salta los valores de 2 en 2 y en cualquier numero que pongamos como los ejemplos de abajo
print(lista1 [::3])
print(lista1 [::4])
#Tambien esta la lista invertida obviamente!
print(lista1[::-1])
print(lista1[::-2])


#Modificar elementos de la lista
#Podemos cambiarlo creando una variable y asignando algun valor diferente al original
lista1[0] = 60
print(lista1)
#Aca hay que respetar las posiciones y no poner alguna fuera del rango que pusimos, por ej hasta el 7 u 8
#Pero solo la posicion, obvio el numero podemos cambiarlo a gusto, es decir el valor

#Ahora probemos en agregar mas elementos a una lista
#ejemplo
lista_kafa = [1, 2, 3]
#Ahora si intentamos hacer una suma como cualquier operacion, en vez de sumar los numeros o solaparse, lo que hace es unirse naturalmente
lista_kafa = lista_kafa + [4, 5, 6]
#En este caso deberia dar una lista completa desde el numero 1 al 6 
print(lista_kafa)
#Si bien esta forma esta buena, no es la mas eficiente ni tampoco la manera mas corta
#Aca viene un ejemplo de la segunda manera:

lista_kafa += [7, 8, 9]#Aca agrego mas numeros para que se sigan sumando, de esta manera con el codigo anterior y este se sumarian del 1 al 9
print(lista_kafa)
#Como se ve esta es mas directa y mas corta, que con listas o datos mas grandes vendria mejor

#Recuperar longitud de una lista
print("longitud de lista", len(lista_kafa))#Con el comando len de esta forma vemos que tan larga y que tanto contenido tiene dicha lista
#Una vez que lo ejecutemos nos dira longitud de la lista 9, ya que antes agregamos numeros del 1 hasta el 9
