"""
Problem: Transcribing DNA into RNA

Given: A DNA string t of length at most 1000 nt.
Return: The transcribed RNA string of t.
"""

def dna_to_rna(dna: str) -> str:
    rna = dna.replace('T','U')
    return rna

if __name__ == '__main__':
    sample = 'GATGGAACTTGACTACGTAAATT'
    assert dna_to_rna(sample) == 'GAUGGAACUUGACUACGUAAAUU'

    with open('../data/rosalind_rna.txt', 'r', encoding='utf-8') as file:
        data = file.read().strip()
        result = dna_to_rna(data)
    with open('../data/002_rna_output.txt', 'w', encoding='utf-8') as file:
        file.write(result)

