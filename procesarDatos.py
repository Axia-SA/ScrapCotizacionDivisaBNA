# -*- encoding: utf-8 -*-
# -*- coding: utf-8 -*- 

import json
from sqlite3 import Error
from functions import color, create_connection_sqlite, escribir_archivo_sql
import datetime
 
 
def create_table(conn, create_table_sql):
	try:
		c = conn.cursor()
		c.execute(create_table_sql)
	except Error as e:
		print(e)
 
 
def procesarDatos():
	database = r"sqlite.db"
 
	sql_create_divisa_table = """ CREATE TABLE IF NOT EXISTS divisa (
                                        currencyId integer NOT NULL,
                                        buy number NOT NULL,
                                        sell number NOT NULL,
                                        date date NOT NULL,
                                        name text NOT NULL,
                                        generated boolean DEFAULT 0,
                                        CONSTRAINT pk_date_currencyId PRIMARY KEY (currencyId,date)
                                    ); """
 
    # create a database connection
	conn = create_connection_sqlite(database)
	contador = 0
 
    # create tables
	if conn is not None:
		# create divisa table
		create_table(conn, sql_create_divisa_table)
		f = open("json.txt")
		data = f.read().rstrip().split('\n')  #rstrip para quitar la última línea en blanco
		f.close()
		cursor = conn.cursor()
		print(color.GREEN + "Generando registros en base de datos" + color.END)
		for d in data:
			if d != None and d != "":
				y = json.loads(d)
				date = datetime.datetime.strptime(y["date"], "%Y-%m-%d").strftime("%Y-%m-%d")
				cursor.execute("SELECT * FROM divisa WHERE currencyId = ? AND date = ?", (y["currencyId"], date))
				if cursor.fetchone() == None:
					reg = (y["currencyId"], y["buy"], y["sell"], date, y["currencyId"])
					cursor.execute("INSERT INTO divisa (currencyId, buy, sell, date, name, generated) VALUES(?,?,?,?,?, FALSE)", reg)
					contador = contador + 1

		print(color.GREEN + "Commit realizado" + color.END)
		conn.commit()

		escribir_archivo_sql()

	else:
		print("Error! cannot create the database connection.")
 
 
if __name__ == '__main__':
	procesarDatos()
