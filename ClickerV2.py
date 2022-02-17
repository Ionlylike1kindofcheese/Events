import tkinter as tk
from functools import partial

window = tk.Tk()
window.title("Clicker V1")
window.config(bg='grey')

numberStatus = 0

def showNumberstatus():
    print('Het huidige nummer is:', str(numberStatus))


def update(commandAction):
    colourUpdate = False
    global numberStatus
    if commandAction == 'increase':
        print("increase comfirmed")
        numberStatus += 1
        colourUpdate = True
    elif commandAction == 'decrease':
        print("decrease comfirmed")
        numberStatus -= 1
        colourUpdate = True
    elif commandAction == 'joined':
        print("mouse entry detected")
        window.config(bg='yellow')
    elif commandAction == 'left':
        print("mouse left detected")
        colourUpdate = True

    if colourUpdate == True:
        if numberStatus > 0:
            window.config(bg='green')
        elif numberStatus < 0:
            window.config(bg='red')
        elif numberStatus == 0:
            window.config(bg='grey')
    
    list[1].config(text=numberStatus)


def enter(event):
    # print('Button-2 entered at x = % d, y = % d'%(event.x, event.y))
    update('joined')


def exit_(event):
    # print('Button-2 left at x = % d, y = % d'%(event.x, event.y))
    update('left')


list = []
textStrings = ["up", numberStatus, "down"]
for x in range(3):
    list.append(tk.Button(text=textStrings[x]))
    list[x].pack(ipadx=25, ipady=10)

list[0].config(command=partial(update, 'increase'))

list[1].config(command=showNumberstatus)
list[1].bind('<Enter>', enter)
list[1].bind('<Leave>', exit_)

list[2].config(command=partial(update, 'decrease'))

window.mainloop()