import pygame
import time
import random
 
pygame.init()
 
display_width = 800 # 창크기 가로
display_height = 600 # 창크기 세로

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,191,255)
bright_red = (255,0,0)
bright_green = (0,160,200)
block_color = (0,0,0) # 색 선언
CHAN_W = 73 # 찬혁 크기

gameDisplay = pygame.display.set_mode((display_width,display_height)) # 창 설정
crash_sound = pygame.mixer.Sound("crash.wav") # crash 사운드 선언
pygame.display.set_caption("Attention! Kiyeok's Trash") # 캡션 글귀선언
CHAN = pygame.image.load('chanhyeok.png')
gameIcon = pygame.image.load('Icon.png')
CHANROOM = pygame.image.load('chanhyeok_room.png').convert()
clock = pygame.time.Clock()
pygame.display.set_icon(gameIcon)

pause = False
 
def things_dodged(count): # 부딪힌 횟수 함수
    font = pygame.font.SysFont("comicsansms", 25)
    text = font.render("                    Kihyeok's Trash   ->   "+str(count), True, black)
    gameDisplay.blit(text,(0,0))
 
def things(thingx, thingy, thingw, thingh, color): # 기혁이 쓰레기 생성 함수
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
 
def chan_object(x,y): # 찬혁 오브젝트 (얼굴)
    gameDisplay.blit(CHAN,(x,y))
 
def text_objects(text, font): # 텍스트 오브젝트 블럭내부
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
 
 
def crash(): # 충돌시 사용 함수
    pygame.mixer.Sound.play(crash_sound)
    pygame.mixer.music.stop()
    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("You eat Trash", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    

    while True: # quit 버튼 종료
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        

        button("Play Again",150,450,100,50,green,bright_green,game_loop) # 재실행 버튼 생성
        button("Quit",550,450,100,50,red,bright_red,quitgame) # 종료 버튼 생성

        pygame.display.update()
        clock.tick(15) 

def button(msg,x,y,w,h,ic,ac,action=None): # 버튼 생성 함수
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y: # 버튼 입력 확인
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None: # 버튼 입력 체크
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
    

def quitgame(): # 종료함수 (다른 함수 매개변수 용 함수)
    pygame.quit()
    quit()

def unpause(): # 일시정지 해제
    global pause
    pygame.mixer.music.unpause()
    pause = False
    

def paused(): # 일시정지 시
    pygame.mixer.music.pause()
    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    

    while pause: # 일시정지시 그만두기
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        button("Continue",150,450,100,50,green,bright_green,unpause)
        button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)   


def game_intro(): # 게임 시작전 화면

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white) # 게임 화면 설정들
        largeText = pygame.font.SysFont("comicsansms",45)
        TextSurf, TextRect = text_objects("Attention! Kiyeok's Trash!!!", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!",150,450,100,50,green,bright_green,game_loop)
        button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)
        
        
    
    

    
def game_loop(): # 본게임 루프
    global pause
    pygame.mixer.music.load('back.wav') # bgm
    pygame.mixer.music.play(-1)
    x = (display_width * 0.45)
    y = (display_height * 0.8)
 
    x_change = 0
 
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 4
    thing_width = 100
    thing_height = 100
 
    thingCount = 1
 
    dodged = 0
 
    gameExit = False
 
    while not gameExit:
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
 
            if event.type == pygame.KEYDOWN: # 키 입력 확인 방향키 누를때마다 5씩 x 증감 속도 높일시 이거 체크
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_p:
                    pause = True
                    paused()
                    
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
 
        x += x_change
        gameDisplay.blit(CHANROOM, [0,0])

        block_color = (random.randrange(0,256), random.randrange(0,256), random.randrange(0,256)) # 쓰레기 오브젝트 반짝거리게 하기위한 색
 
        things(thing_startx, thing_starty, thing_width, thing_height, block_color) # 텍스트 오브젝트 생성
 
 
        
        thing_starty += thing_speed
        chan_object(x,y)
        things_dodged(dodged)
 
        if x > display_width - CHAN_W or x < 0: # 맵 끝으로 가게 되면 사망
            crash()
 
        if thing_starty > display_height: # 피한다면 점점 난이도 증가
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            dodged += 1
            thing_speed += 1
            thing_width += (dodged * 1.12)
 
        if y < thing_starty+thing_height:
 
            if x > thing_startx and x < thing_startx + thing_width or x+CHAN_W > thing_startx and x + CHAN_W < thing_startx+thing_width:  # 충돌 체크
                crash()
        
        pygame.display.update() # 화면 업데이트
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()
