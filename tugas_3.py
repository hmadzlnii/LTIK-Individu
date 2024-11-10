def start():
    print("Start")
    jam = int(input("Masukan jam: "))
    menit = int(input("Masukan menit: "))
    detik = int(input("Masukan detik: "))
    return jam, menit, detik

def finish():
    print("Finish")
    jamF = int(input("Masukan jam: "))
    menitF = int(input("Masukan menit: "))
    detikF = int(input("Masukan detik: "))
    return jamF, menitF, detikF

def selisih(start, finish):
    jamS = finish[0] - start[0]
    menitS = finish[1] - start[1]
    detikS = finish[2] - start[2]
    print(f"\nSelisih: {jamS} jam {menitS} menit {detikS} detik")

start = start()
finish = finish()
selisih(start, finish)
