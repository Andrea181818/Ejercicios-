#ejercicio 1 ///////////////////////////////////////////
#Andrea Melissa Crisostomo Chuchon
nombre=input("Introduzca primer y segundo nombre")
apellido=input("Introduzca apellido paterno y materno")
print(nombre,apellido)

#ejercicio 2 ////////////////////////////////////////////

#area de circulo
pi=3.14
radio=float(input("Introduzca el radio en cm "))
area=pi*radio**2
print("El area es:", area)

#area de triangulo
base=float(input("Introduzca la base "))
altura=float(input("Introduzca la altura "))
area=(base*altura)/2
print("El area es:", area)

#area del cuadrado
lado=float(input("Introduzca el lado "))
area=lado**2
print("El area es:", area)

#ejercicio 3 ////////////////////////////////////////////////////
a=int(input("Introduzca valor1"))
b=int(input("Introduzca valor2"))
C=int(input("Introduzca valor3"))
print("suma total:",a+b+C)
print("resta de valor 1 y 2:",a-b)
print("multiplicacion de todos los valores:",a*b*C)
print("division de valor 1 y 2:",a/b)
print("division entera de valor 1 y 2:",a//b)

#ejercicio 4 /////////////////////////////////////////////////////
a = 3.14
type(a)

#ejercicio 5 /////////////////////////////////////////////////////
import sys
print(sys.argv[0])

#ejercicio 6 /////////////////////////////////////////////////////
a=int(input("Introduzca valor"))
b=(a*(a+1))/2
print("sumatoria:",b)

#ejercicio 7 /////////////////////////////////////////////////////
a=float(input("Introduzca valor 1"))
b=float(input("Introduzca valor 2"))
print("valor 1 es igual que valor 2:",a==b)
print("valor 1 es diferente que valor 2:",a!=b)
print("valor 1 es mayor que valor 2:",a>b)
print("valor 2 es mayor que valor 1:",b>a)

#ejercicio 8 /////////////////////////////////////////////////////
a = "contraseña"
b = input("Introduce la contraseña: ")
if a == b.lower():
    print("La contaseña coincide")
else:
    print("La contraseña no coincide")


