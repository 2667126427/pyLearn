import math

Urv = 0.0125
Uri = 0.15
U = 1.52
I = 15.7

Ur = math.sqrt((Urv / U)**2 + (Uri / I)**2)
print(Ur)
