def primes_upto(n, multiples = set(), output=[]):
    for i in range(2, n + 1):
        if i not in multiples:
            output.append(i)
            multiples_to_n = range(i * i, n + 1, i)
            if multiples_to_n:
                multiples.update(multiples_to_n)
    
    return output

n = int(raw_input("Generate prime number up to: "))
print primes_upto(n)