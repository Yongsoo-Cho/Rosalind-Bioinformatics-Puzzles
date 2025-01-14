with open("rosalind_hamm.txt", "r") as file:
    input = file.read().split('\n')

count = 0

s = input[0]
t = input[1]

for i in range(len(s)):
    if(s[i]!=t[i]):
        count += 1

print(count)