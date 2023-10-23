#a = input("Hay nhap day co so nguyen")
a = "3-5-8-9-4-6-5-8-7-3-1"

print(a.find("1",0,len(a)))
print(a.find("2",0,len(a)))
print(a.find("3",0,len(a)))
print(a.find("4",0,len(a)))
print(a.find("5",0,len(a)))
print(a.find("6",0,len(a)))
print(a.find("7",0,len(a)))
print(a.find("8",0,len(a)))
print(a.find("9",0,len(a)))

print(a)
s = [int(a[0]),int(a[2]),int(a[4]),int(a[6]),int(a[8]),int(a[10]),int(a[12]),int(a[14]),int(a[16]),int(a[18]),int(a[20])]

print(max(s))
print(sum(s))