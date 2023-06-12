import pygame #импортирует библиотеку pygame
import time #импортирует модуль времени
import random #импортит рандомайзер

pygame.init() #initialize запускать библиотеку pygame

dis_width=600
dis_height=400

dis=pygame.display.set_mode((dis_width, dis_height)) #формат экрана

blue=(0,0,225) #переменная с ГОЛУБЫМ цветом
green=(0,255,0)
red=(255,0,0)

snake_speed=15 #скорость
snake_block=10 #размер


font_style=pygame.font.SysFont("bahnschrift",25)

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, blue, [x[0], x[1], snake_block, snake_block])

clock=pygame.time.Clock() #модуль вреиени

pygame.display.set_caption("Snake game by KiberTeam") #название проги

def message(msg, color):
    mesg=font_style.render(msg, True, color)
    dis.blit(mesg,[dis_width/6,dis_height/3])

def gameLoop():
    game_over = False #игра заканчивается
    game_close = False #закрытие
    
    x1 = dis_width / 2  #400
    y1 = dis_height / 2 #300

    x1_change = 0
    y1_change = 0

    dlina_zmeyki = 1
    snake_List = []

    foodx=round(random.randrange(0,dis_width-snake_block)/10.0)*10.0
    foody=round(random.randrange(0,dis_height-snake_block)/10.0)*10.0   

    while not game_over: #запускает цикл

        while game_close  == True:
            dis.fill(red)
            message("Potracheno! Press N to quit, R to restart", blue)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_n:
                        game_over=True
                        game_close=False
                    if event.key==pygame.K_r:
                        gameLoop()

        for event in pygame.event.get(): #обращается к модулю event
                if event.type==pygame.QUIT: #если нажать quit-выходить
                    game_over=True #игра закрывается

                if event.type==pygame.KEYDOWN: #нажатие кнопки
                    if event.key==pygame.K_d or event.key==pygame.K_RIGHT:
                            x1_change=snake_block
                            y1_change=0
                    elif event.key==pygame.K_a or event.key==pygame.K_LEFT:
                            x1_change=-snake_block
                            y1_change=0
                    elif event.key==pygame.K_w or event.key==pygame.K_UP:
                            x1_change=0
                            y1_change=-snake_block
                    elif event.key==pygame.K_s or event.key==pygame.K_DOWN:
                            x1_change=0
                            y1_change=snake_block
        if x1>=dis_width or x1<0 or y1>=dis_height or y1<0:
            game_close=True           
        x1=x1+x1_change
        y1=y1+y1_change                           
        dis.fill(green) #поле fill=заливка                          
        pygame.draw.rect(dis,red,[foodx,foody,snake_block,snake_block])

        snake_Head = [] #голова
        snake_Head.append(x1) #append кладет элементы в объект
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        if len(snake_List) > dlina_zmeyki:
            del snake_List[0]

            for x in snake_List[:-1]:
                if x == snake_Head:
                    game_close = True

                    our_snake(snake_block, snake_List)

        pygame.display.update() #экран обновляется все время
        if foodx==x1 or foody==y1:
            print("O havcik")
            foodx=round(random.randrange(0,dis_width-snake_block)/10.0)*10.0
            foody=round(random.randrange(0,dis_height-snake_block)/10.0)*10.0
            dlina_zmeyki+=1

        clock.tick(snake_speed)


    pygame.quit() #выход
    quit() #выход
gameLoop()