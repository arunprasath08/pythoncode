import turtle as t

t.getscreen()
t.bgcolor("white")

#CircleOne
t.pensize(25)
t.pencolor("red")
t.circle(150)

#CircleTwo
t.lt(90)
t.fd(20)
t.pencolor("white")
t.fd(25)
t.pencolor("red")
t.rt(90)
t.circle(100)
t.lt(90)
t.fd(22)
t.pencolor("white")
t.fd(50)
t.lt(130)

#Star
t.pensize(10)
t.pencolor("blue")
t.fd(60)
t.rt(150)
t.fd(60)
t.lt(80)
t.fd(60)
t.rt(150)
t.fd(60)
t.lt(80)
t.fd(60)
t.rt(150)
t.fd(60)
t.lt(80)
t.fd(60)
t.rt(150)
t.fd(60)
t.lt(80)
t.fd(60)
t.rt(150)
t.fd(60)

#Portion1

t.lt(70)
t.fd(60)
t.lt(170)
t.fd(60)

t.rt(175)
t.fd(60)
t.lt(175)
t.fd(60)

t.rt(175)
t.fd(57)
t.lt(175)
t.fd(60)

t.rt(175)
t.fd(57)
t.lt(175)
t.fd(60)

t.rt(175)
t.fd(57)
t.lt(175)
t.fd(60)

t.rt(175)
t.fd(57)
t.lt(175)
t.fd(60)

t.rt(175)
t.fd(56)
t.lt(175)
t.fd(60)

t.rt(175)
t.fd(55)
t.lt(175)
t.fd(60)

t.rt(175)
t.fd(50)
t.lt(175)
t.fd(60)

t.rt(175)
t.fd(45)
t.lt(175)
t.fd(47)

#Portion2

t.lt(88)
t.fd(54)
t.lt(175)
t.fd(47)

t.lt(175)
t.fd(54)
t.rt(175)
t.fd(47)

t.lt(175)
t.fd(52)
t.rt(175)
t.fd(63)

t.lt(175)
t.fd(54)
t.rt(175)
t.fd(50)

t.lt(175)
t.fd(54)
t.rt(175)
t.fd(50)

t.lt(175)
t.fd(54)
t.rt(175)
t.fd(50)

t.lt(175)
t.fd(54)
t.rt(175)
t.fd(47)

t.lt(175)
t.fd(54)
t.rt(175)
t.fd(49)

t.lt(175)
t.fd(53)
t.rt(175)
t.fd(48)

t.lt(175)
t.fd(52)
t.rt(175)
t.fd(47)

t.lt(175)
t.fd(50)
t.rt(175)
t.fd(42)

t.lt(175)
t.fd(46)

#Portion3

t.lt(90)
t.fd(50)
t.rt(170)
t.fd(50)

t.lt(175)
t.fd(50)
t.rt(175)
t.fd(48)

t.lt(170)
t.fd(50)
t.rt(170)
t.fd(46)

t.lt(170)
t.fd(50)
t.rt(170)
t.fd(45)

t.lt(170)
t.fd(46)
t.rt(170)
t.fd(42)

t.lt(170)
t.fd(41)
t.rt(170)
t.fd(36)

t.lt(170)
t.fd(36)
t.rt(170)
t.fd(31)

t.lt(170)
t.fd(31)
t.rt(170)
t.fd(25)

t.lt(170)
t.fd(25)
t.rt(170)
t.fd(20)

t.lt(170)
t.fd(20)
t.rt(170)
t.fd(15)

t.lt(170)
t.fd(25)

#Portion4
t.lt(65)
t.fd(50)
t.rt(180)
t.fd(55)

t.lt(175)
t.fd(54)
t.rt(175)
t.fd(55)

t.lt(175)
t.fd(55)
t.rt(175)
t.fd(50)

t.lt(175)
t.fd(56)
t.rt(175)
t.fd(51)

t.lt(175)
t.fd(55)
t.rt(175)
t.fd(51)

t.lt(175)
t.fd(53)
t.rt(175)
t.fd(51)

t.lt(175)
t.fd(51)
t.rt(175)
t.fd(50)

t.lt(175)
t.fd(50)
t.rt(175)
t.fd(49)

t.lt(175)
t.fd(50)
t.rt(175)
t.fd(44)

t.lt(175)
t.fd(50)
t.rt(175)
t.fd(43)

t.lt(175)
t.fd(50)
t.rt(175)
t.fd(42)

t.lt(175)
t.fd(50)
t.rt(175)
t.fd(40)

t.lt(175)
t.fd(25)


#Portion5
t.lt(65)
t.fd(50)
t.rt(180)
t.fd(55)

t.lt(175)
t.fd(57)
t.rt(175)
t.fd(55)

t.lt(175)
t.fd(57)
t.rt(175)
t.fd(54)

t.lt(175)
t.fd(57)
t.rt(175)
t.fd(54)

t.lt(175)
t.fd(57)
t.rt(175)
t.fd(53)

t.lt(175)
t.fd(57)
t.rt(175)
t.fd(53)

t.lt(175)
t.fd(57)
t.rt(175)
t.fd(52)

t.lt(175)
t.fd(57)
t.rt(175)
t.fd(51)

t.lt(175)
t.fd(57)
t.rt(175)
t.fd(50)

t.lt(175)
t.fd(57)
t.rt(175)
t.fd(49)

t.lt(175)
t.fd(57)
t.rt(175)
t.fd(46)

t.penup()
t.goto(0,-100)

message="Hail Hydraaaaaa...."
move=True
align='center'
font=("Arial",50, "bold")


t.write(message, move , align, font)
#for character in message:
    #t.write(character, move , align, font)
    #t.speed(0)    

t.mainloop()
