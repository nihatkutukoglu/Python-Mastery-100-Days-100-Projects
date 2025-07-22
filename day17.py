# -*- coding: utf-8 -*-
"""
Created on Mon Jul 21 11:35:48 2025

@author: user
"""

# ----- Gün 17 Projesi : Öğrenci Raporu ----

import csv

def ogrenci_veri_isleme(girdi_dosyasi, cikti_dosyasi):
    try:
        ogrenci_raporlari = []

        with open(girdi_dosyasi, 'r', newline='', encoding='utf-8') as girdidosyasi:
            okuyucu = csv.DictReader(girdidosyasi)

            for row in okuyucu:
                ad = row['Name']
                matematik = int(row['Math'])
                fen = int(row['Science'])
                ingilizce = int(row['English'])

                ortalama = round((matematik + fen + ingilizce) / 3, 2)

                durum = "Geçti" if ortalama >= 60 else "Kaldı"

                ogrenci_raporlari.append({
                    'Name': ad,
                    'Math': matematik,
                    'Science': fen,
                    'English': ingilizce,
                    'Average': ortalama,
                    'Status': durum
                })

        with open(cikti_dosyasi, 'w', newline='', encoding='utf-8') as ciktidosyasi:
            sutun_adlari = ['Name', 'Math', 'Science', 'English', 'Average', 'Status']
            yazici = csv.DictWriter(ciktidosyasi, fieldnames=sutun_adlari)

            yazici.writeheader()
            yazici.writerows(ogrenci_raporlari)

        print(f"Öğrenci raporu '{cikti_dosyasi}' dosyasına başarıyla oluşturuldu.")

    except FileNotFoundError:
        print(f"Hata: '{girdi_dosyasi}' dosyası bulunamadı.")
    except KeyError:
        print("Hata: Girdi dosyasındaki sütun adları geçersiz. Lütfen 'Name', 'Math', 'Science', 'English' sütunlarının doğru olduğundan emin olun.")
    except Exception as e:
        print(f"Beklenmeyen bir hata oluştu: {e}")

girdi_dosyasi_adi = 'students.csv'
cikti_dosyasi_adi = 'student_report.csv'

ogrenci_veri_isleme(girdi_dosyasi_adi, cikti_dosyasi_adi)

                
                
                
                
                
                
                
                
                
                
                