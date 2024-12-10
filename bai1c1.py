def giai_phuong_trinh(a, b):
    if a == 0:
        if b == 0:
            return "Phương trình có vô số nghiệm"
        else:
            return "Phương trình vô nghiệm"
    else:
        x = -b / a
        return f"Phương trình có nghiệm x = {x}"

a = float(input("Nhập giá trị a: "))
b = float(input("Nhập giá trị b: "))

kq = giai_phuong_trinh(a, b)
print(kq)