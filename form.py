from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from random import *

users = [
    {"name": "John Cena", "phone": "070218869", "image": "./images/IMG_7848.png"},
    {"name": "Cena Cena", "phone": "040218862", "image": "./images/org_photo_6553837_1576459572000_edit.png"},
    {"name": "Kevin Cena", "phone": "010218369", "image": "./images/org_photo_6553807_1576457194000_blue.png"},
    {"name": "John Kevin", "phone": "080213869", "image": "./images/org_photo_6553837_1576459572000_edit.png"},
    {"name": "Lavin Cena", "phone": "090215869", "image": "./images/IMG_7848.png"},
    {"name": "Keviny Cena", "phone": "070128869", "image": "./images/org_photo_6553807_1576457194000_blue.png"},
    {"name": "Kenny Cena", "phone": "05054318869", "image": "./images/org_photo_6553837_1576459572000_edit.png"},
    {"name": "John Kane", "phone": "010218869", "image": "./images/IMG_7848.png"},
    {"name": "John son", "phone": "030218869", "image": "./images/org_photo_6553807_1576457194000_blue.png"},
    {"name": "Vil Cena", "phone": "040218869", "image": "./images/org_photo_6553807_1576457194000_blue.png"}
]

winners = []

root = Tk()
run = False
root.title("Lottery Py")

variable = StringVar()
txt = StringVar(root, value='0 of 10')


def treeviewEmployeeUpdate():
    Remove = EmployView.get_children()
    for child in Remove:
        EmployView.delete(child)
    if len(winners) > 0:
        i = 0
        for winner in winners:
            i += 1
            EmployView.insert("", "end", text="", values=(i, winner['phone'], winner['name']))


def start():
    if len(winners) < 3:
        global run
        run = True
        while run:
            ind = randint(0, len(users) - 1)
            variable.set(users[ind]['phone'])
            root.update()
    else:
        messagebox.showinfo("No more winner", "The maximum number of winner is 3!")


def stop():
    global img
    global profile
    if len(winners) < 3:
        global run
        run = False
        index = 0
        for item in users:
            if item['phone'] == variable.get():
                winners.append(item)
                img = PhotoImage(file=item['image']).subsample(33, 19)
                profile = Label(root, image=img).grid(row=1, column=1, sticky=N, pady=70)
                del users[index]
                numOfText = str(len(winners)) + " of 10"
                txt.set(numOfText)
                root.update()
            index += 1
        treeviewEmployeeUpdate()
        pass


def again():
    global img
    global profile
    i = 0
    for winner in winners:
        users.append(winner)
    winners.clear()
    print(len(winners), len(users))
    Remove = EmployView.get_children()
    for child in Remove:
        EmployView.delete(child)

    img = PhotoImage().subsample(33, 19)
    profile = Label(root, image=img).grid(row=1, column=1, sticky=N, pady=70)


numOf = Label(root, textvariable=txt)
phoneWinner = Label(root, textvariable=variable)

numOf.grid(row=0, column=0, sticky=W, pady=10, padx=30)
phoneWinner.grid(row=0, column=0, sticky=S, pady=10)

tvFrame = Frame(root)
tvFrame.grid(row=1, column=0, sticky='news', padx=15)
EmployView = Treeview(tvFrame)
EmployView["columns"] = ("id", "phone", "name")
EmployView.grid(row=2, column=1, columnspan=3)
EmployView.heading("#0", text="ល.រ", anchor="w")
EmployView.column("#0", anchor="w", width=0, stretch=NO)
EmployView.heading("id", text="ល.រ", anchor="w")
EmployView.column("id", anchor="w", width=40, stretch=NO)
EmployView.heading("phone", text="Phones", anchor="w")
EmployView.column("phone", anchor="w", width=120)
EmployView.heading("name", text="Names", anchor="w")
EmployView.column("name", anchor="w", width=150)

btnStart = Button(root, text='Start', width=25, command=start)
btnStop = Button(root, text='Stop', width=25, command=stop)
btnAgain = Button(root, text='Again', width=25, command=again)

btnStart.grid(row=0, column=1, padx=15)
btnStop.grid(row=1, column=1, sticky=N)
btnAgain.grid(row=1, column=1, sticky=N, pady=32)

# img = PhotoImage(file="./images/IMG_7848.png").subsample(33, 19)
#
# profile = Label(root, image=img).grid(row=1, column=1, sticky=N, pady=70)

# windowWidth = root.winfo_reqwidth()
# windowHeight = root.winfo_reqheight()
#
# positionRight = int(root.winfo_screenwidth() / 2 - windowWidth / 2)
# positionDown = int(root.winfo_screenheight() / 2 - windowHeight / 2)

# root.geometry("+{}+{}".format(positionRight, positionDown))

root.geometry("535x280")
treeviewEmployeeUpdate()
root.mainloop()
