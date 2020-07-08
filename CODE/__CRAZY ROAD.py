'''
#######################################
#       Tecnologico de Costa Rica     #
#       Alessandro Hidalgo Prendas    #
#           Carné:2020099003          #  
#                                     #                                     
#                                     #
#                CE-1102              #
#            Python v(3.8.2)          #
#                                     #
#######################################
'''
#=======LIBRARY IMPORTS========#
from tkinter import *
import time
import winsound
import threading
from threading import Thread
from tkinter import messagebox
#===GLOBAL VARIABLES===#
points = 0
seconds = -1
LIVES = 15
#===============================================================================================================================================#
#                                                           #LOBBY SCREEN#                                                                      #
#===============================================================================================================================================#
class LobbyScreen:
    def __init__(self, master):
        frame = Frame(master, highlightthickness=0)
        Label(frame, image=backgroundImage).place(x=0, y=0)
        frame.place(x=0, y=0, width=500, height=480)
        print ("Welcome to CRAZY ROAD","\n","To start, type your NICKNAME")
        # -----------Show the name of the game---------------#
        self.gameName = Label(frame, text="CRAZY ROAD", font=("Berlin Sans FB Demi", 50),fg="black",bg="#9fcaea")
        self.gameName.place(x=10, y=10,width=500 ,height=120)
        # ---------------Show "text = NICKNAME"--------------#
        self.typeName = Label(frame, text=" NICKNAME:", font=("Berlin Sans FB Demi", 12),
                                  fg="white", highlightthickness=0, bg="black")
        self.typeName.place(x=170, y=145, width=200, height=25)
        # ----------Show an ENTRY to write your name---------#
        playerName = StringVar()
        self.entryname = Entry(frame,textvariable = playerName)
        self.entryname.place(x=170, y=170, width=200, height=30)
        self.entryname.config(fg="Black", justify="center", font=("Comic Sans MS", 13))  
        #--------------------PLAY-BUTTON----------------------#
        self.startButton = Button(frame, text=("PLAY"), fg="black", bg="chartreuse",
                                font=("Berlin Sans FB Demi", 20), highlightthickness=0,
                                command =self.openGameScreen)
        self.startButton.place(x=200, y=220, width=140, height=50)
        #--------------INSTRUCTIONS-BUTTON--------------------#
        self.insButton = Button(frame, text=("Instructions"), fg="black", bg="DeepSkyBlue2",
                                font=("Berlin Sans FB Demi", 16), highlightthickness=0,
                                command = self.openInstructionsScreen)
        self.insButton.place(x=200, y=280, width=140, height=30)
        #-----------------HIGHSCORES-BUTTON--------------------#
        self.hsButton = Button(frame, text=("Highscores"), fg="black", bg="DeepSkyBlue2",
                                font=("Berlin Sans FB Demi", 16), highlightthickness=0,
                                command = self.openHighSoresScreen)
        self.hsButton.place(x=200, y=330, width=140, height=30)
        #------------------CREDITS-BUTTON----------------------#
        self.creditsButton = Button(frame, text=("CREDITS"), fg="black", bg="DeepSkyBlue2",
                                font=("Berlin Sans FB Demi", 14), highlightthickness=0,
                                command = self.openCreditsScreen )
        self.creditsButton.place(x=200, y=380, width=140, height=30)
        #-------------------EXIT-FUNCTION-----------------------#
        def exitGame():             #ask if you wanna close the window
            value = messagebox.askquestion("Exit","Are you sure to close the game?")
            if value == "yes":
                window.destroy()
                music_stop()
        #---------------------EXIT-BUTTON----------------------#
        self.exitButton = Button(frame, text=("EXIT"), fg="black", bg="red",
                                font=("Berlin Sans FB Demi", 16), highlightthickness=0,
                                command=exitGame)
        self.exitButton.place(x=200, y=430, width=140, height=30)
#---------------ExitWINDOWS/NewScreenCOMMANDS------------------#
    def openGameScreen(self):
        global nick
        nick = self.entryname.get()
        window.withdraw()
        GameScreen()
        music_stop()
        Highscores()
    def openCreditsScreen(self):
        window.withdraw()
        CreditsScreen()
        music_stop()
    def openInstructionsScreen(self):
        window.withdraw()
        InstructionsScreen()
        music_stop()
    def openHighSoresScreen(self):
        window.withdraw()
        HighScoresScreen()
        music_stop()
    
     
#===============================================================================================================================================#
#                                                          #GAME SCREEN#                                                                        #
#===============================================================================================================================================#

