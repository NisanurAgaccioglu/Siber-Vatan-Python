#1)Bir fonksiyon oluşturun. Emeklilik yaşını 65 olarak belirleyin.Kullanıcıdan yaşını alıp 65 yaş altındakilere emekliliğine kaç yıl kaldığınıveya 65 yas üstüne zaten emekli olduğunu ekrana yazdiriniz.

def emeklilikhesabı(yas):
    emeklilikyasi = 65
    emekliliğekalanyıl = emeklilikyasi - yas
    
    if yas < emeklilikyasi:
        print("Emekliliğinize", emekliliğekalanyıl, "yıl kaldı.")
    else:
        print("Zaten emekli oldunuz.")

yas = int(input("Yaşınızı giriniz: "))
emeklilikhesabı(yas)

#2)Bir fonksiyon oluşturun.Fonksiyon kullanıcıdan iki sayı alıp bu iki sayı arasındaki asal sayıları ekrana bastırın.

def asalsayilar(sayi1, sayi2):
    asal_sayilar = []

    for sayi in range(sayi1, sayi2 + 1):
        #burların formulunu yapamadım bende intten baktım
        if sayi > 1:
            for i in range(2, sayi):
                if (sayi % i) == 0:
                    break
            else:
                asal_sayilar.append(sayi)

    if len(asal_sayilar) > 0:
        print("İki sayı arasındaki asal sayılar:", ", ".join(map(str, asal_sayilar)))
    else:
        print("Girilen aralıkta asal sayı bulunmamaktadır.")

sayi1 = int(input("İlk sayıyı giriniz: "))
sayi2 = int(input("İkinci sayıyı giriniz: "))

asalsayilar(sayi1, sayi2)


#3)İki fonksiyon oluşturun. İki fonksiyon içinde de listeler olsun ilk fonksiyon içindeki listenin en büyük sayısını ikinci fonksiyon içindekilistenin en küçük sayısını toplayıp ekrana bastırın.

def enbuyuksayi(liste):
    return max(liste)

def enkucuksayi(liste):
    return min(liste)

liste1 = [10, 15, 20]
liste2 = [5, 100, 250]
#hocanın verdiği örnek listeler
en_buyuk = enbuyuksayi(liste1)
en_kucuk = enkucuksayi(liste2)

print(en_buyuk + en_kucuk)

#4)Bir fonksiyon oluşturun. Fonksiyon içinde bir tane liste olsun ve bu listenin ilk ve son sayısı eşitse ekrana true değilse false yazdırsın.

def ilkvesonsayiesit(liste):
    if len(liste) >= 2:
        if liste[0] == liste[-1]:#burlarında formulune intten baktım
            return True
    return False

# Örnek listeler
liste1 = [10, 20, 30, 50]
liste2 = [10, 20, 30, 10]

# İlk liste için kontrol
print(ilkvesonsayiesit(liste1))

# İkinci liste için kontrol
print(ilkvesonsayiesit(liste2))


#5)Bir sayının palindrom sayı olup olmadığını kontrol eden fonksiyonu yazınız.
#iki taraftanda okunuşu aynı sayilara polindrom denir
def palindrom_mu(sayi):
    sayi_str = str(sayi)
    tersi_str = sayi_str[::-1]

    if sayi_str == tersi_str:
        return True
    else:
        return False

def palindrom_kontrol(sayi):
    if palindrom_mu(sayi):
        print(sayi, "sayısı palindromdur")
    else:
        print(sayi, "sayısı palindrom değildir")

palindrom_kontrol(525)
palindrom_kontrol(124)
#hocanın verdiği örnekler

#6)Bir fonksiyon oluşturun. Fonksiyon içinde iki liste olsun ilk listenin çift sayılarını ikinci listenin tek sayılarını alıp yeni bir listeye ekleyin ve ekrana yazdırın.
def ciftveteksayilarbirleşecek(liste1, liste2):
    yeni_liste = []

    for num in liste1:
        if num % 2 == 0:
            yeni_liste.append(num)

    for num in liste2:
        if num % 2 != 0:
            yeni_liste.append(num)

    return yeni_liste

#hocanın verdiği örnekler
list1 = [10, 11, 12]
list2 = [13, 14, 15]

#yeni liste oluşturup ekrana böyle yazicaz
yeni_liste = ciftveteksayilarbirleşecek(list1, list2)
print("Yeni liste:", yeni_liste)

#7)Rus ruleti oyunu yazın. Random kütüphanesi kullanarak 1-6 arasında bir sayı seçilsin ve kullanıcıdan bir sayı alsın eşit olduğunda oyun biter.
import random

def rastgelesayi():
    return random.randint(1, 6)#şu randintide arastırdım

def rus_ruleti():
    rastgele_sayi = rastgelesayi()
    tahmin = int(input("tahmininizi girin (1-6 arası bir sayı gir): "))

    if tahmin == rastgele_sayi:
        print("ÖLDÜNNN!")
    else:
        print("Yaşadın!")

rus_ruleti()
#oyunu başlatıoz yukardakiyle
     
