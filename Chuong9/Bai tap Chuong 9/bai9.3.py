a=float(input("Nhập cân nặng(kg): "))
b=float(input("Nhập chiều cao(m): "))
def tinh_BMI(a,b):
    bmi=a/(b*b)
    return bmi
bmi=tinh_BMI(a,b)
print("Chỉ số BMI của bạn là:",bmi) 