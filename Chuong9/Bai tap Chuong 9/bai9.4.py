def tinh_S(n,x):
    S=pow(pow(x,2)+1,n)
    return S
n=int(input("Nhập giá trị n: "))
x=int(input("Nhập giá trị x: "))
S = tinh_S(n,x)
print('S =',S)    