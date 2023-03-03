# Library random
import random

# Fungsi quicksort yang berisikan parameter array
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        datakiri = []
        datakanan = []
        # Melakukan perulangan untuk memerikasa elemen-elemen di dalam (arr).
        for i in range(1, len(arr)):
            if arr[i] < pivot:
                datakiri.append(arr[i])
            else:
                datakanan.append(arr[i])
        return quicksort(datakiri) + [pivot] + quicksort(datakanan)

# Membuat list random dengan elemen berjumlah 11 dan diisi dengan bilangan interger acak antara 1 sampai 25
randomlist = [random.randint(1, 25) for i in range(11)]

# Data list sebelum diurutkan
print("\nData Sebelum diurutkan:", randomlist)
print(75*"=")
print()
# Memanggil fungsi quicksort untuk mengurutkan list
randomlist = quicksort(randomlist)
# Data list setelah diurutkan
print("\nData Setelah diurutkan:", randomlist)
print(75*"=")