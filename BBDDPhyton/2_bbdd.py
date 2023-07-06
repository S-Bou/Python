import sqlite3

miConexion = sqlite3.connect("GestionProductos")
miCursor = miConexion.cursor()

# miCursor.execute('''
# 	CREATE TABLE productos (
# 		codigo_articulo VARCHAR(4) PRIMARY KEY,
# 		nombre_articulo VARCHAR(50),
# 		precio INTEGER,
# 		seccion VARCHAR(20))
# 	''')

miCursor.execute('''
	CREATE TABLE productos (
		ID INTEGER PRIMARY KEY AUTOINCREMENT,
		nombre_articulo VARCHAR(50),
		precio INTEGER,
		seccion VARCHAR(20))
	''')

# productos = [
# ("AR01", "Pelota", 20, "Juguetería"),
# ("AR02", "Pantalón", 15, "Confección"),
# ("AR03", "Destornillador", 25, "Ferretería"),
# ("AR04", "Jarrón", 45, "Cerámica"),
# ]

productos = [
("Pelota", 20, "Juguetería"),
("Pantalón", 15, "Confección"),
("Destornillador", 25, "Ferretería"),
("Jarrón", 45, "Cerámica"),
]

miCursor.executemany("INSERT INTO productos VALUES (NULL,?,?,?)", productos)

miConexion.commit()
miConexion.close()
