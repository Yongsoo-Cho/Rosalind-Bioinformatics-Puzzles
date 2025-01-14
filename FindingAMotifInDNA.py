with open('rosalind_subs.txt', 'r') as file:
    s = file.read().strip().split('\n')

seq = s[0]
motif = s[1]

res = []

for i in range(len(seq)-len(motif)+1):
    if(motif == seq[i:i+len(motif)]):
        res.append(i+1)

print(' '.join(map(str, res)))

# KMP Algorithm is better since it's O(n+m), and this is O(n*m).
# Practically speaking does not really matter, but probably good to know.

# Love this man:
# https://www.youtube.com/watch?v=V5-7GzOfADQ