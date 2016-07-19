#Name Picker
#import the modules we need, for creating a GUI...
import tkinter
#...and for picking random names.
import random

#the list of possible names.
names = ['name1','name2','name3','name4','name5','name6','name7','name8','name9','name10']

#a function that will pick (and display) a name.
def pickName():
    nameLabel.configure(text=random.choice(names))

#create a GUI window.
root = tkinter.Tk()
#set the title.
root.title("Name Picker")
#set the size.
root.geometry("200x100")

#add a label for displaying the name.
nameLabel = tkinter.Label(root, text="", font=('Helvetica', 32))
nameLabel.pack()

#add a 'pick name' button
pickButton = tkinter.Button(text="Pick!", command=pickName)
pickButton.pack()

#start the GUI
root.mainloop()
