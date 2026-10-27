"""Soal Praktik 2 - Validasi Data dengan Schema
Modul Pertemuan 6: Function, Parameter, Return Value, Scope, Lambda,
Module, Package & Library

validasi_data() memakai:
- parameter biasa  : data (dict), schema (dict aturan)
- *args            : fungsi validator tambahan, masing-masing menerima
                     data dan mengembalikan pesan error (str) atau None
- **kwargs         : opsi, mis. strict=True (field tak dikenal = error)
Mengembalikan tuple (is_valid: bool, errors: list).
"""


def validasi_data(data, schema, *validator_tambahan, **opsi):
    errors = []
    strict = opsi.get("strict", False)

    for field, aturan in schema.items():
        if field not in data:
            if aturan.get("required", False):
                errors.append(f"Field '{field}' wajib diisi (required).")
            continue

        nilai = data[field]
        tipe = aturan.get("type")
        if tipe is not None and not isinstance(nilai, tipe):
            errors.append(
                f"Field '{field}' harus bertipe {tipe.__name__}, "
                f"bukan {type(nilai).__name__}."
            )
            continue  # skip cek rentang jika tipe sudah salah

        if "min" in aturan and nilai < aturan["min"]:
            errors.append(f"Field '{field}' minimal {aturan['min']}, got {nilai}.")
        if "max" in aturan and nilai > aturan["max"]:
            errors.append(f"Field '{field}' maksimal {aturan['max']}, got {nilai}.")
        if "pilihan" in aturan and nilai not in aturan["pilihan"]:
            errors.append(
                f"Field '{field}' harus salah satu dari {aturan['pilihan']}."
            )

    if strict:
        for field in data:
            if field not in schema:
                errors.append(f"Field '{field}' tidak dikenal (strict mode).")

    for validator in validator_tambahan:
        pesan = validator(data)
        if pesan:
            errors.append(pesan)

    return (len(errors) == 0, errors)


def cek_nim(data):
    """Validator tambahan: NIM harus 11 digit angka."""
    nim = data.get("nim", "")
    if not (isinstance(nim, str) and nim.isdigit() and len(nim) == 11):
        return "Field 'nim' harus berupa 11 digit angka."
    return None


def main():
    schema = {
        "nama": {"type": str, "required": True},
        "nim": {"type": str, "required": True},
        "umur": {"type": int, "required": True, "min": 17, "max": 60},
        "ipk": {"type": float, "required": True, "min": 0.0, "max": 4.0},
        "jurusan": {"type": str, "required": False,
                    "pilihan": ["Sistem Informasi", "Informatika"]},
    }

    data_benar = {"nama": "Muhammad Dzikri Sagara", "nim": "20241320004",
                  "umur": 20, "ipk": 3.75, "jurusan": "Sistem Informasi"}
    data_salah = {"nama": "Budi", "nim": "12345", "umur": 15,
                  "ipk": 4.5, "jurusan": "Kedokteran"}

    for label, data in [("Data benar", data_benar), ("Data salah", data_salah)]:
        is_valid, errors = validasi_data(data, schema, cek_nim, strict=True)
        print(f"\n{label}: {data}")
        print(f"Valid: {is_valid}")
        if errors:
            print("Errors:")
            for e in errors:
                print(f"  - {e}")


if __name__ == "__main__":
    main()
