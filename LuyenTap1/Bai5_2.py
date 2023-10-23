import re

s = input("Hãy nhập chuỗi kí tự: ")
a = re.findall(r'\d',s)

print(a)
print(sum(a))