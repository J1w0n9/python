fl = open("person.txt", "r")
name = fl.readline()
addr = fl.readline()
fl.close()
print(name)
print(addr)

print(fl.read())