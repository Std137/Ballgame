import tkinter as tk        #подключаем библиотеку управления окнами и виджетами.
from tkinter import ttk as ttk  #подключаем библиотеку управления диологовых окон.
import random                   #подключаем библиотеку random.

col = ['red','green','blue','grey']

'''
--------------------------------------------------------------------------------------------------------------------------
class Briks - предназначен для хранения параметров отдельных кирпичей. Используется в классе Wall.
Конструктор Briks() - вызов без аргументов
Функция GetColor() - аргументов нет. Возвращает цвет текущего кирпича.
Функция BriksStatus() - аргументов нет. Возвращает статус текущего кирпича, 0 - нет, 1 - есть.
Функция BriksOff() - аргументов нет. Изменяет статус сбитого кирпича на 0. Необходима для обозначения уже сбитого кирпича 
--------------------------------------------------------------------------------------------------------------------------
'''

class Briks:
	def __init__(self):
		self.color = (random.sample(col, 1)[0])
		self.status = random.randint(0, 1)
		
	def GetColor(self):
		return self.color

	def BriksStatus(self):
		return self.status

	def BriksOff(self):
		self.status = 0

'''
---------------------------------------------------------------------------------------------------------
class Wall - класс, отвечающий за кирпичную стену. 
Конструктор Wall() - вызов без аргументов.
Функция wall_touch() - аргументы: столбец, строка. Отвечает за действия при соприкосновении мяча и стены 
Функция refresh() - вызов без аргументов. 
---------------------------------------------------------------------------------------------------------
'''
class Wall:
	def __init__(self, canv):
		cent_x = canv.winfo_screenwidth()//2
		for strok in range(7):
			for stolb in range(10):
				self.brick = Briks()
				if self.brick.BriksStatus() == 1:
					canv.create_rectangle(stolb*64, strok*20, stolb*64 + 64, strok*20 + 20, fill= self.brick.GetColor(), tag = ('M'+str(strok)+str(stolb)))
				del self.brick
		canv.create_rectangle(0,0,1,480,fill= 'black', tag = 'A')
		canv.create_rectangle(0,0,640,1,fill= 'black', tag = 'B')
		canv.create_rectangle(639,0,640,480,fill= 'black', tag = 'C')
		canv.create_rectangle(0,468,640,469,fill= 'black', tag = 'D')
		canv.create_rectangle(cent_x-50, 465, cent_x+50, 475, fill= 'red', tag = 'E')



	


class Board:
	def __init__(self,canvas):
		self.canvas = canvas
		self.bd_x = 270
		self.bd_y = 465
		self.bd_w = 100
		self.bd_h = 10
		self.color = 'red'

	def ref_boar(self):
		self.bd_x = self.canvas.winfo_pointerx() - self.canvas.winfo_rootx()- 50
		if self.bd_x < 0:
			self.bd_x = 0
		elif self.bd_x > 540:
			self.bd_x = 540



	def bd_touch(self, pos):
		if (pos[1] > (self.bd_y - 20)):
			if (pos[0] > self.bd_x) and (pos[0] < (self.bd_x+self.bd_w)):
				pos[1] = self.bd_y - 20 
				pos[3] = pos[3] * (-1)
		return pos



'''
--------------------------------------------------------------------------------------------------
class Ball - класс, отвечающий за создание мяча и сохранение его координат.
Конструктор Ball() - аргументы: холст. 
Функция new_pos() - вызов без аргументов. Считывает координаты мяча и возвращает новое положение
--------------------------------------------------------------------------------------------------
'''

class Ball:
	def __init__(self, canvas):
		self.canvas = canvas
		self.x = 310
		self.y = 445
		self.r = 20
		self.dx = -1
		self.dy = -1
		self.color = 'green'
		self.canvas.create_oval(self.x, self.y, self.x + self.r, self.y + self.r , fill= self.color, outline="white", tag = 'F')


	def new_pos(self):
		self.s = self.canvas.coords('F')
		self.x = self.s[0] + self.dx
		self.y = self.s[1] + self.dy

	def get_pos(self):
		return [self.x, self.y, self.dx, self.dy]

	def set_coords(self, new_stp):
		self.dx = new_stp[2]
		self.dy = new_stp[3]


'''
------------------------------------------------------------------------------------------------------------
class Border_Touch - класс, отвечащий за происходящие пи соприкосновении мяча, правого и левого краев поля. Используется в классе Move_Ball. 
Конструктор Border_Touch() - вызов без аргументов. 
Функция border_touch() - вызов без аргументов. Прорабатывает смену направления мяча при касании стены.
------------------------------------------------------------------------------------------------------------
'''

class Border_Touch:
	def __init__(self):
		self.border_x = 620
		self.border_y = 480

	def border_touch(self, coords):
		self.coords = coords
		return self.coords

