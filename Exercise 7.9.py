#fungsi fungsi dictionary

#fungsi len
a = {'satu': 10, 'dua': 20, 'tiga': 30}
b = {'satu': 10, 'dua': 20}
print("a = ", a)
print("b = ", b)
print("nilai len a = ", len(a))
print("nilai len b = ", len(b))

#metode clear
#menghapus elemen
a.clear()
b.clear()
#setelah dihapus
print("nilai len a = ", len(a))
print("nilai len b = ", len(b))

#metode copy
a = {'satu': 10, 'dua': 20, 'tiga': 30}
print("a = ", a)
#membuat copy a
b = a.copy()
print("b = ", b)

#metode items(), key(), dan values()
a = {'satu': 10, 'dua': 20, 'tiga': 30}
print("a = ", a)
item = a.items()
keys = a.keys()
value = a.values()
print("item = ", item)
print("keys = ", keys)
print("value = ", value)

