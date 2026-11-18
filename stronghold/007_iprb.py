"""
Problem: Calculate the probability of producing an offspring with a dominant phenotype from random mating.

Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor,
 m are heterozygous, and n are homozygous recessive.
Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele. Assume that any two organisms can mate.
"""

from utils.file_reader import read_lines

def dominant_phenotype(k: int, m: int, n: int) -> float:
    total = k + m + n
    genotype_aa_aa = (n/total)*((n-1)/(total-1)) * 1.0
    genotype_Aa_Aa = (m/total)*((m-1)/(total-1)) * 0.25
    genotype_Aa_aa = 2 *((m*n)/(total*(total-1))) * 0.5
    recessive_phen = genotype_Aa_Aa + genotype_Aa_aa + genotype_aa_aa
    return 1 - recessive_phen

if __name__ == '__main__':
    result = dominant_phenotype(2,2,2)
    assert round(result,5) == 0.78333
    data = read_lines('../data/rosalind_iprb.txt')
    x,y,z = map(int, data[0].split())
    print(dominant_phenotype(x,y,z))


