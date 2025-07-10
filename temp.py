# # -*- coding: utf-8 -*-
# """
# Spyder Editor

# This is a temporary script file.
# """
#   # print("hello world")

# # input("isminiz nedir")
# # input("Soyadınız nedir")

# #  değişkenler ve sabitler
# # isim,soyisim = "Niggat","Kütük"  #Böylede yapılabilir 
# # isim = "Nihat"
# # soyisim = "kütükoğlu"

# # print(soyisim) 
# # PI=3.14 # Sabit atama büyük harflerle yapılır.
# # Değişken sayıyla başlayamaz. 
# # Türkçe karakter kullanma

# VERİ TİPLERİ (DATA TYPES) 
# Numbers 

# yas = 20 
# print(yas)
# print(5+7)
# print(40 % 7 ) # Kalan bulma 
# print(4**4) # Karesini alma 
# print(40/6) # Bölme
# print(40//6) #Kalansız bölme
# print(round(4.56)) # Yuvarlama 

#   String  - Karakter dizileri
# print("nihat
#       edkadşk
#       akodps
#       sdkpa
#       akpsdi")
     
# print("""nihat
#       edkadşk
#       akodps
#       akpsdi
#       ddsdsadsda""")
#       # Çoklu satırlı yazarsak 3 tırnak kullanacağız. 

# isim = "Nihat"
# print(isim[0]) 
# print(isim[0:3]) # 1. karakterden 3. karaktere kadar

#   # METOTLAR #
# l # \n aşağı satır yapar
# print("nihat" " " * 9) # 9 tane nihat yazar
# print("nihat".upper()) # Bütün harfleri büyütür
# print("NİHATTTTTTT".lower()) # Harfleri küçültür. 
# print("nihat".capitalize()) # İlk harfi büyültür. 
# isim = "nnnihat"
# print(isim.count("n")) # İçinde kaç tane var 
# tweet = "Bu heykel Yozgat'a dikilse tanımadıkları için hoca falan sanarlar, bir şey olmaz yani"
# print(tweet.find("heykel")) 

# isim= "   Nihat can    "
# soyisim= "Kütük"
# print(isim.lstrip()) # Soldaki boşluğu sildi
# print(isim.rstrip()) # sağdaki boşluğu sildi 
# print(isim.strip()) # iki taraftaki boşluğu sildi 
# print(isim.replace("can", "kütükoğlu")) # Değiştirme işlemi yaptı 
# print(f"Benim ismim {isim} soyismim {soyisim}")

# #####  BOOLEAN VERİ TİPİ ###### true false
# print(5>4) 

# # LİSTE VERİ TPİ ###
# insan = ("nihat" ,31, "kütük","pc","tv",37,78,"kastamonu" )
# insanlist = list(insan)
# print(insanlist[0:3]) # 0.cı elemanı verir 
# insanlist[0]= "nicat" // #1. elemanı nicat yaptı. Nihatı değştirdi
# insanlist.append("TÜRK") # EKLEME YAPAR 
# print(insanlist)

# insanlar = (["nihat","memet","amed"] , ["ayşe","fatma","ela"] , [17,22,23])
# insanlarlistesi = list(insanlar)
# # print(insanlarlistesi[0][1]) # 0. listenin 1. indeksteki üyesini verir.
# insanlarlistesi[0][2] = "ahmet" # değiştirdik
# # print(insanlarlistesi)
# # len(insanlar) # uzunluk ölçme 

# # LİSTELERİN METOTLARI ## 
# sayılar = {1,2,3,4,5,6,7,8,9} 
# sayılist = list(sayılar) #bu şekilde list atıyoruz. 
# # print(len(sayılist))
# sayılist.append(1000)# EKLEME YAPTI 
# print(sayılist) 
# sayılist.remove(9) # 9u kaldırdık 
# print(sayılist) 
# sayılist.pop() # son elemanı siler
# print(sayılist) 

