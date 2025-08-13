#1. age nomli variable yarating va unga 14 integer qiymatni taminlang. print() orqali quyidagicha chiqaring. Output:Sizning yoshingiz 14 da.
age = 14 #age degan ozgaruvchiga intager sifatiga 14 qiymat berildi
print("Sizning yoshingiz", age , "da.") # va Output bo'lib chiqyapdi

# 2. name nomli variable yarating va unga "Ali" qiymat bering. print() orqali quyidagicha chiqaring. Output: Salom, Ali
name = "Ali" #name degan ozgaruvchiga intager sifatiga string qiymat berildi
print("Salom",name) # Output bo'lib boshiga salom qoshdik va oxirida name degan ozgaruvchi yozdik

#3. year nomli variable yarating va unga 2005 qiymat bering. current_year nomli variable yarating va unga 2025 qiymat bering. Yoshni hisoblab, quyidagicha chiqaring. Output:Sizning yoshingiz 20 da.
year = 2005 # year degan ozgaruvchi yaratilmoqda va unga integer sifatida ozimizni tugulgan yilni kiritilyapdi
current_year = 2025 #current_year nomli ozgaruvchi yartildi va unga integer sifatida hozirgi yil kiritildi
print("Sizning yoshingiz", (current_year - year ) , "da.") # va Output sifatida year va current_year nomli ozgaruvchilarni qiymati ayrilyapdi

# 4. a va b nomli variablelarga mos ravishda 5 va 8 qiymat bering. Yig‘indisini chiqaring. Output:Yig‘indi: 13
a = 5 # a degan ozgaruvchi yaratilmoqda va unga integer sifatida 5 kiritilyapdi
b = 8 # b degan ozgaruvchi yaratilmoqda va unga integer sifatida 8 kiritilyapdi
print("Yig‘indi:", a + b ) # va ozgaruvchilarni qiymati qoshilyapdi

# 5. number nomli variablega 4 qiymat bering. Uning kvadratini va kubini chiqaring. Output:Kvadrat: 16 Kub: 64
number = 4 # number degan ozgaruvchi yaratilmoqda va unga integer sifatida 4 kiritilyapdi
print(
    "Kvadrat:" , ( number * number ) , 
    "Kub:" , ( number * number * number )  
)
# va Outputda Kvadratni topish uchun ozini oziga kopaytirdik , Kub topish uchun ozini oziga uch marta kopaytirdik 

# 6. radius nomli variablega 7 qiymat bering. Aylana uzunligini (2 * 3.14 * radius) hisoblab chiqaring. Output:Aylana uzunligi: 43.96
radius = 7 #radius degan ozgaruvchi yaratilmoqda va unga integer sifatida 7 kiritilyapdi 
print("Aylana uzunligi:",2 * 3.14 * radius) # va hisoblab Output bolib chiqyapti

# 7. length va width nomli variablelarga 5 va 3 qiymat bering. To‘g‘ri to‘rtburchakning yuzini va perimetrini chiqaring. Output:Yuzi: 15 Perimetri: 16
length = 5 #length degan ozgaruvchi yaratilmoqda va unga integer sifatida 5 kiritilyapdi
width = 3 #width degan ozgaruvchi yaratilmoqda va unga integer sifatida 3 kiritilyapdi
print(
    "Yuzi:",length * width,
    "Perimetri:", 2 * (length + width)
)
# yuzini topish uchun length bilan width bir biriga kopaytiriladi
# perimetirini topish uchun aval length bilan width bir biriga qoshiladi va ikkiga kopaytiriladi
 
# 8. x nomli variablega 2 qiymat bering. Unga 5 qo‘shing, so‘ng 3 ga ko‘paytiring va natijani chiqaring. Output:Natija: 21
x = 2 #x degan ozgaruvchi yaratilmoqda va unga integer sifatida 2 kiritilyapdi
print( "Natija:", (x + 5) * 3 ) # avval qavs ichida ozgaruvchi qiymati bilan 5 qoshilyapdi va natijasi bilan uchga kopaytirilyapdi Output bolib 21 chiqyapdi 

# 9. num1 va num2 nomli variablelarga 6 va 10 qiymat bering. O‘rtacha qiymatini chiqaring. Output O‘rtacha: 8.0
num1 = 6 # num1 degan ozgaruvchi yaratilmoqda va unga integer sifatida 6 kiritilyapdi
num2 = 10 # num2 degan ozgaruvchi yaratilmoqda va unga integer sifatida 10 kiritilyapdi
print("O‘rtacha:",( num1 + num2 ) / 2 ) # va O‘rtacha qiymatini topish uchun aval bir biriga qoshiladi keyin nechta son bolsa yigindisiga bolinadi 

# 10-vazifa: first va second nomli variablelarga 12 va 5 qiymat bering. Ularning yig‘indisi va farqini chiqaring.Output:Yig‘indi: 17 Farq: 7
first = 12 #first degan ozgaruvchi yaratilmoqda va unga integer sifatida 12 kiritilyapdi
second = 5 # second degan ozgaruvchi yaratilmoqda va unga integer sifatida 5 kiritilyapdi
print(
    "Yig‘indi:", first + second ,
    "Farq:",first - second 
)
# Yig‘indi topish uchun first va second ozgaruvchilar bir biriga qoshiladi Farqi topish uchun first va second ozgaruvchilar ayriladi 

