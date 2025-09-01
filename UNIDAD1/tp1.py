
#Copia de ejercicios unidad 1, SECUENCIALES

#Ejercicio 1
print ("hola mundo!")


#Ejercicio 2
nombre = input("Hola, como te llamas:")
print(f"Hola {nombre}!")


#Ejercicio 3
nombre = input("ingrese su nombre:")
apellido = input("ingrese su apellido:")
edad = input("ingrese su edad:")
residencia = input("ingrese su pais de residencia:")

print(f"soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")


#Ejercicio 4
radio = int(input("ingrese el radio de una circunferencia:" ))
pi = 3.14
print("El area del circulo es:" , pi * radio * radio, "y su perimetro es:" , 2 * pi * radio)


#Ejercicio 5
segundos = float(input("ingrese una cantidad aleatoria de segundos:"))
print ("esos segundos equivalen a:", segundos / 3600, "horas")


#Ejercicio 6
numero = int(input("ingrese un número del que desea saber su tabla de multiplicar:" ))
print (f"tabla de multiplicar de:", {numero})
for i in range (0, 11): 
 resultado = numero * i      
 print (f"{numero} * {i} = {resultado}")


 #Ejercicio 7
 print("ingrese un número entero:")
n1 = float(input())
print("ingrese otro número entero:")
n2 = float(input())
suma = n1 + n2
resta = n1 - n2
multiplicación = n1 * n2
div = n1 / n2

print(n1, "+", n2, "=", suma)
print(n1, "-", n2, "=", resta)
print(n1, "*", n2, "=", multiplicación)
print(n1, "/", n2, "=", div)



#Ejercicio 8
altura = float(input("ingrese su altura en metros: " ))
peso = float(input("ingrese su peso en kilos por favor: "))
imc = peso/(altura**2)

print("Su IMC es de:", imc, "kg/m2")


#Ejercicio 9
temp = float(input("ingrese una temperatura en grados celsius: "))
far = (9/5) * temp + 32
print("su quivalente en Farenheit es:", far, "grados")


#Ejercicio 10
num1 = float(input("ingrese el primer número: "))
num2 = float(input("ingrese el segundo número: "))
num3 = float(input("ingrese el tercer número: "))

prom = (num1 + num2 + num3) / 3

print("el promedio de esos 3 números es: ", prom)