# sayıkopyası = sayılar.copy() # Kopyalama işlemi yapıldı 
# print(sayıkopyası)
# a = 1,2,3,4
# b= 4,5,6,7,8
# alist= list(a)
# blist = list(b)
# print(alist.extend(blist)) # birleştirme işlemi yaptık.
# print(alist) 
# # print(alist.count(4)) # kaç defa geçtiğini anlarız 2 defa geçiyor
# alist.insert(0,"nihat") # 0. indekse nihat ekledik.
# print(alist)

# g = 3,5,8,22,31,100,2,69
# glist= list(g)
# glist.sort() # listeyi küçükte büyüğe sıraladı. 
# print(glist)
# glist.sort(reverse = True) # tam tersini yaptı 
# print(glist)


# /// Sep Perametresi /// 
# sep parametresi, Python'da print() fonksiyonunda kullanılan ve 
# çıktıda kullanılan ayırıcıyı belirleyen bir parametredir. 
# Varsayılan olarak, print() fonksiyonu argümanlar arasına boşluk koyar.
# sep parametresi sayesinde bu ayırıcıyı değiştirebilirsiniz.

# print("Python", "SQL", "Veritabanı", sep=" ----")
# print("Python", "SQL", "Veritabanı", sep=" - ")


# # ////// FORMAT /////// 
# # ad = "Ali"
# # yas = 30
# # mesaj = "Benim adım {} ve ben {} yaşındayım.".format(ad, yas)
# # print(mesaj)

# # ad = "Ayşe"
# # yas = 25
# # mesaj = f"Benim adım {ad} ve ben {yas} yaşındayım."
# # print(mesaj)

# # //// SÖZLÜKLER //// 
# # // kimliktekiler elle değiştirilemez. yani ismi değiştiremezsiniz. 
# # Değiştirme kod ile yapılabilir.

# kimlik = {
#     "isim" : "Nihat",
#     "soyisim" :"kütükoğlu",
#     "tc_no" :"1013728428",
#     "sehir" : "bandırma"
    
    
#     } 

# # kimlik["isim"]= "mehmet" #// Değiştirme işlemi 
# # kimlik["yıl"]= "1993" #// Yıl eklendi. 

# # print(kimlik["isim"]) #// kimlikten ismi yazdırdı. 

# # print(kimlik) 

# kimlik = {
#     "isim" : "Nihat",
#     "soyisim" :"kütükoğlu",
#     "tc_no" :"1013728428",
#     "sehir" : "bandırma",
#     "ek bilgiler" : {
#         "email" : "asdas@gmail.com",
#         "kardeş sayısı" : 1 
#         }
    
#     } 
# # print(kimlik)


# # ////// Sözlükler (METOD) ////////////
# # print(kimlik.keys()) #SONUÇ AŞAĞIDA
# # dict_keys(['isim', 'soyisim', 'tc_no', 'sehir', 'ek bilgiler'])
# # print(kimlik.values()) /// sadece valuesleri verir. 
# # print(kimlik.get("sehir")) // Sehir bilgisini getirdi 
# # kimlik.update({"anne_adi":"fatma"}) // Anne adı ekledi. 
# # kimlik.pop("anne_adi") // Anne adini sildi. 
# # print(kimlik) 
# # kimlik.clear() // # Bütün kimlik elemanlarını siler. 


# # /////// DEMETLER //////////
# # demetler (tuples), listelere benzeyen,
# # değiştirilemeyen (immutable) veri yapılarıdır. 
# # Demetler, verilerin değiştirilmeyeceği durumlarda kullanışlıdır.

# # demet = ("elma", "armut", "muz")
# # print(demet[0])  # Çıktı: elma
# # print(demet[2])  # Çıktı: muz
# # print(demet.index("elma")) 
# # (demet[0]) = "MAMA " #// Demet DEĞİŞTİRİLEMEZ. 


# # //////////// KÜMELER /////////////////
# # Python'da kümeler, değiştirilebilir (mutable) ve 
# # düzensiz (unordered) veri yapılarıdır. Yani İNDEKSLEME YAPILAMAZ.
# # Kümelerin içinde tekrar eden elemanlar bulunamaz ve 
# # her eleman benzersizdir.

