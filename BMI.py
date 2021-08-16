
nang = float(input("Nhập cân nặng(m): "))
cao = float(input("Nhập chiều cao(kg): "))
BMI = nang /(cao**2)

if BMI > 40:
    print("Béo phì cấp độ III")
elif BMI>=35:
    print("Béo phì cấp độ II")
elif BMI >=30:
    print("Béo phì cấp độ I")
elif BMI>=25:
    print("Thừa cân")
elif BMI>=18.5:
    print("Bình thường")
elif BMI >=17:
    print("Gày cấp độ I")
elif BMI >=16:
    print("Gày cấp độ II")
else:
    print("Gày cấp độ III")

print("Chỉ số BMI là: %.2F" %BMI)