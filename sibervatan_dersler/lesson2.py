
#PYTON DA VERİLER ,VERİ TİPLERİ#
sayi1 =42
sayi2 =-17
print(type(sayi1)) 
#burda sayının int bir değer olduğunu gösteriyor

sayi1 =42
sayi2 =-17
print(type(sayi2)) 
#burdada aynısı şekilde pyton dilini içerisindeki hazır fonksiyonu kullanarak yapıyor

sayi1 =1.5
sayi2 =-5.5
print(type(sayi1)) 
#ingilizcede virgül yerine nokta kullanılır bu yüzden virgül yerine nokta koy

sayi1 =1.5
sayi2 =-5.5
print(type(sayi2)) 
#float bir değer ikiside

dogru_mu = True
yanlis_mi= False
print(type(dogru_mu))
#bool bir değer olduğunu söylüyor makineye true yada false olarak tanımlanan fakat bazende bir ve sıfır değerlerini verdiği değer

dogru_mu = True
yanlis_mi= False
print(type(yanlis_mi))
#aynı bool değer

sayi1 =42
sayi2 =-17
ondalik1= 3.14
ondalik2= -0.5
dogru_mu = True
yanlis_mi= False

sayi_float=float(sayi1)
print("int to float",sayi_float)
# sayı 42 nin normalde ondalık kısmı sıfır olduğu için çıktıyı 42.0 olarak veriyor çıktı=int to float 42.0 ,int bir deger float oldu

sayi_int= int(ondalik1)
print("float to int",sayi_int)
#çıktı direkt 3 olarak gelir çünkü float bir sayıyı tamd ayıya çeviriyo, yani üstteki örneğin tam tersi

sayi_bool=int(dogru_mu)
print("bool to int",sayi_bool)
#çıktı olarak 1 verir, makine anlayıp 1 e çeviriyor,bool to int 1

sayi_bool=int(yanlis_mi)
print("bool to int",sayi_bool)
#çıktı olarak 0 verir, makine anlayıp 0 e çeviriyor,bool to int 0


print(type(sayi_bool))
#int bir deger, <class 'int'> çıktısı verdi



#İNPUT İŞLEMLERİ#

kullanici_ad=input("Lütfen Adınızı Giriniz:")
print("Hoşgeldin",kullanici_ad)
#hoşgeldin mesajı veren uygulama 
#Lütfen Adınızı Giriniz:nisa
#Hoşgeldin nisa ,çıktısı verdi

sayi1=input("lütfen sayi1 giriniz")
sayi2=input("lütfen sayi2 giriniz")
print(sayi1 + sayi2)
#çalışmayan kod

sayi3=input("1.sayiyı giriniz:")
sayi4=input("2.sayiyi giriniz:")
print(int(sayi3) +int(sayi4))

