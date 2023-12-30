def chia_hai_so_nguyen(a,b):
    if b==0:
        return False
    return a//b
a=int(input('Nhập số a:'))
b=int(input('Nhập số b:'))
ket_qua=chia_hai_so_nguyen(a,b)
print(f'Phần nguyên của {a} chia hết cho {b} là:', ket_qua)