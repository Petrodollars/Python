def giai_bat_phuong_trinh(a, b):
    if a == 0:
        if b > 0:
            return "Bất phương trình có nghiệm với mọi x"
        else:
            return "Bất phương trình vô nghiệm"
    else:
        if a > 0:
            x = -b / a
            return f"Bất phương trình có nghiệm x > {x}"
        else:
            x = -b / a
            return f"Bất phương trình có nghiệm x < {x}"

a = float(input("Nhập giá trị a: "))
b = float(input("Nhập giá trị b: "))

kq = giai_bat_phuong_trinh(a, b)
print(kq)
