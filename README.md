# Invasão Alienígena
Invasão Alienígena é um jogo criado para a disciplina de Álgebra Linear do terceiro semestre de Ciência da Computação no Insper. O jogador tem uma nave e três níveis, e a cada nível possui cinco balas e precisa destruir as naves alieígenas, fazendo com que a bala fuja da atração gravitacional de planetas. 

# Como executar
Para jogar, é necessário clonar ou baixar o repositório no qual o jogo está localizado e ter Python 3 instalado na máquina, além da biblioteca de PyGame. Se você não possui essa biblioteca siga os passos abaixo para conseguir jogar.
1. Acesse o terminal do python;
2. Digite o comando 'pip install pygame' e pressione enter;
3. Espere baixar e pronto!

Para rodar o jogo, entre no arquivo roda.py e clique para rodar, ou se preferir executar pelo terminal, digite o comando: python roda.py

# Como jogar
Após instalar o jogo, clique em iniciar. Para atirar, utilize o botão esquerdo do mouse. A velocidade é controlada por meio da onde o ponteiro do mouse se encontra, ou seja, o quanto mais perto da nave, mais devagar a bala irá, e o quão mais longe, mais rápido. 

# Modelo físico
Para calcularmos a força gravitacional utilizamos vetores. Primeiro começamos calculando a posição vetorial da bala e do corpo celeste. Ele é calculado por uma função da biblioteca PyGame e é dado por: [x,y]. 

``` vetor_bala = pygame.math.Vector2(posicao_da_bala) ``` 
``` vetor_corpo_celeste = pygame.math.Vector2(posicao_do_corpo) ``` 

Após isso decidimos que a constante de gravitação universal seria igual a 7500:

```c = 7500  ```

E calculamos o vetor da diferença dos vetores da posição do corpo e da bala:

``` vetor_diferenca = vetor_corpo_celeste - vetor_bala```

Com esse vetor descoberto, conseguimos aplicar o teorema de pitágoras e descobrir o vetor resultante que seria a hipotenusa de um triangulo retângulo formado por esses vetores: 

``` vetor_resultante = vetor_diferenca.x ** 2 + vetor_diferenca.y ** 2 ```

Com isso, pegamos esse vetor e utilizamos a seguinte formula para calcular a força gravitacional:

```forca_gravitacional = (c)/vetor_resultante```

Com essa força descoberta, agora conseguimos calular a gravidade. Ela é dada pela normalização do vetor da direção multiplicado pela força gravitacional:

```gravidade = vetor_diferenca.normalize() * forca_gravitacional```

Agora, se a bala for atraída pelo campo gravitacional do corpo celeste sua velociade será somada à gravidade, alterando a sua trajetória:

```velocidade_da_bala += gravidade```

Esse código pode ser encotrado na classe ```CorpoCeleste``` no arquivo sprites.py

# Informações extras
O código do jogo está separado em 4 arquivos: variaveis.py, telas.py, sprites.py, roda.py.  
- variveis.py: guarda as variaveis do jogo, como por exemplo cores e tamanho da tela;
- telas.py: possui todas as telas do jogo, separadas em classes, como a tela de início, de jogo e de gameover;
- sprites.py: possui todas as sprites do jogo, como a bala e a nave;
- roda.py: possui o loop principal que faz o jogo rodar, utilizando as classes das telas.
