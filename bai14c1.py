import math

def calculate_sum(a):
    n = 0
    S = 0
    term = 1  
    while term >= a:
        term = 1 / math.factorial(2 * n + 1)
        S += term
        n += 1
    return S

a = float(input("Nhập giá trị a (0 < a < 0.01): "))
if 0 < a < 0.01:
    result = calculate_sum(a)
    print(f"Tổng S = {result}")
else:
    print("Giá trị a không hợp lệ!")