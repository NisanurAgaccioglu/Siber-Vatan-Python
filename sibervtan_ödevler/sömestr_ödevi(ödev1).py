#Kullanıcıdan bir cümle alın, cümlenin başındaki ve sonundaki boşlukları kaldırın, ardından tüm harfleri küçük harfe çevirin.  
kullanici_girişi=input("Lütfen bişey Giriniz:")
kullanici_girişi=kullanici_girişi.strip()
kullanici_girişi=kullanici_girişi.lower()
print(kullanici_girişi)
#Lütfen bişey Giriniz:AY YİLDİZİN İSİGİNİ GÖRÜNCE 
#ay yi̇ldi̇zi̇n i̇si̇gi̇ni̇ görünce çıktısı böylemiş

#Bir string içinde belirli bir karakterin kaç kez geçtiğini sayın.
str1 = "tuğ kaldırıp yürüyecek bozkurdum"
str_count=str1.count("u")
print(str_count)
#count fonksiyonu bir stringde de listdede falanda kullanılıyo ama ikisindede kullanımı farklılaşıyo, üstteki açıklama satırında ne yaptıgı yazıyor

#Kullanıcıdan bir kelime ve bir harf alın, kelimenin içindeki o harfi kaç kez içerdiğ.çıuini kontrol edin.
kullanici_girişi1=input("Lütfen 1kelime Giriniz:")
kullanici_girişi2=input("Lütfen 1harf Giriniz:")
strg=kullanici_girişi1
str_count=strg.count(kullanici_girişi2)
print(str_count)
#kullanıcan iki giriş aldım ve tanımladım, sonra tanımdadıklarımı count fonksiyonunda gereken yerlere koydum 

#İki string'i birleştirin ve ardından bir substring arayın ve konumunu bulun.
ad= "nisa"
soyad= "agaccioglu "
karsilama= "benim adım " + ad + " soyadım " +soyad
print(karsilama)
print(karsilama[3])
karsilama_find =karsilama.find(karsilama[3])
print(karsilama_find)
#ilk başta string yazdım yazdım sonra birleştirdim sonra substring aradım sonra konumunu buldum 

#Kullanıcıdan bir cümle alın ve cümlenin içindeki kelimeleri alfabetik sıraya göre sıralayın.
kullanıcıgirisi1=input("Lütfen cümle Giriniz:")
kullanıcıgirisi1_split=kullanıcıgirisi1.split()
kullanıcıgirisi1=[(kullanıcıgirisi1_split)]
kullanıcıgirisi1_split.sort()
print(kullanıcıgirisi1_split)
#kullanıcan giris aldım sonra bu cümleyi split fonksiyonu ile kelimelerine ayırdım 
#sonra sonra splitli cümleyi alıp sort yaparak alfabetik sıraya dizdim ve ekrana yazdırdım

#Kullanıcıdan iki string alın, bu stringleri birleştirin ve tüm karakterleri küçük harfe çevirin.
kullanici_girişi1=input("Lütfen kelime1 Giriniz:")
kullanici_girişi2=input("Lütfen kelime2 Giriniz:")
birleşmişstring= kullanici_girişi1 + kullanici_girişi2
birleşmişstring=birleşmişstring.lower()
print(birleşmişstring)
#iki tane giriş aldım sonra bunları birleştirdim en sonda lower fonksiyonunu kullanarak küççülttüm tüm karakterleri

#Bir string içinde belirli bir alt dizeyi (substring) arayın ve yerine başka bir alt dize ekleyin.
str = "yasasın ırkımız çine bedel kırkımız"
aranankelime = "çine"
değiştirilinceolcakkelime= "çile"
yenistr=str.replace(aranankelime,değiştirilinceolcakkelime)
print(yenistr)
#ilk başta cümle aldım sonra cümlenin içindeki kelimeyi tanımladım sonrasında cümlenin içindeki kelimenin değiştirilnce olması gereken kelimeyi tanımladım
#sonra replace fonksiyonu kullanarak kelimeleri değiştirdim

