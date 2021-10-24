ngay = input("Ngay:")
ten = input("Ten:")
sang = int(input("So calo cho buoi sang:"))
trua = int(input("So calo cho buoi trua:"))
toi = int(input("So calo cho buoi toi:"))
caloBurntToday = int(input("So calo da van dong trong ngay:"))
total = sang + trua + toi - caloBurntToday
a = "{} co so calo tich luy trong ngay {} la {}"
print(a.format(ten, ngay, total))