# 🔐 WP Credential Extractor

Skrip Python untuk mengekstrak kombinasi credential dari file `.txt` berdasarkan beberapa pola login WordPress (`wp-login.php`) di dalam sebuah folder.

---

## 📌 Fitur

- Scan file-file `.txt` dalam folder yang ditentukan
- Menangkap kombinasi URL + username + password dalam berbagai format:
  - `https://site.com/wp-login.php:user:pass`
  - `https://site.com/wp-login.php|user|pass`
  - `https://site.com/wp-login.php#user@pass`
  - `https://site.com/wp-login.php#user@pass@extra`
  - `https://site.com/wp-login.php : user : pass`
- Multithreading — jumlah thread bisa ditentukan
- Output hasil ke file `result.txt` (atau nama lain sesuai input)
- Warna terminal dengan `colorama`
- Kompatibel Windows & Linux (dengan `clear` / `cls` otomatis)

---

## 📦 Requirement

- Python 3.x
- Modul:
  - `colorama`

Install dependensi:
```bash
pip install colorama
````

---

## 🚀 Cara Pakai

Jalankan skrip:

```bash
python script.py
```

Ikuti prompt:

1. Masukkan folder yang berisi file `.txt`
2. Masukkan nama file hasil (contoh: `result.txt`)
3. Masukkan jumlah thread (disarankan 10-50)
4. Konfirmasi untuk melanjutkan (y/n)

---

## 📂 Contoh Format File Input

Isi file `.txt`:

```
https://example.com/wp-login.php:admin:password123
https://site.net/wp-login.php|root|toor
https://another.net/wp-login.php#user@pass
```

---

## 📜 Output

Setiap hasil yang ditemukan akan dicetak ke terminal dan disimpan ke file output.

Contoh hasil di `result.txt`:

```
https://example.com/wp-login.php#admin@password123
https://site.net/wp-login.php#roo@toor
https://another.net/wp-login.php#user@pass
```

---

## 📊 Catatan

* Semakin banyak file & data, disarankan jumlah thread ditambah
* Script ini hanya membaca file `.txt` di dalam folder yang kamu tentukan
* Pastikan format data sesuai pattern regex yang ada agar bisa terdeteksi

---

## 📣 Credit

Dikembangkan oleh **alex\_asmodeus**
Salt : `alexithema + asmodeus` 🔥

---
