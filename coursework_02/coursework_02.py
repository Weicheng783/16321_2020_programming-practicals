# Resolution: 1280 x 720
from tkinter import Tk, Canvas, IntVar, Label, PhotoImage, StringVar, Entry, Button, messagebox
from random import randint as rand
from time import sleep


def start():
    # global start

    if playername.get() == '':
        messagebox.showinfo(title='Ooops! Please Check the Following...', message='Please type your name correctly！')
        # playername.set('you hit me')
    else:
      if up.get()=='' or down.get()=='' or left.get()=='' or right.get()=='' or up.get()==' ' or down.get()==' ' or left.get()==' ' or right.get()==' ':
        messagebox.showinfo(title='Ooops! Please Check the Following...', message='Please Set Your Customary Control Keys(CCKs) or the Keys are setted illegally！')
      else:
        global canvas, pball, direction, balls, foodcoord, xl, yl, xr, yr, scoreText, score, start, xy, countdown, timermsg, killer, xlg, ylg, xrg, yrg, directiong

        canvas = Canvas(mainwindow, width=1280, height=720)
        canvas.pack()

        start = 1
        starttimer = 0

        balls = []
        xy = (1280/2 -50,720/2 -50,1280/2 +50,720/2 +50)
        xl=xy[0]
        yl=xy[1]
        xr=xy[2]
        yr=xy[3]
        pball = canvas.create_oval(xy, fill="green")

        directiong = rand(0, 3)

        xlg = rand(100, 800)
        ylg = xlg + 300
        xrg = xlg + 100
        yrg = xlg + 400
        killerxy = (xlg,ylg,xrg,yrg)
        killer=canvas.create_oval(killerxy, fill="orange")

        player = canvas.create_text( 1280/2-200 , 10 , fill="white" , font="Times 20 italic bold", text="PLAYER: " + playername.get())
        canvas.config(bg="black")
        score = 0
        txt = "Score:" + str(score)
        scoreText = canvas.create_text( 1280/2+50 , 10 , fill="white" , font="Times 20 italic bold", text=txt)


        canvas.bind("<Left>", leftKey)
        canvas.bind("<Right>", rightKey)
        canvas.bind("<Up>", upKey)
        canvas.bind("<Down>", downKey)

        canvas.bind("<F10>", hide)

        canvas.bind("<"+left.get()+">", leftKey)
        canvas.bind("<"+right.get()+">", rightKey)
        canvas.bind("<"+up.get()+">", upKey)
        canvas.bind("<"+down.get()+">", downKey)

        canvas.bind("<MouseWheel>",zoomer)
        canvas.focus_set()
        direction = "right"
        # return canvas
        placeFood()
        canvas.bind("<KeyPress>", call_back)
        if starttimer == 0:
            countdown = 30
            starttimer = 1
            timermsg = canvas.create_text( 1280/2 , 36 , fill="white" , font="Times 20 italic bold", text="Time Remaining for Next Update: "+str(countdown))
            timer()
        
        # print(foodcoord)

        canvas.after(90, moveBall)
        canvas.after(1000, movekiller)
        # print(str(balls[0]))
        # moveBall()
        # sleep(5)
        # canvas.destroy()

def movekiller():
    global killer, xlg, ylg, xrg, yrg, directiong, countdown
    
    if countdown != 0:
        if directiong == 0 :#"left"
            if xlg > 10:
                canvas.move(killer, -30,0)
                xlg -= 30
                xrg -= 30
            else:
                canvas.delete(killer)
                xlg = rand(100, 800)
                ylg = xlg + 300
                xrg = xlg + 100
                yrg = xlg + 400
                killerxy = (xlg,ylg,xrg,yrg)
                killer=canvas.create_oval(killerxy, fill="orange")
                directiong = rand(0, 3)
        elif directiong == 1: #"right"
            if xrg < 1270:
                canvas.move(killer, 30,0)
                xlg += 30
                xrg += 30
            else:
                canvas.delete(killer)
                xlg = rand(100, 800)
                ylg = xlg + 300
                xrg = xlg + 100
                yrg = xlg + 400
                killerxy = (xlg,ylg,xrg,yrg)
                killer=canvas.create_oval(killerxy, fill="orange")
                directiong = rand(0, 3)
        elif directiong == 2: #"up"
            if ylg > 10:
                canvas.move(killer, 0,-30)
                ylg -= 30
                yrg -= 30
            else:
                canvas.delete(killer)
                xlg = rand(100, 800)
                ylg = xlg + 300
                xrg = xlg + 100
                yrg = xlg + 400
                killerxy = (xlg,ylg,xrg,yrg)
                killer=canvas.create_oval(killerxy, fill="orange")
                directiong = rand(0, 3)
        elif directiong == 3: #"down"
            if yrg < 710:
                canvas.move(killer, 0,30)
                ylg += 30
                yrg += 30
            else:
                canvas.delete(killer)
                xlg = rand(100, 800)
                ylg = xlg + 300
                xrg = xlg + 100
                yrg = xlg + 400
                killerxy = (xlg,ylg,xrg,yrg)
                killer=canvas.create_oval(killerxy, fill="orange")
                directiong = rand(0, 3)
    canvas.after(90, movekiller)



