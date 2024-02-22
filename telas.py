# Arquivo que contém as classes das telas do jogo.
from sprites import Nave, Bala, CorpoCeleste, CorpoCeleste2, CorpoCeleste3, Alvo
from variaveis import *
import pygame

# Classe que representa o jogo, tem todas as informações principais que todas as telas possuem, 
# para que o código fique mais limpo e organizado.
class Jogo:
    def __init__(self, num_alvos):
        # Inicializa o pygame
        pygame.init()
        # Define a legenda da janela
        pygame.display.set_caption('APS1 ALG LIN')
        # Define o tamanho da janela
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        # Cria um grupo de sprites para todos os sprites
        self.all_sprites = pygame.sprite.Group()
        # Chama a classe nave para acessar o sprite da nave
        self.nave = Nave()
        # Adiciona a nave ao grupo de sprites
        self.all_sprites.add(self.nave)
        # Define a quantidade de alvos que será recebida por cada janela
        self.num_alvos = num_alvos
        # Define a quantidade de tiros 
        self.tiros = 6

        # Cria o background
        self.background = pygame.image.load("assets\img\ceu-estrelado.jpeg").convert()
        self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT))

    # Função que faz o jogo rodar, é chamada no loop principal do jogo, em roda.py. 
    # Além disso, chama as funcões que desenham as telas e atualiza o display.
    def roda(self):
        # Chama a função que desenha as tela de início e game over
        self.desenha_tela_inicial_gameover()
        # Chama a função que desenha as telas do jogo
        self.desenha_telas()
        # Atualiza o display
        pygame.display.update()        

    # Função que atualiza o jogo e as telas, é chamada no loop principal do jogo, em roda.py.
    def update(self):
        # Define o clock do jogo
        clock = pygame.time.Clock()

        # Se a quantidade de tiros for igual a 0, retorna a tela de game over
        if self.tiros == 0:
            return TelaGameOver()  

        # Loop para verificar os eventos do jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.tiros > 0:
                        bala = Bala(self.nave.rect.center, event.pos)
                        self.all_sprites.add(bala)
                        self.tiros -= 1

        # Cria um grupo de sprites para os alvos
        self.alvos = pygame.sprite.Group()
        for sprite in self.all_sprites:
            if isinstance(sprite, Alvo):
                self.alvos.add(sprite)
        
        # Loop para verificar as colisões entre as balas e os alvos
        for bala in self.all_sprites:
            if isinstance(bala, Bala):
                gravidade = self.corpo_celeste.calcular_forca_gravitacional(bala)
                bala.vel += gravidade 
                colisoes = pygame.sprite.spritecollide(bala, self.alvos, True)
                for alvo in colisoes:
                    self.num_alvos -= 1
        
        # Atualiza os sprites
        self.all_sprites.update()
        # Desenha as telas
        pygame.display.flip()
        # Define o clock do jogo
        clock.tick(60)
        # Retorna a própria tela
        return self
    
    # Função que desenha tudo que as telas de jogo precisam, para deixar o código mais limpo e não precisar reescrever várias vezes
    def desenha_telas(self):
        # Desenha o fundo
        self.screen.blit(self.background, (0, 0))
        # Desenha os sprites
        self.all_sprites.draw(self.screen)
        # Define a fonte do texto
        fonte = pygame.font.Font(None, 36)
        # Cria o texto
        texto_vidas = fonte.render(f'Tiros: {self.tiros - 1}', True, WHITE)
        # Desenha o texto
        self.screen.blit(texto_vidas, (10, 10))

