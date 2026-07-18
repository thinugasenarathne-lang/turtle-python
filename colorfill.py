import turtle
t=turtle.Turtle()
t.color("red")
t.fillcolor("yellow")
t.begin_fill()
t.circle(50)
t.end_fill()

t.fillcolor("green")
t.begin_fill()
for _ in range (4):
    t.lt(90)
    t.fd(50)
t.end_fill()
turtle.mainloop()
