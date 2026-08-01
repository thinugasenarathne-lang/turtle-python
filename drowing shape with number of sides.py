import turtle
t=turtle.Turtle()
side=(int(turtle.textinput("sides","how many sides side")))
ia=(((side-2)*180)/side)
for i in range(side):
    t.fd(100)
    t.rt(ia)
turtle.mainloop()