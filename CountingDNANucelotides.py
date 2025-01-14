s = input()

A = 0
G = 0
C = 0
T = 0

for c in s:
    if c == 'A':
        A += 1
    elif c == 'G':
        G += 1
    elif c == 'C':
        C += 1
    elif c == 'T':
        T += 1

print(A, C, G, T)