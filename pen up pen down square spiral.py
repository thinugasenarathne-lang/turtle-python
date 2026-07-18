import turtle
t=turtle.Turtle()
for i in range (5,100,5):
    t.fd(i)
    t.up()
    t.fd(i)
    t.down()
    t.fd(i)
    t.rt(90)
   

    t.fd(i)
turtle.mainloop()