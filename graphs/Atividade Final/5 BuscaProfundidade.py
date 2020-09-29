# Classe nó, representa o no da árvore
# não adicionaie os prints por que nos algoritmos recursivos
# atrapalha a legibilidade da saída
class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerdo = None
        self.direito = None
    # adiciona o nó e criando a arvore

    def adicionaNo(self, valor):
        if valor:
            if valor < self.valor:
                if self.esquerdo is None:
                    self.esquerdo = No(valor)
                else:
                    self.esquerdo.adicionaNo(valor)
            elif valor > self.valor:
                if self.direito is None:
                    self.direito = No(valor)
                else:
                    self.direito.adicionaNo(valor)
            else:
                self.valor = valor


raiz = No(6)

raiz.adicionaNo(3)
raiz.adicionaNo(24)
raiz.adicionaNo(9)
raiz.adicionaNo(61)
raiz.adicionaNo(2)
raiz.adicionaNo(15)
raiz.adicionaNo(7)
raiz.adicionaNo(10)


def buscaProfundidadeArvore(raiz):
    if raiz is None:
        return

    else:
        print(raiz.valor, end=" -> ")
        buscaProfundidadeArvore(raiz.esquerdo)
        buscaProfundidadeArvore(raiz.direito)


buscaProfundidadeArvore(raiz)
