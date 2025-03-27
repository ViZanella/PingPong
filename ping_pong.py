import pygame
import sys

pygame.init()

# Definição de cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

# Configurações da tela
largura = 800
altura = 600

# Inicializa a janela do jogo
screen = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Pong")

# Dimensões das raquetes e da bola
raquete_largura = 10
raquete_altura = 60
tamanho_bola = 10

# Posições iniciais das raquetes e da bola
pc_x = 10  # Posição X da raquete do computador
pc_y = altura // 2 - raquete_altura // 2  # Centraliza a raquete verticalmente

player_1_x = largura - 20  # Posição X da raquete do jogador
player_1_y = altura // 2 - raquete_altura // 2  # Centraliza a raquete verticalmente

bola_x = largura // 2 - tamanho_bola // 2  # Centraliza a bola na tela
bola_y = altura // 2 - tamanho_bola // 2  # Centraliza a bola na tela

# Velocidades
raquete_player_1_dy = 5  # Velocidade da raquete do jogador
raquete_pc_dy = 5  # Velocidade da raquete do computador
velocidade_bola_x = 5  # Velocidade horizontal da bola
velocidade_bola_y = 5  # Velocidade vertical da bola

clock = pygame.time.Clock()  # Controlador de tempo

rodando = True  # Variável de controle do loop principal

while rodando:
    # Captura eventos do teclado e da janela
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Se o usuário fechar a janela, encerra o jogo
            rodando = False

    screen.fill(BRANCO)  # Limpa a tela

    # Movimento da bola
    bola_x += velocidade_bola_x
    bola_y += velocidade_bola_y

    # Verifica colisão da bola com as bordas superior e inferior
    if bola_y <= 0 or bola_y >= altura - tamanho_bola:
        velocidade_bola_y = -velocidade_bola_y  # Inverte a direção da bola

    # Reseta a posição da bola caso atinja as laterais da tela
    if bola_x <= 0 or bola_x >= largura - tamanho_bola:
        bola_x = largura // 2 - tamanho_bola // 2
        bola_y = altura // 2 - tamanho_bola // 2

    # Movimento da raquete do computador (segue a bola)
    if pc_y + raquete_altura / 2 < bola_y:
        pc_y += raquete_pc_dy
    elif pc_y + raquete_altura / 2 > bola_y:
        pc_y -= raquete_pc_dy

    # Impede que a raquete do computador saia dos limites da tela
    if pc_y <= 0:
        pc_y = 0
    elif pc_y >= altura - raquete_altura:
        pc_y = altura - raquete_altura

    # Verifica colisão da bola com as raquetes
    bola_rect = pygame.Rect(bola_x, bola_y, tamanho_bola, tamanho_bola)

    if bola_rect.colliderect(
        pygame.Rect(player_1_x, player_1_y, raquete_largura, raquete_altura)
    ):
        velocidade_bola_x = -velocidade_bola_x  # Inverte a direção da bola

    if bola_rect.colliderect(pygame.Rect(pc_x, pc_y, raquete_largura, raquete_altura)):
        velocidade_bola_x = -velocidade_bola_x  # Inverte a direção da bola

    # Captura o estado das teclas
    keys = pygame.key.get_pressed()

    # ERRO: A chamada `keys(pygame.K_UP)` deve ser `keys[pygame.K_UP]`
    if keys[pygame.K_UP] and player_1_y > 0:  # Move a raquete do jogador para cima
        player_1_y -= raquete_player_1_dy

    # ERRO: `raquete_player_1_dy < altura - raquete_altura` deveria ser `player_1_y < altura - raquete_altura`
    if keys[pygame.K_DOWN] and player_1_y < altura - raquete_altura:  # Move a raquete do jogador para baixo
        player_1_y += raquete_player_1_dy

    # Desenha as raquetes e a bola na tela
    pygame.draw.rect(screen, PRETO, (pc_x, pc_y, raquete_largura, raquete_altura))  # Raquete do computador
    pygame.draw.rect(screen, PRETO, (player_1_x, player_1_y, raquete_largura, raquete_altura))  # Raquete do jogador
    pygame.draw.ellipse(screen, PRETO, (bola_x, bola_y, tamanho_bola, tamanho_bola))  # Bola

    pygame.display.flip()  # Atualiza a tela

    clock.tick(120)  # Controla a taxa de atualização do jogo

# Finaliza o pygame e o programa
pygame.quit()
sys.exit()
