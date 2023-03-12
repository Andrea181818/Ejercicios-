#Pregunta N°1
#
base = int(input("Ingrese el lado: "))
for i in range(base):
    print('*'*(base))
#
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in numeros:
    if i % 2 == 0:
        print(i)
#
elementos =[["Sara",41],["Andrea",9],["Luana",14],["Jeferson",25],["Angela",20]]

for i in elementos:
    if i[1] > 18:
        print(i[0])

#Pregunta N°2

biblioteca = {'Harry Potter y la piedra filosofal': 'J.K. Rowling',
        'Cien años de soledad': 'Gabriel García Márquez',
        'El señor de los anillos': 'J.R.R. Tolkien',
        'La sombra del viento': 'Carlos Ruiz Zafón'}
categorias = ["ficción","No ficción"]
usuarios = ["Andrea","Jeferson"]

estados = {'Harry Potter y la piedra filosofal': 'Disponible',
        'Cien años de soledad': 'Disponible',
        'El señor de los anillos': 'Disponible',
        'La sombra del viento': 'Disponible'}


def lista_Categorias():
    print("Las categorias son: ")
    for i in categorias:
        print(i)

def lista_nombre_autores():
    print("Obras y Autores: ")
    for i,e in biblioteca.items():
        print( i , "de" , e)

def cambiar_estado(libro):
    estados[libro] = "Prestado"
    print('Estados de los libros son: ')
    for i in estados.items():
        print(i)

def lista_Usuarios():
    print("Los usuarios son: ")
    for i in usuarios:
        print(i)

lista_Categorias()
lista_nombre_autores()
cambiar_estado('El señor de los anillos')
lista_Usuarios()

#Pregunta N°3

def valor_mayor():
    x = int(input('Ingrese el primer numero: '))
    y = int(input('Ingrese el segundo numero: '))
    return max(x,y)
valor_mayor()

#Pregunta N°4

import sys

def imprimir_argumentos():
    for argumento in sys.argv[1:]:
        print(argumento)

imprimir_argumentos()

#Pregunta N°5

import os

def listar_carpeta(path):
    elementos = os.listdir(path)
    for elemento in elementos:
        elemento_path = os.path.join(path, elemento)
        if os.path.isdir(elemento_path):
            listar_carpeta(elemento_path)
        else:
            print(elemento_path)

#Pregunta N°6

def main():
    evento = obtener_evento()
    asistentes = obtener_asistentes()
    validar_evento(evento, asistentes)

def obtener_evento():
    evento = input('Ingrese el nombre del evento: ')
    return evento

def obtener_asistentes():
    try:
        asistentes = int(input('Ingrese el número de asistentes: '))
    except:
        print('ERROR: El número de asistentes debe ser un número entero.')
    return asistentes

def validar_evento(evento, asistentes):
    if len(evento) < 5:
        print('ERROR: El nombre del evento debe tener al menos 5 caracteres.')
    elif asistentes <= 0:
        print('ERROR: El número de asistentes debe ser mayor que cero.')
    else:
        print(f'El evento {evento} con {asistentes} asistentes ha sido registrado con éxito.')

#Pregunta N°7

def contar_palabras(texto):
    return texto.count('Lorem Ipsum')
def reemplazar_palabras(texto):
    return texto.replace('Lorem Ipsum', 'Texto de relleno')
def dividir_parrafos(texto):
    return texto.split('\n\n')

#Pregunta N°8

def funcion_rango(maximo,step):
    if maximo > 10**5:
        print("Ingrese un numero menor a 10^5")
    else:
        lista = []
        for i in range(1,maximo,step):
            a = 0
            for e in range(1,maximo):
                if i % e == 0 :
                    a = a + 1
            if a <= 2 :
                lista.append(i)
    return lista