class GameScreen():
    def __init__(self):
        
        music_stop()
        self.gameScreen=Toplevel()
        self.gameScreen.minsize(1000,800)
        self.gameScreen.resizable(0,0)
        self.gameScreen.config(bg="black")
        self.gameScreen.iconbitmap("ICON.ico")
        #---------SCORE FUNCTION----------------#
        def score():
            global points
            points = points + 5
            self.counter.configure(text=str(points))
            self.gameScreen.after(1000,score)
        def timer():
            global seconds
            seconds = seconds + 1
            self.secondss.configure(text=str(seconds))
            self.gameScreen.after(1000,timer)
        #-----------------------------------------------#
        print ("Hi", nick.upper(), "Are you Ready??") #print in console
        #------------Show the name CRAZY ROAD-----------#
        self.crazyRoad = Label(self.gameScreen, text="CRAZY ROAD", font=("Berlin Sans FB Demi", 26),
                                fg="white", highlightthickness=0, bg="black")
        self.crazyRoad.place(x=700, y=20, width=300, height=35)
        #------------Show "Player:" in screen-------------#
        self.Player = Label(self.gameScreen, text=('PLAYER:'), font=("Berlin Sans FB Demi", 18),
                                fg="white", highlightthickness=0, bg="black")
        self.Player.place(x=700, y=70, width=300, height=35)
        #-------------Show your NICKNAME-----------------#
        self.Nick = Label(self.gameScreen, text=(nick.upper()), font=("Berlin Sans FB Demi", 28)
                                ,fg="red4", highlightthickness=0, bg="black")
        self.Nick.place(x=700, y=120, width=300, height=35)
        #-------------Show game SECONDS in screen----------#
        self.time = Label(self.gameScreen, text=("TIME:"), font=("Berlin Sans FB Demi", 20),fg="white", bg="black")
        self.time.place(x=700, y=300, width=120, height=35)
        self.STRseconds = Label(self.gameScreen,text = ("Seconds") ,font= ("Berlin Sans FB Demi",20),fg="white",bg="black")
        self.STRseconds.place(x=890,y=300,width=110, height=35)
        self.secondss = Label(self.gameScreen,text = 0 ,font= ("Berlin Sans FB Demi",20),fg="white",bg="black")
        self.secondss.place(x=810,y=300,width=90, height=35)
        timer()
        #-------------Show your SCORE in screen----------#
        self.scoreSTR = Label(self.gameScreen, text=("SCORE:"), font=("Berlin Sans FB Demi", 20)
                              ,fg="white", highlightthickness=0, bg="black")
        self.scoreSTR.place(x=700, y=200, width=120, height=35)
        self.STRpts = Label(self.gameScreen,text = "PTS" ,font= ("Berlin Sans FB Demi",20),fg="white",bg="black")
        self.STRpts.place(x=890,y=200,width=60, height=35)
        self.counter = Label(self.gameScreen,text = 0 ,font= ("Berlin Sans FB Demi",20),fg="white",bg="black")
        self.counter.place(x=810,y=200,width=90, height=35)
        score()
        #----------Show lives
        self.lives= Label(self.gameScreen,text = 0 ,font= ("Berlin Sans FB Demi",20),fg="white",bg="black")
        self.lives.place(x=810,y=400,width=90, height=35)
        self.livesSTR = Label(self.gameScreen, text=("LIFES:"), font=("Berlin Sans FB Demi", 20)
                              ,fg="white", highlightthickness=0, bg="black")
        self.livesSTR.place(x=710, y=400, width=120, height=35)
        
        
        #---------------BUTTON BACK TO LOBBY---------------#
        self.back = Button(self.gameScreen, text=("BACK TO LOBBY"), fg="black", bg="lime",
                                font=("Berlin Sans FB Demi", 14), highlightthickness=0,
                                command = self.returnLOBBY)
        self.back.place(x=780, y=750, width=170, height=30)
        #------------------------------------------------------------------#
        self.c= Canvas(self.gameScreen,width=700,height=800)                #create canvas #
        self.c.place(x=0,y=0)
        self.background = self.c.create_image(350,400,image=mapGAME)        # create the background canvas image #
        self.PLAYERcar = self.c.create_image(510,700, image=playerCar)      # PLAYER CAR create #
        self.ENEMYcar = self.c.create_image(510,-500, image=enemyCar)       # ENEMY CAR create #
        self.TRUCK1 = self.c.create_image(310,-400, image=trucks)           # TRUCK CAR create #
        self.BONUscar = self.c.create_image(210,-400, image=bonusCar)       # BONUS CAR create #
        self.COPScar = self.c.create_image(410,-700, image=COPScar)         # BONUS CAR create #

        
        #------ DETECT COLLITIONS FUNCTIONS----------#
        def collitions(self):
            global LIVES
            self.lives.configure(text=str(LIVES))
           
            if self.c.coords(self.PLAYERcar) == self.c.coords(self.ENEMYcar):
                time.sleep(0.02)
                LIVES -= 1
                winsound.PlaySound("CRASH.wav",winsound.SND_ASYNC)
                gameover()
             
            elif self.c.coords(self.PLAYERcar) == self.c.coords(self.COPScar):
                time.sleep(0.02)
                LIVES -= 1
                winsound.PlaySound("CRASH.wav",winsound.SND_ASYNC)
                gameover()

            elif self.c.coords(self.PLAYERcar) == self.c.coords(self.TRUCK1):
                time.sleep(0.02)
                LIVES -= 2
                winsound.PlaySound("CRASH.wav",winsound.SND_ASYNC)
                gameover()

            elif self.c.coords(self.PLAYERcar) == self.c.coords(self.BONUscar):
                global points
                time.sleep(0.02)
                LIVES -= 1
                winsound.PlaySound("CRASH.wav",winsound.SND_ASYNC)
                gameover()
                

    
 
        def gameover():
            if LIVES >0:
                print ("Still have lives")
            elif LIVES <=0:
                self.openGAMEOVER()
                
                
        
            
