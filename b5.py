'''
Nhập ngày
Nhập tên
Nhập số calo cho buổi sáng
Nhập số calo cho buổi trưa
Nhập số calo cho buổi tối
Nhập số calo đã vận động trong ngày
Tính số calo tích lũy trong ngày = calo sáng + calo trưa + calo tối – calo vận động
Xuất bạn tên có số calo tích lũy trong ngày là : số calo
'''

ngay = input("Ngay:")
ten = input("Ten:")
sang = int(input("So calo cho buoi sang:"))
trua = int(input("So calo cho buoi trua:"))
toi = int(input("So calo cho buoi toi:"))
caloBurntToday = int(input("So calo da van dong trong ngay:"))
total = sang + trua + toi - caloBurntToday
a = "{} co so calo tich luy trong ngay {} la {}"
print(a.format(ten, ngay, total))
