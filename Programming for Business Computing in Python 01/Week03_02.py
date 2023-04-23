AA = int(input())
A = 1000 - AA
B = A // 500
C = (A - A // 500 *500) // 100
D = (A - B*500 - C*100) // 50
E = (A - B*500 - C*100 - D*50) // 10
F = (A - B*500 - C*100 - D*50- E*10) // 5
G = (A - B*500 - C*100 - D*50- E*10 - F*5)



if B < 1 :
  B = None
else :
  B = str(B)+', 1;'

print (A)
print(f'{B} {C} {D} {E} {F} {G}')

#未完成