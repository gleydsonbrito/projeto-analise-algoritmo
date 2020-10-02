# simples implementação do pseudo código
# esse algoritmo não funciona sozinho, é necessário
# ter a implementação de inserir no inicio da lista e do digrafo D

def InsereNoInicioDaLista(L, atual):
    return


def constroi_caminho(i, j, D=None):
    L = []
    atual = j
    while atual.valor != i.valor:
        InsereNoInicioDaLista(L, atual)
        atual.valor = atual.predecessor[i.valor]
    InsereNoInicioDaLista(L, i)
    return L
