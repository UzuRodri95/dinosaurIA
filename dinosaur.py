import pygame
import neat
import time
import os
import random

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000

DINO_RUNNING_IMGS = [
            pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "dinoR1.png"))),
            pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "dinoR2.png")))
                    ]

DINO_RUNNING_GROUND_IMGS = [
            pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "dinoG1.png"))),
            pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "dinoG2.png")))
                            ]

DINO_JUMPING_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "dinoJ.png")))

CACTUS_IMGS = [
            pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "sCactus1.png"))),
            pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "sCactus2.png"))),
            pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "sCactus3.png"))),
            pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "lCactus1.png"))),
            pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "lCactus2.png"))),
            pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "lCactus3.png")))
                ]

GROUND_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "ground.png")))

CLOUD_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "cloud.png")))

BACKGROUND_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "background.png")))

class Dinosaur:
    RUNNING_IMGS = DINO_RUNNING_IMGS
    JUMPING_IMG = DINO_JUMPING_IMG
    RUNNING_GROUND_IMGS = DINO_RUNNING_GROUND_IMGS
    ANIMATION_TIME = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 0
        self.height = self.y
        self.img = self.RUNNING_IMGS[0]
        self.jumping = False
        self.tick_count = 0

    def jump(self):
        if jumping == False:
            self.vel = -10.5
            self.tick_count = 0
            self.height = self.y
            self.jumping = True

    def move(self):
        if self.jumping == True:
            #tick_count is used for gravity, each time date this function is executed
            #it is incremented so if the dino is jumping this will take effect as more
            #time in the air more quick it falls
            self.tick_count += 0.7
            d = self.vel * self.tick_count + 1.5 * self.tick_count**2

            if d >= 16:
                d = 16

            if d < 0:
                d -= 2

            self.y = self.y + d

            if abs(WINDOW_HEIGHT - slef.y) < 20:
                self.jumping = True

    def draw(self, win):
        if jumping == True:
            self.img = self.JUMPING_IMG
        else:
            if self.img_count < self.ANIMATION_TIME:
                self.img = self.RUNNING_IMGS[0]
            elif self.img_count < self.ANIMATION_TIME * 2:
                self.img = self.RUNNING_IMGS[1]
            elif self.img_count < self.ANIMATION_TIME * 3:
                self.img = self.RUNNING_IMGS[0]
            elif self.img_count < self.ANIMATION_TIME * 4:
                self.img = self.RUNNING_IMGS[1]
            elif self.img_count == self.ANIMATION_TIME * 4 + 1:
                self.img = self.RUNNING_IMGS[0]
                self.img_count = 0

        win.blit(self.img,(self.x, self.y))

    def get_mask(self):
        return pygame.mask.from_surface(self.img)


def main():
    print("Hello World")

if __name__ == '__main__':
    main()
