import os.path

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