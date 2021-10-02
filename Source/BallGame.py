'''
BallGame Version 2.0
'''

from tkinter import *   #подключаем библиотеку управления окнами и виджетами
import random


def MoveBall():
    '''
    функция MoveBall - управление движением мяча 
    '''
    global stepX         #функция использует глобальную версию переменной.
    global stepY         #функция использует глобальную версию переменной.
    x0, y0, x1, y1 = holst.coords(ball) #получаем кординаты текущего положения мяча.
    if x0+stepX > 175:        #если следующий шаг выходит за границу окна справа.
        stepX = stepX*(-1)                  #меняем направление: движение влево.
    elif x0+stepX < 0 :        #если следующий шаг выходит за границу окна слева.
        stepX = stepX*(-1)                   #меняем направление: движение вправо.
    if y0+stepY > 175:        #если следующий шаг выходит за границу окна справа.
        stepY = stepY*(-1)                  #меняем направление: движение влево.
    elif y0+stepY < 0 :        #если следующий шаг выходит за границу окна слева.
        stepY = stepY*(-1)                   #меняем направление: движение вправо.
    holst.move(ball,stepX,stepY)    #рисуем мяч в новом положении.
    holst.after(20,MoveBall)       #вызвать функцию MoveBall движения через 10 милисекунд.

x_start=100             #создаём переменную и задаём текущее положение мяча по координате X.
y_start=100             #создаём переменную и задаём текущее положение мяча по координате Y.
stepX=0                 #создаём переменную и задаём шаг движения вправо.
stepY=0
fill_color = 'red'      # устанавливаем заливку круга красным.
out_color = 'white'     # устанавливаем заливку круга красным.

window = Tk()                                               #Создаем окно
window.title("Сбежавший мячик!!!")                          #Выводим название программы в окне
window.geometry("200x200+100+100")                          #задаем размер окна
holst = Canvas(window, width=200, height=200, bg='black')   #Задаем родительское окно, размер, и цвет холста
holst.pack()                                                #Рисуем холст в окне
stepX = 10-random.randint(0, 20)
stepY = 10-random.randint(0, 20)
ball = holst.create_oval(x_start, y_start, x_start+30, y_start+30, fill=fill_color, outline=out_color)
                                                            #Привязываем мяч к переменной
holst.after_idle(MoveBall)                                  #после настройки экрана запускаем движние мяча.
window.mainloop()                                           #запускаем бесконечный цикл до закрытия окна.