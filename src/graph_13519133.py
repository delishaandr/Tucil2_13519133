# File: graph_13519133.py
# File berisi fungsi-fungsi untuk membuat DAG/Directed Acyclic Graph dari masukan file

# Fungsi untuk membuat list yang berisi simpul mata kuliah dan prerequisitenya berdasarkan bacaan line
# Elemen pertama list merupakan nama simpul, sedangkan elemen-elemen berikutnya merupakan semua simpul masuk
# Jika simpul tidak memiliki simpul masuk, list hanya terdiri dari satu elemen
def list_of_vertices(line):
    vertices = [] # list berisi simpul mata kuliah dan prerequisite-nya
    namelist = [] # list of char tiap nama mata kuliah yang terbaca
    for c in line:
        if c == ' ':
            continue
        elif c == ',' or c == '.':
            name = ''.join(namelist) # mengubah list menjadi string nama matakuliah
            vertices.append(name)
            namelist = []
        else:
            namelist.append(c)
    return vertices

# Fungsi untuk membuat list DAG, yaitu list yang berisi list simpul-simpul mata kuliah dan prerequisitenya
def make_dag_list(input):
    dag = []
    for line in input:
        dag.append(list_of_vertices(line))
    return dag