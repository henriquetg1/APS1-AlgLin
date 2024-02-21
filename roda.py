from telas import TelaInicial, TelaJogo1, TelaJogo2, TelaJogo3

tela_atual = TelaInicial()
while True:
    tela_atual.roda()
    tela_atual = tela_atual.update()
