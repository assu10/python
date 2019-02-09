import turtle as t

n,len = map(int, input().split())
t.shape('turtle')
t.speed('fastest')

for i in range(n):
    t.fd(len)
    t.rt((360/n)*2)
    t.fd(len)
    t.lt(360/n)

t.mainloop()