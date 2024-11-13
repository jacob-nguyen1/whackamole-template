import pygame
import random

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        mole_pos = [0,0]
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #print(pygame.mouse.get_pos())
                    if pygame.mouse.get_pos()[0] in range(mole_pos[0]*32,mole_pos[0]*32+32) and pygame.mouse.get_pos()[1] in range(mole_pos[1]*32,mole_pos[1]*32+32):
                        mole_pos[0] = random.randrange(0,20)
                        mole_pos[1] = random.randrange(0,16)
            screen.fill("light green")
            for i in range(32,641,32):
                pygame.draw.line(screen, (0, 0, 0), (i, 0), (i, 512), 1)
            for i in range(32,513,32):
                pygame.draw.line(screen, (0, 0, 0), (0, i), (640, i), 1)

            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_pos[0]*32+3,mole_pos[1]*32+3)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
