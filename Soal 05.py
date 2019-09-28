string1 = input("Masukkan string pertama : ")
string2 = input("Masukkan string kedua   : ")

print("String pertama          :",string1)
print("String kedua            :",string2)

print("----------------------------------------------------------------------------------------")
hitungparamterstring = string1.count(string2)
if (hitungparamterstring == 0):
    print("Tidak Ditemukan")
else:
    print("Banyak Karakter di Paramater ke-2 dari String Pertama : ", hitungparamterstring, str("karakter"))
print("----------------------------------------------------------------------------------------")



