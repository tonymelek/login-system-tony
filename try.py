
# bar = [1, 'two', 3.33, [4], {5: 'five'}, (6)]
# print(bar)
# i = 0
# while i < 5:
#     if (i - 2) == 1:
#         break
#     print(i)
#     i += 1

for i in [5, 4, 2, 1]:
    if i > 2:
        continue
    else:
        print(i)
print("Test".find('st'))
print(([5, 4, 2, 1]).sort())

A0 = dict(zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5)))
A1 = range(10)
A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i: i*i for i in A1}
A6 = [[i, i*i] for i in A1]

print(A3)
