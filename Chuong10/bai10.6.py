def giai_pt_bac_2(a,b,c):
    delta=b*b-4*a*c
    if delta <0:
        return ('Phuong trinh khong co nghiem thuc')
    elif delta ==0:
        x=-b/2*a
        return (f'Phuong trinh co nghiem kep la:{x}')
    else:
        x1=(-b+delta*0.5)/(2*a)
        x2=(-b-delta*0.5)/(2*a)
        return f'Nghiem thu nhat x1 = {x1}\nNghiem thu hai x2 ={x2}'
a=int(input('Nhap a = '))
b=int(input('Nhap b = '))
c=int(input('Nhap c = '))
ket_qua = giai_pt_bac_2(a,b,c)
print(ket_qua)