#------------------EMEMY CARS MOVE-----------------------------------------#
        
        
        def moveENEMY(self):                                # normal enemy move
            collitions(self)
            if self.c.coords(self.ENEMYcar)[1]>=850:
                self.c.move(self.ENEMYcar,0,-1450)
                startTHREAD()
                
            else:
                self.c.move(self.ENEMYcar,0,10)
                time.sleep(0.01)
                moveENEMY(self)
                collitions(self)
        #------------------------
        def moveTRUCK(self):                                # truck move 
            if self.c.coords(self.TRUCK1)[1]>=850:
                self.c.move(self.TRUCK1,0,-1250)
                startTHREAD2()
                
            else:
                self.c.move(self.TRUCK1,0,5)
                time.sleep(0.01)
                moveTRUCK(self)
        #------------------------    
        def moveBONUS(self):                                # bonus car move
            collitions(self)
            if self.c.coords(self.BONUscar)[1]>=850:
                self.c.move(self.BONUscar,0,-2000)
                startTHREAD3()
                
            else:
                self.c.move(self.BONUscar,0,10)
                time.sleep(0.01)
                moveBONUS(self)
                collitions(self)
        #------------------------       
        def moveBG(self):                                   # background move
            if self.c.coords(self.background)[1]>=2000:
                self.c.move(self.background,0,-1750)
                startTHREAD4()                
            else:
                self.c.move(self.background,0,17)
                time.sleep(0.01)
                moveBG(self)
                
                
        #------------------------        
        def moveCOPS(self):                                # truck move
            collitions(self)
            if self.c.coords(self.COPScar)[1]>=850:
                self.c.move(self.COPScar,0,-1750)
                startTHREAD5()
                
            else:
                self.c.move(self.COPScar,0,10)
                time.sleep(0.01)
                moveCOPS(self)
                collitions(self)

                
        #------ THREADS FUNCTIONS----------#

        def startTHREAD():
            thread = Thread(target=moveENEMY,args=(self,))
            thread.daemon = True
            thread.start()
        def startTHREAD2():
            thread2 = Thread(target=moveTRUCK,args=(self,))
            thread2.daemon = True
            thread2.start()
        def startTHREAD3():
            thread3 = Thread(target=moveBONUS,args=(self,))
            thread3.daemon = True
            thread3.start()
        def startTHREAD4():
            thread4 = Thread(target=moveBG,args=(self,))
            thread4.daemon = True
            thread4.start()
        def startTHREAD5():
            thread5 = Thread(target=moveCOPS,args=(self,))
            thread5.daemon = True
            thread5.start()

        startTHREAD()
        startTHREAD2()
        startTHREAD3()
        startTHREAD4()
        startTHREAD5()

        
      #-------------------------------PLAYER MOVEMENT---------------------------------------------#
        def MoveRight(event): 
            if self.c.coords(self.PLAYERcar)[0]>=510:       # Doesnt allow it to move if it is too close to the edge 
                self.c.move(self.PLAYERcar ,0,0)
                collitions(self)
                #winsound.PlaySound("1LIVE.wav",winsound.SND_ASYNC)
            else:
                self.c.move(self.PLAYERcar ,100,0)    # Move 100 pixels to the Right
                collitions(self)
        def MoveLeft(event):  
            if self.c.coords(self.PLAYERcar)[0]<=210:       # Doesnt allow it to move if it is too close to the edge 
                self.c.move(self.PLAYERcar ,0,0)
                collitions(self)
                #winsound.PlaySound("1LIVE.wav",winsound.SND_ASYNC)
            else:
                self.c.move(self.PLAYERcar ,-100,0)   # Move 100 pixels to the Left
                collitions(self)
        def MoveDown(event):
            if self.c.coords(self.PLAYERcar)[1]>=790:       # Doesnt allow it to move if it is too close to the edge 
                self.c.move(self.PLAYERcar ,0,0)
                collitions(self)
                #winsound.PlaySound("1LIVE.wav",winsound.SND_ASYNC)
            else:
                self.c.move(self.PLAYERcar, 0,10)    # Move 10 pixels down
                collitions(self)
        def MoveUp(event):
            if self.c.coords(self.PLAYERcar)[1]<=10 :       # Doesnt allow it to move if it is too close to the edge 
                self.c.move(self.PLAYERcar ,0,0)
                collitions(self)
                #winsound.PlaySound("1LIVE.wav",winsound.SND_ASYNC)
            else:
                self.c.move(self.PLAYERcar, 0,-10)   # Move 10 pixels up
                collitions(self)
        #-------------KEYBOARD CALLS------------------#
        self.c.bind("<Right>",MoveRight)
        self.c.bind("<Left>",MoveLeft)
        self.c.bind("<Down>",MoveDown)
        self.c.bind("<Up>",MoveUp)
        self.c.focus_set()
        
        #--------------------------------------------#


        self.gameScreen.mainloop()
    def returnLOBBY(self): # Return to the menu window and hide the GameWindow #
        openLobby()
        self.gameScreen.destroy()
        global points,seconds,LIVES
        points = 0
        seconds = 0
        LIVES = 15
        #opengame = False
    def openGAMEOVER(self):
        self.gameScreen.destroy()
        GAMEOVER()
        LIVES = 15
        
        
