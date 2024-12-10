def giai_he_phuong_trinh(a1, b1, c1, a2, b2, c2):

    D = a1 * b2 - a2 * b1
    if D != 0:
        x = (c1 * b2 - c2 * b1) / D
        y = (a1 * c2 - a2 * c1) / D
        return f"Hệ có nghiệm duy nhất: x = {x}, y = {y}"
    else:
        if a1 * c2 == a2 * c1:
            return "Hệ có vô số nghiệm"
        else:
            return "Hệ vô nghiệm"

a1 = float(input("Nhập giá trị a1: "))
b1 = float(input("Nhập giá trị b1: "))
c1 = float(input("Nhập giá trị c1: "))
a2 = float(input("Nhập giá trị a2: "))
b2 = float(input("Nhập giá trị b2: "))
c2 = float(input("Nhập giá trị c2: "))

kq = giai_he_phuong_trinh(a1, b1, c1, a2, b2, c2)
print(kq)
