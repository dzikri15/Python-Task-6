"""Entitas Mahasiswa (model)."""


class Mahasiswa:
    """Data mahasiswa dengan NIM sebagai identitas unik."""

    def __init__(self, nim, nama, jurusan, ipk=0.0):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan
        self.ipk = ipk

    def to_dict(self):
        return {"nim": self.nim, "nama": self.nama,
                "jurusan": self.jurusan, "ipk": self.ipk}

    def __repr__(self):
        return (f"Mahasiswa(nim='{self.nim}', nama='{self.nama}', "
                f"jurusan='{self.jurusan}', ipk={self.ipk})")
