# Resolution: 1280 x 720
import os, configparser
from tkinter import Tk, Canvas, IntVar, Label, PhotoImage, StringVar, Entry, Button, messagebox
from random import randint as rand
from time import sleep


def start():
    global start

    if playername.get() == '':
        messagebox.showinfo(title='Ooops! Please Check the Following...', message='Please type your name correctly！')
        # playername.set('you hit me')
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
            player = canvas.create_text( 1280/2-200 , 10 , fill="white" , font="Times 20 italic bold", text="PLAYER: " + file4.read())
            file4.close()

            canvas.config(bg="black")

            file5 = open("score.txt")
            score = int(file5.read())
            txt = "Score:" + str(score)
            scoreText = canvas.create_text( 1280/2+50 , 10 , fill="white" , font="Times 20 italic bold", text=txt)
            file5.close()

        else:
            player = canvas.create_text( 1280/2-200 , 10 , fill="white" , font="Times 20 italic bold", text="PLAYER: " + playername.get())
            canvas.config(bg="black")
            score = 0
            txt = "Score:" + str(score)
            scoreText = canvas.create_text( 1280/2+50 , 10 , fill="white" , font="Times 20 italic bold", text=txt)
        





        canvas.bind("<Left>", leftKey)
        canvas.bind("<Right>", rightKey)
        canvas.bind("<Up>", upKey)
        canvas.bind("<Down>", downKey)

        canvas.bind("<p>", pause)

        canvas.bind("<h>", hide)

        

        canvas.bind("<"+left.get()+">", leftKey)
        canvas.bind("<"+right.get()+">", rightKey)
        canvas.bind("<"+up.get()+">", upKey)
        canvas.bind("<"+down.get()+">", downKey)

        # canvas.bind("<MouseWheel>",zoomer)
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





def pause(event):
    global pause, pausemsg
    if pause == 0:
        pause = 1
        pausemsg = canvas.create_text( 1280/2 , 720/2 , fill="white" , font="Times 20 italic bold", text="The Game Is Paused, Press P to return." )
    else:
        canvas.delete(pausemsg)
        pause = 0


def movekiller():
    global killer, xlg, ylg, xrg, yrg, directiong, countdown, xl, xr, yl, yr, pause, end, leaderfile, score, start, firsttime, movspeed
    if pause == 1:
        canvas.after(90, movekiller)
    elif end == 1:
        canvas.destroy()
        leaderboard()

    else:
        if countdown != 0:
            if xlg-(xl+xr)/2 <= (xr-xl)/2 and xlg-(xl+xr)/2 >= -(xr-xl)/2 and ylg-(yl+yr)/2 <= (yr-yl)/2 and ylg-(yl+yr)/2 >= -(yr-yl)/2:

                # if not os.path.isfile('leader.ini'):
                    # leaderfile = open('leader.ini','r')
                # os.remove('leader.ini') # else:
                # newfile=open('leader.ini','w')
                # newfile.write('')
                # newfile.close()
                # os.remove('leader.ini')
                if firsttime == 1:
                    leaderfile.write(open('leader.ini','w'))
                    leaderfile.add_section('total')
                    leaderfile.set("total","total","1")
                    leaderfile.set("total","1name","")
                    leaderfile.set("total","1score","0")
                    firsttime = 0
                else:
                    leaderfile.write(open('leader.ini','w'))
                    # leaderfile.add_section('total')
                    # leaderfile.set("total","total","1")
                    # leaderfile.set("total","1name","")
                    # leaderfile.set("total","1score","0")
                

            # else:


                end = 1
                # leaderfile.write(open('leader.ini','a'))
                leadernum = leaderfile.get('total', 'total')
                leaderfile.set('total', 'total', str(int(leadernum)+1))
                leaderfile.set('total', str(int(leadernum)+1)+'name', playername.get())
                leaderfile.set('total', str(int(leadernum)+1)+'score', str(score))
                # leaderfile.close()
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



def timer():
        global countdown, foodcoordx, foodcoordy, xl, xr, yr, yl, growth, pball, directiong, pause, end, movspeed

        if pause == 1 or end == 1:
            canvas.after(90, timer)
        else:
            if countdown > 0:
                # boom()
                for i in range (len(foodcoordx)):
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
                # boomdir()
                directiong = rand(0, 3)
                countdown = 30
                movspeed += 15
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


