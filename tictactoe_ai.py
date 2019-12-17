from tkinter import *
from tkinter import messagebox
import pyautogui



 


#just trust me
global k
k = 0

#creating the Tic Tac Toe page
window = Tk()
window.title("Tic-Tac-Toe AI")
window.geometry("192x150+600+300")
window.resizable(False, False)
turn = 1 #player's turn'


#creating the start menu
startMenu = Toplevel(window)
startMenu.title("figure it out")

startMenu.geometry("192x150+600+300")
window.withdraw() #this hides the app window 

label1 = Label(startMenu, text="Randomize who goes first: ")

label1.pack(padx=125, pady=50)
label2 = Label(startMenu, text=" ")
label2.pack(padx=175, pady=60)


#mouse = pymouse.PyMouse()
x,y = pyautogui.position()
print(x)
print(y)
#pyautogui.moveTo(700, 450, 2, pyautogui.easeInQuad) 

def openWindow():
    startMenu.destroy()
    window.deiconify() 
    btn9["text"] = "O"

def callback(event):

    print(event.x)
    print(event.y)
    if event.x > 0 and event.x < 10 and event.y > 40 and event.y < 50:
        openWindow()

canvas= Canvas(startMenu, width=200, height=100)
canvas.bind("<Button-1>", callback)
canvas.place(relx=1.0, rely=1.0, anchor=CENTER)



def randomStart():
    label2["text"] = "AI goes first."
    button10.pack_forget()
    button11 = Button(startMenu, text='Start', width=5, height=5,
                     command= openWindow)
    button11.pack(padx=30, pady=60)
    


button10 = Button(startMenu, text=' ', width=5, height=5,
                     command= randomStart)
button10.pack(padx=30, pady=60)



def buttonPress1(): 
    global turn 
    if btn1["text"] == " ":
        if turn == 1:
            btn1["text"] = "X"
            window.update_idletasks()
            cpuMove()
            window.update_idletasks()
        
        checkWin()
        if checkTie() == 1:
            ans = "It's a tie."
            messagebox.showinfo("Oops!", ans)
            window.destroy()
        
def buttonPress2(): 
    global turn 
    if btn2["text"] == " ":
        if turn == 1:
            btn2["text"] = "X"
            window.update_idletasks()
            cpuMove()
            window.update_idletasks()
        
        checkWin()
        if checkTie() == 1:
            ans = "It's a tie."
            messagebox.showinfo("Oops!", ans)
            window.destroy()

def buttonPress3(): 
    global turn 
    if btn3["text"] == " ":
        if turn == 1:
            btn3["text"] = "X"
            window.update_idletasks()
            cpuMove()
            window.update_idletasks()
            
        
        checkWin()
        if checkTie() == 1:
            ans = "It's a tie."
            messagebox.showinfo("Oops!", ans)
            window.destroy()

def buttonPress4(): 
    global turn 
    if btn4["text"] == " ":
        if turn == 1:
            btn4["text"] = "X"
            window.update_idletasks()
            cpuMove()
            window.update_idletasks()
        
        checkWin()
        if checkTie() == 1:
            ans = "It's a tie."
            messagebox.showinfo("Oops!", ans)
            window.destroy()

def buttonPress5(): 
    global turn 
    if btn5["text"] == " ":
        if turn == 1:
            btn5["text"] = "X"
            window.update_idletasks()
            cpuMove()
            window.update_idletasks()

        checkWin()
        if checkTie() == 1:
            ans = "It's a tie."
            messagebox.showinfo("Oops!", ans)
            window.destroy()

def buttonPress6(): 
    global turn 
    if btn6["text"] == " ":
        if turn == 1:
            btn6["text"] = "X"
            window.update_idletasks()
            cpuMove()
            window.update_idletasks()
            
        
    
        checkWin()
        if checkTie() == 1:
            ans = "It's a tie."
            messagebox.showinfo("Oops!", ans)
            window.destroy()

