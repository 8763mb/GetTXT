AA = int(input())
A = 1000 - AA
B = A // 500
C = (A - A // 500 * 500) // 100
D = (A - B * 500 - C * 100) // 50
E = (A - B * 500 - C * 100 - D * 50) // 10
F = (A - B * 500 - C * 100 - D * 50 - E * 10) // 5
G = (A - B * 500 - C * 100 - D * 50 - E * 10 - F * 5)

output_list = []
if B > 0:
    output_list.append(f"500, {B}")
if C > 0:
    output_list.append(f"100, {C}")
if D > 0:
    output_list.append(f"50, {D}")
if E > 0:
    output_list.append(f"10, {E}")
if F > 0:
    output_list.append(f"5, {F}")
if G > 0:
    output_list.append(f"1, {G}")
    
print(';'.join(output_list))
