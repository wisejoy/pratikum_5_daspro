type Point = tuple [int, int]
#makePoint
def makepoint (x: float, y : float) -> Point :
    return (x,y)
def getabsis(p: Point) -> float :
    return p [0]
def getordinat(p: Point) -> float :
    return p [1]
#Main Function
def panjang_garis (titik1: Point, titik2: Point) -> float:
    return (((getabsis(titik2) - getabsis(titik1))**2) + ((getordinat(titik2) - getordinat(titik1))**2))**0.5
def gradien (titik1: Point, titik2: Point) -> float:
    return ((getordinat(titik2) - getordinat(titik1)) / (getabsis(titik2) - getabsis(titik1)))
def issejajar(p1: Point, p2:Point, p3:Point,p4:Point)->bool:
    return (
        gradien(p1,p2) == gradien(p3,p4) and panjang_garis(p1,p2) == panjang_garis(p3,p4)
    )

#applikasi
print(issejajar(
    (1,2),##input1
    (4,8),##input2
    (3,5),##input3
    (6,11)##input4
))
print (panjang_garis((1,1),(7,9)))
print(gradien((1,1), (7,9)))