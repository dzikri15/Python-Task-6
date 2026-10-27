# Soal Teori — Pertemuan 6: Function, Parameter, Return Value, Scope, Lambda, Module, Package & Library

## 1. Parameter vs Argumen

**Parameter** adalah variabel yang didefinisikan dalam header fungsi sebagai placeholder
(tempat kosong) untuk nilai yang akan diterima. **Argumen** adalah nilai aktual yang
dilewatkan ke fungsi saat pemanggilan. Analoginya: parameter adalah kotak kosong pada
formulir, sedangkan argumen adalah data yang diisi ke dalam kotak tersebut.

```python
def hitung_pajak(harga, tarif):   # harga dan tarif adalah PARAMETER
    return harga * tarif

pajak = hitung_pajak(100000, 0.11)  # 100000 dan 0.11 adalah ARGUMEN
```

## 2. Aturan LEGB dalam Scope Python

LEGB adalah urutan pencarian nama variabel oleh Python, dari yang paling dalam ke
paling luar: **Local → Enclosing → Global → Built-in**. Jika nama tidak ditemukan di
keempat level, Python menghasilkan `NameError`.

- **Local:** variabel di dalam fungsi yang sedang berjalan. Contoh: variabel `x` yang
  didefinisikan di dalam `def dalam()` hanya bisa diakses di dalam fungsi itu.
- **Enclosing:** variabel dari fungsi luar (untuk nested function / closure). Contoh:
  fungsi dalam yang membaca variabel `total` milik fungsi luar pembuat akumulator.
- **Global:** variabel di tingkat modul, di luar semua fungsi. Contoh: konstanta `PI`
  atau `counter` yang dibaca dari berbagai fungsi dalam satu file.
- **Built-in:** nama bawaan Python seperti `print`, `len`, `range`, `Exception`.
  Contoh: `len("hello")` memakai `len` dari built-in scope ketika tidak ada variabel
  bernama `len` di scope yang lebih dalam.

## 3. Pitfall: Objek Mutable sebagai Default Parameter

Ini dianggap pitfall karena **nilai default dievaluasi hanya sekali, saat definisi
fungsi**, bukan setiap kali fungsi dipanggil. Akibatnya, satu objek list/dict/set yang
sama dipakai bersama oleh semua pemanggilan — data dari pemanggilan sebelumnya
"bocor" ke pemanggilan berikutnya:

```python
def tambah_item(item, keranjang=[]):  # list yang sama dipakai terus!
    keranjang.append(item)
    return keranjang

tambah_item("apel")   # ['apel']
tambah_item("jeruk")  # ['apel', 'jeruk']  <- BUKAN ['jeruk']!
```

**Solusi yang benar:** gunakan `None` sebagai sentinel, lalu buat objek baru di dalam
body fungsi:

```python
def tambah_item(item, keranjang=None):
    if keranjang is None:
        keranjang = []
    keranjang.append(item)
    return keranjang
```

## 4. Module vs Package, dan Peran `__init__.py`

- **Module** adalah satu file Python (`.py`) berisi definisi fungsi, kelas, dan variabel
  yang bisa diimpor. Nama modul sama dengan nama file tanpa ekstensi
  (mis. `utilitas_akademik.py` → modul `utilitas_akademik`).
- **Package** adalah direktori yang berisi kumpulan modul-modul terkait, sehingga
  membentuk hierarki (mis. `sistem_informasi.mahasiswa.service`).

File **`__init__.py`** menandai bahwa sebuah direktori adalah package Python (regular
package). File ini boleh kosong (sekadar penanda), atau berisi kode inisialisasi
package, definisi `__all__` untuk mengontrol nama yang diekspor saat `import *`, dan
konfigurasi tingkat package seperti `__version__`. Sejak Python 3.3 ada namespace
package yang bisa tanpa `__init__.py`, tetapi untuk package reguler file ini tetap
direkomendasikan.

## 5. Lambda vs def: Kapan Memakai Masing-Masing?

**Lambda lebih tepat** ketika fungsinya kecil, satu ekspresi, dan hanya dipakai sekali
atau sebagai argumen:

1. Sebagai **key function** di `sorted()`, `min()`, `max()` — mis.
   `sorted(mahasiswa, key=lambda m: m["ipk"])`.
2. Sebagai **callback / argumen singkat** untuk higher-order function seperti `map()`
   dan `filter()` — mis. `filter(lambda x: x >= 80, nilai)`.
3. Untuk **fungsi sekali pakai yang sangat pendek** yang tidak layak diberi nama dan
   didokumentasikan sendiri, mis. pengurutan atau transformasi sebaris.

**def lebih tepat** ketika:

1. Fungsi **lebih dari satu ekspresi** atau butuh statement (loop, `if` bertingkat,
   `try/except`) — lambda hanya boleh satu ekspresi.
2. Fungsi **dipakai berulang kali** atau perlu diberi nama deskriptif dan docstring
   agar mudah dibaca, diuji, dan di-debug.
3. Logikanya **kompleks atau penting** (aturan bisnis, validasi, perhitungan) — fungsi
   `def` dengan nama jelas jauh lebih mudah dipelihara daripada lambda yang panjang.
