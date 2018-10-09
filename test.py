#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def h():
    print("wen")
    m = yield 5
    print(m, "m is")

    d = yield 12
    print(d, "d, is")

    e = yield 18
    print(e, "nana")

c = h()
# f1 = c.send(None)
# next(c)
# print(f1)
# f2 = next(c)
# print(f2)
next(c)
# f = c.send('Fight')
# print(f)
# g = next(c)
# print(g)