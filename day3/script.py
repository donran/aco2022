#!/usr/bin/env python3
import sys, string
a = string.ascii_letters
d = [x.strip() for x in sys.stdin.readlines()]
print("star1:{}".format(sum([a.index((set(l[:len(l)//2]) & set(l[len(l)//2:])).pop())+1 for l in d])))
print("star2:{}".format(sum([a.index(list(set.intersection(*map(set,d[i:i+3])))[0])+1 for i in range(0,len(d),3)])))
print("star2:{}".format([a.index((x&y&z).pop())+1 for (x,y,z) in (map(set,d[i:i+3]) for i in range(0,len(d),3))]))

