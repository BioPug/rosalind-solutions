"""
Problem: calculate the number of rabbits after n month, considering their limited lifespan.

Given: Positive integers n≤100 and m≤20.
Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.
"""
from utils.file_reader import read_text

def alive_rabbits(months: int, lifespan: int) -> int:
    generations = [1] + [0] * (lifespan - 1)
    for i in range(months - 1):
        new_pairs = sum(generations[1:])
        generations = [new_pairs] + generations[:-1]
    return sum(generations)

if __name__ == '__main__':
    assert alive_rabbits(6, 3) == 4
    data = read_text('../data/rosalind_fibd.txt')
    x,y = map(int, data.split())
    print(alive_rabbits(x, y))