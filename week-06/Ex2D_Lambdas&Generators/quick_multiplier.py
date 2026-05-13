# Doubler 

doubler = lambda n: n * 2

print(doubler(8))
print(doubler(-4))
print(doubler("banana"))

# Tripler 
triple = lambda n: n * 3

print(triple(8))
print(triple(-4))
print(triple("banana"))

def multiplier(x):
    return lambda n: n * x 

quadrupler = multiplier(4)
quintupler = multiplier(5)
sextupler = multiplier(6)
septupler = multiplier(7)
octupler = multiplier(8)
nonupler = multiplier(9)
decupler = multiplier(10)

print(quadrupler(2))
print(quintupler(2))
print(sextupler(2))
print(septupler(2))
print(octupler(2))
print(nonupler(2))
print(decupler(2))