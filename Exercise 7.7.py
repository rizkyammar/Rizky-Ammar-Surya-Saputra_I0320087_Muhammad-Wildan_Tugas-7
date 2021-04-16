#Fungsi fungsi string

#metode capitalize
str = "hello world"
a = str.capitalize()
print(a)

#metode center
str = "hello world"
b = str.center(20,'*')
print(b) 

#metode count
str = "hello world"
c = str.count('l')
d = str.count('o')
print("Jumlah huruf l = ", c)
print("Jumlah huruf o = ", d)

#metode endswith
str = "Hello world"
print(str.endswith("world"))
print(str.endswith("world!"))

#metode find
str = "Hello world"
print("str: " + str)
print("str find o = ", str.find('o'))
print("str find l = ", str.find('l'))


#metode index
str = "Hello world"
print("str: " + str)
print("str index o = ", str.index('o'))
print("str index l = ", str.index('l'))

#metode replace
str = "Hello world"
print("str : " + str)
print("str replace Hello = ", str.replace("Hello", "Hai"))
print("str replace world = ", str.replace("world", "Dunia"))

#metode upper and lower
str = "Hello world"
str2 = str.upper()
str3 = str.lower()
print(str)
print(str2)
print(str3)

