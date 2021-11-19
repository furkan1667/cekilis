from random import randint  #Kolona Her biri farklı sayı atamak için bu fonksiyon çağrılır.
for a in range(8):
  dizi = []
  for i in range(6):        #Kolonların içine verilen değer aralığındaki sayılar rastgele atanır(1'den 49'a Kadar)
        dizi.append(randint(1,49))
  print("Kolon" + str(a+1) + str(dizi))     #Oluşturulan Değerler Yazdırılır.

