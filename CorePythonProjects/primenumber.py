def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def generate_prime_number(n, output=[]):
    i = 2
    while len(output) < n:
        if is_prime(i):
            output.append(i)
        
        i += 1
    return output

print(generate_prime_number(15))