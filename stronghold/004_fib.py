"""
Problem: Calculate the total number of rabbit pairs after n month with k offspring pairs per litter.

Given: Positive integers n≤40 and k≤5.
Return: The total number of rabbit pairs that will be present after n months, every pair of reproduction-age rabbits produces a litter of k rabbit pairs.
"""
from utils.file_reader import read_text

def rabbits_count(month:int,litter:int) -> int:
    if not (1 <= month <= 40) or not (1 <= litter <= 5):
        raise ValueError
    if month <= 2:
        return 1
    previous = 1
    pre_previous = 1
    for i in range(3, month+1):
        qnt = previous + litter * pre_previous
        pre_previous = previous
        previous = qnt
    return qnt

if __name__ == '__main__':
    assert rabbits_count(5,3) == 19
    data = read_text('../data/rosalind_fib.txt')
    x,y = map(int, data.split())
    print(rabbits_count(x,y))