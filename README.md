# 🔐 WP Credential Extractor

---

## 📸 Screenshot  
![WP Credential Extractor Screenshot]([screenshot.png](https://raw.githubusercontent.com/alexithema1337/wordpress-parser/refs/heads/main/preview.png))  

---

## 📖 Deskripsi  

Sebuah skrip Python sederhana untuk mengekstrak kombinasi kredensial WordPress dari file-file `.txt` berdasarkan berbagai pola URL login (`wp-login.php`) dalam sebuah folder.

---

## 📌 Fitur

✅ Scan file-file `.txt` dalam folder tertentu  
✅ Menangkap kombinasi **URL + username + password** dari berbagai format:
```

[https://site.com/wp-login.php\:user\:pass](https://site.com/wp-login.php:user:pass)
[https://site.com/wp-login.php|user|pass](https://site.com/wp-login.php|user|pass)
[https://site.com/wp-login.php#user@pass](https://site.com/wp-login.php#user@pass)
[https://site.com/wp-login.php#user@pass@extra](https://site.com/wp-login.php#user@pass@extra)
[https://site.com/wp-login.php](https://site.com/wp-login.php) : user : pass

````

✅ Pilihan format output:
- `wp-login.php|user|pass`
- `wp-login.php@user#pass`

✅ **Multithreading** — jumlah thread bisa diatur sesuai kebutuhan  
✅ Output hasil ke file (misal: `result.txt`) sesuai format pilihan  
✅ Warna terminal dengan `colorama`:
- `[` dan `]` **putih**
- `+` dan `FOUND` **hijau**

✅ Kompatibel **Windows & Linux** (dengan clear/cls otomatis)  
✅ Clean terminal output — tanpa pesan pemrosesan file  

---

## 📦 Requirement

- **Python 3.x**
- Modul:
  ```bash
  pip install colorama
````

---

## 🚀 Cara Pakai

Jalankan skrip:

```bash
python wordpress_parser.py
```

Ikuti prompt di terminal:

1. Masukkan folder yang berisi file `.txt`
2. Masukkan nama file hasil output
3. Masukkan jumlah thread
4. Pilih format output:

   ```
   1. wp-login.php|user|pass
   2. wp-login.php@user#pass
   ```
5. Konfirmasi untuk lanjut `(y/n)`

---

## 📂 Contoh Format File Input

Contoh isi file `.txt`:

```
https://example.com/wp-login.php:admin:password123
https://site.net/wp-login.php|root|toor
https://another.net/wp-login.php#user@pass
https://test.com/wp-login.php#user@pass1@pass2
https://example.org/wp-login.php : user : pass
```

---

## 📜 Output

📌 Contoh hasil di terminal:

```
[+] https://example.com/wp-login.php|admin|password123 [ FOUND ]
[+] https://example.com/wp-login.php|admin|password123 [ FOUND ]
[+] https://example.com/wp-login.php|admin|password123 [ FOUND ]
```

Atau:

```
[+] https://example.com/wp-login.php@admin#password123 [ FOUND ]
[+] https://example.com/wp-login.php@admin#password123 [ FOUND ]
[+] https://example.com/wp-login.php@admin#password123 [ FOUND ]
```

*(tergantung format pilihan)*

📌 Contoh isi file `result.txt` (Format 1):

```
http://site.com/wp-login.php|user|pass
http://site.com/wp-login.php|user|pass
http://site.com/wp-login.php|user|pass
http://site.com/wp-login.php|user|pass
```

Atau (Format 2):

```
http://site.com/wp-login.php@user#pass
http://site.com/wp-login.php@user#pass
http://site.com/wp-login.php@user#pass
http://site.com/wp-login.php@user#pass
```

---

## 📊 Catatan

* Support **username berupa email** dan **password karakter spesial** (contoh: `#`, `@`, `&`)
* Support URL berbasis IP (contoh: `http://8.210.145.197/wp-login.php`)
* Disarankan gunakan **4-8 thread** untuk performa optimal
* Hanya membaca file `.txt` di folder yang ditentukan (tanpa subfolder)
* Pastikan format data sesuai pola regex yang didukung
* Jika tidak ada kredensial ditemukan, cek kembali isi file

---

## 📣 Credit

Dikembangkan oleh **alex\_asmodeusSalt**
