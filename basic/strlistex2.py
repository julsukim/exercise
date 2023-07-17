stem_leaf = []
score = [0, 0, 2, 4, 7, 7, 9, 11, 11, 13, 18, 20]

leaf0 = []
leaf1 = []
leaf2 = []

for i in score:
    if i < 10:
        leaf0.append(i)
    elif i < 20:
        leaf1.append(int(str(i)[-1]))
    elif i < 30:
        leaf2.append(int(str(i)[-1]))

stem_leaf = [leaf0, leaf1, leaf2]

for s in range(len(stem_leaf)):
    print(f'{s}: {stem_leaf[s]}')