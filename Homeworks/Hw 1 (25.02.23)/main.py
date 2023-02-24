import math

def gr(R,m2):
    G = 6.6743 * pow(10,-11)
    mZ = 5.97600 * pow(10,24)
    F = G * ((mZ * m2)/pow(R,2))
    return "{:.10f}".format(F)


R = float(input())
R = R * 1000
m2 = float(input())
#степень числа 10 в массе
m3 = float(input())
m2 = m2 * pow(10,m3)
print(gr(R,m2))