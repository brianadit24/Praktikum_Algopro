a = open("L200180151.txt", "w")
a.write("L200180151" "\n")
a.write("01/25/2000" "\n")
a.write("Arya Mukti A'raafi Zha Putra" "\n")
a.write("Semarang")

a = open("L200180151.txt", "r")
NIM = a.readline()
Tanggal_lahir = a.readline()
Nama = a.readline()
Kota = a.readline()
print(Nama)
print(Kota, Tanggal_lahir)
print(NIM)
a.close()
