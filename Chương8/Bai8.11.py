n=int(input("Nhập n:"))
x=int(input("Nhập x:"))
x_binh=x*x
bieu_thuc1=(x_binh + x + 1)
bieu_thuc2=(x_binh - x + 1)
S1=(bieu_thuc1**n)
S2=(bieu_thuc2**n)
S=S1+S2
print("Giá trị biểu thức là:",S)