from random import random

c = []
w = []
T = []
k = random()*0.05
b = random()*0.002

for i in range(6):
    c.append(random()*55)
    w.append(random()*10)

c.sort()

print 'c=',c

T = []
for i in range(6):
    T.append(100*10**(-(c[i]*k + b))+ w[i])


print 'T=',T