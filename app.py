import pygame

class LiftSimulator:

    def __init__(self, floors, no_of_lifts):
        pygame.init()
        self.floors = floors
        self.no_of_lifts = no_of_lifts
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
        w, h = pygame.display.get_surface().get_size()
        for no in range(self.no_of_lifts):
            for floor in range(self.floors):
                pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(w/10+no*100, h/10+floor*50, 40, 15))
        pygame.display.flip()

lift = LiftSimulator(floors=5, no_of_lifts=3).run()
