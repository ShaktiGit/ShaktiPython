import tkinter
import csv
from tkinter import *
from tkinter import messagebox
root=tkinter.Tk()
def onclose():
    if messagebox.askokcancel("Quit Window","Do You Want To Quit?"):
        root.destroy()
lbl1=Label(root,text="Enter Loc:")
lbl1.pack(side="left")
txt1=Entry(root)
txt1.pack()
def display():
    str1=txt1.get()
    file1 = open(str1)
    file1reader = csv.reader(file1)
    csvlist = list(file1reader)
    strcsv=str(csvlist)
    txtdispl.insert(INSERT,strcsv)

txtdispl=Text(root)
txtdispl.pack(side="right")
btnshow=Button(root,text="Press",command=display)
btnclose=Button(root,text="Close",command=onclose)
btnclose.pack()
btnshow.pack(side="bottom")

root.mainloop()
