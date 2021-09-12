# 27

bag = []
for i in range(3712, 8432 + 1):
    if i % 4 == i % 2:
        if not (i % 13) or not (i % 14) or not (i % 15):
            bag.append(i)
print(len(bag), bag[0])

# 34
bag = []
range4 = range(3 * 4 ** 4 + 3 * 4 ** 3 + 3 * 4 ** 2 + 3 * 4 ** 1 + 3 * 4 ** 0, 4 ** 6)
for i in range(1000, 9999 + 1):
    if i % 3 and i % 17 and i % 19:
        if i in range4:
            bag.append(i)
print(bag[0], bag[-1])

# 40
bag = []
for i in range(1871, 9197 + 1):
    if len(str(i)) != len(hex(i)) - 2:
        if i % 9 == 2 or i % 9 == 4:
            bag.append(i)
print(len(bag), bag[0])

# 51
bag = []
range7 = range(6 * 7 ** 5 + 6 * 7 ** 4 + 6 * 7 ** 3 + 6 * 7 ** 2 + 6 * 7 ** 1 + 6 * 7 ** 0, 7 ** 7)
for i in range7:
    if i % 3 == 2 and i % 8 != 3 and i % 12 != 5:
        bag.append(i)
print(len(bag), bag[-1])

# 53 вот это я не поняла
bag = []
for i in range(10, 1178 + 1):
    if not (i % 2):
        if i % 10 != 0 and i % 10 != 2 and i % 10 != 6 and i % 10 != 8 and i % 100 != 14:
            bag.append(i)
print("53:", sum(bag), bag[0])

# 74
bag = []
mini = 30000
for i in range(5903, 174203 + 1):
    if len(set(str(i))) == len(list(str(i))):
        if len(list(filter(lambda x: int(x) > 4, list(str(i))))) == 3:
            bag.append(i)
            if 30000 - i < mini and 30000 - i > 0:
                mini = i
print(len(bag), mini)

# 85
bag = []
for i in range(15000, 25000 + 1):
    if [i % 7, i % 11, i % 17, i % 19].count(0) == 2:
        bag.append(i)
print(len(bag), bag[-1])

# 155
file = [int(i) for i in open('17-1.txt').read().split()]
bag = []
for i in range(len(file) - 2):
    if file[i] > file[i + 1] and file[i + 1] < file[i + 2]:
        bag.append(i)
print(len(bag), max(bag))
