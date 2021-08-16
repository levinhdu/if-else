
money = int(input("Số tiền đã chi tại cửa hàng: "))
muathem = 0
total = 0
if money < 75:
    muathem = 75 - money
    total = money
    print("Bạn cần mua thêm:",str(muathem) + "$ để được giảm giá")
elif money >= 75 and money<100:
    total = money - 15
    print("Bạn được giảm giá 15$")
elif money>=100 and money<150:
    total = money -25
    print("Bạn được giảm giá 25$")
elif money >=150:
    total = money -50
    print("Bạn được giảm giá 50$")
print("Số tiền bạn phải thanh toán: " ,str(total) + "$")