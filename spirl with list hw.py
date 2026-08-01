import turtle
t=turtle.Turtle()
number=[10,20,30,40,50,60,70,80,90,100]
t.up()
t.goto(-260,0)
t.down()
t.pensize(5)
t.pencolor("red")
for num in number:
    t.circle(num,180)
turtle.mainloop()
