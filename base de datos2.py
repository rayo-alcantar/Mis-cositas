import sqlite3
#Así?
miConexion=sqlite3.connect("BaseDatos")

miCursor=miConexion.cursor()

#CREACIÓN DE BASE DE DATOS
miCursor.execute("CREATE TABLE PRODUCTOS (COD VARCHAR(4) PRIMARY KEY, Articulo VARCHAR(20), Precio INTEGER, Seccion VARCHAR(20))")

productos=[
    ("COD1", "Pelota", 20, "Juguetería"),
    ("COD2", "Pantalón", 180, "Ropa"),
    ("COD3", "Camisa", 150, "Ropa"),
    ("COD4", "Chocolate", 60, "Dulces"),
    ("COD5", "Arroz", 25, "Abarrotes")
]

#INSERTAR DATOS EN LA TABLA
miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?,?)", productos)

miConexion.commit()

miConexion.close()