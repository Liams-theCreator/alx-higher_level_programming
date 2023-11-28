#!/usr/bin/python3
for a in range(ord('a'), ord('z')):
    if chr(a) == 'q' or chr(a) == 'e':
        continue
    else:
        print(chr(a), end="")
