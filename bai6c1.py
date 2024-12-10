def tinh_tong(n):
    S = 3 * (n * (n + 1)) / 2
    return S

n = int(input("Nhập giá trị n: "))

kq = tinh_tong(n)
print(f"Tổng S = {kq}")
