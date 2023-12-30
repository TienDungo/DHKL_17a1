can= ["Giáp","Ất","Bính","Đinh","Mậu","Kỷ","Canh","Tân","Nhâm","Quý"]
chi= ["Tý","Sửu","Dần","Mão","Thìn","Tỵ","Ngọ","Mùi","Thân","Dậu","Tuất","Hợi"]
nhap_nam=int(input("Nhập năm:"))
def am_lich(nam) :
  if nam < 0:
    return "Năm âm lịch không hợp lệ"

  tinh_can = (nam + 6) % 10 + 1
  
  if tinh_can < 1 or tinh_can > 10:
    return "Năm âm lịch không hợp lệ"
  
  tinh_chi = (nam + 8) % 12

  if tinh_chi < 0 or tinh_chi >= 12:
    return "Năm âm lịch không hợp lệ"

  return can[tinh_can - 1] + " " + chi[tinh_chi]

print("Năm",nhap_nam,"lịch âm là năm",am_lich(nhap_nam))