#===============================================================================================================================================#       
#                                                       #INSTRUCTIONS SCREEN#                                                                   #
#===============================================================================================================================================#
        
class InstructionsScreen:
    def __init__(self):
        print ("Here you can see the instructions and key events")
        #-------------------------------------------#
        self.instructions=Toplevel()
        self.instructions.minsize(500,550)
        self.instructions.title("Game INSTRUCTIONS")
        self.instructions.resizable(0,0)
        self.instructions.config(bg="pink")
        self.instructions.iconbitmap("ICON.ico")
        #-------------------------------------------#
        instruct= Canvas(self.instructions,width=500,height=550)
        instruct.create_image(250,150,image=roadImage)
        instruct.create_image(250,275,image=instructions)
        instruct.place(x=0,y=0)
        self.back = Button(self.instructions, text=("BACK"), fg="black", bg="lime",
                                font=("Berlin Sans FB Demi", 14), highlightthickness=0,
                                command = self.returnLOBBY )
        self.back.place(x=420, y=13, width=70, height=30)
    def returnLOBBY(self): # Return to the menu window and hide the Instructions Window #
        openLobby()
        self.instructions.withdraw()
        music_play()
        #INSTRUCTIONS SCREEN LOOP#
        self.instructions.mainloop()
#===============================================================================================================================================#        
#                                                           #HIGHSCORES SCREEN#                                                                 #
#===============================================================================================================================================#
        
class HighScoresScreen:
    def __init__(self):
        print ("Here you can see the highscores")
        #----------------------------------------#
        self.hscores=Toplevel()
        self.hscores.minsize(500,480)
        self.hscores.title("Game HIGHSCORES")
        self.hscores.resizable(0,0)
        self.hscores.iconbitmap("ICON.ico")
        #-----------------------------------------#
        bg = Frame(self.hscores, highlightthickness=0)
        Label(bg, image=highscores).place(x=0, y=0)
        bg.place(x=0, y=0, width=500, height=480)
        #
        self.back = Button(self.hscores, text=("BACK"), fg="black", bg="lime",
                                font=("Berlin Sans FB Demi", 14), highlightthickness=0,
                                command = self.returnLOBBY )
        self.back.place(x=420, y=445, width=70, height=30)

        Highscores()
        read_file()
        print_scores()
        self.hscores.mainloop()

    def returnLOBBY(self): # Return to the menu window and hide the Highscores Window #
        openLobby()
        self.hscores.withdraw()
        music_play()


    
        #HIGSCORES SCREEN LOOP
        
