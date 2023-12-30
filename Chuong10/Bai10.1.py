
n=int(input("Nhập số phần tử của list: "))
m=[]
for i in range(n):
    x=int(input('Nhập phần tử thứ %d:'%(i+1)))
    m.append(x)
print('List vừa nhập là:',m)
so_lon_nhat=max(m)
so_nho_nhat=min(m)
print("Số lớn nhất là:", so_lon_nhat)
print("Số nhỏ nhất là: ",so_nho_nhat)