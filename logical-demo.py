#1)
# sayi = float(input("sayı: "))
# result=(sayi>0) and (sayi<100)
# print(f"Sayı 0 ile 100 arasında mı : {result}")

#2)
# sayi=int(input('Sayı: '))
# result=(sayi>0) and (sayi%2==0)
# print(f'Girilen sayı pozitif çift sayı mı:{result}')

#3)
# email='email@sadikturan'
# password='abc123'

# girilenEmail=(input("email: "))
# girilenPassword=(input("parola: "))

# result=(girilenEmail==email)and(girilenPassword==password)
# print(f'Uygulamaya giriş başarılı mı:{result}')

#4)
# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: ")) 

# result=(a>b) and (a>c)
# print(f"a en büyük sayıdır: {result}")

# result=(b>a) and (b>c)
# print(f"b en büyük sayıdır: {result}")

# result=(c>a) and (c>b)
# print(f"c en büyük sayıdır: {result}")

#5)
# vize1 = float(input("vize1:"))
# vize2 = float(input("vize2:"))
# final = float(input("final:"))

# ortalama= ((vize1+vize2)/2)*0.6+(final * 0.4)
# #result= (ortalama>50) and (final>50)
# result=(ortalama>=50) or (final>=70)

# print(f"Öğrencinin ortalaması: {ortalama} ve geçme durumu: {result}")

#6)
# name=input("Adınız: ")
# kg=float(input("Kilonuz: "))
# hg=float(input("Boyunuz: "))

# index = (kg) / (hg **2)
# zayif=(index >=0) and (index<=18.4)
# normal=(index>18.4) and (index<=24.9)
# kilolu=(index>24.9) and (index<=29.9)
# obez=(index>=29.9) and (index<=34.9)

# print(f"{name} kilo indeksin {index} ve kilo değerlendirmen zayıf:{zayif}")
# print(f"{name} kilo indeksin {index} ve kilo değerlendirmen normail:{normal}")
# print(f"{name} kilo indeksin {index} ve kilo değerlendirmen kilolu:{kilolu}")
# print(f"{name} kilo indeksin {index} ve kilo değerlendirmen obez:{obez}")