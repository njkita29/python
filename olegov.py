import turtle
t=turtle.Pen()
turtle.bgcolor("black")
t.pencolor("aqua")
colors=["blueviolet","crimson","red4","yellow1","seagreen1","aqua","chartreuse2"]
kok=turtle.textinput("ведіть ваше імя","як тебе завати?")
for x in range (100):
    t.pencolor(colors[x%7])
    t.penup()
    t.forward(x*4)
    t.pendown()
    t.write(kok,font=("Arial",int((x+4)/4)))
    t.left(97)