import pygame, random

# display setup
pygame.init()
GAME_WIDTH, GAME_HEIGHT = 394, 700
win = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption("Zero21")

# button variables


# fonts
NUMBER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 40)

# load images
RED_CARD_IMAGE = pygame.image.load('Assets/RedCard.png')
BLUE_CARD_IMAGE = pygame.image.load('Assets/BlueCard.png')
GREEN_CARD_IMAGE = pygame.image.load('Assets/GreenCard.png')
bg = pygame.image.load('Assets/background.jpeg')
play_button = pygame.image.load('Assets/PlayButton.png')

# game variables
score = +10
in_game = False

# colors
WHITE = (205,219,245)
BLACK = (0,0,0)

# setup game loop
FPS = 60
clock = pygame.time.Clock()
run = True


class RedCard(object):
    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        self.num = num
    
    def draw(self, win):
        win.blit(RED_CARD_IMAGE, (self.x, self.y))

class BlueCard(object):
    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        self.num = num
    
    def draw(self, win):
        win.blit(BLUE_CARD_IMAGE, (self.x, self.y))


# draw function
def redraw():
    win.blit(bg, (0,0))
    #win.fill(WHITE)
    if not in_game:
        win.blit(play_button, (70,300))
    else:
        for card in red_cards:
            card.draw(win)
        
        for card in blue_cards:
            card.draw(win)
        
        if len(red_cards) != 0:
            red_num = NUMBER_FONT.render(str(red_cards[-1].num), 1, WHITE)
            win.blit(red_num, (red_cards[-1].x + 12, red_cards[-1].y + 12))
        if len(blue_cards) != 0:
            blue_num = NUMBER_FONT.render(str(blue_cards[-1].num), 1, WHITE)
            win.blit(blue_num, (blue_cards[-1].x + 12, blue_cards[-1].y + 12))

        win.blit(GREEN_CARD_IMAGE, (GAME_WIDTH/2, 500))
        text = NUMBER_FONT.render(str(score), 1, WHITE)
        win.blit(text, (GAME_WIDTH/2 + 5, 520))
    
    pygame.display.update()

def display_message(message):
    pygame.time.delay(500)
    win.blit(bg, (0,0))
    text = WORD_FONT.render(message, 1, BLACK)
    win.blit(text, (30, 300))
    pygame.display.update()
    pygame.time.delay(3000)


red_cards = []
r_x, r_y = 100,300
for i in range(7):
    card = RedCard(r_x, r_y, random.randint(-8,10))
    red_cards.append(card)
    r_x += 10
    r_y += 10

blue_cards = []
b_x, b_y = 300,300
for i in range(7):
    card = BlueCard(b_x, b_y, random.randint(-8,10))
    blue_cards.append(card)
    b_x -= 10
    b_y += 10

while run:
    clock.tick(FPS)
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            #m_x, m_y = pygame.mouse.get_pos()
            m_x, m_y = event.pos
            print(f"{m_x} , {m_y}")
            if not in_game:
                if (70 <= m_x <= 300) and (300 <= m_y <= 440):
                    print("ASd")
                    in_game = True
            if in_game:
                if len(red_cards) != 0:
                    if m_x > red_cards[-1].x and m_x < red_cards[-1].x + 40 and m_y > red_cards[-1].y and m_y < red_cards[-1].y + 60:
                        score += red_cards[-1].num
                        red_cards.pop()
                if len(blue_cards) != 0:
                    if m_x > blue_cards[-1].x and m_x < blue_cards[-1].x + 40 and m_y > blue_cards[-1].y and m_y < blue_cards[-1].y + 60:
                        score += blue_cards[-1].num
                        blue_cards.pop()
            

    redraw()
    
    
    if score > 21 or score < 0:
        pygame.time.delay(500)
        display_message("Sorry, you lost!")
        break

    if len(red_cards) == 0 and len(blue_cards) == 0:
        display_message("Yipee!! You WON!")
        break
                

pygame.quit()