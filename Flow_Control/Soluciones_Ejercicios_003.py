#1

print("\nEjercicio 1")

lista1 =[1, 2, 3, 4, 5]
lista1.append(6)
lista1.insert(2, 10)
lista1[0] = 0
print(lista1)


#2

print("\nEjercicio 2")

lista_a = [1, 2, 3]
lista_b = [4, 5, 6, 1, 2]

lista_a.extend(lista_b)
lista_a.remove(1)
numero_eliminado = lista_a.pop(3)
print(f"numero_eliminado: {numero_eliminado}")
lista_b.clear()
print("lista a:", lista_a)
print("Lista b:", lista_b)

#3
print("\nEjercicio 3")

lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
del lista1[2:5]
print(lista1)


#4
print("\nEjercicio 4")

lista1 = [5, 2, 8, 1, 9, 4, 2]
lista1.sort()
print(lista1)
print(lista1.count(2))
print(7 in lista1)

#Si se quiere hacer mas ordenado y/o profesional se puede hacer de esta forma usando f y cadenas de textos para decir lo que estamos haciendo

lista = [5, 2, 8, 1, 9, 4, 2]
lista.sort()
cantidad_dos = lista.count(2)
esta_el_siete = 7 in lista
print(f"Lista ordenada: {lista}") #Output: Lista ordenada: [1, 2, 2, 4, 5, 8, 9]
print(f"Cantidad de 2: {cantidad_dos}") #Output: Cantidad de 2: 2
print(f"¿Está el 7?: {esta_el_siete}") #Output: ¿Está el 7?: False




#5
print("\nEjercicio 5")

lista_original = [1, 2, 3]
copia_1 = lista_original[:]
copia_2 = lista_original.copy()
Referencia = lista_original
Referencia[0] = 10
print(f"Lista original: {lista_original}")
print(f"Copia 1 (slicing): {copia_1}")
print(f"Copia 2 (copy): {copia_2}")
print(f"Referencia: {Referencia}")


#6

print("\nEjercicio 6")

Frutas = ["Manzana", "pera", "BANANA", "naranja"]
Frutas.sort(key=str.lower)
print(Frutas)
