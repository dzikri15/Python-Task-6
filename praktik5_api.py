"""Soal Praktik 5 - Analisis Data API dengan Lambda & Higher-Order Function
Modul Pertemuan 6: Function, Parameter, Return Value, Scope, Lambda,
Module, Package & Library

Sumber data: JSONPlaceholder (https://jsonplaceholder.typicode.com/users)
- requests : mengambil data dari public REST API
- map/filter/sorted + lambda : memproses dan menganalisis data
- json : menyimpan hasil analisis ke file JSON
"""

import json

import requests

API_URL = "https://jsonplaceholder.typicode.com/users"
OUTPUT_FILE = "hasil_analisis.json"


def main():
    response = requests.get(API_URL, timeout=15)
    response.raise_for_status()
    users = response.json()
    print(f"Data berhasil diambil: {len(users)} user dari {API_URL}")

    # map: ekstrak (nama, email, kota)
    ringkas = list(map(
        lambda u: {"nama": u["name"], "email": u["email"],
                   "kota": u["address"]["city"], "perusahaan": u["company"]["name"]},
        users,
    ))

    # filter: user yang namanya lebih dari 15 karakter
    nama_panjang = list(filter(lambda u: len(u["nama"]) > 15, ringkas))

    # sorted: urutkan berdasarkan kota (A-Z)
    urut_kota = sorted(ringkas, key=lambda u: u["kota"])

    # Analisis tambahan: rata-rata panjang nama (map + statistics manual)
    panjang_nama = list(map(lambda u: len(u["nama"]), ringkas))
    rata_panjang = sum(panjang_nama) / len(panjang_nama)

    hasil = {
        "total_user": len(users),
        "rata_rata_panjang_nama": round(rata_panjang, 2),
        "user_nama_panjang": nama_panjang,
        "jumlah_user_nama_panjang": len(nama_panjang),
        "user_urut_kota": urut_kota,
    }

    print(f"\nTotal user: {hasil['total_user']}")
    print(f"Rata-rata panjang nama: {hasil['rata_rata_panjang_nama']} karakter")
    print(f"User dengan nama > 15 karakter: {hasil['jumlah_user_nama_panjang']}")
    for u in nama_panjang:
        print(f"  - {u['nama']} ({u['kota']})")
    print("\nUser diurutkan berdasarkan kota:")
    for u in urut_kota:
        print(f"  - {u['kota']}: {u['nama']}")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(hasil, f, indent=2, ensure_ascii=False)
    print(f"\nHasil analisis disimpan ke {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
