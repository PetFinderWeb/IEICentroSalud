import csv
import math
from multiprocessing import Pool
import threading
import time
import os
from webScrapper import WebScrapper
import webScrapper
# def f(x):
#     print(str(os.getpid()))
#     return(x)
# def log_result(result):
#     # This is called whenever foo_pool(i) returns a result.
#     # result_list is modified only by the main process, not the pool workers.
#     print(result)
# if __name__ == '__main__':
#     # start 4 worker processes
#     pool = Pool(processes=4)
#     cities = ['valencia', 'madrid', 'barcelona', 'sevilla', 'alicante', 'ibiza', 'santander']
#     for i in range(len(cities)):
#         pool.apply_async(f, args = (cities[i], ), callback = log_result)
#     pool.close()
#     pool.join()
# with Pool(processes=4) as pool:
#     multiple_results = [pool.apply_async(f, (1,)) for i in range(4)]
#     print([res.get(timeout=1) for res in multiple_results])


def Buscar(addresses):
    scrapper = WebScrapper()
    for i in addresses:
        scrapper.searchByAddress(i)


    # sprint(scrapper.searchByAddress(address))
print('hola')
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
