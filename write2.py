import turtle
name=input("what is your name")
mesagge="Hi "+name
t=turtle.Turtle()
t.write(mesagge,font=("arial",20,"bold"),align="center")
t.hideturtle
turtle.mainloop()