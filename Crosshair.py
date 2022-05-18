#Press Ctrl + q to bring up menu
import sys
import time
import keyboard
import pyautogui
from tkinter import *
from tkinter import ttk
from PyQt5 import QtCore, QtGui, QtWidgets

#Globals
CrossHair_Speed = 10
CrossHair_Tension = 4
CrossHair_Pos_X = 959
CrossHair_Pos_Y = 539
CrossHair_Static_Pos_X = 949
CrossHair_Static_Pos_Y = 479

def percentage(current_Pos, old_Pos):
    global CrossHair_Speed
    percentage = abs(current_Pos - old_Pos)
    if percentage == 0:
        percentage = percentage
    if percentage  > 1:
        percentage = percentage / CrossHair_Speed
    return percentage

def CrossHair_Delay(self):
    global CrossHair_Pos_X
    global CrossHair_Pos_Y
    global CrossHair_Tension
    global CrossHair_Static_Pos_X
    global CrossHair_Static_Pos_Y

    O_M_Pos_X, O_M_Pos_Y = pyautogui.position()
    time.sleep(0.01)
    Cur_M_Pos_X, Cur_M_Pos_Y = pyautogui.position()

    X_Percent = percentage(Cur_M_Pos_X, O_M_Pos_X)
    Y_Percent = percentage(Cur_M_Pos_Y, O_M_Pos_Y)

    if O_M_Pos_Y == Cur_M_Pos_Y:
        if CrossHair_Pos_Y > CrossHair_Static_Pos_Y: 
            self.move(CrossHair_Pos_X, CrossHair_Pos_Y)
            CrossHair_Pos_Y = CrossHair_Pos_Y - CrossHair_Tension

        if CrossHair_Pos_Y < CrossHair_Static_Pos_Y:
            self.move(CrossHair_Static_Pos_X, CrossHair_Pos_Y)
            CrossHair_Pos_Y = CrossHair_Pos_Y + CrossHair_Tension

    if O_M_Pos_X == Cur_M_Pos_X:
        if CrossHair_Pos_X > CrossHair_Static_Pos_X:
            self.move(CrossHair_Pos_X, CrossHair_Pos_Y)
            CrossHair_Pos_X = CrossHair_Pos_X -  CrossHair_Tension

        if CrossHair_Pos_X < CrossHair_Static_Pos_X:
            self.move(CrossHair_Pos_X, CrossHair_Pos_Y)
            CrossHair_Pos_X = CrossHair_Pos_X + CrossHair_Tension
    
    if Cur_M_Pos_X > O_M_Pos_X:
        self.move(CrossHair_Pos_X, CrossHair_Pos_Y)
        CrossHair_Pos_X = CrossHair_Pos_X - X_Percent

    if Cur_M_Pos_X < O_M_Pos_X:
        self.move(CrossHair_Pos_X, CrossHair_Pos_Y)
        CrossHair_Pos_X = CrossHair_Pos_X + X_Percent

    if Cur_M_Pos_Y > O_M_Pos_Y:
        self.move(CrossHair_Pos_X, CrossHair_Pos_Y)
        CrossHair_Pos_Y = CrossHair_Pos_Y - Y_Percent

    if Cur_M_Pos_Y < O_M_Pos_Y:
        self.move(CrossHair_Pos_X, CrossHair_Pos_Y)
        CrossHair_Pos_Y = CrossHair_Pos_Y + Y_Percent

class Crosshair(QtWidgets.QWidget):
    
    def __init__(self, parent = None, windowSize  = 24, penWidth = 2):
        QtWidgets.QWidget.__init__(self, parent)
        self.ws = windowSize
        self.resize(windowSize+100, windowSize+100)
        self.pen = QtGui.QPen(QtGui.QColor(255, 0, 255, 255))
        self.pen.setWidth(penWidth)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.WindowTransparentForInput)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.move(QtWidgets.QApplication.desktop().screen().rect().center() - self.rect().center() + QtCore.QPoint(1,1))
    def paintEvent(self, event):
        d = 3
        global CrossHair_Static_Pos_Y
        global CrossHair_Static_Pos_X
        ws = self.ws
        
        res = int(ws/2)
        red = int(ws/d)
        painter = QtGui.QPainter(self)
        painter.setPen(self.pen)
        painter.drawLine(res, 0, res, res - red)            #top line
        painter.drawLine(res, res + red+1, res, ws)        #bottom line
        painter.drawLine(0, res, res - red, res)
        painter.drawLine(res + red, res, ws - 0.5, res)
        self.update()
        time.sleep(0.01)
        CrossHair_Delay(self)
        if keyboard.is_pressed('ctrl+q'):
            Settings_Window()
        if keyboard.is_pressed('ctrl+left arrow'):
            CrossHair_Static_Pos_X = CrossHair_Static_Pos_X - 1
        if keyboard.is_pressed('ctrl+right arrow'):
            CrossHair_Static_Pos_X = CrossHair_Static_Pos_X + 1
        if keyboard.is_pressed('ctrl+up arrow'):
            CrossHair_Static_Pos_Y = CrossHair_Static_Pos_Y - 1
        if keyboard.is_pressed('ctrl+down arrow'):
            CrossHair_Static_Pos_Y = CrossHair_Static_Pos_Y + 1

def Settings_Window():
    global CrossHair_Speed
    root = Tk()
    root.title("Mouse Settings")
    root.geometry("250x250")

    tab_parent = ttk.Notebook(root)
    tab_Settings = ttk.Frame(tab_parent)
    tab_About = ttk.Frame(tab_parent)
    tab_parent.add(tab_Settings, text="Settings")
    tab_parent.add(tab_About, text="About")
    tab_parent.pack(expand=1, fill='both')

    def Set_Cross_Settings():
        global CrossHair_Speed
        global crosshaCrossHair_Tensionir_return
        CrossHair_Speed = int(crosshair_Speed_Settings.get())
        CrossHair_Tension = int(crosshair_Return_Speed.get())
        print(CrossHair_Speed)
                                                                #setting tab layout
    #mouse Tension
    LabelText = Label(tab_Settings, text="Mouse Tension:")
    LabelText.grid(row=0, column=0, padx=0, pady=0)
    crosshair_Speed_Settings = Scale(tab_Settings, from_=1, to=100, orient=HORIZONTAL)
    crosshair_Speed_Settings.grid(row=0, column=1)
    crosshair_Speed_Settings.set(CrossHair_Speed)

    #mouse return to offset 
    Label(tab_Settings, text='Mouse Return speed:').grid(row=1, column=0)
    crosshair_Return_Speed = Scale(tab_Settings, from_=1, to=100, orient=HORIZONTAL)
    crosshair_Return_Speed.grid(row=1, column=1)
    crosshair_Return_Speed.set(CrossHair_Tension)

    Button(tab_Settings, text='Apply', command=Set_Cross_Settings).grid(row=2, column=0)
                                                                #About tab layout
    Label(tab_About, text="Use Ctrl + arrow keys to adjust to position").grid(row=0, column=0)
    Label(tab_About, text="").grid(row=1, column=0)
    root.mainloop()

app = QtWidgets.QApplication(sys.argv)
widget = Crosshair(windowSize=16, penWidth=2)
widget.show()

sys.exit(app.exec_())
