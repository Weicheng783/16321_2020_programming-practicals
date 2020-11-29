# Resolution: 1280 x 720
from tkinter import Tk, Canvas, IntVar, Label, PhotoImage, StringVar, Entry, Button, messagebox
from random import randint as rand
from time import sleep


def start():
    # global start

    if playername.get() == '':
        messagebox.showinfo(title='', message='Please type your name correctly！')
        # playername.set('you hit me')
    else:
    	global canvas, pball, direction, balls, foodcoord, xl, yl, xr, yr, scoreText, score, start

    	canvas = Canvas(mainwindow, width=1280, height=720)
    	canvas.pack()

    	start = 1

    	balls = []
    	xy = (1280/2 -50,720/2 -50,1280/2 +50,720/2 +50)
    	xl=xy[0]
    	yl=xy[1]
    	xr=xy[2]
    	yr=xy[3]
    	# print(xy[0])
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
    	canvas.bind("<MouseWheel>",zoomer)
    	canvas.focus_set()
    	direction = "right"
    	# return canvas

    	placeFood()
    	canvas.bind("<KeyPress>", call_back)
    	# print(foodcoord)

    	canvas.after(90, moveBall)
    	# print(str(balls[0]))
    	# moveBall()
    	# sleep(5)
    	# canvas.destroy()


def zoomer(event):
		global zoomer, xr, xl, yr, yl, pball, food
		if (event.delta > 0):
			canvas.scale("all", (xr-xl)/2, (yr-yl)/2, 1.1, 1.1)
		elif (event.delta < 0):
			canvas.scale("all", (xr-xl)/2, (yr-yl)/2, 0.9, 0.9)
			canvas.configure(scrollregion = canvas.bbox("all"))


def growSnake():
    global score
    score += 10
    txt = "score:" + str(score)
    canvas.itemconfigure(scoreText, text=txt)
    lastElement = len(snake)-1
    lastElementPos = canvas.coords(snake[lastElement])
    snake.append(canvas.create_rectangle(0,0, snakeSize,snakeSize, fill="#FDF3F3"))
    if (direction == "left"):
        canvas.coords(snake[lastElement+1],lastElementPos[0]+snakeSize,lastElementPos[1],lastElementPos[2]+snakeSize,lastElementPos[3])
    elif (direction == "right"):
        canvas.coords(snake[lastElement+1],lastElementPos[0] -snakeSize,lastElementPos[1],lastElementPos[2] -snakeSize,lastElementPos[3])
    elif (direction == "up"):
        canvas.coords(snake[lastElement+1],lastElementPos[0],lastElementPos[1]+snakeSize,lastElementPos[2],lastElementPos[3]+snakeSize)
    else:
        canvas.coords(snake[lastElement+1],lastElementPos[0],lastElementPos[1]-snakeSize,lastElementPos[2],lastElementPos[3]-snakeSize)

def overlapping(a,b):
    if a[0] < b[2] and a[2] > b[0] and a[1] < b[3] and a[3] > b[1]:
        return True
    return False

def moveBall():
	global moveBall, direction, balls, xl, yl, xr, yr, food, score, scoreText
	canvas.pack()
	# foodlenbef = len(foodcoordx)
	# fooddel = []
	for i in range (len(foodcoordx)):
		if foodcoordx[i]-(xl+xr)/2 <= (xr-xl)/2 and foodcoordx[i]-(xl+xr)/2 >= -(xr-xl)/2 and foodcoordy[i]-(yl+yr)/2 <= (yr-yl)/2 and foodcoordy[i]-(yl+yr)/2 >= -(yr-yl)/2:
			canvas.delete(food[i])
			food.remove(food[i])
			foodcoordx.remove(foodcoordx[i])
			foodcoordy.remove(foodcoordy[i])
			score = score + 10
			txt = "Score:" + str(score)
			canvas.itemconfigure(scoreText, text=txt)
			break

	if len(foodcoordx) < 10:
		placeFood()
	# foodlenaft = len(foodcoordx)
	# foodlendiff = foodlenbef - foodlenaft




	# positions = []
	# positions.append(canvas.coords(balls[0]))
    # if positions[0][0] < 0:
    #     canvas.coords(1,width,positions[0][1],width-snakeSize,positions[0][3])
    # elif positions[0][2] > width:
    #     canvas.coords(snake[0],0-snakeSize,positions[0][1],0,positions[0][3])
    # elif positions[0][3] > height:
    #     canvas.coords(snake[0],positions[0][0],0 - snakeSize,positions[0][2],0)
    # elif positions[0][1] < 0:
    #     canvas.coords(snake[0],positions[0][0], height,positions[0][2],height-snakeSize)
    # positions.clear()
    # positions.append(canvas.coords(snake[0]))
	if direction == "left":
		if xl > 10:
		    canvas.move(1, -30,0)
		    xl -= 30
		    xr -= 30
	elif direction == "right":
	    if xr < 1270:
		    canvas.move(1, 30,0)
		    xl += 30
		    xr += 30
	elif direction == "up":
		if yl > 10:
		    canvas.move(1, 0,-30)
		    yl -= 30
		    yr -= 30
	elif direction == "down":
		if yr < 710:
		    canvas.move(1, 0,30)
		    yl += 30
		    yr += 30
	# bHeadPos = canvas.coords(balls[0])
	# foodPos = canvas.coords(food)
	# if overlapping(bHeadPos, foodPos):
	# 	messagebox.showinfo(title='Game Over', message='You touched an object！')

        # moveFood()
        # growSnake()
    # for i in range(1,len(pball)):
    #     if overlapping(sHeadPos, canvas.coords(snake[i])):
    #         gameOver = True
    #         canvas.create_text(width/2,height/2,fill="white",font="Times 20 italic bold", text="Game Over!")
	for i in range(1,len(balls)):
		positions.append(canvas.coords(balls[i]))
	for i in range(len(balls)-1):
		canvas.coords(balls[i+1],positions[i][0], positions[i][1],positions[i][2],positions[i][3])

	canvas.after(90, moveBall)

    # for i in range(1,len(snake)):
    #     positions.append(canvas.coords(snake[i]))
    # for i in range(len(snake)-1):
    #     canvas.coords(snake[i+1],positions[i][0], positions[i][1],positions[i][2],positions[i][3])
    # if 'gameOver' not in locals():

def call_back(event):
	global call_back
	print(event.keysym)

def placeFood():
    global food, foodX, foodY, foodcoordx, foodcoordy, start
    if start==1:
     foodcoordx=[]
     foodcoordy=[]
     food=[]
     start = 0

    lenfood = len(food)
    for i in range (lenfood,lenfood+20):
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
