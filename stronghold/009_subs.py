"""
Problem: Find all occurrences of a motif in a DNA string.

Given: Two DNA strings s and t (each of length at most 1 kbp).
Return: All locations of t as a substring of s.
"""

from utils.file_reader import read_lines

def finding_motiv(line1:str, line2:str) -> list[int]:
    motiv_found = []
    for i in range(len(line1) - len(line2) +1):
        if line1[i:i+len(line2)] == line2:
            motiv_found.append(i+1)
    return motiv_found

if __name__ == '__main__':
    assert finding_motiv('GATATATGCATATACTT', 'ATAT') == [2,4, 10]
    data = read_lines('../data/rosalind_subs.txt')
    x,y = data[0], data[1]
    print(*finding_motiv(x,y))