import turtle
t = turtle.Pen()
t.shape('turtle')

    
def Art():
        t.speed (11)
        t.circle(100)

def Go(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

x=0
y=0
for a in range(9):
    x += 10
    y -= 10
    Go(x,y)
    Art()


for a in range(9):
    x -= 10
    y -= 10
    Go(x,y)
    Art()

for a in range(9):
    x -= 10
    y += 10
    Go(x,y)
    Art()

for a in range(9):
    x += 10
    y += 10
    Go(x,y)
    Art()

t.hideturtle()


