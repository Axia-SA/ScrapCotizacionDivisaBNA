#!/usr/bin/python3
# -*- encoding: utf-8 -*-
# -*- coding: utf-8 -*- 

import os.path
from functions import color, generarUrls, capturarDatos, escribir_archivo_sql
from procesarDatos import procesarDatos
from armarSerieCompleta import armarSerieCompleta

os.system("clear")
print(color.RED + "    ========================================")
print("    | Captura de cotizacion de divisas BNA |")
print("    |    Axia S.A. -  http://axia.com.ar   |")
print("    ========================================" + color.END)

menu = {}
menu['1']= "Generar " + color.GREEN + "hipervinculos" + color.END
menu['2']= color.GREEN + "Iniciar captura " + color.END + "de datos"
menu['3']= color.GREEN + "Procesar datos capturados " + color.END + "eliminando valores repetidos"
menu['4']= color.GREEN + "Armar serie completa "+ color.END +" incluyendo fines de semana y feriados"
menu['5']= "Iniciar proceso " + color.GREEN + "COMPLETO " + color.END
menu['q']= color.YELLOW + "Salir" + color.END

while True:
	options=menu.keys()
	options = sorted(options)
	print(color.BOLD + "-------------------  MENU  ------------------------" + color.END)
	for entry in options:
		print(entry, menu[entry])
	print("-------------------  END  -------------------------")

	selection = input("Seleccion: ")
	if selection =='1':
		generarUrls()
	elif selection == '2':
		confirm = input('  Iniciar captura de datos? s/N: ')
		if confirm == "s":
			capturarDatos()
	elif selection == '3':
		print(color.GREEN + "Procesando datos..." + color.END)
		procesarDatos()
	elif selection == '4':
		print(color.GREEN + "Armando serie..." + color.END)
		armarSerieCompleta(2)
		armarSerieCompleta(3)
		escribir_archivo_sql()
	elif selection == '5':
		confirm = input('  Iniciar proceso completo? s/N: ')
		if confirm == "s":
			confirm = input('  Ejecutar opcion 4? s/N: ')
			generarUrls()
			capturarDatos()
			print(color.GREEN + "Procesando datos..." + color.END)
			procesarDatos()
			if confirm == "s":
				armarSerieCompleta(2)
				armarSerieCompleta(3)
			escribir_archivo_sql()
	elif selection == 'q':
		break
	else: 
		print("no existe la opcion")
		os.system("clear")

