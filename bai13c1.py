import math

def calculate_S(threshold):
    n = 0
    S = 0
    while S <= threshold:
        S += 1 / math.factorial(2 * n + 1)  
        n += 1
    return n - 1, S  

threshold = 1000

n_min, final_S = calculate_S(threshold)
print(f"Số nguyên dương nhỏ nhất n: {n_min}")
print(f"Tổng S khi đó: {final_S}")