import fractions
import itertools

def acos(count):
    """
    This is the main function of this module.
    Returns a list containing the coefficients of the infinite series for
    acos(1 - x/2). The first coefficient is for x^0.5, the second is for
    x^1.5 etc. count is the number of coefficients to return.
    """
    x = acos_square(count)
    return sqrt(x[1:], count)

def sqrt(coef, count):
    """
    Returns the sqrt of coef. coef is a list of ints or fractions. coef[0]
    is always 1 and is the coefficient of x^0. coef[1] is the coefficient of
    x. coef[2] is the coefficient of x^2 etc. Of the returned list, the
    first value is always 1, the second value is the coefficient of x, the
    third value is the coefficient of x^2 etc. count is the number of
    coefficients to return. For example, sqrt([1, 1], 3) = [1, 1/2, -1/8]
    """
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

def sums(total, count):
    """
    Generates all the sequences of positive integers that add up to total.
    count is the number of integers in each sequence. For example,
    sums(4, 3) yiels [1, 1, 2], [1, 2, 1], [2, 1, 1].
    """
    for combo in itertools.combinations(range(1, total), count - 1):
        last = 0
        result = []
        for x in combo:
            result.append(x - last)
            last = x
        result.append(total - last)
        yield result

def factorial(x):
    """Returns x!"""
    result = 1
    for i in range(1, x+1):
        result *= i
    return result

def acos_square(count):
    """
    Like acos but returns the infinite series for (acos(1 - x/2))^2 as a list
    of coefficients. The first coefficient is 0. The second is for x,
    the third is for x^2 etc. count is the number of non zero coefficients to
    return.  acos_square(3) = [0, 1, 1/12, 1/90]
    """
    result = [0, fractions.Fraction(1)]
    for i in range(2, count+1):
        sum = fractions.Fraction(0)
        sub = 1
        for j in range(2, i+1):
            sum += pow_term(result, j, i) / factorial(2*j) * sub
            sub *= -1
        result.append(2*sum)
    return result

def pow_term(p, pow, term):
    """
    Computes the coefficient of x^term of p^pow. p is a list of coefficients.
    p[0]=0, p[1] is the coefficient of x. p[2] is the coefficient of x^2
    etc.
    """
    result = fractions.Fraction(0)
    for terms in sums(term, pow):
        prod = fractions.Fraction(1)
        for t in terms:
            prod *= p[t]
        result += prod
    return result
