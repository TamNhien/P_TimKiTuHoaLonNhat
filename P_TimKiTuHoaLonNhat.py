L = input("Nhập vào danh sách các chuỗi, cách nhau bởi dấu phẩy: ").split(',')
max_upper_string = max(L, key=lambda s: max((i for i, c in enumerate(s) if c.isupper()), default=-1), default="")
print(f"Chuỗi có vị trí ký tự in hoa lớn nhất là: {max_upper_string}" if max_upper_string else "Danh sách không có chuỗi nào có ký tự in hoa.")

