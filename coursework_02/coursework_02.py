# Resolution: 1280 x 720
import os
from tkinter import Tk, Canvas, IntVar, Label, PhotoImage, StringVar, Entry, Button, messagebox
from random import randint as rand
from time import sleep


def startgame():
    global start

    if playername.get() == '':
        messagebox.showinfo(title='Ooops! Please Check the Following...', message='Please type your name correctly！')
    else:
      if up.get()=='' or down.get()=='' or left.get()=='' or right.get()=='' or up.get()==' ' or down.get()==' ' or left.get()==' ' or right.get()==' ':
        messagebox.showinfo(title='Ooops! Please Check the Following...', message='Please Set Your Customary Control Keys(CCKs) or the Keys are setted illegally！')
      else:
        global canvas, starttimer, pball, direction, balls, foodcoord, xl, yl, xr, yr, scoreText, score, start, xy, countdown, timermsg, killer, xlg, ylg, xrg, yrg, directiong, gamefromsave

        canvas = Canvas(mainwindow, width=1280, height=720)
        canvas.pack()

        start = 1
        starttimer = 0

        balls = []

        # check whether Game from saved files
        if gamefromsave == 1:
            file = open("posxl.txt")
            file1 = open("posxr.txt")
            file2 = open("posyl.txt")
            file3 = open("posyr.txt")
            xy = (float(file.read()),float(file2.read()),float(file1.read()),float(file3.read()))
            file.close()
            file1.close()
            file2.close()
            file3.close()
        else:
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
        if gamefromsave == 1:
            file4 = open("name.txt")
            player = canvas.create_text( 1280/2-200 , 30 , fill="white" , font="Times 20 italic bold", text="PLAYER: " + file4.read())
            file4.close()

            canvas.config(bg="black")

            file5 = open("score.txt")
            score = int(file5.read())
            txt = "Score:" + str(score)
            scoreText = canvas.create_text( 1280/2+50 , 30 , fill="white" , font="Times 20 italic bold", text=txt)
            file5.close()

        else:
            player = canvas.create_text( 1280/2-200 , 30 , fill="white" , font="Times 20 italic bold", text="PLAYER: " + playername.get())
            canvas.config(bg="black")
            score = 0
            txt = "Score:" + str(score)
            scoreText = canvas.create_text( 1280/2+50 , 30 , fill="white" , font="Times 20 italic bold", text=txt)

        canvas.create_text( 1280/2-80 , 700 , fill="yellow" , font="Times 20 italic bold", text="<p> to pause, <k> to save, <b> is the Boss Key, <c> to cheat")
        canvas.create_text( 1280/2-80 , 670 , fill="blue" , font="Times 20 italic bold", text="when GreenBall touched the Middle of the OrangeBall, Game Over.")

        canvas.bind("<Left>", leftKey)
        canvas.bind("<Right>", rightKey)
        canvas.bind("<Up>", upKey)
        canvas.bind("<Down>", downKey)

        canvas.bind("<p>", pause)

        canvas.bind("<b>", hide)

        # User Controls
        canvas.bind("<"+left.get()+">", leftKey)
        canvas.bind("<"+right.get()+">", rightKey)
        canvas.bind("<"+up.get()+">", upKey)
        canvas.bind("<"+down.get()+">", downKey)

        canvas.focus_set()
        direction = "right"

        # Food Generate and Timer start
        placeFood()
        canvas.bind("<KeyPress>", call_back)
        if starttimer == 0:
            countdown = 30
            starttimer = 1
            timermsg = canvas.create_text( 1280/2 , 50 , fill="white" , font="Times 20 italic bold", text="Time Remaining for Next Update: "+str(countdown))
            timer()

        canvas.after(90, moveBall)
        canvas.after(1000, movekiller)


def pause(event):
    global pause, pausemsg
    if pause == 0:
        pause = 1
        pausemsg = canvas.create_text( 1280/2 , 720/2 , fill="white" , font="Times 20 italic bold", text="The Game Is Paused, Press <p> to return." )
    else:
        canvas.delete(pausemsg)
        pause = 0