# def zoomer(event):
# 		global zoomer, xr, xl, yr, yl, pball, food
# 		if (event.delta > 0):
# 			canvas.scale("all", (xr-xl)/2, (yr-yl)/2, 1.1, 1.1)
# 		elif (event.delta < 0):
# 			canvas.scale("all", (xr-xl)/2, (yr-yl)/2, 0.9, 0.9)
# 			canvas.configure(scrollregion = canvas.bbox("all"))


def leaderboard():
    global leaderfile, leaders, end, movspeed, gamefromsave
    if end == 1:
        end = 0
        movspeed = 30
        gamefromsave = 0


    if not os.path.isfile('leader.ini'):
        # leaderfile = open('leader.ini','r')
    # else:
        leaderfile.write(open('leader.ini','a'))
        leaderfile.add_section('total')
        leaderfile.set("total","total","1")
        leaderfile.set("total","1name","")
        leaderfile.set("total","1score","0")

    leaders = Canvas(mainwindow, width=1280, height=720)
    leaders.pack()
    leaders.create_text( 1280/2 , 200 , fill="black" , font="Times 20 italic bold", text="L E A D E R B O A R D" )

    highest = 1
    for i in range(int(leaderfile.get('total','total'))):
        if int(leaderfile.get('total',str(i+1)+'score')) >= int(leaderfile.get('total',str(highest)+'score')):
            highest = i+1
    leaders.create_text(1280/2 , 350 , fill="red" , font="Times 20 italic bold", text="1ST Position: "+leaderfile.get('total',str(highest)+'name')+"  Score: "+leaderfile.get('total',str(highest)+'score'))        
    
    secondpos = 1
    for i in range(int(leaderfile.get('total','total'))):
        if int(leaderfile.get('total',str(i+1)+'score')) >= int(leaderfile.get('total',str(secondpos)+'score')) and secondpos != highest:
            secondpos = i + 1

    leaders.create_text(1280/2 , 450 , fill="orange" , font="Times 20 italic bold", text="2ND Position: "+leaderfile.get('total',str(secondpos)+'name')+"  Score: "+leaderfile.get('total',str(secondpos)+'score')) 

    thipos = 1
    for i in range(int(leaderfile.get('total','total'))):
        if int(leaderfile.get('total',str(i+1)+'score')) >= int(leaderfile.get('total',str(thipos)+'score')) and thipos != highest and thipos != secondpos:
            secondpos = i + 1
    leaders.create_text(1280/2 , 550 , fill="purple" , font="Times 20 italic bold", text="3RD Position: "+leaderfile.get('total',str(thipos)+'name')+"  Score: "+leaderfile.get('total',str(thipos)+'score')) 

    # leaderfile.close()

    Button(leaders, text='Back', font=('Arial', 15), width=10, height=1, command=destroyleader).place(x=1280/2, y=600, anchor='nw')



def destroyleader():
    global leaders
    leaders.destroy()


def moveBall():
    global moveBall, direction, balls, xl, yl, xr, yr, food, score, scoreText, pball, growth, xy, pause, end
    if pause == 1 or end == 1:
     canvas.after(90, moveBall)
    else:
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

            growth = 0

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

        #     if overlapping(sHeadPos, canvas.coords(snake[i])):
        #         gameOver = True
        #         canvas.create_text(width/2,height/2,fill="white",font="Times 20 italic bold", text="Game Over!")
        # for i in range(1,len(balls)):
        #  positions.append(canvas.coords(balls[i]))
        # for i in range(len(balls)-1):
        #  canvas.coords(balls[i+1],positions[i][0], positions[i][1],positions[i][2],positions[i][3])

        canvas.after(90, moveBall)

        # for i in range(1,len(snake)):
        #     positions.append(canvas.coords(snake[i]))
        # for i in range(len(snake)-1):
        #     canvas.coords(snake[i+1],positions[i][0], positions[i][1],positions[i][2],positions[i][3])
        # if 'gameOver' not in locals():

