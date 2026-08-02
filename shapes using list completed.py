t.down()
t.pensize(5)
t.pencolor("red")
for num in number:
    t.circle(num,180)
number2=[20,40,60,80,100,120,140,160,180,200]
t.up()
t.goto(0,0)
t.down()
t.pencolor("yellow")
for num2 in number2:
    t.fd(num2)
    t.rt(120)
number3=[20,40,60,80,100,120,140,160,180,200]
t.up()
t.goto(260,0)
t.down()
t.lt(120)
t.pencolor("green")
for num3 in number3:
    t.fd(num3)
    t.rt(90)
t.hideturtle()