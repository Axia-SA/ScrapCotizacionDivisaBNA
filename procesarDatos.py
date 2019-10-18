# -*- encoding: utf-8 -*-
# -*- coding: utf-8 -*- 

import json
from sqlite3 import Error
from functions import color, create_connection_sqlite, escribir_archivo_sql
from armarSerieCompleta import armarSerieCompleta
import datetime
 
 
def create_table(conn, create_table_sql):
	try:
		c = conn.cursor()
		c.execute(create_table_sql)
	except Error as e:
		print(e)
 
 
def procesarDatos():
	database = r"sql.db"
 
	sql_create_divisa_table = """ CREATE TABLE IF NOT EXISTS divisa (
                                        idMoneda integer NOT NULL,
                                        compra number NOT NULL,
                                        venta number NOT NULL,
                                        fecha date NOT NULL,
                                        nombreDivisa text NOT NULL,
                                        generado boolean DEFAULT 0,
                                        CONSTRAINT pk_fecha_idMoneda PRIMARY KEY (idMoneda,fecha)
                                    ); """
 
    # create a database connection
	conn = create_connection_sqlite(database)
	contador = 0
 
    # create tables
	if conn is not None:
		# create divisa table
		create_table(conn, sql_create_divisa_table)
		f = open("datos.txt")
		data = f.read().rstrip().split('\n')  #rstrip para quitar la última línea en blanco
		f.close()
		cursor = conn.cursor()
		print(color.GREEN + "Generando registros en base de datos" + color.END)
		for d in data:
			if d != None or d != "":
				y = json.loads(d)
				date = datetime.datetime.strptime(y["fecha"], "%d/%m/%Y").strftime("%Y-%m-%d")
				cursor.execute("SELECT * FROM divisa WHERE idMoneda = ? AND fecha = ?", (y["idMoneda"], date))
				if cursor.fetchone() == None:
					reg = (y["idMoneda"], y["compra"], y["venta"], date, y["nombreDivisa"])
					cursor.execute("INSERT INTO divisa (idMoneda, compra, venta, fecha, nombreDivisa, generado) VALUES(?,?,?,?,?, FALSE)", reg)
					contador = contador + 1

		print(color.GREEN + "Commit realizado" + color.END)
		conn.commit()

		escribir_archivo_sql()

	else:
		print("Error! cannot create the database connection.")
 
 
if __name__ == '__main__':
	procesarDatos()