import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((30,30))     #Dimensiones de la imagen del jugador
        self.surf.fill((128,255,40))            #Color de relleno de la imagen del jugador
        self.rect= self.surf.get_rect(center=(10,420))

    
class platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((WIDTH, 20))
        self.surf.fill((255,0,0))
        self.rect = self.surf.get_rect(center = (WIDTH/2, HEIGHT - 10))