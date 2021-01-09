# acos

Python code to find the infinite series for acos(1 - 0.5*x) around x = 0.

acos(1 - 0.5*x) = a0 * x^0.5 + a1 * x^1.5 + a2 * x^2.5 + a3 * x^3.5 + ...
around x = 0. This program finds the a0, a1, a2, a3, ...

```
>>> acos.take(acos.acos(), 4)
[Fraction(1, 1), Fraction(1, 24), Fraction(3, 640), Fraction(5, 7168)]
```

So acos(1 - 0.5*x) = x^0.5 + x^1.5 / 24 + 3 * x^2.5 / 640 + 5 * x^3.5 / 7168 + ...