# The following controls the KillerBall movements.
def movekiller():
    global killer, xlg, ylg, xrg, yrg, directiong, countdown, xl, xr, yl, yr, pause, end, score, start, movspeed
    if pause == 1:
        canvas.after(90, movekiller)
    elif end == 1:
        canvas.destroy()
        leaderboard()

    else:
        if countdown != 0:
            if xrg-(xl+xr)/2 <= (xr-xl)/2 and xrg-(xl+xr)/2 >= -(xr-xl)/2 and yrg-(yl+yr)/2 <= (yr-yl)/2 and yrg-(yl+yr)/2 >= -(yr-yl)/2:
                # When the game is over, do some file writing stuff (Record the score, name).
                if not os.path.isfile('total.txt'):
                    newfile = open('total.txt','w')
                    newfile.write('1')
                    newfile.close()

                    newfile = open('1name.txt','w')
                    newfile.write('Anonymous')
                    newfile.close()

                    newfile = open('1score.txt','w')
                    newfile.write('50')
                    newfile.close()

                if os.path.isfile('total.txt'):
                    file = open('total.txt')
                    total = int(file.read())
                    file.close()
                    file = open('total.txt','w')
                    file.write(str(total+1))
                    file.close()

                    newfile = open(str(total+1)+'score.txt','w')
                    newfile.write(str(score))
                    newfile.close()

                    newfile = open(str(total+1)+'name.txt','w')
                    newfile.write(playername.get())
                    newfile.close()

                end = 1

                start = 0

                messagebox.showinfo(title='Ooops!', message=' Your ball is touched the Killer Ball, Game Over! Game Score is saved now, maybe able to read though the leaderboard.')

            if directiong == 0 :#"left"
                if xlg > 10:
                    canvas.move(killer, -30,0)
                    xlg -= movspeed
                    xrg -= movspeed
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
                    xlg += movspeed
                    xrg += movspeed
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
                    ylg -= movspeed
                    yrg -= movspeed
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
                    ylg += movspeed
                    yrg += movspeed
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

# Timer or Counter
def timer():
        global countdown, foodcoordx, foodcoordy, xl, xr, yr, yl, growth, pball, directiong, pause, end, movspeed

        if pause == 1 or end == 1:
            canvas.after(90, timer)
        else:
            if countdown > 0:
                for i in range (len(foodcoordx)):
                    # if the two balls are collided.
                    if foodcoordx[i]-(xl+xr)/2 <= (xr-xl)/2 and foodcoordx[i]-(xl+xr)/2 >= -(xr-xl)/2 and foodcoordy[i]-(yl+yr)/2 <= (yr-yl)/2 and foodcoordy[i]-(yl+yr)/2 >= -(yr-yl)/2:
                        break
                    else:
                         if i == len(foodcoordx)-1:

                          growth = 0
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
                # When the clock is 0, reset the clock to 30, meanwhile level up a bit.
                directiong = rand(0, 3)
                countdown = 30
                movspeed += 15
            canvas.after(1000, timer)

