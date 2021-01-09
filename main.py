from time import *
from math import *
from random import *
from playsound import *
from pygame import *
from os import *

print("<----<---- w e l c o m e to TIC-TAC-TOE w o r l d ---->---->")
print("****************************#**********************************")
print("heeeyyyy! aliens ...you are feeling bored enough??? i have a solution ...follow me please@@@@@@@@@")
sleep(2)
player1=input("please! entre the name of the first player :-")
player2=input("please! entre the name of the second  player :-")
sleep(2)
print("LETS BE AWARE WITH THE RULESSSS:------->>>")
print("Here is the tic-tac-toe table")
print("                            ")
print("POS 1 | POS 2 | POS 3             #here POS:- position ")
print("______|_______|______")
print("POS 4 | POS 5 | POS 6")
print("______|_______|______")
print("POS 7 | POS 8 | POS 9")
print("      |       |      ")
print("                          ")
sleep(4)
print("The above given tik-tac-toe table has 9 different positions(1 to 9) were you can insert your symbols i.e cross(X) or zero (O) ")
print("In each chance , respective players are asked to entre the positions at which his/her symbol get inserted ")
print("RULES FOR POINTS ------> 1) for each win ,winner get 2 points and looser gets 0 points")
print("                         2) If the match get tied both the player get 1 point each")
print(" for any consiquitive pairs of three symbols( horizontal / vertical / daigonsls ),players won that match")
print(" you can play as much as game you want. ")
print("Afer any game you can quit that series and after that final quit , name of the winner is announced with the points")
print ("<--------------********************#########***#########*********************------------------->")
sleep(2)
print(" waitt*** Which player got the chance to play its move first???????????")
sleep(2)
print("lets decide it with a toss")
print(f"heyy {player1} you are lucky enough to get chance to chose for the tosss....tell what you want??")
print("for HEAD ----> Press H ")
print("for TAIL ----> Press T ")
playerchoice=input()
cmpchoice=choice(["H","T"])
print("processiingg.........")
print("                 ")
sleep(3)
if playerchoice==cmpchoice:
    print(f"annnnndddd its {playerchoice} ....hureeeeeyyy!! congrats {player1} you won the toss. you got a chance to play first")
    print(f"{player1} your smybol is --> 'X' ")
    print(f"{player2} your smybol is --> 'O' ")
    chance=player1
    nxtchance=player2
    p1sym = "X"
    p2sym = "O"
else:
    print(f"annnnndddd its {cmpchoice} ....ooopppss!! {player1} you loss but {player2} won the toss and got a chance to play first")
    print(f"{player2} your smybol is --> 'X' ")
    print(f"{player1} your smybol is --> 'O' ")
    chance = player2
    nxtchance = player1
    p1sym = "X"
    p2sym = "O"
sleep(3)
con,point1,point2,match,=1,0,0,0
def display(tt):
    for i in range(5):
        for j in range(5):
            if i%2!=0 and j%2==0 :
              print(end="-")
              print(tt[i][j],end="-")
            elif i%2!=0 and j%2!=0 :
              print(tt[i][j], end="")
            elif i%2==0 and j%2!=0 :
               print(tt[i][j], end="")
            else :
                print(end=" ")
                print(tt[i][j], end=" ")
        print()

def table(tt,p,sym):
    if p in l1 or p in l2:
        print(" this position is already filled . plzzzzzzz enter a valid empty position!!!!")
        temp = int(input("reentre your position plzzz----->"))
        table(temp, sym)
    elif p==1:
        tt[0][0]=sym
        display(tt)
    elif p==2:
        tt[0][2] = sym
        display(tt)
    elif p==3:
        tt[0][4] = sym
        display(tt)
    elif p==4:
        tt[2][0] = sym
        display(tt)
    elif p==5:
        tt[2][2] = sym
        display(tt)
    elif p==6:
        tt[2][4] = sym
        display(tt)
    elif p==7:
        tt[4][0] = sym
        display(tt)
    elif p==8:
        tt[4][2] = sym
        display(tt)
    elif p==9:
        tt[4][4] = sym
        display(tt)
    else:
        print(" WARNING! its is a invalid position ...plz entre in range 1 to 9")
        temp=int(input("reentre your position plzzz----->"))
        table(temp,sym)
def win(l):
    s=set(l)
    if s=={1,2,3} or s=={4,5,6} or s=={7,8,9} or s=={1,4,7} or s=={2,5,8} or s=={3,6,9} or s=={1,5,6} or s=={3,5,7}:
        return True
    else:
        return False
def sound():
    mixer.init()
    mixer.music.load("scam1992.mp3")
    mixer.music.play()
while con:
    tt = [[' ', '|', ' ', '|', ' '], ['-', '+', '-', '+', '-'], [' ', '|', ' ', '|', ' '], ['-', '+', '-', '+', '-'],
          [' ', '|', ' ', '|', ' '], ['-', '+', '-', '+', '-']]
    tie=1
    l1=[]
    l2=[]
    print("<------LETS BEGIN THE WAR-------->")
    print(f" match number {match} ")
    print("      |       |      ")
    print("______|_______|______")
    print("      |       |      ")
    print("______|_______|______")
    print("      |       |      ")
    print("      |       |      ")
    print("                          ")
    match =match+1
    for  i in range(1,10):
         sleep(3)
         if i%2!=0:
             print(f"its {chance} turns")
             p1=int(input(" enter your position:---->"))
             table(tt,p1,p1sym)
             if p1 not in l1 or p1 not in l2:
                 l1.append(p1)

             if win(l1):
                 print(" incredible fantastic excellent extraordinaary marvlous")
                 print(f" hurreeeee !!! {chance} you won the match {match}")
                 playsound("youwin.mp3")
                 point1 = point1 + 2
                 tie = 0
                 sleep(3)
                 break

         else:
             sleep(3)
             print(f"its {nxtchance} turns")
             p2 = int(input(" enter your position :----> "))
             table(tt,p2,p2sym)
             if p2 not in l1 or p2 not in l2:
                 l2.append(p2)
             if win(l1):
                 print(" incredible fantastic excellent extraordinaary marvlous")
                 print(f" hurreeeee !!! {nxtchance} you won the match {match}")
                 playsound('youwin.mp3')
                 point2 = point2 + 2
                 tie = 0
                 sleep(3)
                 break
    if tie:
         print(" ooopssss!! close enough ***___>> MATCH TIE")
    print(" Do you want to play one another game????")
    print(" for yes -----> press 1 ")
    print(" for No -----> press 0 ")
    q = int(input())
    if q == 0:
        con=0
    else:
        con=1
print(f" {chance} and {nxtchance} both of you are jssst amazinggg ")
sleep(2)
print(" IT'S RESULT TIME")
print("prepareing the result .......processiingg plzzzz waitt")
sleep(3)
print(f"{chance} got {point1} out of "+ str(match*2)+" points")
print(f"{nxtchance} got {point2} out of "+ str(match*2) +" points")
if ppoint1>point2:
    print(f" {chance} is the WINNWER of this seriesss....huuureeyyyyyyy")
if point1<point2:
    print(f" {nxtchance} is the WINNWER of this seriesss....huuureeyyyyyyy")
elif point1==point2:
    print(f"both of you have same points so this series end with a draw")
playsound("scam1992.mp3")




