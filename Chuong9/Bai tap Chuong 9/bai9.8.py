def so_hoan_hao(x):
    if x<=0:
        return False
    uoc_so=[]
    for i in range(1,x):
        if x%i==0:
            uoc_so.append(i)
    tong_uoc_so=sum(uoc_so)
    return x==tong_uoc_so
x=int(input('số cần kiểm tra:'))
if so_hoan_hao(x):
    print(f'Số {x} là số hoàn hảo')
else:
    print(f'Số {x} là số không hoàn hảo')