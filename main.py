import pygame, random, time
from mario import Mario
from coin import Coin

# set up pygame modules
pygame.init()
pygame.font.init()
pygame.mixer.init()
my_font = pygame.font.SysFont("Arial", 35)
pygame.display.set_caption("Coin Collector!")

# set up variables for the display
bg = pygame.image.load('images/background.png')
size = (bg.get_size()[0]/3,bg.get_size()[1]/3)
SCREEN_WIDTH = int(size[0])
SCREEN_HEIGHT= int(size[1])
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
bg = pygame.transform.scale(bg,size)


name = "Collect coins as fast as you can!"
message = "Collision not detected"
score_message = 'Score: 0'
score = 0
start_time = time.time()
time_limit = 20
time_message = str(time_limit)

# render the text for later
display_name = my_font.render(name, True, (255, 255, 255))
display_message = my_font.render(message, True, (255, 255, 255))
display_score = my_font.render(score_message, True, (255, 255, 255))
display_time = my_font.render(time_message, True, (255,255,255))


#sound stuff
win_sound = pygame.mixer.Sound('sound/Win.mp3')
lose_sound = pygame.mixer.Sound('sound/Lose.wav')
coin_sound = pygame.mixer.Sound('sound/coin.mp3')

end_sound = False


m = Mario(40, 120)
c = Coin(240, 160)

run = True
game_over = False



while run:
    c.movement(SCREEN_WIDTH, SCREEN_HEIGHT)

    keys = pygame.key.get_pressed()
    if not game_over:
        if keys[pygame.K_d]:
            m.move_direction('right')
        if keys[pygame.K_a]:
            m.move_direction('left')
        if keys[pygame.K_s]:
            m.move_direction('down')
        if keys[pygame.K_w]:
            m.move_direction('up')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if m.rect.colliderect(c.rect):
        pygame.mixer.Sound.play(coin_sound)
        new_pos = (random.randint(0, SCREEN_WIDTH - c.image_size[0]), random.randint(0, SCREEN_HEIGHT - c.image_size[1]))
        c.move(new_pos[0], new_pos[1])

        score += 10
        if score == 100:
            game_over = True
        score_message = 'Score: ' + str(score)

    current_time = time.time()-start_time
    time_remaining = time_limit - current_time

    if time_remaining<0:
        game_over = True

    display_score = my_font.render(score_message, True, (255, 255, 255))
    display_time = my_font.render(time_message, True, (255,255,255))
    screen.blit(bg,(0,0))
    screen.blit(m.image, m.rect)

    screen.blit(display_name, (5, 5))
    screen.blit(display_score, (5, 35))
    screen.blit(display_time,(5,65))


    if not game_over:
        screen.blit(c.image, c.rect)
        time_message = 'Time Remaining: ' + str(round(time_remaining, 2))
    else:
        if score == 100:
            display_message = my_font.render('You win!', True, (255, 255, 255))
            if not end_sound:
                pygame.mixer.Sound.play(win_sound)
                end_sound = True

        else:
            display_message = my_font.render('You lose!', True, (255,255,255))
            if not end_sound:
                pygame.mixer.Sound.play(lose_sound)
                end_sound = True
        screen.blit(display_message, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

    pygame.time.get_ticks()
    pygame.display.update()



