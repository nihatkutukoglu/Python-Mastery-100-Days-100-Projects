

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import sqlite3
import os
from datetime import date
import csv

# ----------------- Ayarlar -----------------
DB_NAME = os.path.join(os.path.expanduser("~"), "Desktop", "club_members.db")
ROLES = ("Üye", "Gönüllü", "Yönetim", "Başkan")
STATUSES = ("Aktif", "Pasif")

# ----------------- Veritabanı -----------------
def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute(
        """
        CREATE TABLE IF NOT EXISTS members (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_no TEXT NOT NULL UNIQUE,
            name TEXT NOT NULL,
            surname TEXT NOT NULL,
            email TEXT UNIQUE,
            phone TEXT,
            faculty TEXT,
            department TEXT,
            class_year INTEGER,
            role TEXT,
            status TEXT,
            join_date TEXT,
            consent INTEGER,
            notes TEXT
        )
        """
    )
    conn.commit()
    conn.close()


def fetch_members(search_term: str | None = None, status_filter: str | None = None, role_filter: str | None = None):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    sql = "SELECT id, student_no, name, surname, email, phone, faculty, department, class_year, role, status, join_date, consent FROM members"
    params = []
    clauses = []

    if search_term:
        like = f"%{search_term}%"
        clauses.append("(student_no LIKE ? OR name LIKE ? OR surname LIKE ? OR email LIKE ?)")
        params.extend([like, like, like, like])
    if status_filter and status_filter != "Hepsi":
        clauses.append("status = ?")
        params.append(status_filter)
    if role_filter and role_filter != "Hepsi":
        clauses.append("role = ?")
        params.append(role_filter)

    if clauses:
        sql += " WHERE " + " AND ".join(clauses)

    sql += " ORDER BY id DESC"
    c.execute(sql, params)
    rows = c.fetchall()
    conn.close()
    return rows