#Kullanıcıdan bir kelime alın ve kelimenin içindeki tüm 'a' harflerini '@' ile değiştirin.
kullanici_girişi1=input("Lütfen kelime Giriniz:")
kullanici_girişi1_replace=kullanici_girişi1.replace("a","@")
print(kullanici_girişi1_replace)
#kullanıcıdan giriş aldım sonra replace fonksiyonunu kullanarak anın yerine @ yazdırıdım

#Kullanıcıdan bir kelime alın ve kelimenin palindrome (tersinden de okunduğunda aynı olan) olup olmadığını kontrol edin.
kelime=input("Lütfen kelime Giriniz:")
kelimenintersi=kelime[::-1]
print("girilen kelimenin tersi = %s " % (kelimenintersi))
if kelimenintersi == kelime :
    print("girilen kelime palindrom")
else:
    print("girilen kelime palindrom değil")
#2.satıra kadar kendim yazdım sonrasına internetten baktım ,if ve elseyi daha önceden gördüğüm için biliyorum 
#ama %s bu karakteri görmedim büyük ihtimal kaçış dizgisi

#Kullanıcıdan bir cümle alın, cümlede geçen kelimelerin içinde en uzun olanını bulun.
cümle=input("Lütfen cümle Giriniz:")
kelimeleriayır = cümle.split()
enuzunkelime= max(kelimeleriayır,key=len) #burdaki key=len max fonksiyonunun içindeki bir arac, key fonksiyonu sayesinde en uzun kelimeyi buluyo
print(enuzunkelime)
#yani key=len max fonksiyonuna hangi kıyaslamayı kullanması gerektiğini belirtir, bu durumda kelimenin uzunluğuna göre kıyaslama yapar
#ilk başta cümleyi aldım sonrasında kelmelere ayırdım ve max, key=len fonksiyonu sayesinde en uzun kelimeyi buldum

#Bir liste oluşturun ve listenin ortasındaki elemanı bulun.
liste=[1,2,3,4,5,]
listeninuzunluğu = len(liste)
ortadakieleman = listeninuzunluğu // 2  #ikiye bölerek ortadaki elemanı buluyom, buçuklu değer verir fakat yuvarlama yaptıüı için küçüğe yuvarlicak
print("listenin ortadaki eleman:",ortadakieleman)
#şimdi ortadaki eleman diyince normalde 3ü vermesi gerekie ama indis 0 dab başladığı için 

#Bir tuple oluşturun, tuplein 2. ve 4. elemanlarını yeni bir tuple olarak alın.
tuple=(10,20,30,40,50,60,70)
yenituple= (tuple[1],tuple[3]) #burya neden 2 v3 4 yazmadım çünkü denedim 
#ve indis sayısından dolayı doğru vermedi ve indis sayarak 2 ve 4. elamanları hangisine denk geliyo hesapladım
print(yenituple)
#tuplein içindeki elamanları yazarken ilk başta normal parantez kullandım sonra kaçıncı elaman olduğunu belli etmek içinde köşeli parantez kullandım

#Bir set oluşturun, set içine bir sayı ekleyin, ardından bu sayıyı setden çıkarın.
#kumeler(sets)
kume={100,200,300,400,500}
eklenensayi=700
kume.add(eklenensayi) #eklenen sayı diye yeni sayıyı tanımlamak lazımmış yoksa olmuyomuş denendi onaylandı
print(kume) #700 eklenmiş hali
kume.remove(eklenensayi) #remove metodu kullanılması gerekiyomuş eklenen sayıyı çıkarmak için 
print(kume)#700 silinmiş hali

