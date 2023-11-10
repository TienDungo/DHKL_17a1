a=float(input("Nhập a:"))
b=float(input("Nhập b:"))
if a==0 and b==0:
    print("Phương trình vô số nghiệm")
elif a==0 and b!=0:
    print("Phương trình vô nghiệm")
else:
    x=-b/a
    print("Nghiệm của phương trình là:",x)