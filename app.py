import pygame

class LiftSimulator:
    
    def __init__(self, floors, lifts):
        pygame.init()
        pygame.font.init()
        self.myfont = pygame.font.Font(None, 18)
        self.floors = floors
        self.lifts = lifts
        self.pos_dic = {}
        self.screen = pygame.display.set_mode((1000, 500))

    def get_request_location(self, pos):
        x, y = pos
        
    
    def run(self):
        flag = True
        self.generate_structure()
        while flag:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    flag = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    print(pos)
    
    def generate_structure(self):
        floor = []
        background = pygame.Surface(self.screen.get_size())
        background.fill((255, 255, 255))
        block = pygame.Surface((60, (self.floors*2)*16))
        block.fill((240, 240, 240))
        brick_w = 40; brick_h = 15
        block_w = 60; block_h = 160
        for lift in range(self.lifts):
            block_x = 50; block_y = 100
            for floor in range(self.floors):
                rect_x = 10; rect_y = 15+floor*30
                brick_x = 30; brick_y = 17+floor*30
                floor_num = self.myfont.render(str(self.floors-(floor+1)), True, (0, 0, 0))
                pygame.draw.rect(block, (255, 0, 0), pygame.Rect(rect_x, rect_y, brick_w, brick_h))
                brick_pos_x = block_x+rect_x+brick_w*lift+35*lift
                brick_pos_y = block_y+rect_y
                self.pos_dic[str(lift)+str(floor)]=(brick_pos_x, brick_pos_y)
                block.blit(floor_num, (brick_x, brick_y))
            block = block.convert()
            background.blit(block, (block_x+75*lift, block_y))
        background = background.convert()
        self.screen.blit(background, (0,0))
        pygame.display.flip()
            

lift = LiftSimulator(floors=5, lifts=4).run()
