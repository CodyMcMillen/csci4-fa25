print("hello World")

import array as arr

a = arr.array(
    'h', # opcode for unsigned short 
    [26] # list
)

b = arr.array('l', [1, 2, 3, 4, 5])

print(a.pop())

print(b.pop())

