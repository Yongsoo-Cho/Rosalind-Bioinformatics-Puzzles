s = input()

complements = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
res = ''.join(complements[c] for c in reversed(s))

print(res)