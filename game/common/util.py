import random
import os

def keepWithinRange(i, l, u):
    if i < l:
        i = l
    elif i > u:
        i = u
    return i


def RND(num):
    return random.randint(1, num)

def imagePath(filename):
    return os.path.join('img', filename)