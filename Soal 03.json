import random

#memasukkan angka dan karakter
listangka=['4', '8','1', '7', '2', '9', '4']
listkarakter=['a']

print("List Input Deret Angka                         : ", listangka)
print("List Input Karakter                            : ", listkarakter)

#mengacak string karakter ke dalam deret angka
listacak = listangka+listkarakter
random.shuffle(listacak) #fungsi berasal dari package import.random
print("Kondisi List Dalam Kondisi Teracak             : ", listacak)

#menghapus string karakter & menyortir deret angka dari yang terkecil ke terbesar
if  (type(listacak) != int):
    listacak.remove('a')
    print("Kondisi List Saat Karakter Dihapus             : ", listacak)
    listacak.sort()
    print("Kondisi List Hanya Angka dan Sudah Terurut     : ", listacak)
else:
    print("Tidak ada nomor ditemukan pada paramater")
