#fungsi fungsi list

#fungsi len()
a = [10,40,30]
print("a = ", a)
print("len (a) = ", len(a))

#fungsi min dan max
print("min a = ", min(a))
print("max a = ", max(a))

#metode append
print("a = ", a)
#sesudah ditambah
a.append(50)
a.append(60)
print("a sesudah ditambah = ", a)

#metode count
a = [10,40,30,10,30,20]
print("a = ", a)
print("jumlah nilai 10 = ", a.count(10))
print("jumlah nilai 30 = ", a.count(30))

#metode index
a = [10,40,30,50,70,30]
print("a = ", a)
print("index (30) = ", a.index(30))
print("index (70) = ", a.index(70))

#metode insert
print("a sebelum ditambah = ", a)
a.insert(90,100)
print("a sesudah ditambah = ", a)

#metode pop()
a = [10,40,30,50,70,80]
print("a awal = ", a)
#menghapus 80 dari list
a.pop()
#menghapus 70 dari list
a.pop()
print("hasi; = ", a)

#metode remove
a = [10,40,30,10,70,40]
print("a awal = ", a)
#menghapus 10 dari list
a.remove(10)
#menghapus 40 dari list
a.remove(40)
print("hasil = ", a)

#metode reverse
a = [10,40,30,10,70,40]
print("a awal = ", a)
a.reverse()
print("a sesudah di reverse = ", a)

#metode sort
a = [10,40,30,10,70,40]
print("a awal = ", a)
a.sort()
print("a sesudah di urutkan = ", a)

#aslinya menggunakan fungsi sort
a = [10,40,30,10,70,40]
b = sorted(a)
print("a = ", a)
print("b = ", b)

