import tkinter as tk        #подключаем библиотеку управления окнами и виджетами.
from tkinter import ttk as ttk  #подключаем библиотеку управления диологовых окон.
import random                   #подключаем библиотеку random.

col = ['red','green','blue','grey']

'''
--------------------------------------------------------------------------------------------------
class Briks - предназначен для хранения параметров отдельных кирпичей. Используется в классе Wall.
Конструктор Briks() - вызов без аргументов
Функция GetColor() - аргументов нет. Возвращает цвет текущего кирпича.
Функция BriksStatus() - аргументов нет. Возвращает статус текущего кирпича, 0 - нет, 1 - есть.
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

'''
--------------------------------------------------------------------------------------------------
class Briks - предназначен для хранения параметров отдельных кирпичей. Используется в классе Wall
--------------------------------------------------------------------------------------------------
'''
class Wall:
	bricks_wall = {}
	def __init__(self):
		for strok in range(7):
			brick_stroka = {}
			for stolb in range(9):
				brick_stroka[stolb] = Briks()
			bricks_wall[strok] = brick_stroka

	def wall_touch(self, stolbec, stroka):
		pass

	def refresh(self):
		pass

class Ball:
	def __init__(self, canvas):
		self.canvas = canvas
		self.x = 320
		self.y = 200
		self.dx = -1
		self.dy = -1
		self.color = 'green'
		self.radius = 10
		self.canvas.create_oval(310, 460, 330, 480 , fill= self.color, outline="white", tag = 'ball')


	def get_move(self):
		return [self.x,self.y,self.dx,self.dy]

	def get_param(self):
		return [self.color, self.radius]

class Move_Ball:
	fps = 10
	def __init__(self, window, canvas, ball):
		self.canvas = canvas
		self.window = window
		#self.wall = wall
		#self.rect = rect
		#self.board = board
		#self.bottom_level = bottom_level
		self.ball = ball 

	def render(self):
		self.canvas.move('ball', -1, -1)
		

	def test(self):
		self.x, self.y, self.dx, self.dy = self.ball.get_move()
		self.new_x = self.x + self.dx
		self.new_y = self.y + self.dy
		#if (self.wall.wall_touch()) or (self.rect.rect_touch()) or (self.board.board_touch()):
		#	self.new_path()
		#if (self.bottom_level.bottom_touch()):
		#	self.game_over()
		self.render()
		self.canvas.after(self.fps, self.test)

class Start_Game(tk.Toplevel):
	def __init__(self, parent):
		super().__init__(parent)
		self.title("Мочи кирпчи")
		self.geometry('640x480+{}+{}'.format(((self.winfo_screenwidth()//2)-320), ((self.winfo_screenheight()//2)-240)))
		self.resizable(0,0)
		self.holsts = tk.Canvas(self, width=640, height=480, bg='black')
		self.holsts.pack()
		self.ball = Ball(self.holsts)
		self.movie_ball = Move_Ball(self, self.holsts, self.ball)
		self.movie_ball.test()


class Score_win(tk.Toplevel):
	def __init__(self, parent):
		super().__init__(parent)
		self.style = ttk.Style()
		self.style.configure('my.TButton', font=('Bauhaus 93', 24, 'bold'), borderwidth='10', borderradius='5')
		self.style.map('my.TButton', foreground=[('pressed', 'blue'), ('active', 'green')], background=[('pressed', '!disabled', 'black'), ('active', 'red')])
		self.style.configure('my.TLabel', font=('Bauhaus 93', 24, 'bold'), borderwidth='10', borderradius='5')
		self.style.map('my.TLabel')
		self.head_name = ttk.Label(self, style= 'my.TLabel', text='Arkanoid @2023').pack(ipady = 20)
		self.btn_quit = ttk.Button(self, style= 'my.TButton', text='Quit', command=lambda: self.destroy()).pack()


class Start_win(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title("Арканоид")
		self.geometry('320x240+{}+{}'.format(((self.winfo_screenwidth()//2)-160), ((self.winfo_screenheight()//2)-120)))
		self.resizable(0,0)
		self.style = ttk.Style()
		self.style.configure('my.TButton', font=('Bauhaus 93', 24, 'bold'), borderwidth='10', borderradius='5')
		self.style.map('my.TButton', foreground=[('pressed', 'blue'), ('active', 'green')], background=[('pressed', '!disabled', 'black'), ('active', 'red')])
		self.style.configure('my.TLabel', font=('Bauhaus 93', 24, 'bold'), borderwidth='10', borderradius='5')
		self.style.map('my.TLabel')
		self.head_name = ttk.Label(self, style= 'my.TLabel', text='Arkanoid @2023').pack(ipady = 20)
		self.btn_start = ttk.Button(self, style= 'my.TButton', text='StarT', command=self.clck_btn_start).pack()
		self.btn_score = ttk.Button(self, style= 'my.TButton', text='Score', command=self.clck_btn_score).pack()
		self.btn_quit = ttk.Button(self, style= 'my.TButton', text='Quit', command=lambda: self.destroy()).pack()
	
	def clck_btn_start(self):
		game_clk = Start_Game(self)
		game_clk.grab_set()
		
	def clck_btn_score(self):
		score_clk = Score_win(self)
		score_clk.grab_set()

class Game_win:
	def __init__(self):
		pass

game = Start_win()
game.mainloop()
