'''Ejercicio 1: Conversor de Temperatura
Escribe un programa que convierta una temperatura de grados Celsius a grados
Fahrenheit.'''

# Solicitar al usuario la temperatura en grados Celsius
celsius = float(input("Ingrese la temperatura en grados Celsius: "))

# Convertir grados Celsius a grados Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Mostrar el resultado
print("La temperatura en grados Fahrenheit es:", fahrenheit)

'''Ejercicio 2: Calculadora de Propina
Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo
una propina del 15% sobre el total de la cuenta.'''

def calcular_total_con_propina(total_cuenta):
    propina = total_cuenta * 0.15
    total_con_propina = total_cuenta + propina
    return total_con_propina

total_cuenta = float(input("Ingrese el total de la cuenta en el restaurante: "))

total_con_propina = calcular_total_con_propina(total_cuenta)

print("El monto total a pagar, incluyendo una propina del 15%, es:", total_con_propina)

'''Ejercicio 3: Verificación de Edad
Escribe un programa que solicite la edad de un usuario y determine si es mayor de
edad (mayor o igual a 18 años) o no.'''

edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("¡Eres mayor de edad!")
else:
    print("Eres menor de edad.")


''' Ejercicio 4 : Crea un programa que cuente el número de vocales en una palabra ingresada por el
usuario.'''


def contar_vocales(palabra):
    vocales = 'aeiouAEIOU'
    conteo = 0
    for letra in palabra:
        if letra in vocales:
            conteo += 1
    return conteo

palabra = input("Ingresa una palabra: ")
print("El número de vocales en la palabra es:", contar_vocales(palabra))

''' Ejercicio 5 : Numeros pares'''

suma_pares = 0

for num in range (1,102): 
    if num % 2 == 0:
        suma_pares += num

print('la suma de los numeros pares es:', suma_pares)  

''' Ejercicio 6 : Palindromo'''

palabra = input ("Ingrese una palabra:")

palabra=palabra.lower()
if palabra == palabra [::-1]:
    print("la palabra ingresada es un palindromo")

else:
    print ("la palabra no es una palindromo")


''' Ejercicio 7 : Calculadora Simple '''

# Definir funciones para cada operación
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

# Solicitar al usuario que ingrese dos números
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

# Función para calcular el índice de masa corporal (IMC)
def calcular_imc(peso, altura):
    return peso / (altura ** 2)


''' Ejercicio 8 ICM indice de masa corporal '''

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

imc = calcular_imc(peso, altura)

print("Su índice de masa corporal (IMC) es:", imc)



'''Ejercicio 9: Conversor de Divisas'''
tasa_decambio = 0.85  # 1 dólar = 0.85 euros

# Solicitar al usuario que ingrese la cantidad de dólares
cantidad_dolares = input("Ingrese la cantidad de dólares a convertir a euros: ")

try:
   
    cantidad_dolares = float(cantidad_dolares)
except ValueError:
    print("Error: Ingrese una cantidad válida de dólares.")
    exit()


cantidad_euros = cantidad_dolares * tasa_decambio


print("${} dólares son equivalentes a {} euros.".format(cantidad_dolares, cantidad_euros))
 # Definir la tasa de cambio de dólares a euros
tasa_decambio = 0.85  # 1 dólar = 0.85 euros


while True:
    cantidad_dolares = input("Ingrese la cantidad de dólares a convertir a euros: ")
    try:
        cantidad_dolares = float(cantidad_dolares)
        break  # Salir del bucle si la conversión fue exitosa
    except ValueError:
        print("Error: Ingrese una cantidad válida de dólares.")


cantidad_euros = cantidad_dolares * tasa_decambio


print("${} dólares son equivalentes a {} euros.".format(cantidad_dolares, cantidad_euros))



'''Ejercicio 10: Dias Semana'''

dias_semana = {
        1: 'lunes',
    2: 'martes',
    3: 'miercoles',
    4:'jueves',
    5:'viernes',
    6:'sabado',
    7:'domingo',
}

numero_dia=int(input('Ingrese numero de día de la semana de 1 a 7: '))

if numero_dia < 1 or numero_dia > 7 :
    print('numero no valido, debe ser entre 1 a 7')

else:
    dia_semana = dias_semana[numero_dia]
    print('El día correspondiente al número {} es {}'.format(numero_dia, dia_semana))