'''
--------------------------------------------------------------------------------------------------
class Move_Ball - класс, отвечающий за перемещение мяча по полю.
Конструктор Move_Ball - аргументы: окно, холст, мяч, касание стены. 
Функция render() - аргументы: дельта х, дельта у. Двигает мяч по заданным координатам.
Функция test() - вызов без аргументов. Проверяет движение мяча.
--------------------------------------------------------------------------------------------------
'''

class Move_Ball:
	fps = 2
	t_dx = {'A':-1, 'B':1,'C':-1, 'E': 1, 'F':1, 'M':1}
	t_dy = {'A':1, 'B':-1,'C':1, 'E': -1, 'F':1, 'M':1}
	t_dm = {'01': 'A', '10':'B', '21':'A', '12':'B', '20':'A','00':'A', '02':'A','22':'A'}

	def __init__(self, window, canva, ball, bdr_touch, boards, wall):
		self.canvas = canva
		self.win = window
		#self.wall = wall
		#self.rect = rect
		#self.board = board
		#self.bottom_level = bottom_level
		self.ball = ball
		self.bdr_touch = bdr_touch
		self.boards = boards
		self.wall = wall


	def render(self, dx, dy):
		self.canvas.move('F', dx, dy)
		self.canvas.moveto('E', self.boards.bd_x, self.boards.bd_y)

	
	def touch(self):
			id_obj = self.canvas.find_overlapping(self.ball.x, self.ball.y, self.ball.x + self.ball.r, self.ball.y + self.ball.r)
			for i in id_obj:
				print(self.canvas.gettags(i))
			if len(id_obj) < 2:
				return 0
			idtoname = self.canvas.gettags(id_obj[1])[0]
			name_obj = idtoname[0]
			if (name_obj == 'D') or (name_obj == 'N'):
				return 0
			if name_obj == 'M':
				m_x = str(int(idtoname[2]) - int(((self.ball.x)//64)) + 1)
				m_y = str(int(idtoname[1]) - int(((self.ball.y)//20)) + 1)
				print(int(((self.ball.x+2)//64)))
				print(int(((self.ball.y+2)//20)))
				print(m_x)
				print(m_y)
				print(idtoname)
				self.canvas.delete(idtoname)
				name_obj = self.t_dm[((m_x)+(m_y))]
			self.ball.dx = self.ball.dx * self.t_dx[name_obj]
			self.ball.dy = self.ball.dy * self.t_dy[name_obj]
	

	def test(self):
		self.boards.ref_boar()
		self.ball.new_pos()
		self.touch()
		self.coords = self.ball.get_pos()
		#self.coords = self.boards.bd_touch(self.coords)
		self.coords = self.bdr_touch.border_touch(self.coords)
		#if (self.wall.wall_touch()) or (self.rect.rect_touch()) or (self.board.board_touch()):
		#	self.new_path()
		#if (self.bottom_level.bottom_touch()):
		#	self.game_over()
		self.render(self.coords[2],self.coords[3])
		self.ball.set_coords(self.coords)
		self.canvas.after(self.fps, self.test)

'''
--------------------------------------------------------------------------------------------------
class Start_Game - класс, отвечающий за создание окна игры. Исполльзуется в классе Start_win.
Конструктор Start_Game - вызов без аргументов.
--------------------------------------------------------------------------------------------------
'''

class Start_Game(tk.Toplevel):
	def __init__(self, parent):
		super().__init__(parent)
		self.title("Мочи кирпчи")
		self.geometry('640x480+{}+{}'.format(((self.winfo_screenwidth()//2)-320), ((self.winfo_screenheight()//2)-240)))
		self.resizable(0,0)
		self.holsts = tk.Canvas(self, width=640, height=480, bg='black', highlightcolor = 'red')
		self.holsts.pack()
		self.ball = Ball(self.holsts)
		self.boards = Board(self.holsts)
		self.bdr_touch = Border_Touch()
		self.wall = Wall(self.holsts)
		self.movie_ball = Move_Ball(self, self.holsts, self.ball, self.bdr_touch, self.boards,self.wall)
		self.movie_ball.test()

'''
--------------------------------------------------------------------------------------------------
class Score_win - класс, отвечающий за создание окна рекордов. Используется в классе Start_win().
Конструктор Score_win() - вызов без аргументов.
--------------------------------------------------------------------------------------------------
'''

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

'''
-----------------------------------------------------------------------------------------------------------------------
class Start_win - класс, отвечающий за создание меню игры.
Конструктор Start_win() - вызов без аргументов. 
Функция clck_btn_start() - вызов без аргументов. Запускает функцию Start_Game(), отвечающую за создание игрового окна.
Функция clck_btn_score() - вызов без аргументов. Запускает функцию Score_win(), отвечающую за создание окна рекордов. 
-----------------------------------------------------------------------------------------------------------------------
'''

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

'''
--------------------------------------------------------------------------------------------------
class Game_win - класс, 
Конструктор Game_win() - 
--------------------------------------------------------------------------------------------------
'''

class Game_win:
	def __init__(self):
		pass

game = Start_win()
game.mainloop()
