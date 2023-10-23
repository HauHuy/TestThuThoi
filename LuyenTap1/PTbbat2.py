import math as m
print("CHƯƠNG TRÌNH GIẢI PHƯƠNG TRÌNH BẬC 2")
a = int(input("Hãy nhập hệ số a: "))
b = int(input("Hãy nhập hệ số b: "))
c = int(input("Hãy nhập hệ số c: "))
if a == 0:
    if b != 0:
        print(f"Nghiệm của phương trình là: {-c/b}")
    elif c == 0:
        print("Pương trình có vô số nghiệm")
    else:
        print("Phương trình vô nghiệm")
else:
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b+m.sqrt(delta)/4*a)
        x2 = (-b-m.sqrt(delta)/4*a)
        print(f"Phương trình có 2 nghiệm: \n x1 = {x1} \n x2 = {x2}")
    elif delta == 0:
        x = -b/2*a
        print(f"Phương trình có nghiệp kép  = {x}")
    else:
        print("Phương trình vô nghiệm")