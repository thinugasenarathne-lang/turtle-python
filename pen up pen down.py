import turtle
t=turtle.Turtle()
for i in range (10):
    t.down()
    t.fd(10)
    t.up()
    t.fd(10)
t.goto(100,100)
t.rt(90)
for i in range (10):
    t.down()
    t.fd(10)
    t.up()
    t.fd(10)
turtle.mainloop()