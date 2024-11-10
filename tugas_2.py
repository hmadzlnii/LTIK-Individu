"""
Nama: Ahmad Zaelani
NIM: 2410023
Kelas: 1A
"""

def login():
    coba = 3
    username = input("Masukan username: ")
    while coba > 0:
        password = input("Masukan password: ")
        if password == "Latihan":
            print("\nSelamat datang di aplikasi ini, ", username)
            break
        else:
            coba -= 1
            if coba > 0:
                print(f"\Password Salah! Kesempatan Anda {coba}x kali lagi")
            else:
                print("\nAnda tidak diperkenankan mengakses aplikasi ini.")
                home()

def home():
    print("===SELAMAT DATANG DI APLIKASI KAMI====")
    pilih = int(input("Silakan ketik '1' untuk login! "))
    if pilih == 1:
        login()

home()