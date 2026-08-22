###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)



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

