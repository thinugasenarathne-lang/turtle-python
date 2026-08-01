import turtle
t=turtle.Turtle()
length=turtle.textinput("size","how long is one side")
ia=turtle.textinput("iner angle","the iner angle of each side")
side=turtle.textinput("sides","how many sides are in your shape")
for i in range (int(side)):
    t.fd((int(length)))
    t.rt(180-(int(ia)))
turtle.mainloop()