def buttonPress7(): 
    global turn 
    if btn7["text"] == " ":
        if turn == 1:
            btn7["text"] = "X"
            window.update_idletasks()
            cpuMove()
            window.update_idletasks()
        
        
        checkWin()
        if checkTie() == 1:
            ans = "It's a tie."
            messagebox.showinfo("Oops!", ans)
            window.destroy()

def buttonPress8(): 
    global turn 
    if btn8["text"] == " ":
        if turn == 1:
            btn8["text"] = "X"
            window.update_idletasks()
            cpuMove()
            window.update_idletasks()
        
        
        checkWin()
        if checkTie() == 1:
            ans = "It's a tie."
            messagebox.showinfo("Oops!", ans)
            window.destroy()

def buttonPress9(): 
    global turn 
    if btn9["text"] == " ":
        if turn == 1:
            btn9["text"] = "X"
            window.update_idletasks()
            cpuMove()
            window.update_idletasks()
        
       
        checkWin()
        if checkTie() == 1:
            ans = "It's a tie."
            messagebox.showinfo("Oops!", ans)
            window.destroy()


    
    
    





#Creating Tic Tac Toe Grid
btn1 = Button(window, text = " ", bg = "yellow", fg = "Black", width=5, height=2, font=('Helvetica', '20'), command = buttonPress1)
btn1.grid(column=1, row = 1)
btn1.pack 

btn2 = Button(window, text = " ", bg = "yellow", fg = "Black", width=5, height=2, font=('Helvetica', '20'), command = buttonPress2)
btn2.grid(column=2, row = 1)
btn2.pack

btn3 = Button(window, text = " ", bg = "yellow", fg = "Black", width=5, height=2, font=('Helvetica', '20'), command = buttonPress3)
btn3.grid(column=3, row = 1)
btn3.pack

btn4 = Button(window, text = " ", bg = "yellow", fg = "Black", width=5, height=2, font=('Helvetica', '20'), command = buttonPress4)
btn4.grid(column=1, row = 2)
btn4.pack


btn5 = Button(window, text = " ", bg = "yellow", fg = "Black", width=5, height=2, font=('Helvetica', '20'), command = buttonPress5)
btn5.grid(column=2, row = 2)
btn5.pack


btn6 = Button(window, text = " ", bg = "yellow", fg = "Black", width=5, height=2, font=('Helvetica', '20'), command = buttonPress6)
btn6.grid(column=3, row = 2)
btn6.pack

btn7 = Button(window, text = " ", bg = "yellow", fg = "Black", width=5, height=2, font=('Helvetica', '20'), command = buttonPress7)
btn7.grid(column=1, row = 3)
btn7.pack


btn8 = Button(window, text = " ", bg = "yellow", fg = "Black", width=5, height=2, font=('Helvetica', '20'), command = buttonPress8)
btn8.grid(column=2, row = 3)
btn8.pack


btn9 = Button(window, text = " ", bg = "yellow", fg = "Black", width=5, height=2, font=('Helvetica', '20'), command = buttonPress9)
btn9.grid(column=3, row = 3)
btn9.pack

print("hello")

def checkTie():
    b1 = btn1["text"]
    b2 = btn2["text"]
    b3 = btn3["text"]
    b4 = btn4["text"]
    b5 = btn5["text"]
    b6 = btn6["text"]
    b7 = btn7["text"]
    b8 = btn8["text"]
    b9 = btn9["text"]

    if b1 == " " or b2 == " " or b3 == " " or b4 == " " or b5 == " " or b6 == " " or b7 == " " or b8 == " " or b9 == " ":
        return 0
    else:
        return 1

