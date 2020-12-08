import math

#a math modul bemutatására készített program
#Az alábbi, itt bemutatott függvények a 3.8. verziótól használhatóak:
# math.comb() math.perm() math.isqrt()


def kiiratas(szoveg, szam): #táblázatszerűen, rendezettem kiírja az értékeket
    szoveghossz = 30 #milyen hosszú legyen a bal oszlop
    txt = "\t" + szoveg
    if len(szoveg) < szoveghossz:
        for i in range(len(szoveg), szoveghossz + 1, 1):
            txt = txt + " " #feltöltöm a szoveghossz változó értékéig szóközökkel
    txt = txt + str(szam)
    print(txt)


def kiiratas2(szam):
    szoveghossz = 10 #milyen hosszú legyen az oszlop
    txt = str(round(szam,4)) 
    if len(txt) < szoveghossz:
        for i in range(len(txt), szoveghossz + 1, 1):
            txt = " " + txt #feltöltöm a szoveghossz változó értékéig szóközökkel
    print(txt, end="")

def pont41(label):
    print(label)
    kiiratas("math.ceil(0)", math.ceil(0))
    kiiratas("math.ceil(-8)", math.ceil(-8))
    kiiratas("math.ceil(13.58)", math.ceil(13.58))
    kiiratas("math.ceil(-13.58)", math.ceil(-13.58))
    print()
    kiiratas("math.comb(90, 5)", math.comb(90, 5)) #3.8. verziótól
    kiiratas("math.comb(45, 6)", math.comb(45, 6))
    kiiratas("math.comb(35, 7)", math.comb(35, 7))
    print()
    kiiratas("math.perm(5, 2)", math.perm(5, 2)) #3.8. verziótól
    kiiratas("math.perm(10, 3)", math.perm(10, 3))
    kiiratas("math.perm(5, 1)", math.perm(5, 1))
    print()
    kiiratas("math.copysign(15, 0.0)", math.copysign(15, 0.0))
    kiiratas("math.copysign(15, -0.0)", math.copysign(15, -0.0))
    kiiratas("math.copysign(13.62, 3.0)", math.copysign(13.62, 3.0))
    kiiratas("math.copysign(13.62, -1.0)", math.copysign(13.62, -1.0))
    print()
    kiiratas("math.fabs(0)", math.fabs(0))
    kiiratas("math.fabs(58)", math.fabs(58))
    kiiratas("math.fabs(-13)", math.fabs(-13))
    kiiratas("math.fabs(-13.5878)", math.fabs(-13.5878))
    print()
    kiiratas("math.factorial(0)", math.factorial(0))
    kiiratas("math.factorial(1)", math.factorial(1))
    kiiratas("math.factorial(5)", math.factorial(5))
    print()
    kiiratas("math.floor(0)", math.floor(0))
    kiiratas("math.floor(-8)", math.floor(-8))
    kiiratas("math.floor(13.58)", math.floor(13.58))
    kiiratas("math.floor(-13.58)", math.floor(-13.58))
    print()
    kiiratas("math.gcd(120, 25)", math.gcd(120, 25))
    kiiratas("math.gcd(24, 60)", math.gcd(24, 60))
    print()
    kiiratas("math.isqrt(68)", math.isqrt(68)) #3.8. verziótól
    kiiratas("math.isqrt(125)", math.isqrt(125))
    print()
        
def pont42(label):
    print(label)

    kiiratas("math.log2(64)", math.log2(64))
    kiiratas("math.log2(128)", math.log2(128))
    print()
    kiiratas("math.log10(100)", math.log10(100))
    kiiratas("math.log10(10000)", math.log10(10000))
    print()
    kiiratas("math.sqrt(68)", math.sqrt(68))
    kiiratas("math.sqrt(125)", math.sqrt(125))
    print()
    
def pont43(label):
    print(label)
    adatok = [-math.pi, -math.pi/2, 0, math.pi/2, math.pi]
    txt = "\t           -math.pi -math.pi/2          0  math.pi/2    math.pi"
    print(txt)
    print("\tmath.sin", end="")
    for i in range (0, len(adatok), 1):
        kiiratas2(math.sin(adatok[i]))
    print()
    print("\tmath.cos", end="")
    for i in range (0, len(adatok), 1):
        kiiratas2(math.cos(adatok[i]))
    print()
    print()

def pont44(label):
    print(label)
    kiiratas("math.degrees(0)", math.degrees(0))
    kiiratas("math.degrees(1)", math.degrees(1))
    kiiratas("math.degrees(3.14)", math.degrees(3.14))
    kiiratas("math.degrees(math.pi)", math.degrees(math.pi))
    kiiratas("math.degrees(math.tau)", math.degrees(math.tau))
    print()
    kiiratas("math.radians(0)", math.radians(0))
    kiiratas("math.radians(90)", math.radians(90))
    kiiratas("math.radians(180)", math.radians(180))
    kiiratas("math.radians(270)", math.radians(270))
    kiiratas("math.radians(360)", math.radians(360))
    kiiratas("math.radians(-270)", math.radians(-270))
    kiiratas("math.radians(-180)", math.radians(-180))
    kiiratas("math.radians(-90)", math.radians(-90))
    
def pont45(label):
    print(label)
    print("\tEzekhez a függvényekhez nem kerültek példák bemutatásra.")

def pont46(label):
    print(label)
    print("\tEzekhez a függvényekhez nem kerültek példák bemutatásra.")

def pont47(label):
    print(label)
    kiiratas("math.pi", math.pi)
    kiiratas("math.e", math.e)
    kiiratas("math.tau", math.tau)
    kiiratas("math.inf", math.inf)
    kiiratas("math.nan", math.nan)

pont41("1.1. Számelméleti és ábrázolási függvények")
pont42("1.2. Hatvány- és logaritmikus függvények")
pont43("1.3. Trigonometrikus (szög-) függvények")
pont44("1.4. Szögátalakítás")
pont45("1.5. Hiperbolikus funkciók")
pont46("1.6. Speciális funkciók")
pont47("1.7. Állandók (konstansok)")
