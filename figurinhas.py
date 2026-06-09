class Figurinha:
    def __init__(self, id, nome, pais, posicao, raridade):
        self.id = id
        self.nome = nome
        self.pais = pais
        self.posicao = posicao
        self.raridade = raridade

    def __str__(self):
        return "[" + str(self.id) + "] " + self.nome + " - " + self.pais + " - " + self.posicao + " - " + self.raridade


class NodoLista:
    def __init__(self, figurinha):
        self.figurinha = figurinha
        self.proximo = None


class NodoFila:
    def __init__(self, figurinha):
        self.figurinha = figurinha
        self.proximo = None


class Fila:
    def __init__(self):
        self._inicio = None
        self._fim = None
        self._tamanho = 0

    def esta_vazia(self):
        return self._inicio is None

    def enqueue(self, figurinha):
        novo = NodoFila(figurinha)
        if self._fim is None:
            self._inicio = novo
            self._fim = novo
        else:
            self._fim.proximo = novo
            self._fim = novo
        self._tamanho = self._tamanho + 1

    def dequeue(self):
        if self.esta_vazia():
            return None
        removido = self._inicio
        self._inicio = self._inicio.proximo
        if self._inicio is None:
            self._fim = None
        self._tamanho = self._tamanho - 1
        return removido.figurinha

    def peek(self):
        if self.esta_vazia():
            return None
        return self._inicio.figurinha

    def limpar(self):
        self._inicio = None
        self._fim = None
        self._tamanho = 0

    def tamanho(self):
        return self._tamanho


class Album:
    def __init__(self, total=20):
        self._cabeca = None
        self._tamanho = 0
        self._total = total
        self._repetidas_cabeca = None
        self._repetidas_tamanho = 0

    def buscar(self, id):
        atual = self._cabeca
        while atual is not None:
            if atual.figurinha.id == id:
                return atual.figurinha
            atual = atual.proximo
        return None

    def adicionar(self, figurinha):
        if self.buscar(figurinha.id) is not None:
            self._adicionar_repetida(figurinha)
            return False
        novo = NodoLista(figurinha)
        novo.proximo = self._cabeca
        self._cabeca = novo
        self._tamanho = self._tamanho + 1
        return True

    def _adicionar_repetida(self, figurinha):
        novo = NodoLista(figurinha)
        novo.proximo = self._repetidas_cabeca
        self._repetidas_cabeca = novo
        self._repetidas_tamanho = self._repetidas_tamanho + 1

    def remover(self, id):
        atual = self._cabeca
        anterior = None
        while atual is not None:
            if atual.figurinha.id == id:
                if anterior is None:
                    self._cabeca = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                self._tamanho = self._tamanho - 1
                return True
            anterior = atual
            atual = atual.proximo
        return False