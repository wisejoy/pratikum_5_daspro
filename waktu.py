type Waktu = tuple[int, int, int]

def MakeWaktu(h: int, m: int, s: int) -> Waktu:
    return (h, m, s)

def GetJam(w: Waktu) -> int:
    return w[0]

def GetMenit(w: Waktu) -> int:
    return w[1]

def GetDetik(w: Waktu) -> int:
    return w[2]

def DetiksSinceMidnight(w: Waktu) -> int:
    return (GetJam(w) * 3600) + (GetMenit(w) * 60) + GetDetik(w)

def IsHalfDay(w: Waktu) -> bool:
    return GetJam(w) == 12 and GetMenit(w) == 0 and GetDetik(w) == 0

def IsBefore(w1: Waktu, w2: Waktu) -> bool:
    return DetiksSinceMidnight(w1) < DetiksSinceMidnight(w2)

def IsAfter(w1: Waktu, w2: Waktu) -> bool:
    return DetiksSinceMidnight(w1) > DetiksSinceMidnight(w2)

print(DetiksSinceMidnight((1, 30, 0)))
print(IsHalfDay((12, 0, 0)))             # True (tepat jam 12 siang)
print(IsHalfDay((8, 30, 0)))              # False (bukan jam 12)
print(IsBefore((8, 0, 0), (10, 15, 0)))   # True (jam 8 sebelum jam 10)
print(IsBefore((14, 0, 0), (10, 15, 0)))  # False (jam 14 bukan sebelum jam 10)
print(IsAfter((14, 30, 0), (10, 15, 0)))  # True (jam 14 setelah jam 10)
print(IsAfter((8, 0, 0), (10, 15, 0)))    # False (jam 8 bukan setelah jam 10)
print(IsAfter((8, 0, 0), (10, 15, 0)))