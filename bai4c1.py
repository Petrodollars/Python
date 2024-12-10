import math

def giai_phuong_trinh_bac_2(a, b, c):
    if a == 0:
        if b != 0:
            x = -c / b
            return f"Phương trình là bậc nhất, có nghiệm duy nhất: x = {x}"
        else:
            if c != 0:
                return "Phương trình vô nghiệm"
            else:
                return "Phương trình có vô số nghiệm"
    else:
        delta = b**2 - 4*a*c
        
        if delta > 0:
            x1 = (-b + math.sqrt(delta)) / (2 * a)
            x2 = (-b - math.sqrt(delta)) / (2 * a)
            return f"Phương trình có 2 nghiệm phân biệt: x1 = {x1}, x2 = {x2}"
        
        elif delta == 0:
            x = -b / (2 * a)
            return f"Phương trình có nghiệm kép: x1 = x2 = {x}"
        
        else:
            return "Phương trình vô nghiệm (không có nghiệm thực)"

a = float(input("Nhập giá trị a: "))
b = float(input("Nhập giá trị b: "))
c = float(input("Nhập giá trị c: "))

kq = giai_phuong_trinh_bac_2(a, b, c)
print(kq)
