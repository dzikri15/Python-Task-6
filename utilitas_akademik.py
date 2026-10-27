"""Soal Praktik 3 - Modul Utilitas Akademik
Modul Pertemuan 6: Function, Parameter, Return Value, Scope, Lambda,
Module, Package & Library

Skala konversi mengikuti modul (Bab 3.1 & studi kasus):
A >= 85, B >= 70, C >= 55, D >= 40, E < 40
Bobot: A=4, B=3, C=2, D=1, E=0
"""

BOBOT_HURUF = {"A": 4, "B": 3, "C": 2, "D": 1, "E": 0}


def konversi_nilai_huruf(nilai):
    """Mengubah nilai angka (0-100) menjadi huruf A/B/C/D/E."""
    if nilai >= 85:
        return "A"
    if nilai >= 70:
        return "B"
    if nilai >= 55:
        return "C"
    if nilai >= 40:
        return "D"
    return "E"


def hitung_ipk(daftar_nilai):
    """Menghitung IPK dari list (sks, nilai_angka).

    Contoh: hitung_ipk([(3, 85), (3, 90), (2, 78)])
    """
    total_sks = 0
    total_bobot = 0
    for sks, nilai in daftar_nilai:
        huruf = konversi_nilai_huruf(nilai)
        total_sks += sks
        total_bobot += sks * BOBOT_HURUF[huruf]
    if total_sks == 0:
        return 0.0
    return total_bobot / total_sks


def generate_transkrip(nama, nim, daftar_mk):
    """Membuat transkrip nilai.

    daftar_mk: list tuple (kode_mk, nama_mk, sks, nilai_angka).
    Mengembalikan dict berisi identitas, detail tiap MK (dengan huruf
    dan bobot), total SKS, dan IPK.
    """
    detail = []
    for kode, nama_mk, sks, nilai in daftar_mk:
        huruf = konversi_nilai_huruf(nilai)
        detail.append({
            "kode": kode, "mata_kuliah": nama_mk, "sks": sks,
            "nilai": nilai, "huruf": huruf, "bobot": BOBOT_HURUF[huruf],
        })
    ipk = hitung_ipk([(d["sks"], d["nilai"]) for d in detail])
    return {
        "nama": nama,
        "nim": nim,
        "mata_kuliah": detail,
        "total_sks": sum(d["sks"] for d in detail),
        "ipk": round(ipk, 2),
    }


if __name__ == "__main__":
    # Testing mandiri modul (hanya jalan saat file dieksekusi langsung)
    print("Mode testing utilitas_akademik:")
    print(f"konversi_nilai_huruf(85) = {konversi_nilai_huruf(85)}")
    print(f"konversi_nilai_huruf(72) = {konversi_nilai_huruf(72)}")
    print(f"hitung_ipk([(3, 85), (3, 90), (2, 78)]) = "
          f"{hitung_ipk([(3, 85), (3, 90), (2, 78)]):.2f}")
