import turtle as t

def rectangle(x,y,deg,beta,color):
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.left(deg)
    for i in range(2):
        t.forward(x)
        t.right(180-beta)
        t.forward(y)
        t.right(beta)
    t.end_fill()
    t.penup()
    t.home()

def triangle(x1,y1,x2,y2,x3,y3,color):
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.goto(x1,y1)
    t.goto(x2,y2)
    t.goto(x3,y3)
    t.end_fill()
    t.penup()
    t.home()

def circle(r,deg, color):
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(r,deg)
    t.end_fill()
    t.penup()
    t.home()

def draw_house():

    # vẽ mặt trước ngôi nhà
    t.penup()
    t.goto(-300,-50)
    rectangle(150,250,0,90,"blue")

    # vẽ cửa chính
    t.goto(-250,-200)
    rectangle(50,100,0,90,"green")

    # vẽ vách bên
    t.goto(-150,-50)
    rectangle(160,250,20,70,"yellow")

    # vẽ cửa sổ
    t.goto(-100,-100)
    rectangle(55,50,20,70,"grey")

    # vẽ mái trước
    t.goto(-150,-50)
    triangle(-225,50,-300,-50,-150,-50,"purple")

    # vẽ mái bên
    t.goto(-225,50)
    rectangle(160,125,20,106.87,"orange")

def draw_tree():
    # vẽ thân cây
    t.goto(150,-150)
    rectangle(50,150,0,90,"brown")

    #vẽ tán cây
    x1 = 100
    y1 = -150
    x2 = 250
    y2 = -150
    x3 = 175
    y3 = -75

    for i in range (3):
        t.goto(x1,y1)
        triangle(x2,y2,x3,y3,x1,y1,"green")
        y1 += 75
        y2 += 75
        y3 += 75

def draw_sun():
    # vẽ mặt trời
    t.goto(50,150)
    circle(50,360,"red")
    t.goto(50, 150)
    t.pendown()
    for i in range (8):
        t.circle(50,45)
        t.right(90)
        if i%2 != 0:
            t.forward(50)
            t.backward(50)
        else:
            t.forward(25)
            t.backward(25)
        t.left(90)

# chọn màu background là cyan
t.bgcolor("light cyan")
t.speed(10)
t.pensize(3)

draw_house()
draw_tree()
draw_sun()

t.hideturtle()
t.done()