import pygame



pygame.init()



screen = pygame.display.set_mode((1200, 800))

pygame.display.set_caption("Game with States, Map, and Player")



clock = pygame.time.Clock()



running = True



# player variables

px = 50

py = 50

pw = 20

ph = 20

speed = 5



# colors

RED = (255, 0, 0)

BLACK = (0, 0, 0)



# tile images

tree = pygame.image.load('tree background.png')  # tree = 2

gravel = pygame.image.load('gravel.png')         # gravel = 3



# map layout

map_layout = [

    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],

    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],

    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],

    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],

    [2, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],

    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],

    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],

    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],

    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],

    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],

    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],

    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],

    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],

    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],

    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],

    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],

]



# collision detection

def is_colliding(x1, y1, w1, h1, x2, y2, w2, h2):

    return (

        x1 < x2 + w2 and x1 + w1 > x2 and

        y1 < y2 + h2 and y1 + h1 > y2

    )



# states

class MainState:

    def __init__(self):

        self.bg_color = (200, 200, 255)

        self.door_x = 550

        self.door_y = 180

        self.door_w = 30

        self.door_h = 30



    def update(self):

        global px, py, current_state

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:

            px -= speed

        if keys[pygame.K_RIGHT]:

            px += speed

        if keys[pygame.K_UP]:

            py -= speed

        if keys[pygame.K_DOWN]:

            py += speed



        if is_colliding(px, py, pw, ph, self.door_x, self.door_y, self.door_w, self.door_h):

            px = house_state.door_x + house_state.door_w + 5

            py = house_state.door_y

            current_state = house_state



    def draw(self):

        screen.fill(self.bg_color)



        for i in range(16):

            for j in range(24):

                tile = map_layout[i][j]

                if tile == 2:

                    screen.blit(tree, (j * 50, i * 50))

                elif tile == 3:

                    screen.blit(gravel, (j * 50, i * 50))



        pygame.draw.rect(screen, BLACK, (self.door_x, self.door_y, self.door_w, self.door_h))

        pygame.draw.rect(screen, RED, (px, py, pw, ph))



class HouseState:

    def __init__(self):

        self.bg_color = (200, 255, 200)

        self.door_x = 10

        self.door_y = 180

        self.door_w = 30

        self.door_h = 30



    def update(self):

        global px, py, current_state

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:

            px -= speed

        if keys[pygame.K_RIGHT]:

            px += speed

        if keys[pygame.K_UP]:

            py -= speed

        if keys[pygame.K_DOWN]:

            py += speed



        if is_colliding(px, py, pw, ph, self.door_x, self.door_y, self.door_w, self.door_h):

            px = main_state.door_x - pw - 5

            py = main_state.door_y

            current_state = main_state



    def draw(self):

        screen.fill(self.bg_color)

        

        # Draw the same map layout to maintain consistency

        for i in range(16):

            for j in range(24):

                tile = map_layout[i][j]

                if tile == 2:

                    screen.blit(tree, (j * 50, i * 50))

                elif tile == 3:

                    screen.blit(gravel, (j * 50, i * 50))



        pygame.draw.rect(screen, BLACK, (self.door_x, self.door_y, self.door_w, self.door_h))

        pygame.draw.rect(screen, RED, (px, py, pw, ph))



# set initial state

main_state = MainState()

house_state = HouseState()

current_state = main_state



# game loop

while running:

    clock.tick(60)



    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False



    current_state.update()

    current_state.draw()



    pygame.display.flip()



pygame.quit()
