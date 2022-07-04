# ScrapCotizacionDivisaBNA
Scraping tool for [*Banco de la Nación Argentina*](www.bna.com.ar) historic USD and EUR currency values.

This tool can get all currency values (`ARS-USD` / `ARS-€`) from each day since february, 2002 to "yesterday".

![Generic badge](https://img.shields.io/badge/made%20with-Python-blue.svg) ![Generic badge](https://img.shields.io/badge/status-PROD-green.svg)


**This project runs on Windows and Linux.**


## Requirements

- Python version >= 3
- [Beautiful Soup]

## ID references for currency type:

Currency ID:

| ID | Currency |
| ------ | ------ |
| 2 | US Dollar (`$`) |
| 3 | Euro (`€`) |

## Run the script!

Execute `./main.py` (or `python main.py`) and follow the menu

```
    ========================================
    | Captura de cotizacion de divisas BNA |
    |    Axia S.A. -  http://axia.com.ar   |
    |  Desarrollado por Cristian Bottazzi  |
    ========================================
-------------------  MENU  ------------------------
1 Generar hipervinculos
2 Iniciar captura de datos
3 Procesar datos capturados eliminando valores repetidos
4 Armar serie completa  incluyendo fines de semana y feriados
5 Iniciar proceso COMPLETO 
q Salir
-------------------  END  -------------------------
Seleccion:

```

### Why exists an option 4?

If you won't need or don't want gaps between dates (weekends, holidays and such), the option 4 can be helpful to generate continuous time series.

It will copy the last currency value until the next existent date. And this values can be recognized by the `true` outputs attributes under `generated` tag.

## Outputs

This script generates three outputs: SQL script, SQLite Database and JSON file.

An example of the obtained data from 2002 to July 2022

`SQL.sql`:
```
INSERT INTO tipo_cambio (moneda, cambio, fuente_cotizacion, fecha_cotizacion) VALUES (2, 1.6, 'BNA Divisa', '2002-01-11');
INSERT INTO tipo_cambio (moneda, cambio, fuente_cotizacion, fecha_cotizacion) VALUES (3, 1.42, 'BNA Divisa', '2002-01-11');
INSERT INTO tipo_cambio (moneda, cambio, fuente_cotizacion, fecha_cotizacion) VALUES (2, 1.6, 'BNA Divisa', '2002-01-12 00:00:00');
INSERT INTO tipo_cambio (moneda, cambio, fuente_cotizacion, fecha_cotizacion) VALUES (3, 1.42, 'BNA Divisa', '2002-01-12 00:00:00');
.
.
.
INSERT INTO tipo_cambio (moneda, cambio, fuente_cotizacion, fecha_cotizacion) VALUES (2, 125.45, 'BNA Divisa', '2022-07-03 00:00:00');
INSERT INTO tipo_cambio (moneda, cambio, fuente_cotizacion, fecha_cotizacion) VALUES (3, 130.7942, 'BNA Divisa', '2022-07-03 00:00:00');
INSERT INTO tipo_cambio (moneda, cambio, fuente_cotizacion, fecha_cotizacion) VALUES (2, 125.95, 'BNA Divisa', '2022-07-04');
INSERT INTO tipo_cambio (moneda, cambio, fuente_cotizacion, fecha_cotizacion) VALUES (3, 131.4288, 'BNA Divisa', '2022-07-04');

```

`json.txt`
```
{"currencyId": 2, "buy": 1.4, "sell": 1.6, "date": "2002-01-11", "name": "Dolar"}
{"currencyId": 3, "buy": 1.24, "sell": 1.42, "date": "2002-01-11", "name": "Euro"}
{"currencyId": 2, "buy": 1.4, "sell": 1.6, "date": "2002-01-11", "name": "Dolar"}
{"currencyId": 3, "buy": 1.24, "sell": 1.42, "date": "2002-01-11", "name": "Euro"}
.
.
.
{"currencyId": 2, "buy": 125.75, "sell": 125.95, "date": "2022-07-04", "name": "Dolar"}
{"currencyId": 3, "buy": 130.9058, "sell": 131.4288, "date": "2022-07-04", "name": "Euro"}
{"currencyId": 2, "buy": 125.75, "sell": 125.95, "date": "2022-07-04", "name": "Dolar"}
{"currencyId": 3, "buy": 130.9058, "sell": 131.4288, "date": "2022-07-04", "name": "Euro"}
```

### Files generated

After run all the steps, the script will create four files:

| File | Content | Example |
| ------ | ------ | ------ |
| `hipervinculos.txt` | List of links to GET data (List of URLs) | Each row represents a day to perform a query on bank website |
| `json.txt` | USD and EUR values obtained and converted to JSON | `{"idMoneda": 3, "compra": 16.7212, "venta": 16.868, "fecha": "2017-02-03", "nombreDivisa": "Euro"}` |
| `sqlite.db` | SQLite Database with all values. Unique by date and currency type | ------ |
| `SQL.sql` | Custom SQL Script (List of INSERT SQL sentences)| `INSERT INTO my_table (...) VALUES (...)` |


Finally, a graph showing devaluation rate of argentine Peso (`ARS`) since february, 2002 to July, 2022.

![Capture](https://github.com/Axia-SA/ScrappingBNA/blob/master/serie.PNG)

Written by Cristian Bottazzi - July 2022


[//]: #
   [Beautiful Soup]: <https://www.crummy.com/software/BeautifulSoup/bs4/doc/>
