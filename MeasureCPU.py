#! /usr/bin/python

import psutil
import csv
from time import time


def guardarCSV(data):
	archivo = open("CPU_1Attacker.csv","a",)
	salida = csv.writer(archivo)
	salida.writerow(data)
	del salida
	archivo.close()

if __name__ == '__main__':
	#--------------- Crea o sobreescribe el archivo -----------------------
	archivo = open("CPU_1Attacker.csv","w")
	salida = csv.writer(archivo)
	salida.writerow(['#','CPU %', 'VirtualMemory %', 'SwapMemory', 'Time'])
	del salida
	archivo.close()

	#---------------- Bucle infinito --------------------------------------
	LastTime = time()
	tiempo = 0
	count = 1;

	while 1==1:
		#---------- se calcula el consumo de CPU y memoria ----------------
		cpu = psutil.cpu_percent(interval=2)
		vmemory = psutil.virtual_memory()
		smemory = psutil.swap_memory()
		print("porcentaje de CPU usado: ",cpu)
		print("porcentaje de memoria virtual usado: ", vmemory[2])
		print("porcentaje de memoria swap usado: ", smemory[3])
		print("--------------------", count)
		
		#--- se calcula el intervalo de tiempo y se suma al acumulado -----
		NowTime = time()
		t = NowTime - LastTime
		tiempo = tiempo + t
		
		#----- guardar la informacion en el archivo CSV -------------------	
		data = [count, cpu, vmemory[2], smemory[3], int(tiempo)]
		guardarCSV(data)
		LastTime = NowTime
		count = count + 1

		




