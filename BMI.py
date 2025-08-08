import tkinter as tk


def calculate_bmi():

        weight_kg = float(weight_entry.get())
        height_cm = float(height_entry.get())

        height_m = height_cm / 100

        bmi = weight_kg / (height_m ** 2)



        if bmi < 18.5:
            result_text = "Zayıf"
        elif 18.5 <= bmi < 25:
            result_text = "Normal"
        elif 25 <= bmi < 30:
            result_text = "Fazla Kilolu"
        else:
            result_text = "Obez"

        result_label.config(text=f"Vücut Kitle İndeksiniz: {bmi:.2f}\nDurumunuz: {result_text}")





window = tk.Tk()
window.title("BMI Hesaplayıcı")
window.geometry("350x250")
window.config(padx=20, pady=20)


height_label = tk.Label(window, text="Boyunuz (cm):")
height_label.pack()

height_entry = tk.Entry(window)
height_entry.pack()

weight_label = tk.Label(window, text="Kilonuz (kg):")
weight_label.pack()

weight_entry = tk.Entry(window)
weight_entry.pack()


calculate_button = tk.Button(window, text="Hesapla", command=calculate_bmi)
calculate_button.pack(pady=10)


result_label = tk.Label(window, text="Sonuç burada görünecek.", font=("Arial", 12))
result_label.pack()


window.mainloop()