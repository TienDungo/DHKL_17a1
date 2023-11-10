def giai_he_phuong_trinh_bac_nhat(a, b):
    if a == 0:
        if b == 0:
            return "Phuong trinh co vo so nghiem"
        else:
            return "Phuong trinh vo nghiem"
    else:
        x = -b / a
        return f"Nghiem cua phuong trinh la x = {x}"

# Sử dụng hàm
a = float(input("Nhap he so a: "))
b = float(input("Nhap he so b: "))
ket_qua = giai_he_phuong_trinh_bac_nhat(a, b)
print(ket_qua)