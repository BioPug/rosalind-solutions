"""
Problem: Calculate a consensus string and profile matrix for collection of DNA strings.

Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)
"""

from utils.file_reader import read_fasta

def build_matrix(seqs: list[str]) -> dict[str, list[int]]:
    length = len(seqs[0])
    matrix = {nt: [0] * length for nt in 'ACGT'}
    for i in seqs:
        for x, nt in enumerate(i):
            matrix[nt][x] += 1
    return matrix

def consensus_string(matrix: dict[str, list[int]]) -> str:
    consensus = ''.join(max('ACGT', key = lambda nt: matrix[nt][i]) for i in range(len(matrix['A'])))
    return consensus


if __name__ == '__main__':
    sample = ['ATCCAGCT', 'GGGCAACT', 'ATGGATCT', 'AAGCAACC', 'TTGGAACT', 'ATGCCATT', 'ATGGCACT']
    assert consensus_string(build_matrix(sample)) == 'ATGCAACT'
    _strings = []
    data = read_fasta('../data/rosalind_cons.txt')
    for k, v in data.items():
        _strings.append(v)
    with open('../data/010_cons_output.txt', 'w', encoding='utf-8') as file:
        file.write(consensus_string(build_matrix(_strings))+'\n')
        for k, v in build_matrix(_strings).items():
            result = f'{k}: {'  '.join(map(str, v))}\n'
            file.write(result)




