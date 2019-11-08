# -*- encoding: utf-8 -*-
# -*- coding: utf-8 -*- 

import sqlite3
import datetime
from functions import color, create_connection_sqlite

def armarSerieCompleta(idMoneda):
	database = r"sql.db"
	conn = create_connection_sqlite(database)
	if conn == None:
		print(color.RED + "No se pudo conectar a la base de datos" + color.END)
		return

	cursor = conn.cursor()
	cursor.execute("SELECT * FROM divisa WHERE idMoneda = "+ str(idMoneda) +" ORDER BY fecha ASC")
	registros = cursor.fetchall()
	fecha_anterior = datetime.datetime.now()
	date_format = "%Y-%m-%d"
	contador = 0
	reg_anterior = None
	for item in registros:
		fecha_actual = datetime.datetime.strptime(item[3], date_format)

		iters = (fecha_actual - fecha_anterior).days - 1
		aux = fecha_anterior
		while iters > 0:
			aux = aux + datetime.timedelta(days=1)
			if aux == fecha_actual:
				break
			reg = (reg_anterior[0], reg_anterior[2], reg_anterior[2], aux, "-", True)
			cursor.execute("INSERT INTO divisa (idMoneda, compra, venta, fecha, nombreDivisa, generado) VALUES(?,?,?,?,?,?)", reg)
			print("Completando fechas desde " + str(fecha_anterior.strftime("%d/%m/%Y")) + " hasta " + str(fecha_actual.strftime("%d/%m/%Y")) + " - iter: " + str(iters) + " - " + repr(aux.strftime("%d/%m/%Y")) + " idMoneda: " + str(item[0]) + " item: " + item[4])
			iters -= 1
			contador += 1
		fecha_anterior = fecha_actual
		reg_anterior = item
	conn.commit()
	print(color.GREEN + "Se agregan " + str(contador) + " registros para esta divisa" + color.END)
	conn.close()



