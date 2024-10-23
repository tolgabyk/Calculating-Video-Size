import tkinter as tk
from tkinter import ttk, messagebox

def boyut_hesapla():
    try:
        secilen_cozunurluk = cozunurluk.get()
        video_suresi = int(sure.get())

        # Çözünürlük ve bit hızları (kbps)
        bit_hizlari = {
            "240p": 500,
            "360p": 750,
            "480p": 1500,
            "720p": 3000,
            "1080p": 4500,
            "1440p (2K)": 9000,
            "2160p (4K)": 16000,
            "4320p (8K)": 35000,
        }
        bit_hizi = bit_hizlari[secilen_cozunurluk]

        # Dosya boyutunu (MB) hesapla
        dosya_boyutu = bit_hizi * video_suresi * 60 / 8 / 1024
        sonuc_etiketi.config(text=f"Video Boyutu: {dosya_boyutu:.2f} MB")
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli bir süre giriniz.")

# Arayüz
pencere = tk.Tk()
pencere.title("Video Boyutu Hesaplayıcı")
pencere.geometry("520x520")  
pencere.resizable(False, False)

stil = ttk.Style()
stil.configure("TLabel", font=("Arial", 13))
stil.configure("TButton", font=("Arial", 13))
stil.configure("TCombobox", font=("Arial", 13))

cozunurluk_etiketi = ttk.Label(pencere, text="Çözünürlük:")
cozunurluk_etiketi.pack(pady=10)
cozunurluk = tk.StringVar()
cozunurluk_combobox = ttk.Combobox(pencere, textvariable=cozunurluk, state='readonly')
cozunurluk_combobox['values'] = ("240p", "360p", "480p", "720p", "1080p", "1440p (2K)", "2160p (4K)", "4320p (8K)")
cozunurluk_combobox.current(0)
cozunurluk_combobox.pack(pady=10)

sure_etiketi = ttk.Label(pencere, text="Video Süresi (dakika):")
sure_etiketi.pack(pady=10)
sure = tk.StringVar()
sure_girdisi = ttk.Entry(pencere, textvariable=sure)
sure_girdisi.pack(pady=10)

hesapla_butonu = ttk.Button(pencere, text="Boyut Hesapla", command=boyut_hesapla)
hesapla_butonu.pack(pady=20)

sonuc_etiketi = ttk.Label(pencere, text="Video Boyutu: ")
sonuc_etiketi.pack(pady=20)

pencere.mainloop()
