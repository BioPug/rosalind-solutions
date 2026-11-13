"""
Problem: Complementing a Strand of DNA

Given: A DNA string s of length at most 1000 nt.
Return: The reverse complement sc of s.
"""

def dna_complementing(dna: str) -> str:
    comp_strand = dna.maketrans('ATGC','TACG')
    return dna.translate(comp_strand)[::-1]

if __name__ == "__main__":
    sample = 'AAAACCCGGT'
    assert dna_complementing(sample) == 'ACCGGGTTTT'

    with open('../data/rosalind_revc.txt', 'r', encoding='utf-8') as file:
        data = file.read().strip()
    result = dna_complementing(data)
    with open('../data/003_revc_output.txt', 'w', encoding='utf-8') as file:
        file.write(result)