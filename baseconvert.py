from math import gcd


def coprime(a, b):
    return gcd(a, b) == 1


def number_to_base(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]


def num_to_bal_base(n,b):
    if n == 0:
        return [0]
    digits = []
    while n:
        n, rem = n//b, n%b
        if rem > b//2:
            n, rem = n+1, rem-b
        digits.append(rem)
    return digits[::-1]


def report(nums, bases):
    for num in nums:
        for base in bases:
            print(f'base10: {num},'
                  f' balanced base{base}: {num_to_bal_base(num, base)},'
                  f' base{base}: {number_to_base(num, base)}')
        print()


if __name__ == '__main__':
    base = 12
    r = base
    # for num in range(1000):
    #     x = num_to_bal_base(num, base)
    #     y = num_to_bal_base(num, base+1)
    #     z = num_to_bal_base(num, base-1)
    #     print(num, z, x, y)
    bases = [3, ]
    nums = range(3, 13*4 + 1)
    report(nums=nums, bases=bases)
    print()
    for num in range(3, 102, 2):
        if coprime(num, num+2):
            print(num, num+2)
        else:
            print("aaaaaaaaa!", num)

"""
    base = 3
    num = 3  # base**6
    num2 = 16  # (1+base)**6
    x = num_to_bal_base(num, base - 1)
    y = num_to_bal_base(num, base)
    z = num_to_bal_base(num, base + 1)
    print(len(str(num)), x, y, z)
    x = num_to_bal_base(num2, base - 1)
    y = num_to_bal_base(num2, base)
    z = num_to_bal_base(num2, base + 1)
    print(len(str(num2)), x, y, z)
    n = []
    for off in range(10):
        print(num_to_bal_base(num, base+off))
        x = num_to_bal_base(num, base + off)[-1]
        n.append(abs(x))
    print(n)"""
