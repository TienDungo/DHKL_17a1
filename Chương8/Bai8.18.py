num = int(input("Nhập số cần kiểm tra: "))

if num < 2:
   print(num, "không phải số nguyên tố")
else:
   for i in range(2, num):
       if num % i == 0:
           print(num, "không phải số nguyên tố")
           break
   else:
       print(num, "là số nguyên tố")