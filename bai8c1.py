def tinh_tong(x, n):
    if x == 1:
        return n
    else:
        S = x * (x**n - 1) / (x - 1)
        return S

x = float(input("Nhập giá trị x: "))
n = int(input("Nhập giá trị n: "))

kq = tinh_tong(x, n)
print(f"Tổng S = {kq}")
