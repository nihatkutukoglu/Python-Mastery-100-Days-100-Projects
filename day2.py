# -*- coding: utf-8 -*-
"""
Created on Mon Jun 30 20:37:31 2025

@author: user
"""


#  ---- Kişiselleştirilmiş Karşılama Programı

name = input("İsminiz nedir? ").strip().title()
age = int(input("Yaşınız kaç? "))
city = input("Hangi şehirde yaşıyorsunuz? ").strip().title()
color = input("Favori renginiz ne? ").strip().lower()
pet = input("Evcil hayvanınız var mı? (Evet/Hayır) ").strip().lower()
activity = input("Boş zamanlarınızda en çok ne yapmaktan hoşlanırsınız? ").strip().lower()

# Karşılama mesajını oluşturalım ve yazdıralım
print("\n--- Kişiselleştirilmiş Karşılama Programı ---")
print(f"Selamlar, {name} hoş geldin!")
print(f"Sen {age} yaşındasın ve {city} şehrinde yaşıyorsun. Ne güzel bir yer!")
print(f"Favori rengin {color.capitalize()}. Gerçekten de göz alıcı bir renk!")
print(f"Evcil hayvanın olup olmadığı hakkında '{pet}' dedin. Güzel!")
print(f"Boş zamanlarında {activity} yapmaktan hoşlanman harika! Keyifli vakit geçiriyorsundur umarım.")
print(f"Seninle tanıştığıma sevindim, {name}! Hadi beraber harika şeyler yapalım!")