def timer():
        global countdown, foodcoordx, foodcoordy, xl, xr, yr, yl, growth, pball, directiong
        if countdown > 0:
            # boom()
            for i in range (len(foodcoordx)):
                if foodcoordx[i]-(xl+xr)/2 <= (xr-xl)/2 and foodcoordx[i]-(xl+xr)/2 >= -(xr-xl)/2 and foodcoordy[i]-(yl+yr)/2 <= (yr-yl)/2 and foodcoordy[i]-(yl+yr)/2 >= -(yr-yl)/2:
                    break
                else:
                     if i == len(foodcoordx)-1:

                      growth = -0.2
                      if xr-xl <= 35:
                       break
                      else:
                       canvas.delete(pball)
                       balls = []
                       xy = (xl -growth,yl -growth,xr +growth,yr +growth)
                       xl=xy[0]
                       yl=xy[1]
                       xr=xy[2]
                       yr=xy[3]
                       pball=canvas.create_oval(xy, fill="green")
                       break


            canvas.itemconfigure(timermsg, text="Time Remaining for Next Update: "+str(countdown))
            countdown -= 1
        else:
            # boomdir()
            directiong = rand(0, 3)
            countdown = 30
        canvas.after(1000, timer)

 # newfile=open(newfilename+'.txt','w')          

# def boom():
#     global xlg, ylg, xrg, yrg, downb, upb, leftb, rightb
#     lftb = canvas.create_oval((xlg-(xrg-xlg)/2, ylg+(yrg-ylg)/2, xrg-xlg, yrg), fill="blue")





# def boomdir():
#     global killer, xlg, ylg, xrg, yrg
#     canvas.delete(killer)
#     xlg = rand(100, 800)
#     ylg = xlg + 300
#     xrg = xlg + 100
#     yrg = xlg + 400
#     killerxy = (xlg,ylg,xrg,yrg)
#     killer=canvas.create_oval(killerxy, fill="orange")


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
	global moveBall, direction, balls, xl, yl, xr, yr, food, score, scoreText, pball, growth, xy
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
			canvas.delete(pball)
			balls = []

			growth = 0.6

			xy = (xl -growth,yl -growth,xr +growth,yr +growth)
			# xy = (1280/2 -growth,720/2 -growth,1280/2 +growth,720/2 +growth)

			xl=xy[0]
			yl=xy[1]
			xr=xy[2]
			yr=xy[3]
			# print(xy[0])
			pball=canvas.create_oval(xy, fill="green")
			balls.append(pball)
			# canvas.scale(pball, (xr-xl)/2, (yr-yl)/2, 1.1, 1.1)
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
		    canvas.move(pball, -30,0)
		    xl -= 30
		    xr -= 30
	elif direction == "right":
	    if xr < 1270:
		    canvas.move(pball, 30,0)
		    xl += 30
		    xr += 30
	elif direction == "up":
		if yl > 10:
		    canvas.move(pball, 0,-30)
		    yl -= 30
		    yr -= 30
	elif direction == "down":
		if yr < 710:
		    canvas.move(pball, 0,30)
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

def hide(event):
    global hider
    if hider == 0:
        hider=1
        # mainwindow.withdraw()
        bosskeydis = canvas.create_image(img=bosskey)
    else:
        hider=0
        canvas.delete(bosskeydis)



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
playername.set("Harvey")

hider = 0

up = StringVar()
up.set("w")

down = StringVar()
down.set("s")

left = StringVar()
left.set("a")

right = StringVar()
right.set("d")

downb = []
rightb = []
upb = []
leftb = []

e = Entry(mainwindow, show=None, font=('Arial', 14), textvariable=playername).place(x=600, y=250, anchor='nw')
# playername.set('you hit me')
Button(mainwindow, text='Start !', font=('Arial', 12), width=10, height=1, command=start).place(x=600, y=350, anchor='nw')
# User control
Label(mainwindow,text='User Settings(Customary Control Keys):', font=('Arial Bold', 15)).place(x=500, y=720/2+50, anchor='nw')
Label(mainwindow,text='UpKey :', font=('Arial Bold', 15)).place(x=450, y=440, anchor='nw')
upk=Entry(mainwindow, show=None, font=('Arial', 14), textvariable=up).place(x=550, y=440, anchor='nw')
Label(mainwindow,text='DownKey:', font=('Arial Bold', 15)).place(x=450, y=470, anchor='nw')
downk=Entry(mainwindow, show=None, font=('Arial', 14), textvariable=down).place(x=570, y=470, anchor='nw')
Label(mainwindow,text='LeftKey:', font=('Arial Bold', 15)).place(x=450, y=500, anchor='nw')
leftk=Entry(mainwindow, show=None, font=('Arial', 14), textvariable=left).place(x=570, y=500, anchor='nw')
Label(mainwindow,text='RightKey:', font=('Arial Bold', 15)).place(x=450, y=530, anchor='nw')
rightk=Entry(mainwindow, show=None, font=('Arial', 14), textvariable=right).place(x=570, y=530, anchor='nw')
Label(mainwindow,text='! Notice: The keys <Left> <Right> <Up> <Down> are kept unchanged intentationally afraid of the Customary Keys do not work.', font=('Arial Bold', 15)).place(x=40, y=570, anchor='nw')

# bosskey = PhotoImage(file="python.png")

foodcoord=[]




mainwindow.mainloop()


