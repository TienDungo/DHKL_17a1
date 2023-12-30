animals = ["ant", "bear", "cat", "dog", "elephant",'fish','goat','hippo']
print("Danh sách thú trong vườn thú:",animals)
print('Số thú trong vườn là:',len(animals))

n = input("Nhập con thú cần tìm: ")
if n in animals:
    print(f"Tìm thấy {n} trong danh sách")
else:
    print(f"Không tìm thấy {n} trong danh sách")