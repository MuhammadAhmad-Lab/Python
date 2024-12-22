from tkinter import *

root=Tk()
root.geometry("400x800")
root.title("Top Window")

def topwindow():
    
    top = Toplevel()
    top.geometry("200x100")
    top.title("TopLevel")
    
    label=Label(top, text="This is the Top Window :)")
    label.pack()
    
    top.mainloop()
    
label2 = Label(root, text = "This is the Root Window")
Button = Button(root, text = "Click Here to Open a window", command = topwindow)

label2.pack()
Button.pack()

root.mainloop()