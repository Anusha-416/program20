'''file=open("sample.txt","w+")
file.write("aanusha")
file.write("ammuuu")
file.close()
.......................................................

file=open("sample.txt","w")
n=eval(input("enter your names with\n"))
file.writelines(n)
file.close
.......................................................
file=open("pract10.py","w")
n=eval(input("enterr"))
file.write(n)
file.close()
.......................................................'''
file=open("pract.txt","w")
enter=eval(input("enter how many lines do you want to enter"))
for i in range(enter):
    data=eval(input("enter line\n"))
file.write(data)
file.close()

file=open("pract.txt","r")
file.read()
print(data)
