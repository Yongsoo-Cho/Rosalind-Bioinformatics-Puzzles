with open('txt', 'r') as file:
    s = file.read().split('\n')
sequences = [seq for seq in s if seq[0]=='>']

#to be continued...