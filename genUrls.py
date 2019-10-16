#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# -*- coding: utf-8 -*- 
import scrapy
import json
import datetime
from datetime import timedelta
from functions import file_len

fechaHoy = datetime.datetime.now()
iteradorFecha = datetime.datetime(2002, 1, 1)  # <--- Iterar desde la siguiente fecha
#iteradorFecha = datetime.datetime(2019, 9, 11)  # <--- Iterar desde la siguiente fecha

url = "https://www.bna.com.ar/Cotizador/HistoricoPrincipales?id=monedas&fecha=_FECHA_&filtroEuro=1&filtroDolar=1&"

f = open("hipervinculos.txt","w+")
delta = fechaHoy - iteradorFecha
totalLineas = delta.days + 1
contador = 0
print("Total de URLs generadas: " + str(totalLineas))

while iteradorFecha < fechaHoy:
	iteradorFecha = iteradorFecha + timedelta(days=1)
	url2 = url.replace("_FECHA_", iteradorFecha.strftime("%d/%m/%Y").lstrip("0").replace(" 0", " ").replace("/","%2F"))
	contador += 1
	if contador < totalLineas:
		f.write(url2 + ",\n")
	else:
		f.write(url2)

f.close()
	