import tkinter as tk
from tkinter import ttk, messagebox

# ---------------------------------------------------------------
# Palet warna (satu tempat supaya tampilan konsisten)
# ---------------------------------------------------------------
WARNA_BG = "#EAF1F8"        # latar jendela
WARNA_HEADER = "#1F4E79"    # biru tua: header & tombol Simpan
WARNA_HEADER_HOVER = "#173B5C"
WARNA_KARTU = "#FFFFFF"     # latar kotak formulir & hasil
WARNA_TEKS = "#1B2A3A"
WARNA_TEKS_PUDAR = "#5B6B7C"
WARNA_GARIS = "#B8C7D9"
WARNA_RESET = "#E8A317"     # kuning: tombol Reset
WARNA_RESET_HOVER = "#C98A0B"
WARNA_KELUAR = "#C0392B"    # merah: tombol Keluar
WARNA_KELUAR_HOVER = "#992D22"

# ---------------------------------------------------------------
# Font
# ---------------------------------------------------------------
FONT_JUDUL = ("Arial", 16, "bold")
FONT_SUBJUDUL = ("Arial", 10)
FONT_LABEL = ("Arial", 11)
FONT_INPUT = ("Arial", 11)
FONT_TOMBOL = ("Arial", 11, "bold")
FONT_HASIL_JUDUL = ("Arial", 11, "bold")
FONT_HASIL = ("Arial", 11)

PROGRAM_STUDI = [
    "Teknik Informatika",
    "Sistem Informasi",
    "Manajemen",
    "Akuntansi",
]

# ---------------------------------------------------------------
# Jendela utama
# ---------------------------------------------------------------
root = tk.Tk()
root.title("Formulir Identitas Mahasiswa")
root.geometry("520x640")
root.resizable(False, False)
root.configure(bg=WARNA_BG)

# Kolom 0 di jendela utama melebar mengikuti ukuran jendela
root.columnconfigure(0, weight=1)

# Gaya Combobox agar warnanya senada dengan tema
gaya = ttk.Style(root)
gaya.theme_use("clam")
gaya.configure(
    "Form.TCombobox",
    fieldbackground=WARNA_KARTU,
    background=WARNA_GARIS,
    foreground=WARNA_TEKS,
    bordercolor=WARNA_GARIS,
    arrowcolor=WARNA_HEADER,
    padding=4,
)
gaya.map(
    "Form.TCombobox",
    fieldbackground=[("readonly", WARNA_KARTU)],
    foreground=[("readonly", WARNA_TEKS)],
    selectbackground=[("readonly", WARNA_KARTU)],
    selectforeground=[("readonly", WARNA_TEKS)],
)
root.option_add("*TCombobox*Listbox.font", FONT_INPUT)
root.option_add("*TCombobox*Listbox.selectBackground", WARNA_HEADER)
root.option_add("*TCombobox*Listbox.selectForeground", "white")


# ---------------------------------------------------------------
# Header (row 0)
# ---------------------------------------------------------------
header = tk.Frame(root, bg=WARNA_HEADER)
header.grid(row=0, column=0, sticky="ew")
header.columnconfigure(0, weight=1)

tk.Label(
    header, text="FORMULIR IDENTITAS MAHASISWA",
    font=FONT_JUDUL, bg=WARNA_HEADER, fg="white",
).grid(row=0, column=0, pady=(16, 2))

tk.Label(
    header, text="Isi data diri Anda, lalu tekan Simpan",
    font=FONT_SUBJUDUL, bg=WARNA_HEADER, fg="#CFE0F1",
).grid(row=1, column=0, pady=(0, 14))


# ---------------------------------------------------------------
# Kotak formulir (row 1): label + input, semua memakai grid()
# ---------------------------------------------------------------
form = tk.Frame(
    root, bg=WARNA_KARTU, padx=20, pady=16,
    highlightbackground=WARNA_GARIS, highlightcolor=WARNA_GARIS,
    highlightthickness=1,
)
form.grid(row=1, column=0, padx=24, pady=(18, 8), sticky="ew")
form.columnconfigure(1, weight=1)


def buat_label(teks, baris, **opsi):
    """Membuat Label di kolom kiri formulir."""
    lbl = tk.Label(
        form, text=teks, font=FONT_LABEL,
        bg=WARNA_KARTU, fg=WARNA_TEKS, anchor="w",
    )
    lbl.grid(row=baris, column=0, sticky="nw", padx=(0, 14), **opsi)
    return lbl


def buat_entry(baris):
    """Membuat Entry di kolom kanan formulir."""
    ent = tk.Entry(
        form, font=FONT_INPUT, width=28,
        bg=WARNA_KARTU, fg=WARNA_TEKS, insertbackground=WARNA_TEKS,
        relief="flat",
        highlightthickness=1, highlightbackground=WARNA_GARIS,
        highlightcolor=WARNA_HEADER,
    )
    ent.grid(row=baris, column=1, sticky="ew", ipady=4, pady=7)
    return ent


# Nama
buat_label("Nama", 0, pady=(11, 0))
entry_nama = buat_entry(0)

# NIM
buat_label("NIM", 1, pady=(11, 0))
entry_nim = buat_entry(1)

# Program Studi (pilihan sederhana)
buat_label("Program Studi", 2, pady=(11, 0))
combo_prodi = ttk.Combobox(
    form, values=PROGRAM_STUDI, state="readonly",
    font=FONT_INPUT, width=26, style="Form.TCombobox",
)
combo_prodi.grid(row=2, column=1, sticky="ew", ipady=2, pady=7)

