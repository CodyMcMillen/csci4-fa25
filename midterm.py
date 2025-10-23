#python

list = [2, 3, 5, 7, 13, 17, 19, 31]

for n in list:
    print((2**n - 1) * (2**(n-1)))