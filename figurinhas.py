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