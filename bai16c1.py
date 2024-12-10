import math

def check_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

def calculate_triangle(a, b, c):
    if not check_triangle(a, b, c):
        return "Ba cạnh không tạo thành tam giác!"
    perimeter = a + b + c
    s = perimeter / 2  
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return perimeter, area

a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

if check_triangle(a, b, c):
    perimeter, area = calculate_triangle(a, b, c)
    print(f"Chu vi tam giác: {perimeter}")
    print(f"Diện tích tam giác: {area}")
else:
    print("Ba cạnh không tạo thành tam giác!")