from tkinter import *

class View:

    topFrame = None
    bottomFrame = None

    def __init__(self, master):
        self.topFrame = Frame(master)
        self.bottomFrame = Frame(master)

        self.topFrame.pack()
        self.bottomFrame.pack()
        
        self.resetButton = Button(self.bottomFrame, text="Reset", command=self.resetSimulation)
        self.resetButton.pack(side=BOTTOM)
    
    def resetSimulation(self):
        pass

class Lift:

    def __init__(self, view):
        self.label = Label(view.topFrame, text="Hello")
        self.label.pack(side=LEFT)


root = Tk()
view = View(root)
l1 = Lift(view)
l2 = Lift(view)
l3 = Lift(view)
root.mainloop()