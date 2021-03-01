# File: others_13519133.py
# File berisi fungsi-fungsi lain untuk menjalankan program

# Fungsi untuk mengubah integer menjadi angka romawi
# Diasumsikan pengambilan mata kuliah hanya 8 semester sehingga angka romawi yang digunakan hanya I, IV dan V
def roman(n):
    ints = (5, 4, 1)
    nums = ('V', 'IV', 'I')
    res = []

    for i in range(len(ints)):
        count = int(n / ints[i])
        res.append(nums[i] * count)
        n -= ints[i] * count
    return ''.join(res)

# Fungsi untuk mengubah array maupun tuple menjadi string
def to_string(l):
    return ''.join(l)

# Fungsi untuk membuat string susunan rencana kuliah berdasarkan topological sort yang telah didapat
def output(list):
    string = ["---------- Susunan Rencana Kuliah ----------\n\n"]
    for i in range(len(list)):
        tup = "Semester ", roman(i+1), ": ", ', '.join(list[i])
        string.append(to_string(tup) + '\n')
    return to_string(string)