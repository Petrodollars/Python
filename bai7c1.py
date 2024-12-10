def tinh_tong(n):
    S = 1 - 1 / (n + 1)
    return S

n = int(input("Nhập giá trị n: "))

kq = tinh_tong(n)
print(f"Tổng S = {kq}")
