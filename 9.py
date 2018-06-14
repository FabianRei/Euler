
n = 1000

class BreakIt(Exception): pass


try:
    for a in range(3,int(n/3)):
        for b in range(2,int((n-a)/2)):
            c = n-b-a
            if a<b<c and a+b+c == n and a ** 2 + b ** 2 == c ** 2:
                print('found!')
                raise BreakIt
except BreakIt:
    pass

print(a, b, c)
print(a*b*c)
print( a** 2 + b ** 2,  c ** 2)