def hide(event):
    global hider, pause, canvashade
    if hider == 0:
        hider=1
        pause=1
        canvashade = Canvas(canvas, width=1280, height=720, bg='white')
        canvashade.pack()
        shademsg = canvashade.create_text( 1280/2 , 720/2 , fill="black" , font="Times 20 italic bold", text="Welcome to Python, You Pressed a BOSS KEY! Press again to restore." )
        # mainwindow.withdraw()
        # bosskeydis = canvas.create_image(img=bosskey)

        if os.path.isfile('python.png'):
            photo = PhotoImage(file='python.png')
            img_label = Label(canvashade, img=photo)
    else:
        hider=0
        pause=0
        canvashade.destroy()

        

        # canvas.delete(bosskeydis)

def call_back(event):
    global call_back, pause, pausemsg, score, movspeed, xl, xr, yl, yr
    # print(event.keysym)
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
            # gamesaver.write(open('config.ini','w'))
            # newfile.write('< Statistics Summary >\n'+'the total number of words :')
            # gamesaver.add_section('db')
            # gamesaver.set("db", "db_pass", "xgmtest")
            # gamesaver.close()
            # print(gamesaver.get("db", "db_pass"))

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

def load():
    global gamefromsave
    if os.path.isfile('name.txt'):
        gamefromsave = 1
        start()
    else:
        messagebox.showinfo(title='Ooops!', message='You have not saved a game ! Please play a little bit the game and press <k> to save.')

    

mainwindow = Tk()

mainwindow.title("Battle Of Balls (adapted)")
mainwindow.geometry('1280x720')



Label(mainwindow,text='Battle Of Balls (adapted)', font=('Arial Bold', 20)).place(x=500, y=200, anchor='nw')
Label(mainwindow,text='Please Type Your Name :', font=('Arial Bold', 15)).place(x=350, y=250, anchor='nw')

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

gamesaver = configparser.ConfigParser()
leaderfile = configparser.ConfigParser()


e = Entry(mainwindow, show=None, font=('Arial', 14), textvariable=playername).place(x=600, y=250, anchor='nw')
# playername.set('you hit me')
Button(mainwindow, text='Start !', font=('Arial', 15), width=10, height=1, command=start).place(x=600, y=350, anchor='nw')
# User control
Button(mainwindow, text='Reload a Game from local', font=('Arial', 15), width=30, height=1, command=load).place(x=800, y=350, anchor='nw')
Label(mainwindow,text='User Settings(Customary Control Keys):', font=('Arial Bold', 15)).place(x=500, y=720/2+50, anchor='nw')
Label(mainwindow,text='UpKey :', font=('Arial Bold', 15)).place(x=450, y=440, anchor='nw')
upk=Entry(mainwindow, show=None, font=('Arial', 14), textvariable=up).place(x=550, y=440, anchor='nw')
Label(mainwindow,text='DownKey:', font=('Arial Bold', 15)).place(x=450, y=470, anchor='nw')
downk=Entry(mainwindow, show=None, font=('Arial', 14), textvariable=down).place(x=570, y=470, anchor='nw')
Label(mainwindow,text='LeftKey:', font=('Arial Bold', 15)).place(x=450, y=500, anchor='nw')
leftk=Entry(mainwindow, show=None, font=('Arial', 14), textvariable=left).place(x=570, y=500, anchor='nw')
Label(mainwindow,text='RightKey:', font=('Arial Bold', 15)).place(x=450, y=530, anchor='nw')
rightk=Entry(mainwindow, show=None, font=('Arial', 14), textvariable=right).place(x=570, y=530, anchor='nw')
Label(mainwindow,text='! Notice: The keys <Left> <Right> <Up> <Down> are kept unchanged intentationally just in case the Customary Keys do not work.', font=('Arial Bold', 15)).place(x=40, y=570, anchor='nw')

# bosskey = PhotoImage(file="python.png")


# else:
#     leaderfile = open('leader.ini','w')
    # leaderfile.add_section('totalplayer')
    # leaderfile.set("totalplayer", "1", "xgmtest")



foodcoord=[]




mainwindow.mainloop()


