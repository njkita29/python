import tkinter
carendcolor="green"
brushsize=10
def ubdeitcolor(color):
    global carendcolor
    carendcolor=color
def ubdetsize(size):
    global brushsize
    brushsize=size

def drow(event):
    x,y=event.x,event.y
    canvas.create_oval(x-brushsize,y-+brushsize,x+brushsize,y+brushsize,fill=carendcolor,outline="")

top=tkinter.Tk()
top.title("peint")
canvas=tkinter.Canvas(top,width=500,height=500)
canvas.pack()

blackbaton=tkinter.Button(top,text="black",bg="gray",command=lambda:ubdeitcolor("black"))
blackbaton.pack(side="left")
greenbuton=tkinter.Button(top,text="green",bg="green",command=lambda:ubdeitcolor("green"))
greenbuton.pack(side="left")
pinkbuton=tkinter.Button(top,text="pink",bg="pink",command=lambda:ubdeitcolor("pink"))
pinkbuton.pack(side="left")
bluebuton=tkinter.Button(top,text="blue",bg="blue",command=lambda:ubdeitcolor("blue"))
bluebuton.pack(side="left")
orangebuton=tkinter.Button(top,text="orange",bg="orange",command=lambda:ubdeitcolor("orange"))
orangebuton.pack(side="left")
redbuton=tkinter.Button(top,text="red",bg="red",command=lambda:ubdeitcolor("red"))
redbuton.pack(side="left")
smolbaton=tkinter.Button(top,text="smol",command=lambda:ubdetsize(5))
smolbaton.pack(side="right")
mediumbutton=tkinter.Button(top,text="medium",command=lambda:ubdetsize(10))
mediumbutton.pack(side="right")
bigbaton=tkinter.Button(top,text="big",command=lambda:ubdetsize(15))
bigbaton.pack(side="right")
cliarbuton=tkinter.Button(top,text="cliar",command=lambda:ubdeitcolor("white"))
cliarbuton.pack(side="right")
canvas.bind("<B1-Motion>",drow)
top.mainloop()