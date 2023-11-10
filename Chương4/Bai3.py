m = int(input("Nhập một số tự nhiên m: "))
n = int(input("Nhập một số tự nhiên n (lớn hơn m): "))
if m >= 0 and n >= 0 and m < n:
    for i in range(1, n + 1):
        if i % m == 0:
            print(i)
else:
    print("Vui lòng nhập lại hai số tự nhiên m va n (m < n).")