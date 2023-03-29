#Ejercicio N°1

import pandas as pd
df= pd.read_csv("caso_mora.csv")

#Ejercicio N°1.1

from datetime import datetime

df['fec_ing_empleo'] = pd.to_datetime(df['fec_ing_empleo'], format="%d/%m/%Y")
df['Años_Trabajdos'] = datetime.now().year - df['fec_ing_empleo'].dt.year

#Ejercicio N°2

import sqlite3

conn = sqlite3.connect('SqLite1.db')

df.to_sql('Tabla_caso_mora', conn, if_exists='append', index=False)

conn.close()

#Ejercicio N°2.2

def leer_registros():

    conn = sqlite3.connect('SqLite1.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Tabla_caso_mora")
    registros = cursor.fetchall()

    for registro in registros:
        print(registro)

    conn.close()

leer_registros()

#Ejercicio N°3

conn = sqlite3.connect('SqLite1.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS mi_tabla (id INTEGER PRIMARY KEY, nombre TEXT, edad INTEGER)''')

nombre = input('Ingresa el nombre: ')
edad = int(input('Ingresa la edad: '))

cursor.execute("INSERT INTO mi_tabla (nombre, edad) VALUES (?, ?)", (nombre, edad))

conn.commit()
conn.close()