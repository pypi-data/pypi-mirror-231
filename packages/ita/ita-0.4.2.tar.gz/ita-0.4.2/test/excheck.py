import ita

def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def foo(x, n):
    return x + (10 ** (-n))


def ex3_4(vp, vs, t):
  return (vp * vs) / (vp - vs) * t

def ex3_6(a,b):
  print('A =', a, 'B =', b)
  print('Arithmetic mean:', (a + b) / 2)
  print('Geometric mean:', (a * b) ** 0.5)

def ex5_6(image, y1, x1, y2, x2, color):
  if x2 - x1 >= y2 - y1:
    for i in range(x1, x2 + 1):
       y = round((i - x1) / (x2 - x1) * (y2 - y1) + y1)
       image[y][i] = color
  else:
    for i in range(y1, y2 + 1):
       x = round((i - y1) / (y2 - y1) * (x2 - x1) + x1)
       image[i][x] = color

print("*** pass ***")
ita.excheck.excheck(foo, [((1,8),1.0), ((1,9),1.0)])
ita.excheck.excheck(foo, [((1,5),1.0), ((1,6),1.0)], places=4)
print("*** fail ***")
ita.excheck.excheck(foo, [((1,6),1.0)])

print("*** pass ***")
ita.excheck.excheck(fib, [((1,),1), ((2,),2), ((6,),13),((25,),121393)])
print("*** fail ***")
ita.excheck.excheck(fib, [((25,),121393)], timeout=0.0001)

print("*** pass ***")
ita.excheck.excheck(ex3_4)
ita.excheck.excheck(ex3_6)
ita.excheck.excheck(ex5_6)


