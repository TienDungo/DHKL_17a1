a=[74,74,72,72,73,69,69,71,76,71]
b=[]
for i in a:
    s=i/0.0254
    b.append(s)
print(b[0:4])
print(b[-3:])
chieu_cao_trung_binh=sum(b)/len(b)
print('chiều cao trung bình:',chieu_cao_trung_binh)
print('chiều cao lớn nhất:',max(b))
print('chiều cao nhỏ nhất:',min(b))
b.sort()
print('giá trị tăng dần:',b)
b.reverse()
print('giá trị giảm dần:',b)
