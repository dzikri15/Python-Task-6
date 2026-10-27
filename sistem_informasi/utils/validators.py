"""Validator untuk entitas Mahasiswa."""


def validasi_mahasiswa(nim, nama, jurusan, ipk):
    """Mengembalikan (True, '') jika valid, (False, pesan) jika tidak."""
    if not (isinstance(nim, str) and nim.isdigit() and len(nim) == 11):
        return False, "NIM harus berupa 11 digit angka."
    if not nama or not isinstance(nama, str):
        return False, "Nama tidak boleh kosong."
    if not jurusan or not isinstance(jurusan, str):
        return False, "Jurusan tidak boleh kosong."
    if not (0.0 <= ipk <= 4.0):
        return False, "IPK harus berada dalam rentang 0.0 - 4.0."
    return True, ""