# The following is the leaderboard section, it is executed at the end of the game.
def leaderboard():
    global leaders, end, movspeed, gamefromsave
    if end == 1:
        end = 0
        movspeed = 50
        gamefromsave = 0

    if not os.path.isfile('total.txt'):
        newfile = open('total.txt','w')
        newfile.write('1')
        newfile.close()

        newfile = open('1name.txt','w')
        newfile.write('Anonymous')
        newfile.close()

        newfile = open('1score.txt','w')
        newfile.write('50')
        newfile.close()

    leaders = Canvas(mainwindow, width=1280, height=720)
    leaders.pack()
    leaders.create_text( 1280/2 , 200 , fill="black" , font="Times 20 italic bold", text="L E A D E R B O A R D" )

    if os.path.isfile('total.txt'):
        file = open('total.txt')
        totalnum = int(file.read())
        file.close()

        highest = 1
        for i in range(totalnum):
            filehighest = open(str(highest)+'score.txt')
            filescore = open(str(i+1)+'score.txt')

            if int(filescore.read()) >= int(filehighest.read()):
                highest = i+1
            filescore.close()
            filehighest.close()

        filehighest = open(str(highest)+'name.txt')
        filehighest2 = open(str(highest)+'score.txt')

        leaders.create_text(1280/2 , 350 , fill="red" , font="Times 20 italic bold", text="1ST Position: "+filehighest.read()+"  Score: "+filehighest2.read())

        filehighest.close()
        filehighest2.close()

        secondpos = 1
        for i in range(totalnum):
            filehighest = open(str(secondpos)+'score.txt')
            filescore = open(str(i+1)+'score.txt')

            if int(filescore.read()) >= int(filehighest.read()) and secondpos != highest:
                secondpos = i+1

            filescore.close()
            filehighest.close()

        filehighest = open(str(secondpos)+'name.txt')
        filehighest2 = open(str(secondpos)+'score.txt')

        leaders.create_text(1280/2 , 450 , fill="orange" , font="Times 20 italic bold", text="2ND Position: "+filehighest.read()+"  Score: "+filehighest2.read())

        filehighest.close()
        filehighest2.close()

        thipos = 1
        for i in range(totalnum):
            filehighest = open(str(thipos)+'score.txt')
            filescore = open(str(i+1)+'score.txt')

            if int(filescore.read()) >= int(filehighest.read()) and secondpos != highest and thipos != secondpos:
                thipos = i+1

            filescore.close()
            filehighest.close()

        filehighest = open(str(thipos)+'name.txt')
        filehighest2 = open(str(thipos)+'score.txt')

        leaders.create_text(1280/2 , 550 , fill="purple" , font="Times 20 italic bold", text="3RD Position: "+filehighest.read()+"  Score: "+filehighest2.read())

        filehighest.close()
        filehighest2.close()

        Button(leaders, text='Back', font=('Arial', 15), width=10, height=1, command=destroyleader).place(x=1280/2, y=600, anchor='nw')

def destroyleader():
    global leaders
    leaders.destroy()

# The following controls the User Ball movement.
def moveBall():
    global moveBall, direction, balls, xl, yl, xr, yr, food, score, scoreText, pball, growth, xy, pause, end
    if pause == 1 or end == 1:
     canvas.after(90, moveBall)
    else:
        canvas.pack()
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

            growth = 0

            xy = (xl -growth,yl -growth,xr +growth,yr +growth)

            xl=xy[0]
            yl=xy[1]
            xr=xy[2]
            yr=xy[3]
            pball=canvas.create_oval(xy, fill="green")
            balls.append(pball)
            break

        if len(foodcoordx) < 10:
         placeFood()

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

        canvas.after(90, moveBall)

# Boss Key section
def hide(event):
    global hider, pause, canvashade
    if hider == 0:
        hider=1
        pause=1
        canvashade = Canvas(canvas, width=1280, height=720, bg='white')
        canvashade.pack()
        shademsg = canvashade.create_text( 1280/2 , 720/2 , fill="black" , font="Times 20 italic bold", text="Welcome to Python, You Pressed a BOSS KEY! Press <b> again to restore." )


        if os.path.isfile('python.png'):
            photo = PhotoImage(file='python.png')
            img_label = Label(canvashade, image=photo)
            # img_label.pack()
    else:
        hider=0
        pause=0
        canvashade.destroy()

# Pause, Save, Cheat sections
def call_back(event):
    global call_back, pause, pausemsg, score, movspeed, xl, xr, yl, yr

    if event.keysym == "p":
        if pause == 0:
            pause = 1
            pausemsg = canvas.create_text( 1280/2 , 720/2 , fill="white" , font="Times 20 italic bold", text="The Game Is Paused, Press <p> to return." )
        else:
            canvas.delete(pausemsg)
            pause = 0
    elif event.keysym == "k":
        if pause == 0:
            pause = 1

            newfile=open('name.txt','w')
            newfile.write(playername.get())
            newfile.close()

            newfile=open('score.txt','w')
            newfile.write(str(score))
            newfile.close()

            newfile=open('posxl.txt','w')
            newfile.write(str(xl))
            newfile.close()

            newfile=open('posxr.txt','w')
            newfile.write(str(xr))
            newfile.close()

            newfile=open('posyl.txt','w')
            newfile.write(str(yl))
            newfile.close()

            newfile=open('posyr.txt','w')
            newfile.write(str(yr))
            newfile.close()

            pausemsg = canvas.create_text( 1280/2 , 720/2 , fill="white" , font="Times 20 italic bold", text="Game saved successfully, Press <k> to return." )
        else:
            canvas.delete(pausemsg)
            pause = 0
    elif event.keysym == 'c':
        score += 50
        if movspeed >= 15:
         movspeed -= 5