# Classe que representa as primeira tela do jogo, herda da classe Jogo.
class TelaJogo1(Jogo):
    def __init__(self):
        super().__init__(1)
        # Cria um alvo
        self.alvo = Alvo((WIDTH // 2 + 150, HEIGHT // 2 - 300))
        # Cria um corpo celeste
        self.corpo_celeste = CorpoCeleste((WIDTH // 2 - 50, HEIGHT // 2))  
        # Adiciona os sprites ao grupo de sprites
        self.all_sprites.add(self.alvo, self.corpo_celeste)

    # Função que desenha a tela inicial e a tela de game over, tem que ser implementada nas telas de jogo para que seja ignorada
    def desenha_tela_inicial_gameover(self):    
        pass
    
    # Função que atualiza o jogo e as telas, é chamada no loop principal do jogo, em roda.py.
    def update(self):
        # Se a quantidade de alvos for igual a 0, retorna a próxima tela
        if self.num_alvos == 0:
            return TelaJogo2()
        return super().update()
    
class TelaJogo2(Jogo):
    def __init__(self):
        super().__init__(2)
        # Cria dois alvos
        self.alvo = Alvo((WIDTH // 2 + 300, HEIGHT // 2 - 300))
        self.alvo2 = Alvo((WIDTH // 2 - 150, HEIGHT // 2 - 300))
        # Cria dois corpos celestes
        self.corpo_celeste = CorpoCeleste((WIDTH // 2 - 240 , HEIGHT // 2 + 60))  
        self.corpo_celeste2 = CorpoCeleste2((WIDTH // 2 + 30 , HEIGHT // 2 - 75))  
        # Adiciona os sprites ao grupo de sprites
        self.all_sprites.add(self.corpo_celeste, self.corpo_celeste2, self.alvo, self.alvo2)
    
    # Função que desenha a tela inicial e a tela de game over, tem que ser implementada nas telas de jogo para que seja ignorada
    def desenha_tela_inicial_gameover(self):
        pass
    
    # Função que atualiza o jogo e as telas, é chamada no loop principal do jogo, em roda.py.
    def update(self):
        # Se a quantidade de alvos for igual a 0, retorna a próxima tela
        if self.num_alvos == 0:
            return TelaJogo3()
        # Retorna a própria tela
        return super().update()

class TelaJogo3(Jogo):
    def __init__(self):
        super().__init__(3)
        # Cria três alvos
        self.alvo = Alvo((WIDTH // 2 + 150, HEIGHT // 2 - 300))
        self.alvo2 = Alvo((WIDTH // 2 - 150, HEIGHT // 2 - 300))
        self.alvo3 = Alvo((WIDTH // 2 - 250, HEIGHT // 2 - 300))
        # Cria três corpos celestes
        self.corpo_celeste = CorpoCeleste((WIDTH // 2 - 325 , HEIGHT // 2 - 50))  
        self.corpo_celeste2 = CorpoCeleste2((WIDTH // 2 + 25 , HEIGHT // 2 + 50))  
        self.corpo_celeste3 = CorpoCeleste3((WIDTH // 2 + 300 , HEIGHT // 2 - 100))  
        # Adiciona os sprites ao grupo de sprites
        self.all_sprites.add(self.corpo_celeste, self.corpo_celeste2, self.corpo_celeste3, self.alvo, self.alvo2, self.alvo3)

    # Função que desenha a tela inicial e a tela de game over, tem que ser implementada nas telas de jogo para que seja ignorada
    def desenha_tela_inicial_gameover(self):
        pass

    # Função que atualiza o jogo e as telas, é chamada no loop principal do jogo, em roda.py.
    def update(self):
        # Se a quantidade de alvos for igual a 0, retorna a próxima tela
        if self.num_alvos == 0:
            return TelaVenceu()
        # Retorna a própria tela
        return super().update()
    
# Classe que representa a tela inicial do jogo, herda da classe Jogo.
class TelaInicial(Jogo):
    def __init__(self):
        super().__init__(0)
        # Carrega a imagem do arquivo
        self.logo_ = pygame.image.load('assets/img/INVASÃO ALIENÍGENA LOGO.png')
        # Redimensiona a imagem para o tamanho desejado
        self.logo = pygame.transform.scale(self.logo_, (810, 150))
        # Obtém o retângulo da imagem
        self.logo_rect = self.logo.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 150))
        # Define a fonte do texto
        self.font = pygame.font.Font('assets/fonts/space-age.regular.ttf', 60)
        # Cria o texto
        self.text = self.font.render("Iniciar", True, WHITE)
        # Obtém o retângulo do texto
        self.text_rect = self.text.get_rect(center=(WIDTH // 2, HEIGHT // 2+50))
        # Cria o texto
        self.text2 = self.font.render("Sair", True, WHITE)
        # Obtém o retângulo do texto
        self.text2_rect = self.text2.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 150))

    # Função que desenha a tela inicial e a tela de game over
    def desenha_tela_inicial_gameover(self):
        # Preenche a tela com a cor preta
        self.screen.fill(BLACK)
        # Desenha a imagem
        self.screen.blit(self.logo, self.logo_rect)
        # Desenha o texto
        pygame.draw.rect(self.screen, BLACK, self.text_rect)
        # Desenha o texto
        self.screen.blit(self.text, self.text_rect)
        # Desenha o texto
        pygame.draw.rect(self.screen, BLACK, self.text2_rect)
        # Desenha o texto
        self.screen.blit(self.text2, self.text2_rect)

    # Função que desenha as telas do jogo, tem que ser chamada nas telas que não são de jogo para que seja ignorada
    def desenha_telas(self):
        pass

    # Função que atualiza o jogo e as telas, é chamada no loop principal do jogo, em roda.py.
    def update(self):
        # Loop para verificar os eventos do jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # Se o botão do mouse for pressionado 
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Se o botão esquerdo do mouse for pressionado no retângulo do texto
                if self.text_rect.collidepoint(event.pos):
                    # Retorna a próxima tela
                    return TelaJogo1()
                # Se o botão esquerdo do mouse for pressionado no retângulo do texto
                elif self.text2_rect.collidepoint(event.pos):
                    # Sai do jogo
                    pygame.quit()
                    quit()
        # Retorna a própria tela
        return self

class TelaGameOver(Jogo):
    def __init__(self):
        super().__init__(0)
        self.font = pygame.font.Font('assets/fonts/space-age.regular.ttf', 90)
        self.text = self.font.render("Game Over", True, RED)
        self.text_rect = self.text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
        self.font = pygame.font.Font('assets/fonts/space-age.regular.ttf', 30)
        self.text2 = self.font.render("Tentar Novamente", True, WHITE)
        self.text2_rect = self.text2.get_rect(center=(WIDTH // 2, HEIGHT // 2+50))
        self.text3 = self.font.render("Voltar para o Menu Principal", True, WHITE)
        self.text3_rect = self.text3.get_rect(center=(WIDTH // 2, HEIGHT // 2+150))
        self.text4 = self.font.render("Sair", True, WHITE)
        self.text4_rect = self.text4.get_rect(center=(WIDTH // 2, HEIGHT // 2+250))

    def desenha_tela_inicial_gameover(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.text, self.text_rect)
        pygame.draw.rect(self.screen, BLACK, self.text2_rect)
        self.screen.blit(self.text2, self.text2_rect)
        pygame.draw.rect(self.screen, BLACK, self.text3_rect)
        self.screen.blit(self.text3, self.text3_rect)
        pygame.draw.rect(self.screen, BLACK, self.text4_rect)
        self.screen.blit(self.text4, self.text4_rect)

    def desenha_telas(self):
        pass

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.text2_rect.collidepoint(event.pos):
                    return TelaJogo1()
                elif self.text3_rect.collidepoint(event.pos):
                    return TelaInicial()
                elif self.text4_rect.collidepoint(event.pos):
                    pygame.quit()
                    quit()
        return self
    
class TelaVenceu(Jogo):
    def __init__(self):
        super().__init__(0)
        self.font = pygame.font.Font('assets/fonts/space-age.regular.ttf', 90)
        self.text = self.font.render("Você venceu!", True, GOLD)
        self.text_rect = self.text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
        self.font = pygame.font.Font('assets/fonts/space-age.regular.ttf', 30)
        self.text2 = self.font.render("Voltar para o Menu Principal", True, WHITE)
        self.text2_rect = self.text2.get_rect(center=(WIDTH // 2, HEIGHT // 2+50))
        self.text3 = self.font.render("Sair", True, WHITE)
        self.text3_rect = self.text3.get_rect(center=(WIDTH // 2, HEIGHT // 2+150))

    def desenha_tela_inicial_gameover(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.text, self.text_rect)
        pygame.draw.rect(self.screen, BLACK, self.text2_rect)
        self.screen.blit(self.text2, self.text2_rect)
        pygame.draw.rect(self.screen, BLACK, self.text3_rect)
        self.screen.blit(self.text3, self.text3_rect)

    def desenha_telas(self):
        pass

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.text2_rect.collidepoint(event.pos):
                    return TelaInicial()
                elif self.text3_rect.collidepoint(event.pos):
                    pygame.quit()
                    quit()
        return self