# Alamat (widget Text, bisa lebih dari satu baris)
buat_label("Alamat", 3, pady=(11, 0))
text_alamat = tk.Text(
    form, font=FONT_INPUT, width=28, height=4, wrap="word",
    bg=WARNA_KARTU, fg=WARNA_TEKS, insertbackground=WARNA_TEKS,
    relief="flat", padx=6, pady=6,
    highlightthickness=1, highlightbackground=WARNA_GARIS,
    highlightcolor=WARNA_HEADER,
)
text_alamat.grid(row=3, column=1, sticky="ew", pady=7)


# ---------------------------------------------------------------
# Tombol (row 2): Simpan, Reset, Keluar
# ---------------------------------------------------------------
def buat_tombol(induk, teks, warna, warna_hover, perintah, kolom):
    """Membuat tombol berwarna dengan efek hover."""
    tombol = tk.Button(
        induk, text=teks, command=perintah,
        font=FONT_TOMBOL, bg=warna, fg="white",
        activebackground=warna_hover, activeforeground="white",
        relief="flat", bd=0, cursor="hand2", width=11, pady=7,
    )
    tombol.grid(row=0, column=kolom, padx=6)
    tombol.bind("<Enter>", lambda e: tombol.config(bg=warna_hover))
    tombol.bind("<Leave>", lambda e: tombol.config(bg=warna))
    return tombol


def ambil_data():
    """Mengambil nilai dari semua input (Entry, Combobox, Text)."""
    return {
        "nama": entry_nama.get().strip(),
        "nim": entry_nim.get().strip(),
        "prodi": combo_prodi.get().strip(),
        # Text.get membutuhkan indeks awal "1.0" dan akhir "end-1c"
        "alamat": text_alamat.get("1.0", "end-1c").strip(),
    }


def simpan():
    """Validasi input, lalu tampilkan hasilnya pada Label."""
    data = ambil_data()

    # Validasi: Nama dan NIM tidak boleh kosong
    if not data["nama"]:
        messagebox.showwarning("Data belum lengkap", "Nama tidak boleh kosong.")
        entry_nama.focus_set()
        return
    if not data["nim"]:
        messagebox.showwarning("Data belum lengkap", "NIM tidak boleh kosong.")
        entry_nim.focus_set()
        return

    # Kolom opsional yang kosong ditampilkan sebagai tanda strip
    prodi = data["prodi"] or "-"
    alamat = data["alamat"] or "-"

    label_hasil_judul.config(text="Data berhasil disimpan")
    nilai_hasil["Nama"].config(text=data["nama"])
    nilai_hasil["NIM"].config(text=data["nim"])
    nilai_hasil["Program Studi"].config(text=prodi)
    nilai_hasil["Alamat"].config(text=alamat)


def reset():
    """Mengosongkan seluruh formulir dan hasil."""
    entry_nama.delete(0, tk.END)
    entry_nim.delete(0, tk.END)
    combo_prodi.set("")
    text_alamat.delete("1.0", tk.END)
    label_hasil_judul.config(text="Hasil Input")
    for lbl in nilai_hasil.values():
        lbl.config(text="-")
    entry_nama.focus_set()


def keluar():
    """Menutup aplikasi setelah konfirmasi."""
    if messagebox.askyesno("Keluar", "Yakin ingin keluar dari aplikasi?"):
        root.destroy()


frame_tombol = tk.Frame(root, bg=WARNA_BG)
frame_tombol.grid(row=2, column=0, pady=(6, 10))

buat_tombol(frame_tombol, "Simpan", WARNA_HEADER, WARNA_HEADER_HOVER, simpan, 0)
buat_tombol(frame_tombol, "Reset", WARNA_RESET, WARNA_RESET_HOVER, reset, 1)
buat_tombol(frame_tombol, "Keluar", WARNA_KELUAR, WARNA_KELUAR_HOVER, keluar, 2)


# ---------------------------------------------------------------
# Kotak hasil (row 3): menampilkan data yang disimpan
# ---------------------------------------------------------------
kotak_hasil = tk.Frame(
    root, bg=WARNA_KARTU, padx=20, pady=12,
    highlightbackground=WARNA_GARIS, highlightcolor=WARNA_GARIS,
    highlightthickness=1,
)
kotak_hasil.grid(row=3, column=0, padx=24, pady=(4, 20), sticky="ew")
kotak_hasil.columnconfigure(1, weight=1)

label_hasil_judul = tk.Label(
    kotak_hasil, text="Hasil Input", font=FONT_HASIL_JUDUL,
    bg=WARNA_KARTU, fg=WARNA_HEADER, anchor="w",
)
label_hasil_judul.grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 6))

# Setiap baris hasil: Label judul di kolom 0, Label nilai di kolom 1
nilai_hasil = {}
for i, kunci in enumerate(["Nama", "NIM", "Program Studi", "Alamat"], start=1):
    tk.Label(
        kotak_hasil, text=kunci, font=FONT_HASIL,
        bg=WARNA_KARTU, fg=WARNA_TEKS_PUDAR, anchor="nw",
    ).grid(row=i, column=0, sticky="nw", padx=(0, 14), pady=2)

    nilai = tk.Label(
        kotak_hasil, text="-", font=FONT_HASIL,
        bg=WARNA_KARTU, fg=WARNA_TEKS, anchor="nw",
        justify="left", wraplength=290,
    )
    nilai.grid(row=i, column=1, sticky="nw", pady=2)
    nilai_hasil[kunci] = nilai


# Fokus awal ke kolom Nama; tombol X pada jendela juga meminta konfirmasi keluar
entry_nama.focus_set()
root.protocol("WM_DELETE_WINDOW", keluar)

root.mainloop()
