# Arquivo principal do jogo, responsável por rodar o jogo e alternar entre as telas.
from telas import TelaInicial, TelaJogo1, TelaJogo2, TelaJogo3

tela_atual = TelaInicial()
# Loop principal do jogo
while True:
    tela_atual.roda()
    tela_atual = tela_atual.update()