def insert_member(**kw):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    try:
        c.execute(
            """
            INSERT INTO members
            (student_no, name, surname, email, phone, faculty, department, class_year, role, status, join_date, consent, notes)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                kw.get("student_no"), kw.get("name"), kw.get("surname"), kw.get("email"),
                kw.get("phone"), kw.get("faculty"), kw.get("department"), kw.get("class_year"),
                kw.get("role"), kw.get("status"), kw.get("join_date"), kw.get("consent"), kw.get("notes"),
            ),
        )
        conn.commit()
        return c.lastrowid
    finally:
        conn.close()


def update_member(member_id: int, **kw):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute(
        """
        UPDATE members SET
            student_no=?, name=?, surname=?, email=?, phone=?, faculty=?, department=?,
            class_year=?, role=?, status=?, join_date=?, consent=?, notes=?
        WHERE id=?
        """,
        (
            kw.get("student_no"), kw.get("name"), kw.get("surname"), kw.get("email"), kw.get("phone"),
            kw.get("faculty"), kw.get("department"), kw.get("class_year"), kw.get("role"), kw.get("status"),
            kw.get("join_date"), kw.get("consent"), kw.get("notes"), member_id,
        ),
    )
    conn.commit()
    conn.close()


def delete_member(member_id: int):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("DELETE FROM members WHERE id=?", (member_id,))
    conn.commit()
    conn.close()


# ----------------- GUI -----------------
class ClubApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Topluluk Üye Kayıt - SQLite")
        self.geometry("1100x650")

        # ---- Menü ----
        menubar = tk.Menu(self)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="CSV Dışa Aktar", command=self.export_csv)
        file_menu.add_separator()
        file_menu.add_command(label="Çıkış", command=self.quit)
        menubar.add_cascade(label="Dosya", menu=file_menu)
        self.config(menu=menubar)

        # ---- Form ----
        form = ttk.LabelFrame(self, text="Üye Bilgileri")
        form.pack(fill="x", padx=10, pady=8)

        # Satır 1: Öğrenci No, Ad, Soyad, Sınıf
        ttk.Label(form, text="Öğrenci No:").grid(row=0, column=0, sticky="w", padx=6, pady=6)
        self.v_student_no = tk.StringVar()
        ttk.Entry(form, textvariable=self.v_student_no).grid(row=0, column=1, sticky="ew", padx=6, pady=6)

        ttk.Label(form, text="Ad:").grid(row=0, column=2, sticky="w", padx=6, pady=6)
        self.v_name = tk.StringVar()
        ttk.Entry(form, textvariable=self.v_name).grid(row=0, column=3, sticky="ew", padx=6, pady=6)

        ttk.Label(form, text="Soyad:").grid(row=0, column=4, sticky="w", padx=6, pady=6)
        self.v_surname = tk.StringVar()
        ttk.Entry(form, textvariable=self.v_surname).grid(row=0, column=5, sticky="ew", padx=6, pady=6)

        ttk.Label(form, text="Sınıf:").grid(row=0, column=6, sticky="w", padx=6, pady=6)
        self.v_class_year = tk.StringVar()
        ttk.Entry(form, textvariable=self.v_class_year, width=6).grid(row=0, column=7, sticky="w", padx=6, pady=6)

        # Satır 2: E-posta, Telefon, Fakülte, Bölüm
        ttk.Label(form, text="E-posta:").grid(row=1, column=0, sticky="w", padx=6, pady=6)
        self.v_email = tk.StringVar()
        ttk.Entry(form, textvariable=self.v_email).grid(row=1, column=1, sticky="ew", padx=6, pady=6)

        ttk.Label(form, text="Telefon:").grid(row=1, column=2, sticky="w", padx=6, pady=6)
        self.v_phone = tk.StringVar()
        ttk.Entry(form, textvariable=self.v_phone).grid(row=1, column=3, sticky="ew", padx=6, pady=6)

        ttk.Label(form, text="Fakülte:").grid(row=1, column=4, sticky="w", padx=6, pady=6)
        self.v_faculty = tk.StringVar()
        ttk.Entry(form, textvariable=self.v_faculty).grid(row=1, column=5, sticky="ew", padx=6, pady=6)

        ttk.Label(form, text="Bölüm:").grid(row=1, column=6, sticky="w", padx=6, pady=6)
        self.v_department = tk.StringVar()
        ttk.Entry(form, textvariable=self.v_department).grid(row=1, column=7, sticky="ew", padx=6, pady=6)

        # Satır 3: Rol, Durum, Katılım Tarihi, KVKK
        ttk.Label(form, text="Rol:").grid(row=2, column=0, sticky="w", padx=6, pady=6)
        self.v_role = tk.StringVar(value=ROLES[0])
        ttk.Combobox(form, textvariable=self.v_role, values=("Üye","Gönüllü","Yönetim","Başkan"), state="readonly").grid(row=2, column=1, sticky="ew", padx=6, pady=6)

        ttk.Label(form, text="Durum:").grid(row=2, column=2, sticky="w", padx=6, pady=6)
        self.v_status = tk.StringVar(value=STATUSES[0])
        ttk.Combobox(form, textvariable=self.v_status, values=("Aktif","Pasif"), state="readonly").grid(row=2, column=3, sticky="ew", padx=6, pady=6)

        ttk.Label(form, text="Katılım Tarihi (YYYY-MM-DD):").grid(row=2, column=4, sticky="w", padx=6, pady=6)
        self.v_join_date = tk.StringVar()
        ttk.Entry(form, textvariable=self.v_join_date).grid(row=2, column=5, sticky="ew", padx=6, pady=6)

        self.v_consent = tk.IntVar(value=0)
        ttk.Checkbutton(form, text="KVKK Onayı Alındı", variable=self.v_consent).grid(row=2, column=6, columnspan=2, sticky="w", padx=6, pady=6)

        # Satır 4: Notlar (çok satırlı)
        ttk.Label(form, text="Notlar:").grid(row=3, column=0, sticky="nw", padx=6, pady=6)
        self.txt_notes = tk.Text(form, height=3)
        self.txt_notes.grid(row=3, column=1, columnspan=7, sticky="ew", padx=6, pady=6)

        # Form esneme
        for col in (1,3,5,7):
            form.columnconfigure(col, weight=1)

        # Butonlar
        btns = ttk.Frame(self)
        btns.pack(fill="x", padx=10)
        ttk.Button(btns, text="Ekle", command=self.add_member).pack(side="left", padx=4, pady=6)
        ttk.Button(btns, text="Güncelle", command=self.update_selected).pack(side="left", padx=4, pady=6)
        ttk.Button(btns, text="Sil", command=self.delete_selected).pack(side="left", padx=4, pady=6)
        ttk.Button(btns, text="Temizle", command=self.clear_form).pack(side="left", padx=4, pady=6)

        # ---- Filtre/Arama ----
        filt = ttk.LabelFrame(self, text="Arama / Filtre")
        filt.pack(fill="x", padx=10, pady=8)
        ttk.Label(filt, text="Ara (No/Ad/Soyad/E-posta):").pack(side="left", padx=(8,4))
        self.v_search = tk.StringVar()
        ttk.Entry(filt, textvariable=self.v_search, width=30).pack(side="left", padx=(0,8))

        ttk.Label(filt, text="Durum:").pack(side="left")
        self.v_status_filter = tk.StringVar(value="Hepsi")
        ttk.Combobox(filt, textvariable=self.v_status_filter, values=("Hepsi",)+STATUSES, state="readonly", width=10).pack(side="left", padx=4)

        ttk.Label(filt, text="Rol:").pack(side="left")
        self.v_role_filter = tk.StringVar(value="Hepsi")
        ttk.Combobox(filt, textvariable=self.v_role_filter, values=("Hepsi",)+ROLES, state="readonly", width=12).pack(side="left", padx=4)

        ttk.Button(filt, text="Uygula", command=self.populate_tree).pack(side="left", padx=8)
        ttk.Button(filt, text="Sıfırla", command=self.reset_filters).pack(side="left")

        # ---- Liste ----
        columns = ("id","student_no","name","surname","email","phone","faculty","department","class_year","role","status","join_date","consent")
        self.tree = ttk.Treeview(self, columns=columns, show="headings")
        headers = {
            "id":"ID","student_no":"Öğrenci No","name":"Ad","surname":"Soyad","email":"E-posta","phone":"Telefon",
            "faculty":"Fakülte","department":"Bölüm","class_year":"Sınıf","role":"Rol","status":"Durum","join_date":"Katılım","consent":"KVKK"
        }
        for col in columns:
            self.tree.heading(col, text=headers[col])
        self.tree.column("id", width=50, anchor="center")
        self.tree.column("student_no", width=110)
        self.tree.column("name", width=110)
        self.tree.column("surname", width=110)
        self.tree.column("email", width=170)
        self.tree.column("phone", width=110)
        self.tree.column("faculty", width=120)
        self.tree.column("department", width=150)
        self.tree.column("class_year", width=60, anchor="e")
        self.tree.column("role", width=90)
        self.tree.column("status", width=80)
        self.tree.column("join_date", width=100)
        self.tree.column("consent", width=60, anchor="center")
        self.tree.pack(fill="both", expand=True, padx=10, pady=(0,10))

        vsb = ttk.Scrollbar(self.tree, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)
        vsb.pack(side="right", fill="y")

        self.tree.bind('<<TreeviewSelect>>', self.on_select)

        # İlk yükleme
        self.populate_tree()

        # Seçili kayıt ID
        self.selected_id = None

    # ---- Yardımcılar ----
    def current_form_data(self):
        jd = self.v_join_date.get().strip() or date.today().strftime("%Y-%m-%d")
        notes = self.txt_notes.get("1.0", tk.END).strip()
        cy = self.v_class_year.get().strip()
        cy_val = int(cy) if cy.isdigit() else None
        return dict(
            student_no=self.v_student_no.get().strip(),
            name=self.v_name.get().strip(),
            surname=self.v_surname.get().strip(),
            email=self.v_email.get().strip() or None,
            phone=self.v_phone.get().strip() or None,
            faculty=self.v_faculty.get().strip() or None,
            department=self.v_department.get().strip() or None,
            class_year=cy_val,
            role=self.v_role.get(),
            status=self.v_status.get(),
            join_date=jd,
            consent=int(self.v_consent.get()),
            notes=notes or None,
        )

    def validate_required(self, data: dict):
        if not data["student_no"]:
            messagebox.showwarning("Uyarı", "Öğrenci No zorunludur.")
            return False
        if not data["name"] or not data["surname"]:
            messagebox.showwarning("Uyarı", "Ad ve Soyad zorunludur.")
            return False
        return True

    def populate_tree(self):
        # Filtreler ve arama
        term = self.v_search.get().strip()
        st_filter = self.v_status_filter.get()
        rl_filter = self.v_role_filter.get()

        for r in self.tree.get_children():
            self.tree.delete(r)
        rows = fetch_members(term or None, st_filter, rl_filter)
        for row in rows:
            # consent 0/1 => E/H göster
            row = list(row)
            row[-1] = "E" if row[-1] else "H"
            self.tree.insert('', tk.END, values=row)

    def reset_filters(self):
        self.v_search.set("")
        self.v_status_filter.set("Hepsi")
        self.v_role_filter.set("Hepsi")
        self.populate_tree()

    def add_member(self):
        data = self.current_form_data()
        if not self.validate_required(data):
            return
        try:
            insert_member(**data)
            messagebox.showinfo("Başarılı", "Üye eklendi.")
            self.clear_form()
            self.populate_tree()
        except sqlite3.IntegrityError as e:
            msg = str(e)
            if "student_no" in msg:
                messagebox.showerror("Hata", "Bu Öğrenci No zaten kayıtlı.")
            elif "email" in msg:
                messagebox.showerror("Hata", "Bu e-posta zaten kayıtlı.")
            else:
                messagebox.showerror("Hata", f"Tekrarlı veri: {e}")
        except Exception as e:
            messagebox.showerror("Hata", f"Üye eklenemedi: {e}")

    def on_select(self, _):
        sel = self.tree.selection()
        if not sel:
            return
        vals = self.tree.item(sel[0], 'values')
        # id, student_no, name, surname, email, phone, faculty, department, class_year, role, status, join_date, consent
        self.selected_id = int(vals[0])
        self.v_student_no.set(vals[1])
        self.v_name.set(vals[2])
        self.v_surname.set(vals[3])
        self.v_email.set(vals[4] if vals[4] != 'None' else '')
        self.v_phone.set(vals[5] if vals[5] != 'None' else '')
        self.v_faculty.set(vals[6] if vals[6] != 'None' else '')
        self.v_department.set(vals[7] if vals[7] != 'None' else '')
        self.v_class_year.set(str(vals[8]) if vals[8] not in (None, 'None') else '')
        self.v_role.set(vals[9])
        self.v_status.set(vals[10])
        self.v_join_date.set(vals[11] if vals[11] != 'None' else '')
        self.v_consent.set(1 if vals[12] == 'E' else 0)
        # Notlar Treeview'da yok; düzenlemek için veritabanından çekmek gerekir (isteğe bağlı).

    def update_selected(self):
        if not self.selected_id:
            messagebox.showwarning("Uyarı", "Güncellemek için bir kayıt seçin.")
            return
        data = self.current_form_data()
        if not self.validate_required(data):
            return
        try:
            update_member(self.selected_id, **data)
            messagebox.showinfo("Başarılı", "Kayıt güncellendi.")
            self.clear_form()
            self.populate_tree()
        except sqlite3.IntegrityError as e:
            msg = str(e)
            if "student_no" in msg:
                messagebox.showerror("Hata", "Bu Öğrenci No zaten kayıtlı.")
            elif "email" in msg:
                messagebox.showerror("Hata", "Bu e-posta zaten kayıtlı.")
            else:
                messagebox.showerror("Hata", f"Tekrarlı veri: {e}")
        except Exception as e:
            messagebox.showerror("Hata", f"Güncelleme hatası: {e}")

    def delete_selected(self):
        if not self.selected_id:
            messagebox.showwarning("Uyarı", "Silmek için bir kayıt seçin.")
            return
        if not messagebox.askyesno("Onay", "Seçili üyeyi silmek istediğinize emin misiniz?"):
            return
        try:
            delete_member(self.selected_id)
            messagebox.showinfo("Başarılı", "Kayıt silindi.")
            self.clear_form()
            self.populate_tree()
        except Exception as e:
            messagebox.showerror("Hata", f"Silme hatası: {e}")

    def clear_form(self):
        self.selected_id = None
        self.v_student_no.set("")
        self.v_name.set("")
        self.v_surname.set("")
        self.v_email.set("")
        self.v_phone.set("")
        self.v_faculty.set("")
        self.v_department.set("")
        self.v_class_year.set("")
        self.v_role.set(ROLES[0])
        self.v_status.set(STATUSES[0])
        self.v_join_date.set("")
        self.v_consent.set(0)
        self.txt_notes.delete("1.0", tk.END)
        for sel in self.tree.selection():
            self.tree.selection_remove(sel)

    def export_csv(self):
        path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV", "*.csv")], initialfile="uyeler.csv")
        if not path:
            return
        rows = fetch_members(self.v_search.get().strip() or None, self.v_status_filter.get(), self.v_role_filter.get())
        try:
            with open(path, "w", newline="", encoding="utf-8") as f:
                w = csv.writer(f)
                w.writerow(["id","student_no","name","surname","email","phone","faculty","department","class_year","role","status","join_date","consent","notes"])
                # Notları ayrıca çekmek gerekebilir; basitlik için consent ile sınırlı tuttuk.
                # İsterseniz burada JOIN ile notes da eklenebilir.
                for r in rows:
                    w.writerow(list(r) + [None])
            messagebox.showinfo("Tamam", "CSV dosyası kaydedildi.")
        except Exception as e:
            messagebox.showerror("Hata", f"CSV kaydedilemedi: {e}")


if __name__ == "__main__":
    init_db()
    app = ClubApp()
    app.mainloop()

