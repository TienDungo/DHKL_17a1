nam=int(input("Nhập năm: "))
if nam %4 == 0:
    if nam %100 == 0:
        if nam %400 == 0:
            print(nam,"Là năm nhuận. ")
        else:
            print(nam,"Không là năm nhuận. ")
    else:
        print(nam,"Là năm nhuận.")
else:
    print(nam,"Không là năm nhuận. ")