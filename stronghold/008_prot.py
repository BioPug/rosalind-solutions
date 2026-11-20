"""
Problem: Translate an RNA string into the protein string it encodes.

Given: An RNA string s corresponding to a strand of mRNA.
Return: The protein string encoded by s.
"""

from utils.file_reader import read_text
from utils.bio_tables import RNA_CODON_TABLE

def rna_into_protein(seq:str) -> str:
    codons = []
    protein = []
    for i in range(0,len(seq),3):
        codons.append(seq[i:i+3])
    for codon in codons:
        amino_acid = RNA_CODON_TABLE[codon]
        if amino_acid == 'Stop':
            break
        protein.append(amino_acid)
    return ''.join(protein)

if __name__ == '__main__':
    assert rna_into_protein('AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA') == 'MAMAPRTEINSTRING'
    data = read_text('../data/rosalind_prot.txt')
    print(rna_into_protein(data))