#WIN CONDITIONS
def checkWin(): 
    b1 = btn1["text"]
    b2 = btn2["text"]
    b3 = btn3["text"]
    b4 = btn4["text"]
    b5 = btn5["text"]
    b6 = btn6["text"]
    b7 = btn7["text"]
    b8 = btn8["text"]
    b9 = btn9["text"]


    if b1 == b4 and b4 == b7 and (b1 == "X" or b1 == "O"): #first column going down
       win(b1)

    if b2 == b5 and b5 == b8 and (b2 == "X" or b2 == "O"): #second column going down
       win(b2)
    
    if b3 == b6 and b6 == b9 and (b3 == "X" or b3 == "O"): #third column going down
       win(b3)
    
    if b1 == b2 and b2 == b3 and (b3 == "X" or b3 == "O"): #first column left to right
       win(b3)

    if b4 == b5 and b5 == b6 and (b4 == "X" or b4 == "O"): #second column left to right
       win(b4)

    if b7 == b8 and b8 == b9 and (b7 == "X" or b7 == "O"): #third column left to right
       win(b7)
    
    


    if b1 == b5 and b5 == b9 and (b1 == "X" or b1 == "O"): #diagonal from top left to right
       win(b1)

    if b3 == b5 and b5 == b7 and (b3 == "X" or b3 == "O"): #diagonal from top right to left
       win(b3)

  #  elif btn2["text"] == "X" and btn4["text"] == "X" and btn7["text"] == "X": 
   #    win(btn1["text"])


def win(player):
    ans = "Game over! "  + player + " wins! "
    messagebox.showinfo("Congratulations", ans)
    window.destroy()


