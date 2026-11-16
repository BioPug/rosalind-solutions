"""
Problem: Calculate the Hamming Distance between two DNA sequences.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
Return: The Hamming distance dH(s,t).
"""
from utils.file_reader import read_lines

def hamming_distance(seq1: str, seq2: str) -> int:
    return sum(seq1 != seq2 for seq1, seq2 in zip(seq1, seq2))

if __name__ == '__main__':
    assert hamming_distance('GAGCCTACTAACGGGAT','CATCGTAATGACGGCCT') == 7
    data = read_lines('../data/rosalind_hamm.txt')
    print(hamming_distance(*data))



