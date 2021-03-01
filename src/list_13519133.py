# File: list_13519133.py
# File berisi fungsi-fungsi untuk membuat dan mengubah list yang berhubungan dengan DAG

# Fungsi untuk membuat list semua matkul yang tidak memiliki prerequisite sehingga dapat langsung diambil dalam satu semester
def make_matkul_list(list):
    matkul_list = []
    for l in list:
        if len(l) == 1: # List matkul yang tidak memiliki prerequisite akan hanya memiliki satu elemen yaitu matkul itu sendiri
            matkul_list.append(l[0])
    return matkul_list

# Fungsi untuk menghapus matkul yang sudah diambil dari list graph
def del_matkul_from_list(mlist, glist):
    i = 0
    j = len(glist)
    while (i != j):
        for m in mlist:
            glist[i] = del_from_list(m, glist[i])
        if len(glist[i]) == 0: # Jika list kosong setelah matkul dihapus, list tersebut dihapus dari list graf
            glist.pop(i)
            j -= 1
        else:
            i += 1
    return glist

# Fungsi untuk delete elemen dari list
# Jika pada list terdapat elemen n, maka n di-delete dari list
def del_from_list(n, list):
    i = 0
    while (i < len(list)):
        if list[i] == n:
            list.pop(i)
        else:
            i += 1
    return list
