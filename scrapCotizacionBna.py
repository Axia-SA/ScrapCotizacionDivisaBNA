#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# -*- coding: utf-8 -*- 
import scrapy
import json
import datetime
from datetime import timedelta
from functions import file_len

fechaHoy = datetime.datetime.now()

class Moneda:
    compra = ''
    venta = ''
    idMoneda = ''
    fecha = ''
    objFecha = datetime.datetime.now()
    def __init__(self, idD, c, v, f, nD):
        self.idMoneda = idD
        self.compra = c
        self.venta = v
        self.fecha = f
        self.nombreDivisa = nD

# Obtiene de la página del Banco Nación las cotizaciones de las divisas

class BootstrapTableSpider(scrapy.Spider):
    name = "tabla"

    def start_requests(self):
        f = open("hipervinculos.txt", "r")
        urls = f.read().split(',')
        f.close()

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        fecha = ''
        m = []

        for row in response.xpath('//*[@id="tablaDolar"]//tbody/tr'):
            divisa = row.xpath('td[1]//text()').extract_first()
            compra = row.xpath('td[2]//text()').extract_first()
            venta = row.xpath('td[3]//text()').extract_first()
            fecha = row.xpath('td[4]//text()').extract_first()
            compra = compra.replace(',', '.')
            venta = venta.replace(',', '.')

            idDivisa = 0
            agregar = 0
            nombreDivisa = ''
            if divisa == "Dolar U.S.A":
                idDivisa = 2
                nombreDivisa = 'Dolar'
                agregar = 1
            if divisa == "Real (*)":
                idDivisa = 4
                agregar = 1
                nombreDivisa = 'Real'
                compra = float(compra)/100
                venta = float(venta)/100
            if divisa == "Euro":
                idDivisa = 3
                agregar = 1
                nombreDivisa = 'Euro'
            if divisa == "Libra Esterlina":
                idDivisa = 5
                agregar = 1
                nombreDivisa = 'Libra Esterlina'

            if agregar:
                tmp = Moneda(idDivisa, float(compra), float(venta), fecha, nombreDivisa)
                m.append(tmp)

        for row in response.xpath('//*[@id="tablaEuro"]//tbody/tr'):
            divisa = row.xpath('td[1]//text()').extract_first()
            compra = row.xpath('td[2]//text()').extract_first()
            venta = row.xpath('td[3]//text()').extract_first()
            fecha = row.xpath('td[4]//text()').extract_first()
            compra = compra.replace(',', '.')
            venta = venta.replace(',', '.')

            idDivisa = 0
            agregar = 0
            nombreDivisa = ''
            if divisa == "Dolar U.S.A":
                idDivisa = 2
                nombreDivisa = 'Dolar'
                agregar = 1
            if divisa == "Real (*)":
                idDivisa = 4
                agregar = 1
                nombreDivisa = 'Real'
                compra = float(compra)/100
                venta = float(venta)/100
            if divisa == "Euro":
                idDivisa = 3
                agregar = 1
                nombreDivisa = 'Euro'
            if divisa == "Libra Esterlina":
                idDivisa = 5
                agregar = 1
                nombreDivisa = 'Libra Esterlina'

            if agregar:
                tmp = Moneda(idDivisa, float(compra), float(venta), fecha, nombreDivisa)
                m.append(tmp)

        f = open("datos.txt","a+")

        for row in m:
            s = json.dumps(row.__dict__)
            f.write(s + "\n")

        f.close()