#===============================================================================================================================================#       
#                                                        #CREDITS SCREEN#                                                                       #
#===============================================================================================================================================#
        
class CreditsScreen:
    def __init__(self):
        print ("Here you can see the game credits")
        
        self.credits=Toplevel()
        self.credits.minsize(646,586)
        self.credits.title("Game CREDITS")
        self.credits.resizable(0,0)
        self.credits.config(bg="gray")
        self.credits.iconbitmap("ICON.ico")
        #------------
        Credits= Canvas( self.credits,width=646,height=586)
        Credits.create_image(323,293,image=creditsimg)
        Credits.place(x=0,y=0)
        self.back = Button(self.credits, text=("BACK"), fg="black", bg="lime",
                                font=("Berlin Sans FB Demi", 14), highlightthickness=0,
                                command = self.returnLOBBY )
        self.back.place(x=560, y=550, width=70, height=30)
    def returnLOBBY(self): # Return to the menu window and hide the Credits Window #
        openLobby()
        self.credits.withdraw()
        music_play()
        #CREDITS SCREEN LOOP
        self.credits.mainloop()

#===============================================================================================================================================#       
#                                                        #GAME OVER SCREEN#                                                                     #
#===============================================================================================================================================#
        
class GAMEOVER:
    def __init__(self):
        print ("TOU LOSE")
        
        self.gover=Toplevel()
        self.gover.minsize(800,200)
        self.gover.title("GAME OVER")
        self.gover.resizable(0,0)
        self.gover.config(bg="BLACK")
        self.gover.iconbitmap("ICON.ico")
        #------------
        self.GAMEover = Label(self.gover, text=("GAME OVER"), font=("Berlin Sans FB Demi", 90),fg="white", bg="black")
        self.GAMEover.place(x=0, y=10, width=800, height=100)
        
        self.back = Button(self.gover, text=("EXIT"), fg="black", bg="lime",
                                font=("Berlin Sans FB Demi", 18), highlightthickness=0,
                                command = self.EXIT )
        self.back.place(x=330, y=130, width=200, height=50)
    def EXIT(self): # Return to the menu window and hide the GAME OVER Window #
        music_play()
        self.gover.destroy()
        window.destroy()
        #GAME OVER SCREEN LOOP
        self.credits.mainloop()
        LIVES = 15
        
#======================WINDOW CONFIGURES================================================================#
def Highscores():  # Creación de los mejores puntajes #
        #read_file()
        global P1_SCORE,P2_SCORE,P3_SCORE
        global points,nick
        file = open("highscores.txt","w")
        file.write(nick.upper())
        file.close()

def openLobby():
    window.deiconify()
    music_play()

############    
def music():        # load the song 
        winsound.PlaySound("menuSONG.wav",winsound.SND_ASYNC)
def music_stop():   # stop music function 
        winsound.PlaySound(None,0)
def music_play():   # start music function 
    music_thread=Thread(target=music,args=())
    music_thread.daemon = True
    music_thread.start()
    
music_play()

######################################################################################
window = Tk()
window.title("CRAZY ROAD")      # Window Title 
window.minsize(500, 480)        # Window Size 
window.iconbitmap("ICON.ico")   # Window Icon 
window.resizable(0, 0)          # Lock resizable option 
#----------ImageLoads-------------#
backgroundImage = PhotoImage(file="backgIMAGE.gif") # Lobby background image 
playerCar = PhotoImage(file="JEEP.png")             # Player car image 
enemyCar = PhotoImage(file="enemiesCars.png")       # Normal enmey car image 
trucks = PhotoImage(file="trucks.png")              # truck image 
bonusCar = PhotoImage(file="bonus.png")             # bonus car image
COPScar = PhotoImage(file="COPS.png")               # COPS car image 
instructions = PhotoImage(file="INSTRUCTIONS.png")  # PNG instructions
roadImage = PhotoImage(file="ROAD.png")             # Instructiosn background image
creditsimg = PhotoImage(file="CREDITS.png")         # credits img 
highscores = PhotoImage(file="highscores.png")      # higscores background image 
mapGAME = PhotoImage(file="ROADEDITED.png")         # GameScreen background image 
#
windowLobby = LobbyScreen(window)
window.mainloop()
