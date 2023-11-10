def tinh_tien_lai(goc, lai_suat, thoi_gian):
    tien_lai = goc * (lai_suat / 100) * thoi_gian
    return tien_lai

goc = float(input("Nhập số tiền gốc: "))
lai_suat = float(input("Nhập tỷ lệ lãi suất hàng năm: "))
thoi_gian = int(input("Nhập số tháng gửi: "))

tien_lai = tinh_tien_lai(goc, lai_suat, thoi_gian)
tong_so_tien = goc + tien_lai

print(f"Số tiền lãi là: {tien_lai}")
print(f"Tổng số tiền sau khi kết thúc kỳ hạn là: {tong_so_tien}")