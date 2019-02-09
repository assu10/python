import turtle as t

t.shape('turtle')
# for i in range(4):
#     t.forward(100)
#     t.right(90)

# n = int(input(0))
# t.color('red')
# t.begin_fill()
# for i in range(n):
#     t.forward(100)
#     t.right(360/n)
# t.end_fill()

#t.circle(120)

# n = 60
#
# t.speed('fastest')
#
# for i in range(n):
#     t.circle(120)
#     t.right(360/n)

t.speed('fastest')

for i in range(300):
    t.forward(i)
    t.right(91)
t.mainloop()