"""
Problem: Identify the string with the highest GC-content from FASTA file and returns its percentage and ID.

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
Return: The ID of the string having the highest GC-content, followed by the GC-content of that string.
"""
from utils.file_reader import read_fasta

def calculate_gc_content(dna:str) -> float:
    if not dna:
        return 0.0
    gc_count = dna.count('G')+dna.count('C')
    return (gc_count / len(dna)) * 100

if __name__ == '__main__':
    assert calculate_gc_content("CGCG") == 100.0
    highest_gc = -1.0
    highest_id = ''
    dna = read_fasta('../data/rosalind_gc.txt')
    for k,v in dna.items():
       current_gc = calculate_gc_content(v)
       if current_gc > highest_gc:
           highest_gc = current_gc
           highest_id = k
    print(f'{highest_id}\n{highest_gc}')
