import pygame

def get_image(sheet,x,y,width,height):
    image = pygame.Surface((width,height), pygame.SRCALPHA)
    image.blit(sheet,(0,0),(x,y,width, height))
    return image



def main():
    pygame.init()
    screen = pygame.display.set_mode((640,480))
    big_image = pygame.image.load("C:\\game_lessons\\lesson_1\\map\\village\\Serene_Village_32x32.png")
    red_house = get_image(big_image,320,670,150,125)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    
        screen.fill((0,0,0))
        screen.blit(red_house,(0,0))
        screen.blit(red_house,(120,0))
        screen.blit(red_house,(240,0))
        screen.blit(red_house,(360,0))
        screen.blit(red_house,(480,0))
                    

        
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()

