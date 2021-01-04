import fractions
import itertools

def acos(terms):
    x = acos_square(terms)
    return sqrt(x[1:], terms)

def sqrt(coef, count):
    coef = [fractions.Fraction(x) for x in coef]
    while len(coef) < count:
        coef.append(fractions.Fraction(0))
    result = [fractions.Fraction(1)]
    for i in range(1, count):
        sum = fractions.Fraction(0)
        for j in range(1, i):
            sum += result[j]*result[i-j]
        result.append((coef[i] - sum) / fractions.Fraction(2))
    return result

def sum_count(total, terms):
    for combo in itertools.combinations(range(1, total), terms - 1):
        last = 0
        result = []
        for x in combo:
            result.append(x - last)
            last = x
        result.append(total - last)
        yield result

def factorial(x):
    result = 1
    for i in range(1, x+1):
        result *= i
    return result

def acos_square(terms):
    result = [0, fractions.Fraction(1)]
    for i in range(2, terms+1):
        sum = fractions.Fraction(0)
        sub = 1
        for j in range(2, i+1):
            sum += pow_term(result, j, i) / factorial(2*j) * sub
            sub *= -1
        result.append(2*sum)
    return result

def pow_term(p, pow, term):
    result = fractions.Fraction(0)
    for terms in sum_count(term, pow):
        prod = fractions.Fraction(1)
        for t in terms:
            prod *= p[t]
        result += prod
    return result
