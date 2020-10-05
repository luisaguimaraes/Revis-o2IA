import copy


###VARIÁVEIS GLOBAIS
# Nenhuma

###FUNÇÕES
# Verifica se ganhou
def verifica_se_ganhou(tab):
    a = True
    if tab[0][0] != 0: a = False
    if tab[0][1] != 1: a = False
    if tab[0][2] != 2: a = False
    if tab[1][0] != 3: a = False
    if tab[1][1] != 4: a = False
    if tab[1][2] != 5: a = False
    if tab[2][0] != 6: a = False
    if tab[2][1] != 7: a = False
    if tab[2][2] != 8: a = False
    return a


# Verifica se os dois tabuleiros são iguais
def tabuleiros_iguais(tab1, tab2):
    sao_iguais = True
    for i in range(3):
        for j in range(3):
            if tab1[i][j] != tab2[i][j]:
                sao_iguais = False
    return sao_iguais


# Imprime o tabuleiro
def imprime_tabuleiro(tab):
    print('Profundidade do nó:', tab[3][0])
    print(tab[0])
    print(tab[1])
    print(tab[2])


def expandir(tab):  # retorna um conjunto de nós filhos com as próximas jogadas possíveis
    jogadas = []  # armazena os tabuleiros jogadas possíveis
    # 1 se vazio esta no meio do tabuleiro
    if tab[1][1] == 0:
        # move pra baixo
        a = copy.deepcopy(tab)  # copia o objeto
        a[1][1] = a[0][1]
        a[0][1] = 0
        a[3][0] = a[3][0] + 1  # profundidade do nó
        a[3][1] = tab  # criar referencia para o nó pai
        jogadas.append(a)
        # move pra direita
        a = copy.deepcopy(tab)  # copia o objeto
        a[1][1] = a[1][0]
        a[1][0] = 0
        a[3][0] = a[3][0] + 1  # profundidade do nó
        a[3][1] = tab
        jogadas.append(a)
        # move pra esquerda
        a = copy.deepcopy(tab)  # copia o objeto
        a[1][1] = a[1][2]
        a[1][2] = 0
        a[3][0] = a[3][0] + 1  # profundidade do nó
        a[3][1] = tab
        jogadas.append(a)
        # move pra cima
        a = copy.deepcopy(tab)  # copia o objeto
        a[1][1] = a[2][1]
        a[2][1] = 0
        a[3][0] = a[3][0] + 1  # profundidade do nó
        a[3][1] = tab
        jogadas.append(a)
    # 2 se vazio esta no canto esquerdo superior
    elif tab[0][0] == 0:
        # move pra cima
        a = copy.deepcopy(tab)  # copia o objeto
        a[0][0] = a[1][0]
        a[1][0] = 0
        a[3][0] = a[3][0] + 1  # profundidade do nó
        a[3][1] = tab
        jogadas.append(a)
        # move pra esquerda
        a = copy.deepcopy(tab)  # copia o objeto
        a[0][0] = a[0][1]
        a[0][1] = 0
        a[3][0] = a[3][0] + 1  # profundidade do nó
        a[3][1] = tab
        jogadas.append(a)
    # 3 se vazio esta no canto direito superior
    elif tab[0][2] == 0:
        # move pra cima
        a = copy.deepcopy(tab)  # copia o objeto
        a[0][2] = a[1][2]
        a[1][2] = 0
        a[3][0] = a[3][0] + 1  # profundidade do nó
        a[3][1] = tab
        jogadas.append(a)
        # move pra direita
        a = copy.deepcopy(tab)  # copia o objeto
        a[0][2] = a[0][1]
        a[0][1] = 0
        a[3][0] = a[3][0] + 1  # profundidade do nó
        a[3][1] = tab
        jogadas.append(a)
    # 4 se vazio esta no canto inferior esquerdo
    elif tab[2][0] == 0:
        # move pra baixo
        a = copy.deepcopy(tab)  # copia o objeto
        a[2][0] = a[1][0]
        a[1][0] = 0
        a[3][0] = a[3][0] + 1  # profundidade do nó
        a[3][1] = tab
        jogadas.append(a)
        # move pra esquerda
        a = copy.deepcopy(tab)  # copia o objeto
        a[2][0] = a[2][1]
        a[2][1] = 0
        a[3][0] = a[3][0] + 1  # profundidade do nó
        a[3][1] = tab
        jogadas.append(a)
    # 5 se vazio esta no canto inferior direito
    elif tab[2][2] == 0:
        # move pra baixo
        a = copy.deepcopy(tab)  # copia o objeto
        a[2][2] = a[1][2]
        a[1][2] = 0
        a[3][0] = a[3][0] + 1  # profundidade do nó
        a[3][1] = tab
        jogadas.append(a)
        # move pra direita
        a = copy.deepcopy(tab)  # copia o objeto
        a[2][2] = a[2][1]
        a[2][1] = 0
        a[3][0] = a[3][0] + 1  # profundidade do nó
        a[3][1] = tab
        jogadas.append(a)
    # 6 se vazio esta no meio da linha de cima
    elif tab[0][1] == 0:
        # move pra cima
        a = copy.deepcopy(tab)  # copia o objeto
        a[0][1] = a[1][1]
        a[1][1] = 0
        a[3][0] = a[3][0] + 1  # profundidade do nó
        a[3][1] = tab
        jogadas.append(a)
        # move pra direita
        a = copy.deepcopy(tab)  # copia o objeto
        a[0][1] = a[0][0]
        a[0][0] = 0
        a[3][0] = a[3][0] + 1  # profundidade do nó
        a[3][1] = tab
        jogadas.append(a)
        # move pra esquerda
        a = copy.deepcopy(tab)  # copia o objeto
        a[0][1] = a[0][2]
        a[0][2] = 0
        a[3][0] = a[3][0] + 1  # profundidade do nó
        a[3][1] = tab
        jogadas.append(a)
    # 7 se vazio esta no meio da linha de baixo
    elif tab[2][1] == 0:
        # move pra baixo
        a = copy.deepcopy(tab)  # copia o objeto
        a[2][1] = a[1][1]
        a[1][1] = 0
        a[3][0] = a[3][0] + 1  # profundidade do nó
        a[3][1] = tab
        jogadas.append(a)
        # move pra direita
        a = copy.deepcopy(tab)  # copia o objeto
        a[2][1] = a[2][0]
        a[2][0] = 0
        a[3][0] = a[3][0] + 1  # profundidade do nó
        a[3][1] = tab
        jogadas.append(a)
        # move pra esquerda
        a = copy.deepcopy(tab)  # copia o objeto
        a[2][1] = a[2][2]
        a[2][2] = 0
        a[3][0] = a[3][0] + 1  # profundidade do nó
        a[3][1] = tab
        jogadas.append(a)
    # 8 se vazio esta no meio da coluna da esquerda
    elif tab[1][0] == 0:
        # move pra baixo
        a = copy.deepcopy(tab)  # copia o objeto
        a[1][0] = a[0][0]
        a[0][0] = 0
        a[3][0] = a[3][0] + 1  # profundidade do nó
        a[3][1] = tab
        jogadas.append(a)
        # move pra cima
        a = copy.deepcopy(tab)  # copia o objeto
        a[1][0] = a[2][0]
        a[2][0] = 0
        a[3][0] = a[3][0] + 1  # profundidade do nó
        a[3][1] = tab
        jogadas.append(a)
        # move pra esquerda
        a = copy.deepcopy(tab)  # copia o objeto
        a[1][0] = a[1][1]
        a[1][1] = 0
        a[3][0] = a[3][0] + 1  # profundidade do nó
        a[3][1] = tab
        jogadas.append(a)
    # 9 se vazio esta no meio da coluna da direita
    elif tab[1][2] == 0:
        # move pra baixo
        a = copy.deepcopy(tab)  # copia o objeto
        a[1][2] = a[0][2]
        a[0][2] = 0
        a[3][0] = a[3][0] + 1  # profundidade do nó
        a[3][1] = tab
        jogadas.append(a)
        # move pra cima
        a = copy.deepcopy(tab)  # copia o objeto
        a[1][2] = a[2][2]
        a[2][2] = 0
        a[3][0] = a[3][0] + 1  # profundidade do nó
        a[3][1] = tab
        jogadas.append(a)
        # move pra direita
        a = copy.deepcopy(tab)  # copia o objeto
        a[1][2] = a[1][1]
        a[1][1] = 0
        a[3][0] = a[3][0] + 1  # profundidade do nó
        a[3][1] = tab
        jogadas.append(a)

    # retorno do conjunto de jogadas (nós)
    return jogadas


