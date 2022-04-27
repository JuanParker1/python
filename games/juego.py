import random
import sys
import time
import pygame
from pygame.locals import *
                        #####Las posiciones de referencia para una ventana o trabajar con eso es la esquina superior izquierda
pygame.init()
vec= pygame.math.Vector2 #Inicializa un objeto vector/"variables" con 2 dimensiones. Esto se va a utilizar como constructor de vectores en el resto del codigo

Height=450      ####ALtura y anchura de la ventana
Width=400
ACC=0.5         ###Utilizados para "movimiento realista" y gravedad   junto con vec declarada mas arriba
FRIC=-0.12
FPS= 60

FramePerSec= pygame.time.Clock()

displaysurface=pygame.display.set_mode((Width,Height))
pygame.display.set_caption("Game")          ###Nombre a la ventana

class Juego:
    def __init__(self):
            self.maximo=0

    def iniciarJuego(self,maxima=0):
        

        class Player(pygame.sprite.Sprite):
            def __init__(self):
                super().__init__()
                self.surf = pygame.Surface((30,30))     #Dimensiones de la imagen del jugador
                self.surf.fill((128,255,40))            #Color de relleno de la imagen del jugador
                self.rect= self.surf.get_rect()

                self.pos= vec((10,385))
                self.vel= vec(0,0)              ####    Vectores de dos cordenadas (x,y) (eje horizontal    ,   eje vertical)
                self.acc= vec(0,0)  #### Acceleration
                self.jumping = False  
                self.score=0

            def move(self):
                self.acc=vec(0,0.5)

                pressed_keys = pygame.key.get_pressed()

                if pressed_keys[K_LEFT]:
                    self.acc.x=-ACC
                if pressed_keys[K_RIGHT]:
                    self.acc.x=ACC    

                self.acc.x += self.vel.x * FRIC
                self.vel += self.acc
                self.pos += self.vel + 0.5 * self.acc

                if self.pos.x > Width:
                    self.pos.x = 0
                if self.pos.x < 0:
                    self.pos.x = Width
            
                self.rect.midbottom = self.pos

            def update(self):
                hits = pygame.sprite.spritecollide(self ,platforms, False)
                if self.vel.y > 0:        
                    if hits:
                        if self.pos.y < hits[0].rect.bottom:
                            if hits[0].point == True:   ##
                                hits[0].point = False   ##
                                #self.score += 1         ## 
                            self.pos.y = hits[0].rect.top +1         ###"Alinea" la posicion vertical del P1 con la plataforma
                            self.vel.y = 0
                            self.jumping = False
            
            def jump(self):
                hits = pygame.sprite.spritecollide(self, platforms, False)
                if hits and not self.jumping:
                    self.jumping=True
                    self.vel.y = -15   

            def cancel_jump(self):
                if self.jumping:
                    if self.vel.y < -3:
                        self.vel.y = -3
                self.jumping=False
        class platform(pygame.sprite.Sprite):
            def __init__(self):
                super().__init__()
                self.surf = pygame.Surface((Width, 20))
                self.surf.fill((255,0,0))
                self.rect = self.surf.get_rect(center = (Width/2, Height - 10))
                self.point=False
        class blockplat(pygame.sprite.Sprite):              ####Esta clase la he metido yo para diferenciar entre bloque base y plataformas de subida
            def __init__(self):
                super().__init__()
                self.surf = pygame.Surface((100, 20))
                self.surf.fill((0,0,255))
                self.rect = self.surf.get_rect(center = (random.randint(0,Width-10),
                                                        random.randint(20, Height-20)))
                self.point=True

        def check(platform, groupies):
            if pygame.sprite.spritecollideany(platform,groupies):
                return True
            else:
                for entity in groupies:
                    if entity == platform:
                        continue
                    if (abs(platform.rect.top - entity.rect.bottom) < 60) and (abs(platform.rect.bottom - entity.rect.top) < 60):
                        return True
                C = False
        
        def plat_gen():
            while len(platforms) < 6:
                width = random.randrange(50,100)
                p  = blockplat()      
                C = True
                
                while C:
                    p = blockplat()
                    p.rect.center = (random.randrange(0, Width - width),
                                    random.randrange(-50, 0))
                    C = check(p, platforms)
                platforms.add(p)
                all_sprites.add(p)

        def checkmax(self,score):
            if self.maximo<score:
                self.maximo=score


           

        p1=Player()
        base=platform()


        all_sprites= pygame.sprite.Group()              ##Grupo para dibujar
        all_sprites.add(base)
        all_sprites.add(p1)


        platforms=pygame.sprite.Group()                 ##Grupo para "hittear" ver colisiones
        platforms.add(base)


        for x in range(random.randint(4,5)):
            C = True
            pl = blockplat()
            while C:
                pl = blockplat()
                C = check(pl, platforms)
            platforms.add(pl)
            all_sprites.add(pl)

        while True:
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:                ###Esto se añade aqui y no en elmetodo move(), por que aqui estamos recogiendo eventos
                    if event.key == pygame.K_UP:
                        p1.jump()
                if event.type==pygame.KEYUP:
                    if event.key==pygame.K_UP:
                        p1.cancel_jump()

           

            displaysurface.fill((0,0,0))        ###Rellenamos el display que hemos declarado al inicio en la linea 16

            ##Declaracion de la fuentes

            f = pygame.font.SysFont("Verdana", 20)     ##

            #Formateo de los textos

            g  = f.render(str(p1.score), True, (123,255,0))   ##
            hp  = f.render("MAX PUNT - "+str(self.maximo), True, (123,255,0))   ##
            
            ##Proyeccion de los textos sobre el display

            displaysurface.blit(g, (Width -80,10))   ##         
            displaysurface.blit(hp, (Width/10, 10))   ##               


            p1.move()
            p1.update()


            plat_gen()


            for entity in all_sprites:
                displaysurface.blit(entity.surf,entity.rect)
                

                
            if p1.rect.top <= Height / 3:           #### SUbe la pantalla según sube el jugador
                p1.pos.y += abs(p1.vel.y)
                for plat in platforms:
                    plat.rect.y += abs(p1.vel.y)
                    if plat.rect.top >= Height:
                        p1.score+=1
                        plat.kill()                ##Elimina las plataformas que se quedan por debajo      Esto habra que hacerlo si o si all bajar por que si no se generaran plataformas de mas al volver a subir
                        

            """if p1.rect.top >=Height:             ### Baja la pantalla segun baja el jugadorº        HAY QUE PULIR MAS
                p1.pos.y -=5*abs(p1.vel.y)
                for plat in platforms:
                    plat.rect.y -= 5*abs(p1.vel.y)
            """
            if p1.rect.top >Height:            #Si bajas de la linea de abajo el juego acaba  
                for entity in all_sprites:
                    entity.kill()
                    time.sleep(1)
                    displaysurface.fill((255,255,255))

                    ##Declaracion de la fuente

                    f = pygame.font.SysFont("Verdana", 20)     ##

                    ##Formateo de los textos

                    g  = f.render(("GAME OVER"), True, (0,0,0))   ##
                    h  = f.render(("Puntuacion: "+str(p1.score)), True, (0,0,0))   ##
                    rp  = f.render(("Para volver a jugar pulsa espacio"), True, (0,0,0))   ##

                    ## Proyectado de los textos

                    displaysurface.blit(g, (Width/3, Height/2-50))
                    displaysurface.blit(h, ((Width/3)-10, Height/2))
                    displaysurface.blit(rp, ((Width/8)-10, (Height/2)+100))


                    pygame.display.update()
                    
                            
                    for event in pygame.event.get():
                        print("Pilla eventos")
                        if event.type==pygame.KEYDOWN:
                            print("Evento keydown")
                            if event.key==pygame.K_SPACE:
                                print("Espacio")


                                
                                checkmax(self,p1.score)
                                
                                
                                self.iniciarJuego(self.maximo)
                            elif event.key!=pygame.K_SPACE:
                                print("No  espacios")
                                pygame.quit()
                                sys.exit()
                


            pygame.display.update()
            FramePerSec.tick(FPS)

juego=Juego()
Juego.iniciarJuego(juego)


            




