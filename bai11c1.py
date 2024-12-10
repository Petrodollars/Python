def giai_thua(k):
    result = 1
    for i in range(1, k+1):
        result *= i
    return result

def tinh_tong(n):
    S = 0
    for i in range(1, n+1):
        S += giai_thua(i)
    return S

n = int(input("Nhập giá trị n: "))

kq = tinh_tong(n)
print(f"Tổng S = {kq}")