def imprime_as_jogadas(tab):
    print("\nAs jogadas foram:")
    pilha = []
    while (tab[3][1] != None):  # vai até o nó raiz
        pilha.append(tab)
        tab = tab[3][1]
    pilha.append(tab)
    while (len(pilha) > 0):
        temp = pilha.pop()
        imprime_tabuleiro(temp)


#############################
# HEURÍSTICAS
#############################
# Número de peças fora do lugar
def h1(tab):
    a = 0
    if tab[0][0] != 0: a = a + 1
    if tab[0][1] != 1: a = a + 1
    if tab[0][2] != 2: a = a + 1
    if tab[1][0] != 3: a = a + 1
    if tab[1][1] != 4: a = a + 1
    if tab[1][2] != 5: a = a + 1
    if tab[2][0] != 6: a = a + 1
    if tab[2][1] != 7: a = a + 1
    if tab[2][2] != 8: a = a + 1
    return a


# Distancia Manhattan
def h2(tab):
    h = 0
    for i in range(3):
        for j in range(3):
            if (tab[i][j] == 0):
                h = h + abs(0 - i) + abs(0 - j)
            if (tab[i][j] == 1):
                h = h + abs(0 - i) + abs(1 - j)
            if (tab[i][j] == 2):
                h = h + abs(0 - i) + abs(2 - j)
            if (tab[i][j] == 3):
                h = h + abs(1 - i) + abs(0 - j)
            if (tab[i][j] == 4):
                h = h + abs(1 - i) + abs(1 - j)
            if (tab[i][j] == 5):
                h = h + abs(1 - i) + abs(2 - j)
            if (tab[i][j] == 6):
                h = h + abs(2 - i) + abs(0 - j)
            if (tab[i][j] == 7):
                h = h + abs(2 - i) + abs(1 - j)
            if (tab[i][j] == 8):
                h = h + abs(2 - i) + abs(2 - j)
    return h


