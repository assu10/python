import turtle as t

n = 5
t.shape('arrow')
for i in range(5):
    t.fd(100)
    t.rt((360/n)*2)
    t.fd(100)
    t.lt(360/n)