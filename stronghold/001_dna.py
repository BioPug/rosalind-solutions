"""
Problem: Counting DNA Nucleotides

Given: A DNA string s of length at most 1000 nt.
Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
"""

def count_nt(dna: str) -> list[int]:
    nt_list = [dna.count('A'), dna.count('C'), dna.count('G'),dna.count('T')]
    return nt_list

if __name__ == '__main__':
    sample = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
    assert count_nt(sample) == [20,12,17,21]

    with open('../data/rosalind_dna.txt', 'r', encoding='utf-8') as file:
        data = file.read().strip()
    result = count_nt(data)
    print(*result)
