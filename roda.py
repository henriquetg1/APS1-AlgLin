from telas import TelaJogo1, TelaJogo2, TelaJogo3

tela_atual = TelaJogo1()
while True:
    tela_atual.roda()
    tela_atual = tela_atual.update()
