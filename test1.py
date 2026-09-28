# Nama File: test1.py
# Nama/NIM: Bintang Fitra Wisesha / 24060126140223
# Tanggal: 28 September 2025

# Definisi Tipe Bentukan Point 3D
ThreeDPoint = tuple[float, float, float]

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


# Fungsi utama: menghitung luas segitiga 3D dengan rumus cross product
def LuasSegiTelu(p1: ThreeDPoint, p2: ThreeDPoint, p3: ThreeDPoint) -> float:
    ux = JukukAbsis(p2) - JukukAbsis(p1)
    uy = JukukOrdinat(p2) - JukukOrdinat(p1)
    uz = JukukApotema(p2) - JukukApotema(p1)

    vx = JukukAbsis(p3) - JukukAbsis(p1)
    vy = JukukOrdinat(p3) - JukukOrdinat(p1)
    vz = JukukApotema(p3) - JukukApotema(p1)

    nx = uy*vz - uz*vy
    ny = uz*vx - ux*vz
    nz = ux*vy - uy*vx
    return round(0.5 * (nx**2 + ny**2 + nz**2)**0.5, 5)
    
# DENGAN INI SAYA MENYATAKAN BAHWA SAYA MENGERJAKAN SENDIRI TANPA BANTUAN KECERDASAN ARTIFISAL
# JANGAN DIUBAH!!
print(eval(input()))