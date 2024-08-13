from tkinter import *
from PIL import Image, ImageTk
from random import randint
#main page
root =Tk()
root.title("RCP")
root.configure(background="#9b59b6")


#pictures for rcp_user
rock_img = ImageTk.PhotoImage(Image.open("/Users/prabagaranec/Desktop/guvi mern stack/Mern-Stack-guvi/day 3/rps/rock_user.png"))
paper_img = ImageTk.PhotoImage(Image.open("/Users/prabagaranec/Desktop/guvi mern stack/Mern-Stack-guvi/day 3/rps/paper_user.png"))
scissor_img = ImageTk.PhotoImage(Image.open("/Users/prabagaranec/Desktop/guvi mern stack/Mern-Stack-guvi/day 3/rps/scissors_user.png"))


#pictures for rcp_computer
rock_img_comp = ImageTk.PhotoImage(Image.open("/Users/prabagaranec/Desktop/guvi mern stack/Mern-Stack-guvi/day 3/rps/rock.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("/Users/prabagaranec/Desktop/guvi mern stack/Mern-Stack-guvi/day 3/rps/paper.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("/Users/prabagaranec/Desktop/guvi mern stack/Mern-Stack-guvi/day 3/rps/scissors.png"))



#insert picture
comp_label = Label(root, image=rock_img_comp, bg="#9b59b6")
user_label = Label(root, image=rock_img, bg="#9b59b6")
comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=5)



#scores
playerScore = Label(root, text=0, font=100, bg="#9b59b6", fg="white")
computerScore = Label(root, text=0, font=100, bg="#9b59b6", fg="white")
computerScore.grid(row=1, column=1)
playerScore.grid(row=1, column=3)


#indicators
user_ind = Label(root, font=50, text= "USER", bg="#9b59b6", fg="white")
user_ind.grid(row=0, column=3)
comp_ind = Label(root, font=50, text= "COMPUTER", bg="#9b59b6", fg="white")
comp_ind.grid(row=0, column=1)


#messages
msg =Label(root, font=50, bg="#9b59b6", fg="white")
msg.grid(row=3, column=2)



#update message
def updateMessage(x):
    msg['text'] = x



#update user_score
def updateUserScore():
    score = int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)

def updateCompScore():
    score = int(computerScore["text"])
    score += 1
    computerScore["text"] = str(score)

#check winner
def checkWinner(player, computer):
    if player == computer:
        updateMessage("its a tie")
    elif player =="rock":
        if computer =="paper":
            updateMessage("You lose")
            updateCompScore()
        else:
            updateMessage("You win")
            updateUserScore()
    elif player =="paper":
        if computer =="scissor":
            updateMessage("You lose")
            updateCompScore()
        else:
            updateMessage("You win")
            updateUserScore()
    elif player =="scissor":
        if computer =="rock":
            updateMessage("You lose")
            updateCompScore()
        else:
            updateMessage("You win")
            updateUserScore()



#update choices
choices =["rock", "paper", "scissor"]

def updateChoices(x):
#for computer
    compChoice = choices[randint(0,2)]
    if compChoice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice =="paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)

#for user    
    if x=="rock":
        user_label.configure(image=rock_img)
    elif x=="paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)
    
    checkWinner(x, compChoice)

#buttons
rock = Button(root, width=20, height=2, text="ROCK", bg="#FF3E4D", fg="red", command= lambda:updateChoices("rock"))
rock.grid(row=2, column=1)
paper = Button(root, width=20, height=2, text="PAPER", bg="#FAD02E", fg="red", command= lambda:updateChoices("paper"))
paper.grid(row=2, column=2)
scissor = Button(root, width=20, height=2, text="SCISSORS", bg="#0ABDE3", fg="red", command= lambda:updateChoices("scissor"))
scissor.grid(row=2,column=3)



root.mainloop()










