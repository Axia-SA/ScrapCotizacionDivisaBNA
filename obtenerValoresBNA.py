#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# -*- coding: utf-8 -*- 

import requests
from bs4 import BeautifulSoup
import json
import datetime
from functions import color

dateHoy = datetime.datetime.now()

class Moneda:
    buy = ''
    sell = ''
    currencyId = ''
    date = ''
    objdate = datetime.datetime.now()
    def __init__(self, idD, c, v, f, nD):
        self.currencyId = idD
        self.buy = c
        self.sell = v
        self.date = f
        self.name = nD

f = open("hipervinculos.txt", "r")
urls = f.read().split(',')
f.close()
f = open("hipervinculos.txt", "r")
lines = len(f.readlines())
f.close()

print(color.GREEN + "Inicio toma de datos." + color.END)

line = 0
m = []
for url in urls:
    if (url == ''):
        continue
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')

    line+=1
    prc = (line*100/lines)
    print(color.YELLOW + ' -> Progreso: [%d%%]\r'%prc + '% ' + color.END, end="")

    for row in soup.find_all("tr"):
        cells = row.find_all("td")
        if (cells != []):
            moneda = cells[0].text
            buy = cells[1].text
            sell = cells[2].text
            date = cells[3].text
            buy = buy.replace(',', '.')
            sell = sell.replace(',', '.')

            if (cells[0].text == "Dolar U.S.A" ):
                idDivisa = 2
                name = 'Dolar'
                agregar = 1
            elif (cells[0].text == "Euro"):
                idDivisa = 3
                agregar = 1
                name = 'Euro'
            elif (cells[0].text == "Real (*)"):
                idDivisa = 4
                agregar = 1
                name = 'Real'
                buy = float(buy)/100
                sell = float(sell)/100
            elif (cells[0].text == "Libra Esterlina"):
                idDivisa = 5
                agregar = 1
                name = 'Libra Esterlina'
            
            date_str = cells[3].text        # Date String
            format_str = '%d/%m/%Y'         # Format
            datetime_obj = datetime.datetime.strptime(date_str, format_str)

            if agregar:
                tmp = Moneda(idDivisa, float(buy), float(sell), str(datetime_obj.date()), name)
                m.append(tmp)

print(color.GREEN + "Escribiendo archivo JSON" + color.END)

f = open("json.txt","w")
for row in m:
    s = json.dumps(row.__dict__)
    f.write(s + "\n")
f.close()

print(color.GREEN + "Archivo generado exitosamente." + color.END)