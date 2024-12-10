import math

def tinh_bieu_thuc(x, n):
    S = 1  
    temp = x  

    for i in range(n):
        temp = math.sqrt(temp)  
        S += temp  
    
    return S

x = float(input("Nhập giá trị x: "))
n = int(input("Nhập số lượng dấu căn n: "))

kq = tinh_bieu_thuc(x, n)
print(f"Giá trị của biểu thức là: {kq}")