#Bir dictk oluşturun, dicte yeni bir anahtar-değer çifti ekleyin, ardından bir anahtarı silin.
dict={"anahtar1":"deger1","anahtar2":"deger2"}
yenianahtar= "anahtar3"
yenideger= "deger3"
dict[yenianahtar] = yenideger #dicte yeni anahtar ve değer eklmek için bunu kullanıyomuşuz 
silincekanahtar = 'anahtar2'
del dict[silincekanahtar] #del kelimesi pythonda bir değişkeni silmek için kullanılıyomuş !!
print(dict)
#dict oluşturdum içine yeni anahtar ve deger atadım sonra silincek anahtar ve degeri belirledim ve del yardımıyla sildim

#Bir liste oluşturun, listenin ortasına yeni bir sayı ekleyin.
liste =[1,2,3,4,5]
listeninuzunluğu = len(liste)
eklenceksayi = 7
ortadakieleman = len(liste) // 2 
liste.insert(ortadakieleman,eklenceksayi) #listelerde eklemek için insert kullanmak gerekiyomuş
print("yeni Liste:",liste)


#Bir liste oluşturun ve listenin ortasındaki elemanı bir tuplee ekleyin.
liste=[1,2,3,4,5,6]
tuple=(10,20,30)
listeninuzunluğu = len(liste)
ortadakieleman = listeninuzunluğu // 2  
yenituple=tuple + (ortadakieleman,) #(,)koymayınca yanına yemi sayı eklemiyo !!
print(yenituple)

#Bir set oluşturun ve setin elemanlarını içeren bir liste oluşturun, ardından bu liste elemanlarının toplamını hesaplayın.
kume={100,200,300,400,500,}
kume_list=list(kume)
print("kume to list",kume_list)
listeelemantoplam = sum(kume_list) #sum() fonksiyonu bir liste içindeki elemanların toplamını veriyormuş !!
print("liste elemanlarının toplamı:",listeelemantoplam)

#Bir dict oluşturun ve dictin içindeki string türündeki değerlerin karakter sayılarının toplamını bulun.
dict={"anahtar1":"bozkurt","anahtar2":"çağ"} #degerler yerine kelimeler yazıyorum
toplam_karakter_sayisi = sum(len(deger) for deger in dict.values())
print("String Değerlerin Toplam Karakter Sayısı:", toplam_karakter_sayisi)
#bunu yapmak için yardım aldım ama anladığım kadarıyla olay şöyle işliyo
#my_dict.values(): Bu ifade, sözlüğün değerlerini içeren bir görünüm (view) nesnesini döndürür. Yani, sözlükteki her bir değeri içeren bir iterable (gezilebilir) nesnedir.
#for deger in my_dict.values(): Bu ifade, her bir değeri (deger) sözlük değerleri üzerinde gezinerek alır.
#len(deger): Bu ifade, her bir değerin uzunluğunu (karakter sayısını) döndürür.
#len(deger) for deger in my_dict.values(): Bu ifade, sözlük değerlerinin uzunluklarını içeren bir liste üreteci (list comprehension) oluşturur.
#sum(...): Bu ifade, üretilen uzunluk listesinin elemanlarını toplar.

#Bir liste oluşturun ve listenin içindeki en büyük sayıyı bulun, ancak sadece aritmetik operatörler (+, -, *, /) kullanmadan yapın.
liste = [1,2,3,4,5]
enbuyuksayi = max(liste)
print("listedeki en buyuk sayı:", enbuyuksayi)
#max fonksiyonunu kullanarak listedeki en buyk sayı budum

#Bir dict oluşturun ve dictin içindeki string türündeki değerlerin hepsini birleştirerek tek bir string elde edin.
dict={"anahtar1":"yaşasın","anahtar2":"ırkımız","anahtar3":"çine","anahtar4":"bedel","anahtar5":"kırkımız"} #degerler yerine kelimeler yazıyorum
deger1=dict["anahtar1"]
deger2=dict["anahtar2"]
deger3=dict["anahtar3"]
deger4=dict["anahtar4"]
deger5=dict["anahtar5"]
print(deger1,deger2,deger3,deger4,deger5)
#hepsi için deger ataması yapıyorum ve ekrana yazdırıyorum