#############################
# ALGORITMOS DE BUSCA
#############################

# Busca em Largura/extensão
def busca_extensao(tab_inicial):
    fila = []
    fila.append(tab_inicial)  # adiciona no fim da fila
    nos_exp = 0  # numero de nós expandidos
    while (len(fila) > 0):
        nodoTemp = fila.pop(0)  # retira do início da fila
        nos_exp = nos_exp + 1
        print('\nNó expandido:', nos_exp)
        imprime_tabuleiro(nodoTemp)
        if verifica_se_ganhou(nodoTemp) == True:
            print("\n*** Solução encontrada! Parabéns! ***")
            imprime_as_jogadas(nodoTemp)
            break;
        else:
            nodos_filhos = expandir(nodoTemp)
            for n in nodos_filhos:
                fila.append(n)


# Busca em Largura/extensão (sem nós repetidos)
def busca_extensao_sem_repetidos(tab_inicial):
    fila = []
    filaRepet = []  # usada para verificar expanção de repetidos
    fila.append(tab_inicial)  # adiciona no fim da fila
    filaRepet.append(tab_inicial)
    nos_exp = 0  # numero de nós expandidos
    while (len(fila) > 0):
        nodoTemp = fila.pop(0)  # retira do início da fila
        nos_exp = nos_exp + 1
        print('\nNó expandido:', nos_exp)
        imprime_tabuleiro(nodoTemp)
        if verifica_se_ganhou(nodoTemp) == True:
            print("\n*** Solução encontrada! Parabéns! ***")
            imprime_as_jogadas(nodoTemp)
            break;
        else:
            nodos_filhos = expandir(nodoTemp)
            for nt in nodos_filhos:
                # verifica se nós já foi expandido
                # vamos percorrer toda a filaRepet e ver se já existe
                ja_existe = False
                for x in filaRepet:
                    if (tabuleiros_iguais(nt, x)):
                        ja_existe = True
                        break  # se já achou repetido pode parar a busca
                if (ja_existe == False):
                    fila.append(nt)
                    filaRepet.append(nt)


