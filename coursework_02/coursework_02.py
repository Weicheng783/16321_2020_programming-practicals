# Resolution: 1280 x 720
from tkinter import Tk, Canvas, IntVar, Label, PhotoImage, StringVar, Entry, Button, messagebox
from random import randint as rand
from time import sleep


def start():


    if playername.get() == '':
        messagebox.showinfo(title='', message='Please type your name correctly！')

    else:
    	global canvas, pball, direction, balls, foodcoord, xl, yl, xr, yr

    	canvas = Canvas(mainwindow, width=1280, height=720)
    	canvas.pack()
    	
    	balls = []
    	xy = (1280/2 -50,720/2 -50,1280/2 +50,720/2 +50)
    	xl=xy[0]
    	yl=xy[1]
    	xr=xy[2]
    	yr=xy[3]

    	pball=canvas.create_oval(xy, fill="green", activefill="red")
    	balls.append(pball)

    	player = canvas.create_text( 1280/2 , 10 , fill="white" , font="Times 20 italic bold", text="PLAYER: " + playername.get())
    	canvas.config(bg="black") 
    	score = 0
    	txt = "Score:" + str(score)
    	scoreText = canvas.create_text( 1280/1.5 , 10 , fill="white" , font="Times 20 italic bold", text=txt)


    	canvas.bind("<Left>", leftKey)
    	canvas.bind("<Right>", rightKey)
    	canvas.bind("<Up>", upKey)
    	canvas.bind("<Down>", downKey)
    	canvas.focus_set()
    	direction = "right"

    	
    	placeFood()
    	canvas.bind("<KeyPress>", call_back)
    	
    	canvas.after(90, moveBall)



def moveBall():
	global moveBall, direction, balls, xl, yl, xr, yr, food
	canvas.pack()
	for i in range(len(foodcoordx)):
		if foodcoordx[i]-(xl+xr)/2 <= (xr-xl)/2 and foodcoordx[i]-(xl+xr)/2 >= -(xr-xl)/2 and foodcoordy[i]-(yl+yr)/2 <= (yr-yl)/2 and foodcoordy[i]-(yl+yr)/2 >= -(yr-yl)/2:
			canvas.delete(food[i])
	
	if direction == "left":
		if xl > 10:
		    canvas.move(1, -10,0)
		    xl -= 10
		    xr -= 10
	elif direction == "right":
	    if xr < 1270:
		    canvas.move(1, 10,0)
		    xl += 10
		    xr += 10
	elif direction == "up":
		if yl > 10:
		    canvas.move(1, 0,-10)
		    yl -= 10
		    yr -= 10
	elif direction == "down":
		if yr < 710:
		    canvas.move(1, 0,10)
		    yl += 10
		    yr += 10
	
	for i in range(1,len(balls)):
		positions.append(canvas.coords(balls[i]))
	for i in range(len(balls)-1):
		canvas.coords(balls[i+1],positions[i][0], positions[i][1],positions[i][2],positions[i][3])
	
	canvas.after(90, moveBall)

    

def call_back(event):
	global call_back
	print(event.keysym)

def placeFood():
    global food, foodX, foodY, foodcoordx, foodcoordy
    foodcoordx=[]
    foodcoordy=[]
    food=[]
    for i in range (0,20):
    	food.append(canvas.create_rectangle(0,0, 10, 10, fill="steel blue" ))
    	foodX = rand(0,1250)
    	foodY = rand(0,700)
    	foodcoordx.append(foodX)
    	foodcoordy.append(foodY)
    	canvas.move(food[i], foodX, foodY)

def leftKey(event):
    global direction
    direction = "left"

def rightKey(event):
    global direction
    direction = "right"

def upKey(event):
    global direction
    direction = "up"

def downKey(event):
    global direction
    direction = "down"


mainwindow = Tk()

mainwindow.title("Battle Of Balls (adapted)")
mainwindow.geometry('1280x720')

Label(mainwindow,text='Battle Of Balls (adapted)', font=('Arial Bold', 20)).place(x=500, y=200, anchor='nw')
Label(mainwindow,text='Please Type Your Name :', font=('Arial Bold', 15)).place(x=350, y=250, anchor='nw')

playername = StringVar()
e = Entry(mainwindow, show=None, font=('Arial', 14), textvariable=playername).place(x=600, y=250, anchor='nw')
# playername.set('you hit me')
Button(mainwindow, text='Start !', font=('Arial', 12), width=10, height=1, command=start).place(x=600, y=350, anchor='nw')

foodcoord=[]




mainwindow.mainloop()


