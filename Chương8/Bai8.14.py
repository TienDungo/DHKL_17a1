N = int(input("Nhập số lượng số nguyên N: "))

sum = 0
for i in range(N):
    num = int(input("Nhập số nguyên thứ %d: " % (i+1)))
    sum += num

print("Tổng của", N, "số nguyên vừa nhập là:", sum)