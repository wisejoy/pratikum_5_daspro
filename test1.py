# Nama File: test1.py
# Nama/NIM: Bintang Fitra Wisesha / 24060126140223
# Tanggal: 28 September 2025

# Definisi Tipe Bentukan Point 3D
type ThreeDPoint = tuple[float, float, float]

# Konstruktor
def GaweTitik3D(x: float, y: float, z: float) -> ThreeDPoint:
    return (x, y, z)

# Selektor
def JukukAbsis(p: ThreeDPoint) -> float:
    return p[0]


def JukukOrdinat(p: ThreeDPoint) -> float:
    return p[1]


def JukukApotema(p: ThreeDPoint) -> float:
    return p[2]


# Fungsi bantu: menghitung panjang sisi segitiga dalam ruang 3D
def PanjangSisi(a: ThreeDPoint, b: ThreeDPoint) -> float:
    return (((JukukAbsis(b) - JukukAbsis(a)) ** 2) +
            ((JukukOrdinat(b) - JukukOrdinat(a)) ** 2) +
            ((JukukApotema(b) - JukukApotema(a)) ** 2)) ** 0.5


# Fungsi utama: menghitung luas segitiga 3D dengan rumus Heron
def LuasSegiTelu(p1: ThreeDPoint, p2: ThreeDPoint, p3: ThreeDPoint) -> float:
    a = PanjangSisi(p1, p2)
    b = PanjangSisi(p2, p3)
    c = PanjangSisi(p3, p1)

    s = (a + b + c) / 2
    luas = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return luas


# Contoh input yang valid:
# LuasSegiTelu((0, 0, 0), (3, 0, 0), (0, 4, 0))

# DENGAN INI SAYA MENYATAKAN BAHWA SAYA MENGERJAKAN SENDIRI TANPA BANTUAN KECERDASAN ARTIFISAL
# JANGAN DIUBAH!!
print(eval(input()))