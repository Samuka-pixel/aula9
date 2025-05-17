from tkinter import *
file = open('teste.txt', "w")
agn = Tk()
Label(agn, text='First Name').grid(row=0)
Label(agn, text='Last Name').grid(row=1)
Label(agn, text='Phone Number').grid(row=2)
Label(agn, text='adress').grid(row=3)
Label(agn, text='email').grid(row=4)
e1 = Entry(agn)
def e1_input():
    firstname = e1.get()
    file.write(f'nome: {firstname}\n/')
e2 = Entry(agn)
def e2_input():
    lastname = e2.get()
    file.write(f'nome: {lastname}\n/')
e3 = Entry(agn)
def e3_input():
    pnumber = e3.get()
    file.write(f'nome: {pnumber}\n/')
e4 = Entry(agn)
def e4_input():
    adress = e4.get()
    file.write(f'nome: {adress}\n/')
e5 = Entry(agn)
def e5_input():
    email = e5.get()
    file.write(f'nome: {email}\n/')
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)
def wrapper():
    e1_input()
    e2_input()
    e3_input()
    e4_input()
    e5_input()
button = Button(agn, text="Submit", command=wrapper).grid(row=5)

agn.geometry("400x200")
agn.mainloop()