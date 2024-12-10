def tinh_tong(x, n):
    if x == 1:
        
        return n + 1
    else:
        S = (1 - x**(n+1)) / (1 - x)
        return S

x = float(input("Nhập giá trị x: "))
n = int(input("Nhập giá trị n: "))

kq = tinh_tong(x, n)
print(f"Tổng S = {kq}")
