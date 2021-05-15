import pygame

pygame.init() #initialize game

win = pygame.display.set_mode((550,550)) # window and dimesions

pygame.display.set_caption('Tic-Tac-Toe')

x1 = pygame.draw.rect(win, (255, 255, 255) , (25,25,150,150))
x2 = pygame.draw.rect(win, (255, 255, 255) , (200,25,150,150))
x3 = pygame.draw.rect(win, (255, 255, 255) , (375,25,150,150))

y1 = pygame.draw.rect(win, (255, 255, 255) , (25,200,150,150))
y2 = pygame.draw.rect(win, (255, 255, 255) , (200,200,150,150))
y3 = pygame.draw.rect(win, (255, 255, 255) , (375,200,150,150))

z1 = pygame.draw.rect(win, (255, 255, 255) , (25,375,150,150))
z2 = pygame.draw.rect(win, (255, 255, 255) , (200,375,150,150))
z3 = pygame.draw.rect(win, (255, 255, 255) , (375,375,150,150))

run = True


draw_obj = 'rect'

x1_open = True

while run: #main loop

    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

            if x1.collidepoint(pos) and x1_open:
                if draw_obj == 'rect':
                    pygame.draw.rect(win, (255, 0, 0) , (50,50,100,100))
                    draw_obj = 'circle'
                else:
                    pygame.draw.circle(win, (0, 255, 0) , (100,100), 50)
                    draw_obj = 'rect'
                x1_open = False

            if x2.collidepoint(pos) and x2_open:
                if draw_obj == 'rect':
                    pygame.draw.rect(win, (255, 0, 0) , (225,50,100,100))
                    draw_obj = 'circle'
                else:
                    pygame.draw.circle(win, (0, 255, 0) , (275,100), 50)
                    draw_obj = 'rect'
                x2_open = False

            if x3.collidepoint(pos) and x3_open:
                if draw_obj == 'rect':
                    pygame.draw.rect(win, (255, 0, 0) , (400,50,100,100))
                    draw_obj = 'circle'
                else:
                    pygame.draw.circle(win, (0, 255, 0) , (450,100), 50)
                    draw_obj = 'rect'
                x3_open
            if y1.collidepoint(pos):
                if draw_obj == 'rect':
                    pygame.draw.rect(win, (255, 0, 0) , (50,225,100,100))
                    draw_obj = 'circle'
                else:
                    pygame.draw.circle(win, (0, 255, 0) , (100,275), 50)
                    draw_obj = 'rect'

            if y2.collidepoint(pos):
                if draw_obj == 'rect':
                    pygame.draw.rect(win, (255, 0, 0) , (225,225,100,100))
                    draw_obj = 'circle'
                else:
                    pygame.draw.circle(win, (0, 255, 0) , (275,275), 50)
                    draw_obj = 'rect'

            if y3.collidepoint(pos):
                if draw_obj == 'rect':
                    pygame.draw.rect(win, (255, 0, 0) , (400,225,100,100))
                    draw_obj = 'circle'
                else:
                    pygame.draw.circle(win, (0, 255, 0) , (450,275), 50)
                    draw_obj = 'rect'

            if z1.collidepoint(pos):
                if draw_obj == 'rect':
                    pygame.draw.rect(win, (255, 0, 0) , (50,400,100,100))
                    draw_obj = 'circle'
                else:
                    pygame.draw.circle(win, (0, 255, 0) , (100,450), 50)
                    draw_obj = 'rect'

            if z2.collidepoint(pos):
                if draw_obj == 'rect':
                    pygame.draw.rect(win, (255, 0, 0) , (225,400,100,100))
                    draw_obj = 'circle'
                else:
                    pygame.draw.circle(win, (0, 255, 0) , (275,450), 50)
                    draw_obj = 'rect'

            if z3.collidepoint(pos):
                if draw_obj == 'rect':
                    pygame.draw.rect(win, (255, 0, 0) , (400,400,100,100))
                    draw_obj = 'circle'
                else:
                    pygame.draw.circle(win, (0, 255, 0) , (450,450), 50)
                    draw_obj = 'rect'

    pygame.display.update()

pygame.quit()
