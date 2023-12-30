a=[]                                                              #1
while True:
    b=int(input('Nhập một số:'))
    a.append(b)
    c=int(input("Nhập tiếp một số:  1: có   2: không"))
    if c==1:
        continue
    if c==0:
        break                                                     #2,3
print('List:',a)
for n in a:
    def kiem_tra_so_nguyen_to(n):
        if n<=1:
            return False
        for i in range(2,n):
            if i%n==0:
                return 'không phai so nguyen to'
            return n
so_nguyen_to=kiem_tra_so_nguyen_to(n)  
print("Các số nguyên tố trong list là:",so_nguyen_to)               #4
so_duong=[]
so_am=[]
for m in a:
    if m>0:
        so_duong.append(m)
    if m<0:
        so_am.append(m)
if so_am:
    trung_binh_am=sum(so_am)/len(so_am)
    print('Các phần tử âm trong list:',so_am)
    print('Trung bình cộng các phần tử âm:',trung_binh_am)
if so_duong:
    trung_binh_duong=sum(so_duong)/len(so_duong)
    print('Các phần tử dương trong list:',so_duong)
    print('Trung bình cộng các phần tử dương:',trung_binh_duong)    #5 
so_lon_nhat=max(a)
so_nho_nhat=min(a)
print('Giá trị max trong list:',so_lon_nhat)
print('Giá trị min trong list:',so_nho_nhat)                        #6
a.sort()                                                            #7
print('List sắp tăng dần:',a)