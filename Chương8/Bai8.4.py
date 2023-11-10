import math
a=float(input("Nhập độ dài cạnh a:"))
b=float(input("Nhập độ dài cạnh b:"))
c=float(input("Nhập độ dài cạnh c:"))
p=(a+b+c)/2
dien_tich=math.sqrt(p*(p-a)*(p-b)*(p-c))
print("Diện tích tam giác là:",dien_tich)