from random import random, randint

c = []
w = []
T = []
k = random()*0.05
b = random()*0.002
n = randint(6,50)


for i in range(n):
    c.append(random()*55)
    w.append(random()*10)

c.sort()

print 'c=',c

T = []
for i in range(n):
    T.append(100*10**(-(c[i]*k + b))+ w[i])


print 'T=',T