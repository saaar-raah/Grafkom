from tkinter import Tk, Canvas
from math import sin, cos, radians
from datetime import datetime

class Point:
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Point((self.x + other.x), ((self.y + other.y)))
    
    def __sub__(self, other):
        return Point((self.x - other.x), ((self.y - other.y)))

    def offsetByVector(self, angle, length):
        return Point((int(cos(angle) * length) + self.x), (int(sin(angle) * length + self.y)))

class ClockHands:  
    tKinter = Tk()
    longHand = "" 
    shortHand = "" 
    secondHand = ""
    cornerCircle1 = Point(10, 10)
    cornerCircle2 = Point(210, 210)
    

    def centerPoint(self):
        return Point(((self.cornerCircle1.x + self.cornerCircle2.x)/2), ((self.cornerCircle1.y + self.cornerCircle2.y)/2))        

    def updateClock(self, canvas):        
        rotate = lambda: self.updateClock(canvas)
    #   print(time)
        # mengulang selama 100 milisecond
        canvas.after(100, rotate)
    
    def run(self):
        self.tKinter.mainloop()

    def __init__(self):
        canvas = Canvas(self.tKinter, width=220, height=220)
        canvas.configure(bg="black")
        canvas.create_oval(self.cornerCircle1.x, self.cornerCircle1.y, self.cornerCircle2.x, self.cornerCircle2.y, fill = "black", width = 3)
        center = self.centerPoint()

        def createTickMark(angle, dFromCenter, length, mark):
            angle -= 90.0
            rads = radians(angle)
            p1 = center.offsetByVector(rads, dFromCenter)
            p2 = center.offsetByVector(rads, dFromCenter + length)
            mark(p1, p2)

        #BUAT GARIS PADA JAM
        sm_Tick = lambda p1, p2: canvas.create_line(p1.x, p1.y, p2.x, p2.y, fill = "white")
        lg_Tick = lambda p1, p2: canvas.create_line(p1.x, p1.y, p2.x, p2.y, fill = 'red', width=3)

        #GARIS PADA MENIT
        for angle in range(0, 360, 6):
            createTickMark(angle, 90, 9, sm_Tick)
        #GARIS PADA JAM
        for angle in range(0, 360, 30):
            createTickMark(angle, 80, 19, lg_Tick)

        canvas.pack()
        self.tKinter.wm_title("JAM ANALOG By Kelompok 01")
        #Prepare the code to be run in the main loop   
        self.updateClock(canvas)

if __name__ == "__main__":
    Hand = ClockHands()
    Hand.run()
