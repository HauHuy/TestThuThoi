x = int(input("Nhập số có 9 chữ số: "))

x1 = int(x/1000000)
x2 = int((x%1000000)/1000)
x3 = int(x%1000)

print(str(x1)+"-"+str(x2)+"-"+str(x3))