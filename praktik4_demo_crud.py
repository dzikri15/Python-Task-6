"""Soal Praktik 4 - Demo CRUD Package sistem_informasi
Modul Pertemuan 6: Function, Parameter, Return Value, Scope, Lambda,
Module, Package & Library

Jalankan dari root folder tugas ini agar package dapat diimpor:
    python3 praktik4_demo_crud.py
"""

from sistem_informasi.service import MahasiswaService


def main():
    svc = MahasiswaService()

    print("== CREATE ==")
    for nim, nama, jurusan, ipk in [
        ("20241320004", "Muhammad Dzikri Sagara", "Sistem Informasi", 3.75),
        ("20241320030", "Muhammad Alamsyah", "Sistem Informasi", 3.60),
        ("20241320038", "Fakhry Ahmad Fauzan", "Sistem Informasi", 3.80),
    ]:
        ok, pesan = svc.tambah(nim, nama, jurusan, ipk)
        print(f"  [{('OK' if ok else 'GAGAL')}] {pesan}")

    print("\n== READ (semua) ==")
    for mhs in svc.daftar():
        print(f"  - {mhs}")

    print("\n== READ (satu, NIM 20241320004) ==")
    print(f"  {svc.cari('20241320004')}")

    print("\n== UPDATE (IPK 20241320004 -> 3.85) ==")
    ok, pesan = svc.update("20241320004", ipk=3.85)
    print(f"  [{('OK' if ok else 'GAGAL')}] {pesan}")
    print(f"  {svc.cari('20241320004')}")

    print("\n== DELETE (NIM 20241320030) ==")
    ok, pesan = svc.hapus("20241320030")
    print(f"  [{('OK' if ok else 'GAGAL')}] {pesan}")

    print("\n== READ (sisa) ==")
    for mhs in svc.daftar():
        print(f"  - {mhs}")
    print(f"  Total mahasiswa: {len(svc.daftar())}")


if __name__ == "__main__":
    main()
