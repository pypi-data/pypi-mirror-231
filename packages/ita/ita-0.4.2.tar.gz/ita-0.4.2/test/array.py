import ita

x = ita.array.make1d(10)
assert(len(x) == 10 and x[0] == 0 and x[-1] == 0)
x = ita.array.make1d(20, value='a')
assert(len(x) == 20 and x[0] == 'a' and x[-1] == 'a')
x = ita.array.make1d(5, value='a', random=True)
assert(len(x) == 5 and 0 <= x[0] <=1 and 0<= x[-1] <= 1)

x = ita.array.make2d(10,20)
assert(len(x) == 10 and len(x[0]) == 20 and len(x[-1]) == 20)

x = ita.array.make3d(5,8,11)
assert(len(x) == 5 and len(x[0]) == 8 and len(x[-1]) == 8)
assert(len(x[0][0]) == 11 and len(x[1][1]) == 11 and len(x[-1][-1]) == 11)

x = ita.array.make2d(3,4, value="hoge")
x[1][2] = "fuga"
ita.array.print2d(x, colLabels=["col"]*4, rowLabels=["row"]*3)


