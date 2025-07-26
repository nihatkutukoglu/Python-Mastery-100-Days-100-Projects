# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 12:10:21 2025

@author: user
"""

import requests 

API_KEY = "ee22787bb099a12fc06b5587235eda79" 

CITY_NAME = input("Şehir ismini giriniz")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

def get_weather(city_name):

    complete_url = f"{BASE_URL}q={city_name}&appid={API_KEY}&units=metric&lang=tr"

    try:
        response = requests.get(complete_url) # API'ye GET isteği gönder
        data = response.json() # Gelen JSON yanıtını Python sözlüğüne çevir

        if data["cod"] == 200:
            main_data = data["main"]
            weather_data = data["weather"][0] 

            temperature = main_data["temp"]
            feels_like = main_data["feels_like"]
            humidity = main_data["humidity"]
            description = weather_data["description"]
            city_display_name = data["name"] 

            print(f"\n--- {city_display_name} Hava Durumu ---")
            print(f"Sıcaklık: {temperature}°C")
            print(f"Hissedilen: {feels_like}°C")
            print(f"Nem Oranı: %{humidity}")
            print(f"Durum: {description.capitalize()}") 
            print("---------------------------\n")

        else:

            print(f"Hata: {data['message']}")
            print("Şehir bulunamadı veya API anahtarınız hatalı olabilir.")

    except requests.exceptions.ConnectionError:
        print("Bağlantı hatası oluştu. İnternet bağlantınızı kontrol edin.")
    except Exception as e:
        print(f"Beklenmedik bir hata oluştu: {e}")

# --- UYGULAMAYI ÇALIŞTIRMA ---
if __name__ == "__main__":
    print("Hava Durumu Uygulamasına Hoş Geldin!")
    print(f"Varsayılan şehir: {CITY_NAME}")

    while True:
        choice = input("Hava durumunu görmek için 'evet' yazın veya çıkmak için 'çıkış' yazın: ").lower()
        if choice == "evet":
            get_weather(CITY_NAME)
        elif choice == "çıkış":
            print("Uygulamadan çıkılıyor. Güle güle!")
            break
        else:
            print("Geçersiz seçim. Lütfen 'evet' veya 'çıkış' yazın.")
            
            
            
            
            
            
            
            
            