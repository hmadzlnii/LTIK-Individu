"""
Nama: Ahmad Zaelani
NIM: 2410023
Kelas: 1A
"""

def fibonacci(x):
    if x <= 1:
        return x
    else:
        return fibonacci(x - 1) + fibonacci(x - 2)

long = int(input("Masukan banyak angka fibonacci: "))

for i in range(long):
    print(fibonacci(i))



