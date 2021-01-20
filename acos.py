import fractions
import itertools

def acos():
    """
    This is the main function of this module.
    yields the coefficients of the infinite series for acos(1 - x/2).
    The first coefficient is for x^0.5, the second is for x^1.5 etc.
    """
    return sqrt(itertools.islice(inverse(2*x for x in _cos_coefs()), 1, None))

def inverse(coefs):
    """
    Yields the coefficients of the inverse of coefs. coefs[0] must be 0;
    coefs[1] must be non-zero.
    """
    coefs = iter(coefs)
    coeflist = []
    coeflist.append(next(coefs))
    coeflist.append(fractions.Fraction(next(coefs)))
    result = [fractions.Fraction(0), 1 / coeflist[1]]
    yield result[0]
    yield result[1]
    for i in itertools.count(2):
        next_coef = next(coefs, _no_more)
        if next_coef is not _no_more:
            coeflist.append(fractions.Fraction(next_coef))
        sum = fractions.Fraction(0)
        for j in range(2, min(i+1, len(coeflist))):
            sum += _pow_term(result, j, i) * coeflist[j]
        next_term = -sum / coeflist[1]
        result.append(next_term)
        yield next_term

def eval(coefs, x, terms=10):
    """
    Evaluates coefs at x. The optional parameter terms indicates how many
    terms to evaluate in case coefs does not have a finite length. coefs[0] is
    the constant coefficient. coefs[1] is the coefficient of x. coefs[2] is
    the coefficient of x^2 etc.
    """
    prod = 1
    result = 0.0
    if not hasattr(coefs, '__len__'):
        coefs = take(coefs, terms)
    for coef in coefs:
        result += coef*prod
        prod *= x
    return result

def sqrt(coefs):
    """
    Yields the coefficients of the sqrt of coefs. coefs[0] must be one.
    """
    coefs = iter(coefs)
    next(coefs)
    result = [fractions.Fraction(1)]
    yield result[0]
    for i in itertools.count(1):
        sum = fractions.Fraction(0)
        for j in range(1, i):
            sum += result[j]*result[i-j]
        next_term = (fractions.Fraction(next(coefs, 0)) - sum) / 2
        result.append(next_term)
        yield next_term

def take(series, count):
    """
    Returns the first count values of series.
    """
    return list(itertools.islice(series, count))

_no_more = object()

def _cos_coefs():
    """
    Yields 0, 1/2!, -1/4!, 1/6! etc
    """
    yield 0
    sign = 1
    prod = 2
    for i in itertools.count(2, 2):
        yield fractions.Fraction(sign, prod)
        sign *= -1
        prod *= i+1
        prod *= i+2

def _sums(total, count):
    """
    Generates all the sequences of positive integers that add up to total.
    count is the number of integers in each sequence. For example,
    _sums(4, 3) yiels [1, 1, 2], [1, 2, 1], [2, 1, 1].
    """
    for combo in itertools.combinations(range(1, total), count - 1):
        last = 0
        result = []
        for x in combo:
            result.append(x - last)
            last = x
        result.append(total - last)
        yield result

def _pow_term(p, pow, term):
    """
    Computes the coefficient of x^term of p^pow. p is a list of coefficients.
    p[0]=0, p[1] is the coefficient of x. p[2] is the coefficient of x^2
    etc.
    """
    result = fractions.Fraction(0)
    for terms in _sums(term, pow):
        prod = fractions.Fraction(1)
        for t in terms:
            prod *= p[t]
        result += prod
    return result
