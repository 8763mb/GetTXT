AA = int(input())
A = 1000 - AA
B = A // 500
C = (A - A // 500 * 500) // 100
D = (A - B * 500 - C * 100) // 50
E = (A - B * 500 - C * 100 - D * 50) // 10
F = (A - B * 500 - C * 100 - D * 50 - E * 10) // 5
G = (A - B * 500 - C * 100 - D * 50 - E * 10 - F * 5)

if B < 1:
  B = None
else:
  B = '500, ' + str(B)

if C < 1:
  C = None
else:
  C = '100, ' + str(C)

if D < 1:
  D = None
else:
  D = '50, ' + str(D)

if E < 1:
  E = None
else:
  E = '10, ' + str(E)

if F < 1:
  F = None
else:
  F = '5, ' + str(F)

if G < 1:
  G = None
else:
  G = '5, ' + str(G)

if B is not None:
  print(B, end=';')
if C is not None:
  print(C, end=';')
if D is not None:
  print(D, end=';')
if E is not None:
  print(E, end=';')
if F is not None:
  print(F, end=';')
if G is not None:
  print(G)