# Busca em Largura/extensão (sem nós repetidos)
# Heurística número de Peças fora do lugar
def busca_extensao_sem_repetidos_h1(tab_inicial):
    fila = []
    filaRepet = []  # usada para verificar expanção de repetidos
    fila.append(tab_inicial)  # adiciona no fim da fila
    filaRepet.append(tab_inicial)
    nos_exp = 0  # numero de nós expandidos
    while (len(fila) > 0):
        nodoTemp = fila.pop(0)  # retira do início da fila
        nos_exp = nos_exp + 1
        # if(nos_exp%1000==0):
        print('\nNó expandido:', nos_exp)
        imprime_tabuleiro(nodoTemp)
        if verifica_se_ganhou(nodoTemp) == True:
            print("\n*** Solução encontrada! Parabéns! ***")
            imprime_as_jogadas(nodoTemp)
            break;
        else:
            filhos = expandir(nodoTemp)
            filhos_nao_repet = []
            for nt in filhos:
                # verifica se nós já foi expandido
                # vamos percorrer toda a filaRepet e ver se já existe
                ja_existe = False
                for x in filaRepet:
                    if (tabuleiros_iguais(nt, x)):
                        ja_existe = True
                        break  # se já achou repetido pode parar a busca
                if (ja_existe == False):
                    filhos_nao_repet.append(nt)
            h = 9  # valor da heuristica (quanto menor melhor)
            # acha a melhor heurística (h1)
            for nr in filhos_nao_repet:
                if (h1(nr) < h):
                    h = h1(nr)  # ao final h tem o menor valor de h1
            # só adiciona na fila os que tem a melhor h1
            for nr in filhos_nao_repet:
                if (h1(nr) == h):
                    fila.append(nr)
                    filaRepet.append(nr)


# Busca em Largura/extensão (sem nós repetidos)
# Heurística número de Peças fora do lugar
def busca_extensao_sem_repetidos_h2(tab_inicial):
    fila = []
    filaRepet = []  # usada para verificar expanção de repetidos
    fila.append(tab_inicial)  # adiciona no fim da fila
    filaRepet.append(tab_inicial)
    nos_exp = 0  # numero de nós expandidos
    while (len(fila) > 0):
        nodoTemp = fila.pop(0)  # retira do início da fila
        nos_exp = nos_exp + 1
        # if(nos_exp%1000==0):
        print('\nNó expandido:', nos_exp)
        imprime_tabuleiro(nodoTemp)
        if verifica_se_ganhou(nodoTemp) == True:
            print("\n*** Solução encontrada! Parabéns! ***")
            imprime_as_jogadas(nodoTemp)
            break;
        else:
            filhos = expandir(nodoTemp)
            # filhos_nao_repet = filhos
            filhos_nao_repet = []
            for nt in filhos:
                # verifica se nós já foi expandido
                # vamos percorrer toda a filaRepet e ver se já existe
                ja_existe = False
                for x in filaRepet:
                    if (tabuleiros_iguais(nt, x)):
                        ja_existe = True
                        break  # se já achou repetido pode parar a busca
                if (ja_existe == False):
                    filhos_nao_repet.append(nt)
            h = 1000  # valor da heuristica (quanto menor melhor)
            # acha a melhor heurística (h2)
            for nr in filhos_nao_repet:
                if (h2(nr) < h):
                    h = h2(nr)  # ao final h tem o menor valor de h2
            # só adiciona na fila os que tem a melhor h2
            for nr in filhos_nao_repet:
                if (h2(nr) == h):
                    fila.append(nr)
                    filaRepet.append(nr)


####################
### MENU
####################
tab_inicial = [[2, 5, 8], [1, 4, 7], [3, 0, 6], [0, None]]
print('*** IA em Quebra-cabeça de 8 peças ***')
print('O tabuleiro esta assim: ')
imprime_tabuleiro(tab_inicial)
print('Informe qual algoritmo deseja utilizar: ')
print("1: Busca Cega em Extensão")
print("2: Busca Cega em Extensão sem nós repetidos")
print("3: Busca Com Informação Heurística peças fora do lugar")
print("4: Busca Com Informação Heurística Dist. Manhattan")
op = int(input('Informe uma opção:'))
if (op == 1):
    busca_extensao(tab_inicial)
elif (op == 2):
    busca_extensao_sem_repetidos(tab_inicial)
elif (op == 3):
    busca_extensao_sem_repetidos_h1(tab_inicial)
elif (op == 4):
    busca_extensao_sem_repetidos_h2(tab_inicial)