import csv
from multiprocessing import Pool
import threading
import time
from webScrapper import WebScrapper

"""Aproximación a la paralelización del web scrapping"""


def Buscar(addresses):
    scrapper = WebScrapper()
    for i in addresses:
        scrapper.searchByAddress(i)


    # sprint(scrapper.searchByAddres(address))
if __name__ == "__main__":
    threads = list()
    file = open("directorio-de-bibliotecas-valencianas_2020.csv", 'r')
    jsonDatos = []
    # CSV to JSON
    datosDiccionario = csv.DictReader(file, delimiter=';')
    for row in datosDiccionario:
        jsonDatos.append(row['Municipi / Municipio'])
    jsonDatos = jsonDatos[0:360]
    cantidad = len(jsonDatos)
    numHilos = 6
    elementosPorHilo = cantidad/numHilos
    start = time.time()
    for index in range(numHilos):
        x = threading.Thread(target=Buscar, args=(
            jsonDatos[index*60:index*60 + index*60+60],))
        threads.append(x)
        x.start()
    for index, thread in enumerate(threads):
        thread.join()
    end = time.time()
    tiempo = end - start
    print('he terminado. Tardé ' + str(tiempo))
