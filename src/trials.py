import random

a = [1, 8, 3]
a.append(int((1 / a.pop()) * a.pop()))
print([[0, 1], [0, -1], [1, 0], [-1, 0]][random.randint(0, 3)] )