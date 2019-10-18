import os.path
import sqlite3

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def capturarDatos():
	print(color.GREEN + "Iniciando..." + color.END)
	os.system("scrapy runspider scrapCotizacionBna.py")
	print(color.GREEN + "Finalizado." + color.END)

def generarUrls():
	print(color.GREEN + "Iniciando..." + color.END)
	os.system("python genUrls.py")
	print(color.GREEN + "Finalizado." + color.END)

def file_len(fname):
    return sum(1 for line in open(fname)) + 1

def create_connection_sqlite(db_file):
   """ create a database connection to the SQLite database
   specified by db_file
   :param db_file: database file
   :return: Connection object or None
   """
   conn = None
   try:
      conn = sqlite3.connect(db_file)
      return conn
   except Error as e:
      print(e)

   return conn

def escribir_archivo_sql():
   database = r"sql.db"
   conn = create_connection_sqlite(database)
   if conn == None:
      print(color.RED + "No se pudo conectar a la base de datos" + color.END)
      return
   cursor = conn.cursor()
   print(color.GREEN + "Generando archivo SQL" + color.END)
   cursor.execute("SELECT * FROM divisa ORDER BY fecha ASC")
   rows = cursor.fetchall()
   f = open("SQL.sql","w+")
   contador = 0
   for y in rows:
      f.write("INSERT INTO tipo_cambio (moneda, cambio, fuente_cotizacion, fecha_cotizacion) VALUES (" + str(y[0]) + ", " + str(y[2]) + ", \"BNA Divisa\", \"" + str(y[3]) + "\");\n")
      contador += 1
   f.close()
   conn.close()
   print(color.YELLOW + "Se ha generado un archivo SQL con ", contador, " registros" + color.END)