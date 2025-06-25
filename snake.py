import pygame as py
import random
import os
py.mixer.init()

py.init()
#Background image

White=(255,255,255)
Red=(255,0,0)
Black=(0,0,0)
Green=(104,56,74)
screen_width=1000
screen_height=600
#Creating window
gameWindow=py.display.set_mode((1000,600))
bgimg=py.image.load("snake.mp3")
bgimg=py.transform.scale(bgimg, (screen_width,screen_height)).convert_alpha()
brimg=py.image.load("snake.mp1")
brimg=py.transform.scale(brimg, (screen_width,screen_height)).convert_alpha()
bcimg=py.image.load("snake.mp4")
bcimg=py.transform.scale(bcimg, (screen_width,screen_height)).convert_alpha()
py.display.update()
py.display.set_caption("Sumit First Snake Game")


clock=py.time.Clock()
#Creating a game loop
font=py.font.SysFont(None,55)
def text_screen(text,color,x,y):
      screen_text=font.render(text,True,color)
      gameWindow.blit(screen_text,[x,y])

def plot_snake(gameWindow,color,snk_list,snake_size):
            for x,y in snk_list:
                  py.draw.rect(gameWindow,color, (x,y,snake_size,snake_size))
#with open("highscore.txt",'r') as f:
            #highscore=f.read() 
def welcome():
      exit_game=False
      while not exit_game:
            gameWindow.fill(White)
            gameWindow.blit(bgimg, (0,0))
            text_screen("Welcome To Snake Game",Black,240,250)
            text_screen("press space button to start",Black,220,300)
            for event in py.event.get():
                  if event.type==py.QUIT:
                        exit_game=True
                  if event.type==py.KEYDOWN:
                        if event.key==py.K_SPACE:
                              py.mixer.music.load("puzzle.mp3")
                              py.mixer.music.play()
                              game_loop()
            py.display.update()
            clock.tick(60)
def game_loop():
      #Creating variables
      exit_game=False
      game_over=False
      snake_x=45
      snake_y=55
      snake_size=30
      fps=40
      velocity_x=2
      velocity_y=0
      init_velocity=5
      score=0
      food_x=random.randint(0,screen_width//2)
      food_y=random.randint(0,screen_height//2)
      snk_list=[]
      snk_lenght=1
      #bug free file
      if(not os.path.exists("highscore.txt")):
            with open ("highscore.txt","w") as f:
                  f.write("0")
      with open("highscore.txt","r") as f:
            highscore=f.read() 
      while not exit_game:
            if game_over:
                  with open("highscore.txt",'w') as f:
                        f.write(str(highscore)) 
                  gameWindow.fill(White)
                  gameWindow.blit(bcimg,(0,0))
                  text_screen("Game over! Press enter to continue", Red ,100,100)
                  for event in py.event.get():
                        if event.type==py.QUIT:
                              exit_game=True
                  
                        if event.type==py.KEYDOWN:
                              if event.key==py.K_RETURN:
                                    welcome()
            else:
                  for event in py.event.get():
                        if event.type==py.QUIT:
                              exit_game=True
                  
                        if event.type==py.KEYDOWN:
                              if event.key==py.K_RIGHT:
                                    velocity_x=init_velocity
                                    velocity_y=0
                              if event.key==py.K_LEFT:
                                    velocity_x=-init_velocity
                                    velocity_y=0
                              if event.key==py.K_UP:
                                    velocity_x=0
                                    velocity_y=-init_velocity
                              if event.key==py.K_DOWN:
                                    velocity_y=init_velocity
                                    velocity_x=0
                              if event.key==py.K_q:
                                    score+=10
                  snake_x+=velocity_x
                  snake_y+=velocity_y
                  if abs(snake_x-food_x)<26 and abs(snake_y-food_y)<26:
                        score+=10
                        print("score",score)
                        food_x=random.randint(0,screen_width//2)
                        food_y=random.randint(0,screen_height//2)
                        snk_lenght+=5
                        if score>int(highscore):
                              highscore=score
                  gameWindow.fill(Green)
                  gameWindow.blit(brimg ,(0,0))
                  text_screen("Score:"+str(score)+" Highscore: "+str(highscore),Red,5,5)
                  py.draw.rect(gameWindow,White, (food_x,food_y,snake_size,snake_size))
                  head=[]
                  head.append(snake_x)
                  head.append(snake_y)
                  snk_list.append(head)
                  if len(snk_list)>snk_lenght:
                        del snk_list[0]
                  if head in snk_list[:-1]:
                        game_over=True
                        py.mixer.music.load("gameover2.mp3")
                        py.mixer.music.play()
                  if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                        game_over=True
                        py.mixer.music.load("gameover2.mp3")
                        py.mixer.music.play()
                  #py.draw.rect(gameWindow,Black, (snake_x,snake_y,snake_size,snake_size))
                  plot_snake(gameWindow,Black,snk_list,snake_size)
            py.display.update()
            clock.tick(fps)
            
      py.quit()
      quit()
welcome()
