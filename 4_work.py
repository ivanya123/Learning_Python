def get_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort()
    return divisors


def function_prime_number(n):
    divisors = get_divisors(n)
    if len(divisors) == 2:
        return False, divisors
    else:
        return True, divisors


l, r = input().split()

count = 0
for i in range(int(l), int(r) + 1):
    bool_, divisors = function_prime_number(i)
    if bool_:
        if not function_prime_number(len(divisors))[0]:
            count += 1

print(count)
