#  coding=utf-8
#C6: simulate squear
#思想：逼近的近似值思路


def mysqrt(x, epsilon):
    assert x >=0
    assert epsilon > 0
    low = 0
    high = x
    guess = (low + high) / 2.0
    ctr = 1
    while abs(guess**2-x) > epsilon and ctr <=100:
        if low**2 < x:
            low = guess
        else:
            high = guess
        guess = (low+high)/2.0
        ctr += 1
    print guess

def testmysqrt():
    mysqrt(4,0.001)
    mysqrt(9,0.00001)
    mysqrt(1000,0.0001)

testmysqrt()



