import ita

print("version of ita:", ita.__version__)

assert(len(ita.gen_hw_data()) == 2)
assert(len(ita.gen_spring_data()) == 2)
assert(sum(map(len,ita.lifegame_glider())) == 64)
assert(sum(map(len,ita.lifegame_acorn())) == 4800)


