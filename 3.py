A0 = dict(zip(('a','b','c','d','e'),('1','2','3','4','5')))
A1 = list(range(10))
A2 = [i for i in A1 if i in A0]
A3 = sorted(A0[i] for i in A0)
A4 = [[i,i*i] for i in A1]

for key in list(globals()):
    if key.startswith('A'):
        print(key,globals()[key])
