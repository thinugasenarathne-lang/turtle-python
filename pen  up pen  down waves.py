import turtle
t=turtle.Turtle()
for i in range (20,200,20):
    t.circle(i,90)
    t.up()
    t.circle(i,90)
    t.down()
turtle.mainloop()