# # sayi = {1,2,5,7,7,19,82,26}
# # print(sayi)
# # sayi.add(100) #// 100 ekledik. 
# # sayi.discard(7) # 7'yi sildik. 

# # Kümelerde birleştirme işlemi : 
# # yeni = {11,21,31,82,26} # birleştirme işlemi yaptık. 
# # #Aynı olanları tekrar yazmadık 
# # sayi.update(yeni)
# # print(sayi)

# # a = {1,2,3,4,5,6}
# # b = {4,5,6,7,8}

# # a.difference(b) # a'nin b'den farkı nedir. 
# # a.intersection(b) / a'nin b ile kesişimi 

# # a= 9.9 

# # c = int(a)

# # b= 5.7
# # d=int(b)

# # print(c+d)

# # //// SETS

# # Mylist = [10, 20, 30, 40, 50, 60, 70, 70, 50, 40]
# # print(len(Mylist))
# # MySet = set(Mylist)
# # # print(MySet)

# # myset1= [10,15,20,25,30]
# # myset2=set(myset1)
# # # print(myset2)

# # MySet.union(myset2) 
# # MySet.intersection(myset2)


# # countryList = ["tr","fr","gr","tr","tr","gr","gr","hun","rus"]
# # print(len(countryList))
# # print(len(set(countryList))) # Kaç ülkeye satış yapmışız anlamışısız.

# # /////////// FARKLI OLUŞTURMALAR 


# # emptySet = {}
# # emptySet = set()

# # emptySet.add(10)
# # emptySet.add(20)
# # emptySet.add(20)
# # emptySet.add(30)

# # print(emptySet)


# # emptylist = list()

# # emptylist.append(10)
# # emptylist.append(10)
# # emptylist.append(15)

# # print(emptylist)


# # //////// QUİZ 
# # 1) Asagidaki string'in 5. harfini bir degiskene atayiniz

# # my_string = "Python Ogreniyorum" 
# # Degiskenquiz = my_string[5]
# # print(Degiskenquiz) 

# # 2) Asagidaki String'in 
# # 5. ve 8. karakteri arasindaki tum harflerini yazdiriniz (5 ve 8 dahil)

# # my_new_string = "ProgramlamayaMerhabaDedik"
# # print(my_new_string[4:8])



# # 3) Asagidaki String'i kod ile tersten yazin

# # my_last_string = "Afyonkarahisarlilastiramadiklarimizdanmisiniz"
# # print(my_last_string[::-1])



# # 4) Asagidaki islemin sonucu hangi veri tipinde olacaktir?

# # 4 + 12.2 + 48
# # print(type(4 + 12.2 + 48))

# # 5) Asagidaki islemin sonucu kactir?


# # 6) Bu listeyi en az 2 farkli yoldan olusturunuz: [1,3,"a"]

# # a = (1,3,"a")

# # alist = list(a)

# # print (alist)

# # # veya 

# # a = list()
# # a.append(1)
# # a.append(3)
# # a.append("a")

# # print (a)



# # 7) Asagidaki "b"'yi tek satirda aliniz:
# # my_list = [3.14,4,[2,3,"b"],True]

# # print(my_list[2][2]) 



# # 8) Asagidaki "a"'yi tek satirda aliniz:
# # my_dictionary = {"key1":20.25, "kk2":[40,{"k21":"a"}]}

# # print(my_dictionary["kk2"][1]["k21"])


# # 9) Asagidaki liste set'e cevirilince hangi degerler icinde kalacaktir?
# # my_list_to_be_set = [3,4,9,3,21,22,4,3,9,10,21,22]



# # print(set(my_list_to_be_set))

nickname = "nihat"
password = "123123123"

ad = input("İsminizi giriniz")
sifre = input("şifrenizi giriniz")

if ad == nickname and sifre == password :
    print("hoşgeldiniz")
    
else :
    print("hatalı giriş ")









