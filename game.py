import pygame

# display setup
pygame.init()
GAME_WIDTH, GAME_HEIGHT = 393, 700
win = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption("Zero21")

# button variables


# fonts


# load images
RED_CARD_IMAGE = pygame.image.load('Assets/RedCard.png')
BLUE_CARD_IMAGE = pygame.image.load('Assets/BlueCard.png')
bg = pygame.image.load('Assets/background.jpeg')

# game variables


# colors
WHITE = (205,219,245)

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
    for card in red_cards:
        card.draw(win)
    
    for card in blue_cards:
        card.draw(win)

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

