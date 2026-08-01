import turtle
t=turtle.Turtle()
p=300
while True:
    u1=turtle.textinput("User 01","Talk")
    u1r="User: "+u1
    t.color("red")
    t.up()
    t.goto(-400,p)
    p=p+-50
    t.down()
    t.write(u1r,font=("arial",20,"bold"),align="left")
    if u1== "exit":
        t.up()
        t.goto(-300,p)
        t.down()
        t.color("black")
        t.write("User 01 has left",font=("arial",20,"bold"),align="left")
        break
    u2=turtle.textinput("User 02","Talk")
    u2r=u2+"User: "
    t.color("yellow")
    t.up()
    t.goto(390,p)
    p=p+-50
    t.down()
    t.write(u1r,font=("arial",20,"bold"),align="right")
    if u2== "exit":
        t.up()
        t.goto(300,p)
        t.down()
        t.color("black")
        t.write("User 01 has left",font=("arial",20,"bold"),align="left")
        break