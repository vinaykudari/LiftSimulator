import pygame

class LiftSimulator:

    def __init__(self, floors, lifts):
        pygame.init()
        self.floors = floors
        self.lifts = lifts
        self.screen = pygame.display.set_mode((1000, 500))
    
    def run(self):
        flag = True
        self.generate_structure()
        while flag:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    flag = False
    
    def generate_structure(self):
        floor = []
        background = pygame.Surface(self.screen.get_size())
        background.fill((255, 255, 255))
        for no in range(self.lifts):
            block = pygame.Surface((60, (self.floors*2)*16))
            block.fill((240, 240, 240))
            w, h = block.get_size()
            for lift in range(self.lifts):
                for floor in range(self.floors):
                    pygame.draw.rect(block, (255, 0, 0), pygame.Rect(10, 15+floor*30, 40, 15))
                background.blit(block, (50+75*lift, 100))
        background = background.convert()
        self.screen.blit(background, (0,0))
        pygame.display.flip()
            

lift = LiftSimulator(floors=5, lifts=3).run()
