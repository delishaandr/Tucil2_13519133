# File: main_13519133.py
# Program Utama

import list_13519133
import graph_13519133
import others_13519133
import os

path = os.path.dirname(__file__)
input = os.path.relpath('..\\test\\1.txt', path)
# file '1.txt' dapat diganti dengan file apapun yang ada di dalam folder test

# Membaca file dan membuat list DAG berdasarkan bacaan file
f = open(input, "r")
graphList = graph_13519133.make_dag_list(f)
f.close()

# Melakukan algoritma Topological Sort
# Membuat list topSort, yaitu list yang berisi list semua mata kuliah yang dapat diambil dalam satu semester
# Banyak indeks list topSort merupakan banyak semester yang dibutuhkan untuk mengambil semua mata kuliah
# Iterasi hingga graphList kosong, yaitu hingga semua mata kuliah terambil
topSort = []
while(len(graphList) != 0):
    matkulList = list_13519133.make_matkul_list(graphList)
    graphList = list_13519133.del_matkul_from_list(matkulList, graphList)
    topSort.append(matkulList)

# Write dan print output
savePath = '../test'
fileName = "output.txt"
dirFile = os.path.join(savePath, fileName)
outputFile = open(dirFile, "r+")            # membuat file output susunan rencana kuliah
outText = others_13519133.output(topSort)   
print(outText)                              # print susunan rencana kuliah ke layar
outputFile.write(outText)
outputFile.close()