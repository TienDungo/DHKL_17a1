def A(n,x):
    a=pow(pow(x,2)+x+1,n)+pow(pow(x,2)-x+1,n)
    return a
n=float(input('Nhập n:'))
x=float(input('Nhập x:'))
a=A(n,x)
print('A=',a) 