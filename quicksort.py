import os
import random

os.system("cls")

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        kiri = []
        kanan = []
        for i in arr[1:]:
            if i < pivot:
                kiri.append(i)
            else:
                kanan.append(i)
        return quick_sort(kiri) + [pivot] + quick_sort(kanan)

# import array random
arr = [random.randint(1, 25) for _ in range(12)]
print("Array sebelum diurutkan :", arr)
print()

# mengurutkan array menggunakan quicksort
arr_sorted = quick_sort(arr)
print("array setelah diurutkan :", arr_sorted)
