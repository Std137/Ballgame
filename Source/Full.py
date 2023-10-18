from tkinter import *           #подключаем библиотеку управления окнами и виджетами.
from tkinter import messagebox  #подключаем библиотеку управления диологовых окон.
import random                   #подключаем библиотеку random.

col = ['red','green','blue','grey']

'''
--------------------------------------------------------------------------------------------------
class Briks - предназначен для хранения параметров отдельных кирпичей. Используется в классе Wall
--------------------------------------------------------------------------------------------------
'''

class Briks:
	def __init__(self):
		self.color = (random.sample(self.col, 1)[0])
		self.status = random.randint(0, 1)
		
	def GetColor(self):
		return self.color

	def BriksStatus(self):
		return self.status

	def BriksOff(self):
		self.status = 0


class Field:
	holst = 0
	def __init__(self,canvas):
		self.holst = canvas
		self.GameField = []
		for i in range(13):
			for	we in range(7):
				self.GameField.append(Briks((49*i),20*we))			

	def ShowField(self):
		for j in self.GameField:
			if j.BriksStatus() == 1:
				self.holst.create_rectangle(j.BriksPositionX(), j.BriksPositionY(), j.BriksPositionX()+49, j.BriksPositionY()+20, fill=j.RetColor(), outline=out_color)



class Board:
	boardposx = 0
	boardposy = 0
	brush = 0
	board = 0
	def __init__(self,canvas):
		self.boardposx = 320
		self.boardposy = 440
		self.brush = canvas
		self.board = self.brush.create_rectangle(self.boardposx-50, self.boardposy, self.boardposx+50, self.boardposy+20, fill='green')

	def MoveBoard(self):
		self.brush.coords(self.board,self.boardposx-50, self.boardposy, self.boardposx+50, self.boardposy+20)
		
	def SetPosition(self,xpos,ypos):
		self.boardposx = xpos
		self.boardposy = ypos
	def GetPosition(self):
		return [self.boardposx, self.boardposy]

class GameInit:
	windows = 0
	holsts = 0
	def __init__(self):
		self.windows = Tk()
		self.windows.title("Сбежавший мячик!!!")                        #Выводим название программы в окне
		self.windows.geometry('640x480+{}+{}'.format(((self.windows.winfo_screenwidth()//2)-320), ((self.windows.winfo_screenheight()//2)-240)))
		self.windows.resizable(0,0)                                     #Запрет изменния рзмера окна
		self.holsts = Canvas(self.windows, width=640, height=480, bg='black')
	def getholst(self):
		return self.holsts
	def getwindow(self):
		return self.windows

class game GameMode:
	def __init__(self):
		gm = GameModel()
		gm.getwindow().mainloop()
	def Start():
	def Game():
	def GameOver():
x_start=320         #создаём переменную и задаём текущее положение мяча по координате X.
y_start=240         #создаём переменную и задаём текущее положение мяча по координате Y.
stepX=0             #создаём переменную и задаём шаг движения вправо.
stepY=0             #создаём переменную и задаём шаг движения вверх.
fill_color = 'green'  # устанавливаем заливку круга красным.
out_color = 'white' # устанавливаем заливку круга красным.
gm = GameModel()
Game = Field(gm.getholst())
Game.ShowField()
boards= Board(gm.getholst())
gm.getholst().pack()
                   
