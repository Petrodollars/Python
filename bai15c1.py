import math

def calculate_exponential(x, ep):
    n = 0
    term = 1  
    result = 1  
    while abs(term) >= ep:
        n += 1
        term = (x ** n) / math.factorial(n)
        result += term
    return result

x = float(input("Nhập giá trị x: "))
ep = float(input("Nhập giá trị ep (0 < ep < 1): "))
if 0 < ep < 1:
    result = calculate_exponential(x, ep)
    print(f"Giá trị gần đúng của e^{x} = {result}")
else:
    print("Giá trị ep không hợp lệ!")