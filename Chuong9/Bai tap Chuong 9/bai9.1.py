def sign(x):
    if x<0:
        return -1
    if x>0:
        return 1
    else:
        return 0
print(sign(8))
print(sign(-8))
print(sign(0))