def cpuMove():
   

    #finishing moves
    if btn1["text"] == "O" and btn9["text"] == "O" and btn5["text"] == " ": 
        btn5["text"]= "O"
        return
    
    if btn1["text"] == "O" and btn7["text"] == "O" and btn4["text"] == " ": 
        btn4["text"]= "O"
        return


    if btn7["text"] == "O" and btn3["text"] == "O" and btn5["text"] == " ": 
        btn5["text"]= "O"
        return


    if btn7["text"] == "O" and btn9["text"] == "O" and btn8["text"] == " ": 
        btn8["text"]= "O"
        return

    
    if btn3["text"] == "O" and btn6["text"] == " " and btn9["text"] == "O": 
        btn6["text"]= "O"
        return

    if btn9["text"] == "O" and btn7["text"] == "O" and btn5["text"] == " ":
        if btn1["text"] == "X":
            btn3["text"] = "O"
            return
        elif btn4["text"] == "X":
            btn3["text"] = "O"
            return
        else:
            btn1["text"]= "O"
            return

    if btn6["text"] == "O" and btn9["text"]== "O" and btn3["text"] == " ":
        
        btn3["text"] = "O"
        return

    if btn1["text"] == "O" and btn3["text"]== "O" and btn2["text"] == " ":
        
        btn2["text"] = "O"
        return

     #-block


    if btn5["text"] == "X" and btn8["text"]== "X" and btn2["text"] == " ":

        
        btn2["text"] = "O"
        return


    if btn5["text"] == "X" and btn8["text"]== " " and btn2["text"] == "X":

        
        btn8["text"] = "O"
        return

    if btn5["text"] == "X" and btn6["text"]== "X" and btn4["text"] == " ":

        
        btn4["text"] = "O"
        return
    if btn5["text"] == "X" and btn8["text"]== " " and btn2["text"] == "X":

        
        btn8["text"] = "O"
        return

    if btn5["text"] == "X" and btn6["text"]== " " and btn4["text"] == "X":

        
        btn6["text"] = "O"
        return
    #cpu start bottom right cases
    
    if btn1["text"] == " " and btn2["text"] == " " and btn3["text"] == " " and btn4["text"]== " " and btn5["text"]== " " and btn6["text"] == "X" and btn7["text"] == " " and btn8["text"] == " " and btn9["text"] == "O":
        
        btn7["text"]= "O"
        return

    if btn1["text"] == " " and btn2["text"] == " " and btn3["text"] == " " and btn4["text"]== " " and btn5["text"]== " " and btn6["text"] == "X" and btn7["text"] == " " and btn8["text"] == " " and btn9["text"] == "O":
        btn7["text"]= "O"
        return 

    if btn1["text"] == " " and btn2["text"] == " " and btn3["text"] == " " and btn4["text"]== "X" and btn5["text"]== " " and btn6["text"] == " " and btn7["text"] == " " and btn8["text"] == " " and btn9["text"] == "O":
        btn7["text"]= "O"
        return 

    if btn1["text"] == " " and btn2["text"] == "X" and btn3["text"] == " " and btn4["text"]== " " and btn5["text"]== " " and btn6["text"] == " " and btn7["text"] == " " and btn8["text"] == " " and btn9["text"] == "O":
        btn7["text"]= "O"
        return 

    if btn1["text"] == " " and btn2["text"] == " " and btn3["text"] == "X" and btn4["text"]== " " and btn5["text"]== " " and btn6["text"] == " " and btn7["text"] == " " and btn8["text"] == " " and btn9["text"] == "O":
        btn7["text"]= "O"
        return 

    if btn1["text"] == " " and btn2["text"] == " " and btn3["text"] == " " and btn4["text"]== " " and btn5["text"]== " " and btn6["text"] == " " and btn7["text"] == " " and btn8["text"] == "X" and btn9["text"] == "O":
        btn7["text"]= "O"
        return 

    if btn1["text"] == "X" and btn2["text"] == " " and btn3["text"] == " " and btn4["text"]== " " and btn5["text"]== " " and btn6["text"] == " " and btn7["text"] == " " and btn8["text"] == " " and btn9["text"] == "O":
        btn7["text"]= "O"
        return 

    if btn5["text"]== " " and btn6["text"] == "X" and btn7["text"] == "O" and btn8["text"] == "X" and btn9["text"] == "O":
        btn1["text"]= "O"
        return
        

        #-cpu goes right -player goes middle
    if btn1["text"] == " " and btn2["text"] == " " and btn3["text"] == " " and btn4["text"]== " " and btn5["text"]== "X" and btn6["text"] == " " and btn7["text"] == " " and btn8["text"] == " " and btn9["text"] == "O":
        
        btn1["text"]= "O"
        return
    if btn1["text"] == "O" and btn5["text"]== "X" and btn9["text"] == "O" and btn7["text"] == "X":
        
        btn3["text"] = "O"
        return

    if btn1["text"] == "O" and btn5["text"]== "X" and btn9["text"] == "O" and btn3["text"] == "X":
        
        btn7["text"] = "O"
        return
    #-tie 
    if btn4["text"] == "X" and btn5["text"]== "X" and btn9["text"] == "O" and btn1["text"] == "O":
        
        btn6["text"] = "O"
        return

    if btn5["text"] == "X" and btn6["text"]== "X" and btn4["text"] == " ":

        
        btn4["text"] = "O"
        return

     #special cases
    if btn2["text"] == "O" and btn3["text"]== "X" and btn4["text"] == "X" and btn7["text"] == "O" and btn1["text"] == " ":

        
        btn1["text"] = "O"
        return

    if btn1["text"] == "X" and btn2["text"]== "O" and btn3["text"] == " " and btn4["text"] == "O" and btn7["text"] == "O":

        
        btn3["text"] = "O"
        return

    if btn1["text"] == "X" and btn2["text"]== "O" and btn5["text"] == "X" and btn8["text"] == "X" and btn7["text"] == "O" and btn9["text"] == "O":

        
        btn4["text"] = "O"
        return

    if btn1["text"] == "X" and btn2["text"]== "O" and btn3["text"] == "X" and btn4["text"] == "O" and btn5["text"] == "X" and btn7["text"] == "O" and btn8["text"] == "X" and btn9["text"] == "O":

        
        btn6["text"] = "O"
        return

    if btn1["text"] == " " and btn2["text"]== "O" and btn3["text"] == "X" and btn5["text"] == "X" and btn8["text"] == "X":

        
        btn1["text"] = "O"
        return
    

    

  

    


        

    

    



window.mainloop()