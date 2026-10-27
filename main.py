"""Soal Praktik 3 - Program Utama (mengimpor modul utilitas_akademik)
Modul Pertemuan 6: Function, Parameter, Return Value, Scope, Lambda,
Module, Package & Library
"""

import utilitas_akademik as ua


def main():
    daftar_mk = [
        ("SI101", "Pemrograman Python", 3, 90),
        ("SI102", "Basis Data", 3, 85),
        ("SI103", "Analisis Sistem", 3, 78),
        ("SI104", "Jaringan Komputer", 2, 88),
    ]
    transkrip = ua.generate_transkrip(
        "Muhammad Dzikri Sagara", "20241320004", daftar_mk
    )
    print(f"Transkrip Nilai - {transkrip['nama']} ({transkrip['nim']})")
    for mk in transkrip["mata_kuliah"]:
        print(f"  {mk['kode']} {mk['mata_kuliah']} ({mk['sks']} SKS): "
              f"{mk['nilai']} ({mk['huruf']}, bobot {mk['bobot']})")
    print(f"Total SKS: {transkrip['total_sks']}")
    print(f"IPK: {transkrip['ipk']:.2f}")


if __name__ == "__main__":
    main()
