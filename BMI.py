# import tkinter as tk
#
# window = tk.Tk()
# window.title("Vücut Kitle İndeksi (BMI) Hesaplayıcı")
# window.minsize(width=650, height=400)
# window.config(padx=20, pady=20)
#
# def hesapla_bmi():
#     try:
#         kilo = float(kilo_giris.get())
#         boy = float(boy_giris.get())
#
#         if kilo <= 0 or boy <= 0:
#             sonuc.config(text="Kilo ve boy sıfırdan büyük olmalı!", fg="red")
#             return
#
#         # Boyu santimetreden metreye çevir
#         boy_metre = boy / 100
#
#         bmi = kilo / (boy_metre ** 2)
#         result_message = ""
#
#         if bmi < 18.5:
#             result_message = "Zayıf"
#         elif 18.5 <= bmi < 24.9:
#             result_message = "Normal Kilolu"
#         elif 25 <= bmi < 29.9:
#             result_message = "Fazla Kilolu"
#         else:
#             result_message = "Obez"
#
#         sonuc.config(text=f"BMI Değeriniz: {bmi:.2f}\nDurumunuz: {result_message}", fg="blue")
#
#     except ValueError:
#         sonuc.config(text="Lütfen geçerli bir sayı girin!", fg="red")
#
# kilo_label = tk.Label(text="Kilonuzu girin (kg):", font=("arial", 15, "bold"))
# kilo_label.pack()
#
# kilo_giris = tk.Entry(width=15)
# kilo_giris.pack(pady=(0, 30))
#
#
# boy_label = tk.Label(text="Boyunuzu girin (cm):", font=("arial", 15, "bold"))
# boy_label.pack()
#
# boy_giris = tk.Entry(width=15)
# boy_giris.pack(pady=5)
#
#
# hesapla = tk.Button(text="Hesapla", font=("arial", 15, "bold"), command=hesapla_bmi)
# hesapla.pack(pady=30)
#
# sonuc = tk.Label(text="Sonuç Burada Gözükecektir.", font=("arial", 15, "bold"))
# sonuc.pack(pady=5)
#
# window.mainloop()