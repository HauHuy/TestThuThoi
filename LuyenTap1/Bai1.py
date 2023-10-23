s1 = input("Nhập họ và tên: ")
print(s1.find(" ",0,len(s1)))
s2 = s1[:4]
s3 = s1[5]
s4 = s1[6:8]
s5 = s1[8:9]
s6 = s1[9:]
print(s2.upper() + " "+ s3.upper() +s4+s5.upper()+s6)