# -*- coding: utf-8 -*-

import random
zh_ex = u"正"
fu_ex = u"反"
zh_count = 0
fu_count = 0

def toss_a_coin():
    val = random.randint(0, 1)
    return val

def toss_coins(loop):
    a = b = 0
    i = 0
    while i < loop:
        val = toss_a_coin()
        if val == 1:
            a += 1
	else:
            b += 1
        i += 1
    return a, b

if '__main__' == __name__:
    n = input( "Input the number you would try:")
    zh_count, fu_count = toss_coins(n)
    print "The %s count is %d, %s count is %d" % (zh_ex, zh_count, fu_ex, fu_count)
    
