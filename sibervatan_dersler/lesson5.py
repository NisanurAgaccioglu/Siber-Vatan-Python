#KARAR YAPILARI#

a=90
b="siber vatan"

num1,num2,num3=5,55,65
#sırayla tanımlanmış oluyo
print("sayilaar",num1,num2,num3)

num1=num1+55
num2=num2+55
num3=num3+90

num1+=num2
num1+=90

num1/=num2


numbers=(50,55,65)
print(type(numbers))
#tuple sınıfı

num1,num2,num3=numbers
print(num2)
#55 çıktısını verdi

a,b,c,d=50,100,50,75
print(str(a < b) )
#true çıktısını verir
print(a < b) 
#true çıktısını verir

sonuc=(a < b) 
#tanımlama yaptık
print(sonuc)

a,b,c,d=50,100,50,75
sonuc=(a>b)
print(sonuc)
sonuc=(a==c)
print(sonuc)
sonuc=(a>d)
print(sonuc)
sonuc=(a!=c)
print(sonuc)


username1="ceku"
username2="arif"

print("A.R.O.G 'a hoşgeldiniz.\n")
username_input=input("bir kullanıcı adı giriniz:")

sonuc=(username1==username_input)
print("eşleşme sonucu...",sonuc)
sonuc=(username2==username_input)
print("eşleşme sonucu...",sonuc)

sonuc=(username1.lower()==username_input.lower())
sonuc2=(username2.lower()==username_input.lower())
sonuc3=(sonuc != sonuc2)
print("eşleşme sonucu...",sonuc3)
#lower yaparak karakterleri küçülttük kullanıcı giriş yaptıgında buyuk kucuk hatası olmasın diye



#ÖDEV
#KULLANICIDAN ALINAN EMAİL VE ŞİFRENİN ÖNCEDEN TANIMLANMIŞ SÖZLÜK İÇERİSİNDE BULUNUP BULUNMADIĞINI BULAN VE BUNU EKRANA YAZDIRAN PROGRAMI YAZINIZ
users= {
    "ali@gmail":"ali321",
    "ayşe@gmail":"ayşe321"
} 

print("A.R.O.G  Portalına Hoşgeldiniz\n")
print("Lutfen A.R.O.G Bilgilerinizi Giriniz")

input_mail=input("mail giriniz :")
input_şifre=input("şifre giriniz :")

sonuc_mail=(input_mail in users.keys())
sonuc_şifre=(input_şifre in users.values())

sonuc_final=(int(sonuc_mail)+int(sonuc_şifre)==2)
print("eşleşme durumu:",sonuc_final)

fruits=["elma","muz","portakal","kivi"]
#(<bir şey> <operatör> <bir şey>)
print("kiraz" in fruits)

x=y=[10,20,30]
z=[10,20,30]
print(x is y)
print(x is z)
print(x == z)
#is karşılaştırma operatörü ,iki değişkenin adresini karşılıyor
#(==) eşit mi demek ,çıktılarını içindeki dğerlerin aynı olup olmadığını karşılaştırıyor


#ÖDEV
#kullanıcıdan bir vize%40 bir final %60 notu alıp ortalaması 50 den yüksekse geçti (true/false) yazdırın
#input_vize=input("vize notu giriniz :")
#input_final=input("final notu giriniz :")
#sayi_int= int(input_vize,input_final)
#("float to int",sayi_int)
#vize=input_vize
#final=input_final
#ortalama=vize*0.4+final*0.6
#sonuc=(50>ortalama)
#print(sonuc)
#bunlar çalışmayan kodlar geriye döndüğümde ne düşündüğümü anlamak için bıraktım

vize_input = int(input("vize notunuzu giriniz:"))
final_input = int(input("final notunuzu giriniz:"))
ortalama = (int(vize_input*40/100) + int(final_input*60/100))
print(ortalama>= 50)
#bunlar çalışan kodlar

#ödev
#girilen bir sayının pozitif çift sayı olduğu durumda ekrana true, tek sayı olma durumunda false yazdıran programı yazın
girilen_sayi=int(input("sayi:"))
result=(girilen_sayi>0) and (girilen_sayi%2==0)
print("sonuc..:"+ str(result))


#KOŞUL İF VE ELSE KONUSU
#örnek
x=98
y=23
if (x>y):
    print("en buyuk sayi:" ,x)
elif(x==y):
    print("sayilar esittir")
else:
    print("en buyuk asayi:" ,y)


#if ():
   # <eger koşul doğru (true) ise çalışacak kodlar>
#else:
   # <eger koşul yanlış (false) ise çalışsacak kodlar>


kullanici_takim=input( "takıma adı giriniz:")

if kullanici_takim=="galatasaray":
    print("en sevdiğin renkler: sari ve kırmızı")
elif kullanici_takim=="fenerbahçe":
    print("en sevdiğin renkler: sari ve lacivert") 
elif kullanici_takim=="beşiktaş":
    print("en sevdiğin renkler: siyah ve beyaz")
elif kullanici_takim=="galatasaray":
    print("en sevdiğin renkler: sari ve kırmızı")
elif kullanici_takim=="kardemir karabük spor":
    print("en sevdiğin renkler: lacivert ve bordo")



#kullnıcıdan alınan adı ve şifre bilgilerini kontrol eden ve ekrana bilgi yazan programı yazınız
username_input=input( "kullanıcı adı giriniz:")
şifreinput=input( "şifre giriniz:")
username="nisa"
şifre="nisa321"

if username_input=="nisa" and şifreinput=="nisa321":
    print("giriş başarılı")
elif username_input=="nisa" and şifreinput!="nisa321":
    print("şifre hatalı")
elif şifreinput!="nisa321" and username_input=="nisa":
    print("kullanıcı adı hatalı")
elif şifreinput!="nisa321" and username_input!="nisa":
    print("her ikiside hatalı")

#yanlış olan yere != koyulcak


#kullanıcıdan alına iki sayının istenilen matematiksel işleme tabi tutarak sonucu ekrana yazdıran programi yazınız
#toplama için 1
#çıkarma için 2
#çarma için 3
#bölme için 4
#hangi işlemi tercih edersiniz ?

print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*HOSGELDİNİZ*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
print("toplama icin 1")
print("cikarma icin 2")
print("carpma icin 3")
print("bolme icin 4'ü tuşlayınız")
tercih_input =int(input("Hangi işlemi tercih edersiniz?:"))
sayi_input = int(input("ilk sayiyi giriniz:"))
sayi_input2 = int(input("ikinci sayiyi giriniz:"))  


if tercih_input==1:
    print(sayi_input+sayi_input2)
elif tercih_input==2:
    print(sayi_input - sayi_input2)
elif tercih_input==3:
    print(sayi_input * sayi_input2)
else:
    tercih_input==4
    print(sayi_input/sayi_input2)


