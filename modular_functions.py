#raises 'a' base to 'e' exponent and takes it's mod
def modpow(a, e, m):
    result =1
    apow =a
    while (e != 0):
        if (e & 0x01 == 0x01):
            result = (result * apow) % m
        e >>=1
        apow=(apow*apow) % m
    return result


def modinvers(a, m):
    gcd, x, y = ext_euc(a,m);
    if x<0:
        return x+m
    return x


def ext_euc(a, b):
    x0 = 1;x1 = 0
    y0 = 0;y1 = 1
    n = 1
    while b != 0:
        r = a % b
        q = a // b
        a = b
        b = r
        x = x1
        y = y1
        x1 = q * x1 + x0
        y1 = q * y1 + y0
        x0 = x
        y0 = y
        n = -n
    x = n * x0
    y = -n * y0
    return a, x, y