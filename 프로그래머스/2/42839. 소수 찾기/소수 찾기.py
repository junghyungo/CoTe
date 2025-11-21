import itertools

def isPrime(number):
    for i in range(2, number):
        if (number % i == 0):
            return False
    return True
    
def solution(numbers):
    numbers = list(map(int, numbers))
    
    combs = []
    for i in range(1, len(numbers)+1):
        combs += list(itertools.permutations(numbers, i))
        
    num_combs = set()
    for comb in combs:
        num = 0
        for i in range(len(comb)):
            num += 10**i * comb[i]
        
        if num == 1 or num == 0:
            continue
        else:
            if (isPrime(num)):
                num_combs.add(num)
                
    return len(num_combs)
    