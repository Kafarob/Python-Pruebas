#1
print("\nEjercicio 1:")
num1 = int(input("Por favor introduce un numero:"))
num2 = int(input("Por favor introduce el segundo numero"))
if num1 < num2:
    print(f"{num2} es mayor que {num1}")
elif num1 > num2:
    print(f"{num1} es mayor que {num2}")
else:
    print("Ambos numeros son identicos")




#2
print("\nEjercicio 2:")

num1 = float(input("Primer numero:"))
num2 = float(input("Segundo numero"))
operacion = input("Introduce un simbolo: (+. -, *, /):")

if operacion == "+":
    resultado = num1 + num2
elif operacion == "-":
    resultado = num1 - num2
elif operacion == "*":
    resultado = num1 * num2
elif operacion == "/":
    resultado = num1 / num2
    if num2 == 0:
        print("No se puede dividir un numero por 0")
    else:
        resultado = num1 / num2
if 'resultado' in locals():#Esto sirve para comprobar si existe la variable resultado y que la muestre
    print(f"El resultado es: {resultado}")

#3
#En este ejercicio habia que aplicar formulas de residuo y modulo las cuales no conocia muy bien, asi que este ejercicio me lo salte


#4
print("\nEjercicio 4:")
edad = int(input(" Introduce una edad:"))

if 0 <= edad <= 2:
    print("Edad de bebe")
elif 3 <= edad <= 12:
    print("Edad de un niño")
elif 13 <= edad <= 17:
    print("Edad de Adolescente")
elif 18 <= edad <= 64:
    print("Edad Adulta")
elif edad >=64:
    print("Adulto Mayor")
else:
    print ("Entrada o edad no valida")