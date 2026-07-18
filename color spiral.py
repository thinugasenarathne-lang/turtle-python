import turtle
t=turtle.Turtle()
turtle.colormode(255)
t.pensize(3)
for i in range(20,200,20):
    t.circle(i,180)
    t.color(50,i,200)
turtle.mainloop()
