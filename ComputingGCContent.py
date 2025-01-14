def gc_content(sequence):
    gc_count = sequence.count('G') + sequence.count('C')
    return (gc_count/len(sequence))*100
def parse_fasta(data):
    fasta_dict = {}
    lines = data.strip().split('\n')

    seq_name = None
    for line in lines:
        if line.startswith('>'):
            seq_name = line[1:]
            fasta_dict[seq_name] = ""
        else:
            fasta_dict[seq_name] += line
    return fasta_dict

with open("rosalind_gc.txt", "r") as file:
    s = file.read()
fasta_dict = parse_fasta(s)

max_gc = 0
max_label = None

for label, seq in fasta_dict.items():
    content = gc_content(seq)
    if content > max_gc:
        max_label = label
        max_gc = content

print(max_label)
print(max_gc)