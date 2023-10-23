x = int(input("Nhập số nguyyên có 5 chữ số: "))

x1 = int((x/10000))
x2 = int((x%10000)/1000)
x3 = int((x%1000)/100)
print(str(x1)+str(x2)+str(x3))