# Bir tahmin veya danışma uygulamasının basit bir versiyonu
# Bu program, kullanıcının sorduğu soruya rastgele yanıtlar verir.
# Amaç: if-elif-else yapısı pratiği yapmak ve kullanıcıyla etkileşim kurmak.


import random     # Rastgele sayı üretmek için 'random' modülü içe aktarılır.

# Kullanıcıdan ismini alır.
isim = input('Adın nedir ? ')

# Kullanıcıyı karşılayan bir mesaj gösterilir.
print(f'Merhaba {isim}, hoşgeldin.')

# Sonsuz döngü: Kullanıcı çıkmak isteyene kadar devam eder.
while True:

    # Kullanıcıdan bir soru alınır.
 soru = input('Ne sormak istersin ? ')

    # 1 ile 25 arasında rastgele bir sayı seçilir.
 cevap=random.randint(1,25)

    # Rastgele sayıya göre bir cevap verilir.
 if cevap==1:
    print('Evet kesinlikle.')
 elif cevap==2:
    print('Bunun doğru bir şey olduğunu düşünmüyorum.')
 elif cevap==3:
    print('Doğru yoldasın! Böyle devam et.')
 elif cevap==4:
    print('Tekrar düşünmeye ne dersin.')
 elif cevap == 5:
    print('Kalbinin sesini dinlemeye ne dersin.')
 elif cevap == 6:
    print('Durumu bir uzmana danışmaya ne dersin.')
 elif cevap == 7:
    print('Bu konuda bir arkadaşından fikir almalısın.')
 elif cevap == 8:
    print('Geçmişte benzer bir olay yaşadıysan o zaman ne yaptığını düşün. ')
 elif cevap == 9:
    print('Her şeyin bir zamanı var.')
 elif cevap == 10:
    print('Hata yapmaktan korkma, çünkü hata yapmak insana özgüdür.')
 elif cevap == 11 :
    print('Hedefler büyük, sen daha büyüksün! Ama önce biraz kahkaha at.')
 elif cevap == 12 :
    print('Kahveni al, derin bir nefes çek ve ‘Ben bunu başarırım’ de.')
 elif cevap == 13 :
    print('Yapabilirsen, yap! Yapamazsan da en azından denemiş olursun, ikisi de kârdır.')
 elif cevap == 14 :
    print('Cevap evet ama ben seni sonradan ‘keşke yapmasaydım’ diye ağlarken görmek istemem.')
 elif cevap == 15 :
    print('Ben yapmam ama sen dene istersen :)')
 elif cevap == 16 :
    print('Sence de bu sorunun cevabını zaten bilmiyor musun?')
 elif cevap == 17 :
    print('Kafanı değil, kalbini dinle.')
 elif cevap == 18 :
    print('Bunu başarabileceğini biliyorum, sadece denemeye devam et!')
 elif cevap == 19 :
    print('Emin olmasan bile denemeye değer. Her büyük başarı, bir cesaret adımıyla başlar.')
 elif cevap == 20 :
    print('Sen zaten her şeyin üstesinden gelebilirsin! Sadece kendine inan.')
 elif cevap == 21 :
    print('Kendi kurallarını kendin yaz! Kimse senin gibi düşünemez.')
 elif cevap == 22 :
    print('Bugün zor gelse de, yarın bu anı hatırlayıp gülümseyeceksin.')
 elif cevap == 23 :
    print('Daha önce hiç denemediysen, şimdi tam zamanı!')
 elif cevap == 24 :
    print('Hata yapmaktan korkma, en azından iyi bir hikâyen olur.')
 else:
    print('Bu, senin için bir öğrenme fırsatı olabilir')

    # Kullanıcıya başka bir soru sormak isteyip istemediği sorulur.
 devam = input('Başka bir şey sormak ister misin ? (evet/hayır): ').lower()
 if devam == 'evet':
     print('Harika haber.')
 else:
     print('Görüşmek üzere, umarım doğru yolu bulursun.Kendine çok yüklenme tamam mı ? 👋')
     break    # Kullanıcı devam etmek istemiyorsa döngü sonlandırılır.
