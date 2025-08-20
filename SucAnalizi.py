import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df= pd.read_csv("crime_safety_dataset.csv")
pd.set_option("display.max_rows", None)   # Tüm satırları göster
pd.set_option("display.width", None)      # Genişliği sınırsız yap
pd.set_option("display.max_colwidth", None) # Sütun içeriğini kesme
#
# # print(df.head(10))
#
# --- 1. En çok görülen suç türleri ---
suc_sayisi = df["crime_type"].value_counts()
print("\n En Çok Görülen Suç Türleri", suc_sayisi)

plt.figure(figsize=(8,5))
suc_sayisi.plot(kind="bar")
plt.title("En Çok Görülen Suç Türleri")
plt.ylabel("Suç Sayısı")
plt.xlabel("Suç Türü")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# --- 2. Hangi şehirlerde daha çok suç işlenmiş ---
sehir_suc_sayisi = df["city"].value_counts()
print("\nEn çok suç işlenen şehirler:\n", sehir_suc_sayisi)

plt.figure(figsize=(8,5))
sehir_suc_sayisi.head().plot(kind="bar")
plt.title("En Çok Suç İşlenen Şehirler")
plt.xlabel("Şehir")
plt.ylabel("Sayı")
plt.tight_layout()
plt.show()

# --- 3. Mağdurların yaş dağılımı ---
plt.figure(figsize=(10,6))
plt.hist(df['victim_age'], bins=25, color='green', edgecolor='black')
plt.title("Mağdur Yaş Dağılımı (Histogram)")
plt.xlabel("Yaş")
plt.ylabel("Kişi Sayısı")
plt.grid(True, linestyle='-', alpha=0.7)
plt.tight_layout()
plt.show()

# --- 4. Kadın/Erkek mağdur oranı ---
cinsiyet_sayisi = df['victim_gender'].value_counts()
print("\nMağdur cinsiyet dağılımı:\n", cinsiyet_sayisi)
plt.figure(figsize=(10,6))
plt.pie(cinsiyet_sayisi, labels=cinsiyet_sayisi.index , autopct='%1.1f%%', startangle=90, colors=['blue','pink','lightblue','gray'])
plt.title("Mağdur Cinsiyet Oranı")
plt.show()


# --- 5. Zaman (yıl) bazında suç dağılımı ---
df['date'] = pd.to_datetime(df['date'])
df['year'] = df['date'].dt.year
year_counts = df['year'].value_counts().sort_index()

plt.figure(figsize=(8,5))
plt.plot(year_counts.index, year_counts.values, marker='o', linestyle='-', color='purple')
plt.title("Yıllara Göre Suç Dağılımı")
plt.xlabel("Yıl")
plt.ylabel("Suç Sayısı")
plt.grid(True)
plt.show()

# --- 6. Suç Türü × Cinsiyet Analizi ---
suc_cinsiyet_analiz = pd.crosstab(df["crime_type"],df['victim_gender'])
print("\nSuç türü × Cinsiyet tablosu:\n", suc_cinsiyet_analiz)
suc_cinsiyet_analiz.plot(kind="bar",stacked=True, figsize=(12,6))
plt.title("Suç Türü × Cinsiyet Dağılımı (İlk 10 Suç Türü)")
plt.xlabel("Suç Türü")
plt.ylabel("Mağdur Sayısı")
plt.xticks(rotation=45, ha='right')
plt.legend(title="Cinsiyet")
plt.tight_layout()
plt.grid(True)
plt.show()


