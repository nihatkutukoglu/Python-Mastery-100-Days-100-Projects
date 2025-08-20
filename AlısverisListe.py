# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox

class AlisverisListesi:
    def __init__(self, pencere):
        self.pencere = pencere
        self.pencere.title("Alışveriş Listesi")
        self.pencere.geometry("400x350")

        self.liste = []

        baslik = tk.Label(pencere, text="🛒 Alışveriş Listesi", font=("Arial", 14, "bold"))
        baslik.pack(pady=10)

        self.liste_kutusu = tk.Listbox(pencere, font=("Arial", 11))
        self.liste_kutusu.pack(fill="both", expand=True, padx=10, pady=5)

        self.giris = tk.Entry(pencere, font=("Arial", 11))
        self.giris.pack(fill="x", padx=10, pady=5)

        ekle_btn = tk.Button(pencere, text="Ekle", command=self.oge_ekle)
        ekle_btn.pack(side="left", padx=10, pady=5)

        sil_btn = tk.Button(pencere, text="Seçileni Sil", command=self.oge_sil)
        sil_btn.pack(side="left", padx=5, pady=5)

        temizle_btn = tk.Button(pencere, text="Listeyi Temizle", command=self.liste_temizle)
        temizle_btn.pack(side="left", padx=5, pady=5)

        cikis_btn = tk.Button(pencere, text="Çıkış", command=pencere.destroy)
        cikis_btn.pack(side="right", padx=10, pady=5)

    def oge_ekle(self):
        oge = self.giris.get().strip()
        if not oge:
            messagebox.showwarning("Uyarı", "Lütfen ürün adı girin.")
            return
        self.liste.append(oge)
        self.liste_kutusu.insert(tk.END, oge)
        self.giris.delete(0, tk.END)

    def oge_sil(self):
        secilen = self.liste_kutusu.curselection()
        if not secilen:
            messagebox.showinfo("Bilgi", "Silmek için ürün seçin.")
            return
        index = secilen[0]
        self.liste.pop(index)
        self.liste_kutusu.delete(index)

    def liste_temizle(self):
        if not self.liste:
            return
        if messagebox.askyesno("Onay", "Listeyi tamamen temizlemek istiyor musunuz?"):
            self.liste.clear()
            self.liste_kutusu.delete(0, tk.END)

if __name__ == "__main__":
    pencere = tk.Tk()
    uygulama = AlisverisListesi(pencere)
    pencere.mainloop()
