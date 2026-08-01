import turtle
t=turtle.Turtle()
side=turtle.textinput("sides","how many sides are in your shape")
length=turtle.textinput("size","how long is one side")
for i in range(int(side)):
    t.fd((int(length)))
    t.rt(360/(int(side)))
turtle.mainloop()