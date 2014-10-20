def gcd(a, b):
    if a == b:
        return b
    elif a > b:
        return gcd(a - b, b)
    else:
        return gcd(a, b - a)


def simplify_fraction(fraction):
    nom = fraction[0]
    denum = fraction[1]
    g = gcd(nom, denum)
    nom //= g
    denum //= g
    return (nom, denum)
