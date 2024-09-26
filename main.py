from tkinter import *

# Setting up Main Window
root = Tk()
root.geometry("400x300")
root.title("Main Window")

# Function to open New (Top Level) Window
def topwin():
    # Setting up Top Window
    top = Toplevel()
    top.geometry("180x100")
    top.title("TopLevel Window")
    
    # Adding a label widget to Top Window
    label_top = Label(top, text="This is a toplevel window")
    label_top.pack()

# Adding a label and button widget to Root (Main) Window
label_main = Label(root, text="This is the root window")
label_main.pack()

btn = Button(root, text="Click here to open another window", command=topwin)
btn.pack()

# Entering the main event loop
root.mainloop()
