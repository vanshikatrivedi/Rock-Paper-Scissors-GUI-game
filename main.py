
from tkinter import *
from tkinter import messagebox as tmsg
import random

def pick():
	a = random.choice(["Scissor","Rock","Paper"])
	return a


root = Tk()

root.title("ROCK-PAPER-SCISSOR")
root.geometry("660x220")
root.minsize(height = "260", width = "710")

#images
hand = PhotoImage(file = "Hand.png")
paper = PhotoImage(file = "paper.png")
rock_image = PhotoImage(file = "rock.png")


#functions
def rock_button():
	comp = pick()
	if comp == "Paper":
	    return tmsg.showinfo("Paper","Oops! You lose :(")
	elif comp == "Scissor":
	    return tmsg.showinfo("Scissor","You win :)")
	elif comp == "Rock":
	    return tmsg.showinfo("Rock ", "Its a draw! ")



def paper_button():
	comp = pick()
	if comp == "Paper":
	    return tmsg.showinfo("Paper","Its a draw!")
	elif comp == "Scissor":
	    return tmsg.showinfo("Scissor","Oops! You lose :(")
	elif comp == "Rock":
	    return tmsg.showinfo("Rock ", "You win :)")
def scissor_button():
	comp = pick()
	if comp == "Paper":
	    return tmsg.showinfo("Paper","You win :)")
	elif comp == "Scissor":
	    return tmsg.showinfo("Scissor","Its a draw!")
	elif comp == "Rock":
	    return tmsg.showinfo("Rock ", "Oops! You lose :(")

def reset_options():
	comp = random.choice(a)
	print(comp)


Rock = Button(root,image=hand ,height  = "250", width = "230" , command = rock_button).grid()
Paper = Button(root,image=paper ,height  = "250", width = "230" , command = paper_button).grid(row = 0 ,column = 1)
Scissor = Button(root,image=rock_image ,height  = "250", width = "230" , command = scissor_button).grid(row = 0 ,column = 2)




root.mainloop()