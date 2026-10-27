"""CRUD Mahasiswa dengan penyimpanan in-memory (dictionary).

Kunci dictionary adalah NIM, sehingga setiap NIM bersifat unik.
"""

from ..model.mahasiswa import Mahasiswa
from ..utils.validators import validasi_mahasiswa


class MahasiswaService:
    def __init__(self):
        self._db = {}  # nim -> Mahasiswa

    def tambah(self, nim, nama, jurusan, ipk=0.0):
        """Create: tambah mahasiswa baru. Gagal jika NIM sudah ada."""
        valid, error = validasi_mahasiswa(nim, nama, jurusan, ipk)
        if not valid:
            return False, error
        if nim in self._db:
            return False, f"NIM {nim} sudah terdaftar."
        self._db[nim] = Mahasiswa(nim, nama, jurusan, ipk)
        return True, f"Mahasiswa {nama} ditambahkan."

    def cari(self, nim):
        """Read (satu): cari mahasiswa berdasarkan NIM."""
        return self._db.get(nim)

    def daftar(self):
        """Read (semua): kembalikan list seluruh mahasiswa."""
        return list(self._db.values())

    def update(self, nim, nama=None, jurusan=None, ipk=None):
        """Update: ubah field yang diberikan saja."""
        mhs = self._db.get(nim)
        if mhs is None:
            return False, f"NIM {nim} tidak ditemukan."
        if nama is not None:
            mhs.nama = nama
        if jurusan is not None:
            mhs.jurusan = jurusan
        if ipk is not None:
            mhs.ipk = ipk
        return True, f"Data NIM {nim} diperbarui."

    def hapus(self, nim):
        """Delete: hapus mahasiswa berdasarkan NIM."""
        if nim not in self._db:
            return False, f"NIM {nim} tidak ditemukan."
        del self._db[nim]
        return True, f"Mahasiswa NIM {nim} dihapus."
