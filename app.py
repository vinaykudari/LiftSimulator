import pygame

class Lift:
    def __init__(self, screen, floors, no_of_lifts):
        floor = []
        w, h = pygame.display.get_surface().get_size()
        for no in range(no_of_lifts):
            for floor in range(floors):
                pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(w/10+no*100, h/10+floor*50, 40, 15))
        pygame.display.flip()

        while True:
            event = pygame.event.wait()

            if event.type == pygame.QUIT:
                break

pygame.init()
screen = pygame.display.set_mode((1000, 500))
lift = Lift(screen, floors=4, no_of_lifts=3)
