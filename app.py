import pygame
import numpy as np

class TwoWayDict(dict):
    def __setitem__(self, key, value):
        # Remove any previous connections with these values
        if key in self:
            del self[key]
        if value in self:
            del self[value]
        dict.__setitem__(self, key, value)
        dict.__setitem__(self, value, key)

    def __delitem__(self, key):
        dict.__delitem__(self, self[key])
        dict.__delitem__(self, key)

    def __len__(self):
        """Returns the number of connections"""
        return dict.__len__(self) // 2

class LiftOperation():
    floors = None
    lifts = None
    liftPosVec = []
    blockVector = []

    def __init__(self, liftSim):
        # global floors
        # global lifts
        # global liftPosVec
        # global blockVector
        
        self.floors = liftSim.floors
        self.lifts = liftSim.lifts
        self.blockVector = []
        self.liftPosVec = []

        for lift in range(self.lifts):
            active_floor = np.random.randint(0, self.floors)
            self.blockVector.append(self.generate_block_vector(active_floor, self.floors))
            self.liftPosVec.append(active_floor)
        

    def get_nearest_lift(self, floor, *blockVector):
        lift_level = {blockVector.index(block)+1:abs(np.where(np.array(block) == 1)[0] - floor) for block in blockVector}
        return min(lift_level, key=lift_level.get)

    def generate_block_vector(self, floor, floors):
        block = np.zeros(floors)
        block[floor] = 1
        return(list(block))

class LiftSimulator:
    
    def __init__(self, floors, lifts):
        pygame.init()
        pygame.font.init()
        
        self.myfont = pygame.font.Font(None, 18)
        self.floors = floors
        self.lifts = lifts
        self.pos_dic = TwoWayDict()
        self.screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
        self.liftOperation = LiftOperation(self)

    def get_request_location(self):
        """performance can be optimized here"""
        fil = filter(self.is_pressed, [i if type(i) == tuple else (0, 0, 0, 0) for i in self.pos_dic.values()])
        if len(fil) == 0:
            pass
        else:
            print(self.pos_dic[fil[0]])
            return self.pos_dic[fil[0]]
        
    def get_brick_coordinates(self, pos):
        x, y = pos
        return(x, y, x+self.brick_w, y+self.brick_h)

    def is_pressed(self, coordinates):
        x, y = self.pos
        x1, y1, x2, y2 = coordinates
        if x in range(x1, x2+1) and y in range(y1, y2+1):
            return True

    def run(self):
        flag = True
        self.generate_structure()
        while flag:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    flag = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.pos = pygame.mouse.get_pos()
                    self.get_request_location()
                if event.type == pygame.VIDEORESIZE:
                    pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                    self.generate_structure()

    def lift(self):
        print("Lift position vector: " +str(self.liftOperation.liftPosVec))
        for pos in range(len(self.liftOperation.liftPosVec)):
            x1, y1, x2, y2 = self.pos_dic[str(pos)+","+str(self.liftOperation.liftPosVec[pos])]
            print(x1, y1)
            liftSurface = pygame.Surface((self.brick_w, self.brick_h))
            pygame.draw.rect(liftSurface, (0, 0, 255), pygame.Rect(0, 0, self.brick_w, self.brick_h))
            self.blocks[pos].blit(liftSurface, (0, 0))
            self.background.blit(self.blocks[pos], (x1, y1))

    
    def generate_structure(self):
        floor = []
        self.background = pygame.Surface(self.screen.get_size())
        self.background.fill((255, 255, 255))
        block = pygame.Surface((60, (self.floors*2)*16))
        block.fill((240, 240, 240))
        self.blocks = []
        self.brick_w = 40; self.brick_h = 15
        self.block_w = 60; self.block_h = 160

        for lift in range(self.lifts):
            block_x = 50; block_y = 100
            for floor in range(self.floors):
                rect_x = 10; rect_y = 15+floor*30
                brick_x = 30; brick_y = 17+floor*30
                floor_num = self.myfont.render(str(self.floors-(floor+1)), True, (0, 0, 0))
                pygame.draw.rect(block, (255, 0, 0), pygame.Rect(rect_x, rect_y, self.brick_w, self.brick_h))
                brick_pos_x = block_x+rect_x+self.brick_w*lift+35*lift
                brick_pos_y = block_y+rect_y
                self.pos_dic[str(lift)+','+str(self.floors-(floor+1))]=self.get_brick_coordinates((brick_pos_x, brick_pos_y))
                block.blit(floor_num, (brick_x, brick_y))
            self.blocks.append(block)
            block = block.convert()
            self.background.blit(block, (block_x+75*lift, block_y))

        self.lift()
        self.background = self.background.convert()
        self.screen.blit(self.background, (0,0))
        
        pygame.display.flip()
            

lift = LiftSimulator(floors=8, lifts=5).run()

