# Gerekli kütüphaneleri içe aktarıyoruz.
# plyer kütüphanesinden 'notification' modülünü kullanacağız.
from plyer import notification
# time modülünü, bildirimler arasında bekleme yapmak için kullanacağız.
import time


def bildirim_gonder(baslik, mesaj, bekleme_suresi=5):
    try:
        # notification.notify() fonksiyonu, bildirimi gönderir.
        notification.notify(
            title=baslik,
            message=mesaj,
            app_name="Python Geri Bildirim Uygulaması",  # 'Phyton' yazım hatası düzeltildi.
            # app_icon="python_logo.ico", # Bu satır, projenin yanında bu isimde bir ikon dosyası gerektirir.
            timeout=bekleme_suresi  # Bildirimin ekranda kalacağı süre.
        )
        print(f"'{baslik}' başlıklı bildirim gönderildi.")
    except Exception as e:
        print(f"Bildirim gönderilirken bir hata oluştu: {e}")


# --- Ana Program Bloğu ---

if __name__ == "__main__":
    # Bu blok, dosya doğrudan çalıştırıldığında çalışır.

    print("Masaüstü bildirimleri başlıyor...")
    print("---------------------------------")

    # İlk bildirimi gönderelim.
    bildirim_gonder(
        baslik="Günlük Hatırlatma",
        mesaj="Yapılacaklar listeni kontrol etmeyi unutma!",
        bekleme_suresi=10  # Bu bildirim 10 saniye ekranda kalacak.
    )

    # 10 saniye bekleyelim, böylece ilk bildirimden sonra ikinci bir bildirim gönderilir.
    time.sleep(10)

    # İkinci bildirimi gönderelim.
    bildirim_gonder(
        baslik="Proje İpuçları",
        mesaj="Python'da yeni projeler için fikir üretmeye devam et!",
        bekleme_suresi=8  # Bu bildirim 8 saniye ekranda kalacak.
    )

    print("---------------------------------")
    print("Bildirim döngüsü tamamlandı.")
