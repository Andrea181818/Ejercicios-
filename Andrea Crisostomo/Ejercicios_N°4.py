#Ejercicio N°1

__name__=='__main__'

#Ejercicio N°2

import random

class Sorteo:
    def __init__(self, max_valor, cantidad_elementos):
        self.lista_valores = []
        self.max_valor = max_valor
        self.cantidad_elementos = cantidad_elementos
    
    def sortear_numeros(self):
        for i in range(self.cantidad_elementos):
            num_aleatorio = random.randint(1, self.max_valor)
            self.lista_valores.append(num_aleatorio)
    
    def mostrar(self):
        print(self.lista_valores)
    
    def escoger_aleatorio(self):
        return random.choice(self.lista_valores)

#Ejemplo

sorteo1 = Sorteo(100,10)

Sorteo.sortear_numeros(sorteo1)
Sorteo.mostrar(sorteo1)
Sorteo.escoger_aleatorio(sorteo1)

#Ejercicios N°3

import requests

def obtener_tipo_cambio():
    url = "https://api.apis.net.pe/v1/tipo-cambio-sunat"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print("Tipo de cambio:")
        print(f"Dólar: {data}")
    else:
        print(f"Error: {response.status_code}")

def obtener_pokedex():
    url = "https://pokeapi.co/api/v2/pokedex/1/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print("Pokémon en la Pokédex:")
        for pokemon in data['pokemon_entries']:
            print(pokemon['pokemon_species']['name'])
    else:
        print(f"Error: {response.status_code}")

def obtener_datos_pokemon(nombre_pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Datos de {nombre_pokemon}:")
        print(f"Altura: {data['height']}")
        print(f"Peso: {data['weight']}")
        print("Tipos:")
        for tipo in data['types']:
            print(f"- {tipo['type']['name']}")
    else:
        print(f"Error: {response.status_code}")

#Ejemplo

obtener_tipo_cambio()
obtener_pokedex()
obtener_datos_pokemon("raticate")

#Ejercicio N°4

from datetime import datetime

class Registro:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        with open(nombre_archivo, 'w') as archivo:
            archivo.write('')

    def guardar_input(self, mensaje):
        fecha_actual = datetime.now().strftime('%Y-%m-%d')
        with open(self.nombre_archivo, 'a') as archivo:
            archivo.write(f'{fecha_actual}-{self.nombre_archivo}-{mensaje}\n')
    
    def mostrar_registro(self):
        with open(self.nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            print(contenido)

#Ejemplo

Registro1 = Registro("Andrea")
Registro.guardar_input(Registro1,"Hola")
Registro.mostrar_registro(Registro1)

#Ejercicio N°5

import re

def validar_celular(numero):

    if not re.match(r'^9\d*$', numero):
        return print("El numero debe empezar por 9")

    if len(numero) != 9:
        return print("Ingrese un numero de 9 caracteres")

    return print("Numero validado")

#Ejemplo
validar_celular('154865236')
validar_celular('94865236')
validar_celular('954865236')

#Ejercicio N°6

pip install pyinstaller

pyinstaller Ejercicios_N°4.py