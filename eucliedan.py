def rec_euc(a, b):
    if b == 0:
        return a
    return rec_euc(b, a % b)


def rec_euc2(a, b):
    if b != 0:
        return rec_euc(b, a % b)
    return a


def euc(a, b):
    while b != 0:
        m = a % b;
        a = b;
        b = m;
    return a


def kib_euc(a, b):
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


def rec_kib_euc(a, b, x, y):
    if a==0:
        x=0
        y=1
        return b
    x1=1
    y1=1
    lnko = rec_kib_euc(b%a, a,x1,y1)
    x=y1-(b//a)*x1
    y=x1
    return lnko


print(euc(139, 14))
print(rec_euc(139, 14))
print(str(rec_euc2(139, 14)) + "\n" + str(kib_euc(112, 63)))

lnko,x,y=kib_euc(112,63)
print(str(lnko) +" "+str(x)+" "+str(y))

print(rec_kib_euc(112,63,1,0))