# Placefood section
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

# Reload the game section.
def load():
    global gamefromsave
    if os.path.isfile('name.txt'):
        gamefromsave = 1
        startgame()
    else:
        messagebox.showinfo(title='Ooops!', message='You have not saved a game ! Please play a little bit the game and press <k> to save.')

mainwindow = Tk()

mainwindow.title("Battle Of Balls (adapted)")
mainwindow.geometry('1280x720')

Label(mainwindow,text='Battle Of Balls (adapted)', font=('Arial Bold', 20)).place(x=500, y=50, anchor='nw')
Label(mainwindow,text='Please Type Your Name :', font=('Arial Bold', 15)).place(x=350, y=100, anchor='nw')

# Initalise Important Data and Control Codes.
playername = StringVar()
playername.set("Harvey")

gamefromsave = 0

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

firsttime = 1

movspeed = 30

pause = 0
end = 0

e = Entry(mainwindow, show=None, font=('Arial', 14), textvariable=playername).place(x=650, y=100, anchor='nw')

Button(mainwindow, text='Start !', font=('Arial', 15), width=10, height=1, command=startgame).place(x=350, y=150, anchor='nw')
Button(mainwindow, text='Reload a Game from local', font=('Arial', 15), width=30, height=1, command=load).place(x=550, y=150, anchor='nw')

# User control (Customary Control keys)

Label(mainwindow,text='User Settings(Customary Control Keys):', font=('Arial Bold', 15)).place(x=500, y=200, anchor='nw')
Label(mainwindow,text='UpKey :', font=('Arial Bold', 15)).place(x=450, y=230, anchor='nw')
upk=Entry(mainwindow, show=None, font=('Arial', 14), textvariable=up).place(x=550, y=230, anchor='nw')
Label(mainwindow,text='DownKey:', font=('Arial Bold', 15)).place(x=450, y=260, anchor='nw')
downk=Entry(mainwindow, show=None, font=('Arial', 14), textvariable=down).place(x=570, y=260, anchor='nw')
Label(mainwindow,text='LeftKey:', font=('Arial Bold', 15)).place(x=450, y=290, anchor='nw')
leftk=Entry(mainwindow, show=None, font=('Arial', 14), textvariable=left).place(x=570, y=290, anchor='nw')
Label(mainwindow,text='RightKey:', font=('Arial Bold', 15)).place(x=450, y=320, anchor='nw')
rightk=Entry(mainwindow, show=None, font=('Arial', 14), textvariable=right).place(x=570, y=320, anchor='nw')
Label(mainwindow,text='Notice: The four direction keys <Left> <Right> <Up> <Down> are reserved unchanged.', font=('Arial Bold', 15)).place(x=50, y=350, anchor='nw')
Label(mainwindow,text='Guidence(During the game): 1.Press <p> to pause, 2.<b> is the Boss Key, ', font=('Arial Bold', 15)).place(x=40, y=380, anchor='nw')
Label(mainwindow,text='3.Press <k> to save the game: You can reload it from the main manu once you stored.', font=('Arial Bold', 15)).place(x=50, y=410, anchor='nw')
Label(mainwindow,text='4.Press <c> to cheat: Each time you pressed the key <c>, your score will be added by 50', font=('Arial Bold', 15)).place(x=50, y=440, anchor='nw')
Label(mainwindow,text=' and the speed of the KillerBall will go down.', font=('Arial Bold', 15)).place(x=50, y=470, anchor='nw')
Label(mainwindow,text='5.Game Over: Once the ball you control(the green one)', font=('Arial Bold', 15)).place(x=50, y=500, anchor='nw')
Label(mainwindow,text='touches the middle of the KillerBall(orange one), the game is over and your score will be saved.', font=('Arial Bold', 15)).place(x=50, y=530, anchor='nw')
Label(mainwindow,text='6.LeaderBoard: Once the game finished, the leaderboard window will come out. press back to return', font=('Arial Bold', 15)).place(x=50, y=560, anchor='nw')

Label(mainwindow,text='Have a nice day :)', font=('Arial Bold', 20)).place(x=1280/2-150, y=620, anchor='nw')


foodcoord=[]
mainwindow.mainloop()
