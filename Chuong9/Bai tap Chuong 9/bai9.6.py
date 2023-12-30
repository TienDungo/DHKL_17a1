def kiem_tra_so_nguyen_to(x):
    if x<=1:
        return False
    for i in range(2,x+1):
        if i%x==0:
            return False
        return True
x=int(input('Nhập một số: '))
a=kiem_tra_so_nguyen_to(x)
print(a)
