import pygame

# display setup
pygame.init()
GAME_WIDTH, GAME_HEIGHT = 394, 700
win = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption("Zero21")

# button variables


# fonts
NUMBER_FONT = pygame.font.SysFont('comicsans', 40)

# load images
RED_CARD_IMAGE = pygame.image.load('Assets/RedCard.png')
BLUE_CARD_IMAGE = pygame.image.load('Assets/BlueCard.png')
GREEN_CARD_IMAGE = pygame.image.load('Assets/GreenCard.png')
bg = pygame.image.load('Assets/background.jpeg')

# game variables
score = -10

# colors
WHITE = (205,219,245)
BLACK = (0,0,0)

# setup game loop
FPS = 60
clock = pygame.time.Clock()
run = True


class RedCard(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self, win):
        win.blit(RED_CARD_IMAGE, (self.x, self.y))

class BlueCard(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self, win):
        win.blit(BLUE_CARD_IMAGE, (self.x, self.y))


# draw function
def redraw():
    win.blit(bg, (0,0))
    #win.fill(WHITE)
    for card in red_cards:
        card.draw(win)
    
    for card in blue_cards:
        card.draw(win)
    
    win.blit(GREEN_CARD_IMAGE, (GAME_WIDTH/2, 500))
    text = NUMBER_FONT.render(str(score), 1, WHITE)
    win.blit(text, (GAME_WIDTH/2 + 5, 520))
    
    pygame.display.update()

red_cards = []
r_x, r_y = 100,300
for i in range(7):
    card = RedCard(r_x, r_y)
    red_cards.append(card)
    r_x += 10
    r_y += 10

blue_cards = []
b_x, b_y = 300,300
for i in range(7):
    card = BlueCard(b_x, b_y)
    blue_cards.append(card)
    b_x -= 10
    b_y += 10

while run:
    clock.tick(FPS)
    redraw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            print(f"{m_x} , {m_y}")
            for red_card in red_cards:
                if m_x > red_card.x and m_x < red_card.x + 40 and m_y > red_card.y and m_y < red_card.y + 60:
                    print("FOUND")

