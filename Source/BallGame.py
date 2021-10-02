from tkinter import *
import time

def on_closing():
    global window
    window.destroy()  # Закрыть окно

def PaintBall(paint_command, x_coord, y_coord):
    '''
    Функция PaintBell - Рисование мяча на экране
    paint_command - 1- Нарисовать мяч, красным. 2 - Нарисовать мяч черным
    x_coord - Координата X
    y_coord - Координата Y
    '''
    if paint_command == 1:
        fill_color = 'red'
        out_color = 'white'
    else:
        fill_color = 'black'
        out_color = 'black'
    holst.create_oval(x_coord, y_coord, x_coord+30, y_coord+30, fill=fill_color, outline=out_color)#Рисуем мяч на холсте
    

def MoveBall():
    global x_start
    global y_start
    global step
    holst.after(2000,MoveBall)
    PaintBall(2,x_start,y_start)
    x_start=x_start+step
    if (x_start+step) > 170:
        step = -10
    elif (x_start+step) < 1:
        step = 10
    x_start=x_start+step
    PaintBall(1,x_start,y_start)

x_start=100
y_start=100
step=10
window = Tk() #Создаем окно
window.title("Сбежавший мячик!!!") #Выводим название программы в окне
window.geometry("200x200+100+100") #задаем размер окна
window.protocol("WM_DELETE_WINDOW", on_closing)
holst = Canvas(window, width=200, height=200, bg='black') #Задаем окно, размер, и цвет холста
holst.pack() #Рисуем холст в окне
PaintBall(1,x_start,y_start)
holst.after_idle(MoveBall)
window.mainloop()

