import math

x = int(input("Nhập số nguyên x: "))
pi = math.pi
e = math.e
print(abs(((2*pi*x-1)/(2*pi*x*x))))
print((e**(math.sin(x)))/(2*pi*(math.sqrt(x*x-1))))
print((1/(2*pi*math.sqrt(math.sin(x)))))
print(math.sin(1/(2*pi*math.sqrt(x))))