# 11. a, b, c nomli variablelarga 2, 4, 5 qiymat bering. Yig‘indi va ko‘paytmani chiqaring. Output:Yig‘indi: 11 Ko‘paytma: 40
a = 2 # a degan ozgaruvchi yaratilmoqda va unga integer sifatida 2 kiritilyapdi
b = 4 # b degan ozgaruvchi yaratilmoqda va unga integer sifatida 4 kiritilyapdi
c = 5 # c degan ozgaruvchi yaratilmoqda va unga integer sifatida 5 kiritilyapdi
print(
    "Yig‘indi: ",a + b + c ,
    "Ko‘paytma:" , a * b * c
)
# Yig‘indi topish uchun ozgaruvchilar bir biriga qoshiladi Kopaytma topish uchun ozgaruvchilar bir biriga kopaytiriladi

# 12. hour va minute nomli variablelarga 2 va 30 qiymat bering. Umumiy minutni chiqaring. Output:
hour = 2 # hour degan ozgaruvchi yaratilmoqda va unga integer sifatida 2 kiritilyapdi
minute = 30 # minute degan ozgaruvchi yaratilmoqda va unga integer sifatida 30 kiritilyapdi
print("Umumiy minut:", ( hour * 60 ) + minute )
# minut topish uchun soatni kopaytiramiz 60 minutga va qoshamiz hozirgi minutga

# 13. kg nomli variablega 3 qiymat bering. Gramm va tonnaga aylantirib chiqaring. Output:
kg = 3 # kg degan ozgaruvchi yaratilmoqda va unga integer sifatida 3 kiritilyapdi

print(
    "Gramm:" , kg * 1000 ,
    "Tonna:", kg / 1000
)
# gramm topish uchun hozirgi kgni kopaytiramiz 1000ga tonna topish uchun kg ni bolamiz 1000ga

# 14. p va q nomli variablelarga 10 va 3 qiymat bering. Bo‘lish va butun bo‘lish natijasini chiqaring. Output:
p = 10 # p degan ozgaruvchi yaratilmoqda va unga integer sifatida 10 kiritilyapdi
q = 3 # q degan ozgaruvchi yaratilmoqda va unga integer sifatida 3 kiritilyapdi
print(
    "Bo‘lish:", p / q , 
    "Butun bo‘lish:",p // q
)
# bolish topish uchun p / q butun bolish uchun p // q yani uch o'ni ichida necha marta sigadi

# 15. pi nomli variablega 3.14159 qiymat bering. Uni 2 xonagacha yaxlitlab chiqaring. Output:Yaxlitlangan: 3.14
pi = 3.14159 # pi degan ozgaruvchi yaratilmoqda va unga integer sifatida 3.14159 kiritilyapdi
print("Yaxlitlangan:",round(pi,2))
# round degan functionda soni 2 xonali qildik

# 16. n1, n2, n3 nomli variablelarga 5, 7, 9 qiymat bering. O‘rtacha qiymatini 1 xonagacha yaxlitlab chiqaring. Output:
n2 = 7 # n1 degan ozgaruvchi yaratilmoqda va unga integer sifatida 7 kiritilyapdi
n1 = 5 # n2 degan ozgaruvchi yaratilmoqda va unga integer sifatida 5 kiritilyapdi
n3 = 9 # n3 degan ozgaruvchi yaratilmoqda va unga integer sifatida 9 kiritilyapdi
print( "O‘rtacha:", ( n1+ n2 + n3 ) / 3 )
# O‘rtacha soni topishimiz uchun aval ozgaruvchilarni yiginisini chiqiramiz va uni 3 ga bolamiz  

# 17. sm nomli variablega 1234 qiymat bering. Metr va kilometrga aylantirib chiqaring. Output:
sm = 1234 # pi degan ozgaruvchi yaratilmoqda va unga integer sifatida 3.14159 kiritilyapdi
print(
    "Metr:", sm / 100 ,
    "Kilometr:", sm / 100000
)
# metr topishimiz uchun sm ni bolamiz 100 metrga kilometr topish uchun sm bolamiz 100000

# 18. a va b nomli variablelarga 8 va 2 qiymat bering. Farqi, yig‘indisi, ko‘paytmasi va bo‘linmasini chiqaring. Output:
a = 8 # a degan ozgaruvchi yaratilmoqda va unga integer sifatida 8 kiritilyapdi
b = 2 # b degan ozgaruvchi yaratilmoqda va unga integer sifatida 2 kiritilyapdi
print(
    "Farq:", a - b ,
    "Yig‘indi:", a + b,
    "Ko‘paytma:", a * b,
    "Bo‘lish:", a / b
)
# farqi topish uchun ozgaruvchilarni ayramiz yigindisini topish uchun ozgaruvchilarni bir birga qoshamiz kopaytma
# topish uchun ozgaruvchilarni bir birga kopaytiramiz bolish topish uchun ozgaruvchilarni bir biriga bolamiz

# 19. som nomli variablega 300000 qiymat bering. Uni dollarga va yevroga aylantirib chiqaring (1$ = 12000, 1€ = 13000). Output:Dollar: 25.0 Yevro: 23.076923076923077
som = 300000 # som degan ozgaruvchi yaratilmoqda va unga integer sifatida 300000 kiritilyapdi
print(
    "Dollar:", som / 12000 ,
    "Yevro:", som / 13000
)
# dollar topish somni bolamiz 12000 yevro topish uchun somni bolamiz 13000

# 20. a va b nomli variablelarga qiymat bering va ularning id() qiymatlarini chiqaring. Output:a id: 9793216 b id: 9793216
b = 2 # a degan ozgaruvchi yaratilmoqda va unga integer sifatida 3 kiritilyapdi
a = 3 # b degan ozgaruvchi yaratilmoqda va unga integer sifatida 2 kiritilyapdi
print(
    "a id:" ,id(a),
    "b id:" ,id(b)
)
# id sini chiqarish uchun shunchaki id functiondan foydalanamiz
