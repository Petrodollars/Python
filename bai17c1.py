def calculate_area(x1, y1, x2, y2, x3, y3):
    return abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2

def check_triangle_points(x1, y1, x2, y2, x3, y3):
    area = calculate_area(x1, y1, x2, y2, x3, y3)
    return area > 0

x1, y1 = map(float, input("Nhập tọa độ điểm 1 (x1, y1): ").split())
x2, y2 = map(float, input("Nhập tọa độ điểm 2 (x2, y2): ").split())
x3, y3 = map(float, input("Nhập tọa độ điểm 3 (x3, y3): ").split())

if check_triangle_points(x1, y1, x2, y2, x3, y3):
    print("3 điểm tạo thành tam giác!")
else:
    print("3 điểm không tạo thành tam giác!")