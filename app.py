import pygame

class Lift:
    def __init__(self, screen, floors, no_of_lifts):
        floor = []
        w, h = pygame.display.get_surface().get_size()
        for i in range(floors):
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(w/2, h/10+i*50, 40, 15))
        pygame.display.flip()

        while True:
            event = pygame.event.wait()

            if event.type == pygame.QUIT:
                break

pygame.init()
screen = pygame.display.set_mode((1000, 500))
lift = Lift(screen, floors=8, no_of_lifts=6)
