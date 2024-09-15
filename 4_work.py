def get_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort()
    return divisors


def is_prime_or_composite(n):
    divisors = get_divisors(n)
    if len(divisors) == 2:
        return False, divisors
    else:
        return True, divisors


l, r = [int(i) for i in input().split()]

count = 0
for i in range(l, r + 1):
    bool_, divisors = is_prime_or_composite(i)
    if bool_:
        if not is_prime_or_composite(len(divisors))[0]:
            count += 1

print(count)
