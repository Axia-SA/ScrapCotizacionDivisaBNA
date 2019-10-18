# ScrappingBNA
Scrapping tool for *Banco de la Nación Argentina* historic USD and EUR currency values

![Generic badge](https://img.shields.io/badge/made%20with-Python-blue.svg) ![Generic badge](https://img.shields.io/badge/status-PROD-green.svg)

This script will get all values for USD and EUR (€) from January 2002 to yesterday.

**This project runs on Windows and Linux.**


### Requirements

- Python version >= 3
- [Scrapy]

### Files generated

After run all the steps, the script will create four files:

| File | Content |
| ------ | ------ |
| `hipervinculos.txt` | List of links to GET data (List of URLs) |
| `datos.txt` | Raw data of currency values for USD and EUR (JSON) |
| `sql.db` | Database with values. Unique by date and currency type (SQLite) |
| `SQL.sql` | SQL Script to add results on a database (List of SQL sentences)|

### Run the script!

Execute `./main.py` (or `python main.py`) and follow the menu

```
  =======================================
  | Captura de cotizacion de divisas BNA |
  |    Axia S.A.  - http://axia.com.ar   |
  =======================================
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

### Results

An example of the obtained data from 2002 to August 2019

![Capture](https://github.com/Axia-SA/ScrappingBNA/blob/master/serie.PNG)


[//]: #
   [Scrapy]: <https://scrapy.org>
