"""Soal Praktik 1 - Fungsi Statistik Deskriptif
Modul Pertemuan 6: Function, Parameter, Return Value, Scope, Lambda,
Module, Package & Library

Hanya memakai standard library (statistics, math).
"""


import math
import statistics


def hitung_statistik(data):
    """Menerima list angka, mengembalikan dict statistik deskriptif.

    - mean   : rata-rata (statistics.mean)
    - median : nilai tengah (statistics.median)
    - modus  : nilai paling sering muncul (statistics.multimode;
               satu nilai jika modusnya tunggal, list jika lebih dari satu)
    - range  : max - min
    - std_dev: simpangan baku populasi (statistics.pstdev)
    """
    if not data:
        raise ValueError("Data tidak boleh kosong")

    modus_list = statistics.multimode(data)
    modus = modus_list[0] if len(modus_list) == 1 else modus_list

    return {
        "mean": statistics.mean(data),
        "median": statistics.median(data),
        "modus": modus,
        "range": max(data) - min(data),
        "std_dev": statistics.pstdev(data),
    }


def main():
    nilai = [85, 90, 78, 92, 88, 90, 76, 95, 89, 90]
    hasil = hitung_statistik(nilai)
    print(f"Data nilai: {nilai}")
    print(f"Jumlah data : {len(nilai)}")
    print(f"Mean        : {hasil['mean']:.2f}")
    print(f"Median      : {hasil['median']:.2f}")
    print(f"Modus       : {hasil['modus']}")
    print(f"Range       : {hasil['range']}")
    print(f"Std. Dev    : {hasil['std_dev']:.2f}")
    # Bukti pemakaian math: verifikasi manual std dev populasi
    mean = hasil["mean"]
    cek = math.sqrt(sum((x - mean) ** 2 for x in nilai) / len(nilai))
    print(f"Verifikasi (math.sqrt): {cek:.2f}")


if __name__ == "__main__":
    main()
