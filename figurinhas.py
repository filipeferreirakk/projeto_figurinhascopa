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

    def listar(self):
        if self._cabeca is None:
            print("Album vazio.")
            return
        atual = self._cabeca
        while atual is not None:
            print(atual.figurinha)
            atual = atual.proximo

    def porcentagem(self):
        if self._total == 0:
            return 0
        return (self._tamanho / self._total) * 100
    
    def mostrar_repetidas(self):
        if self._repetidas_cabeca is None:
            print("Nenhuma figurinha repetida.")
            return
        atual = self._repetidas_cabeca
        while atual is not None:
            print(atual.figurinha)
            atual = atual.proximo

    def contar_repetidas(self):
        return self._repetidas_tamanho
    
    def tem_repetida(self, id):
        atual = self._repetidas_cabeca
        while atual is not None:
            if atual.figurinha.id == id:
                return True
            atual = atual.proximo
        return False

    def remover_repetida(self, id):
        atual = self._repetidas_cabeca
        anterior = None
        while atual is not None:
            if atual.figurinha.id == id:
                if anterior is None:
                    self._repetidas_cabeca = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                self._repetidas_tamanho = self._repetidas_tamanho - 1
                return atual.figurinha
            anterior = atual
            atual = atual.proximo
        return None
    
    def buscar_por_jogador(self, nome):
        resultado = Fila()
        atual = self._cabeca
        while atual is not None:
            if atual.figurinha.nome.lower() == nome.lower():
                resultado.enqueue(atual.figurinha)
            atual = atual.proximo
        return resultado

    def buscar_por_selecao(self, pais):
        resultado = Fila()
        atual = self._cabeca
        while atual is not None:
            if atual.figurinha.pais.lower() == pais.lower():
                resultado.enqueue(atual.figurinha)
            atual = atual.proximo
        return resultado

    def tamanho(self):
        return self._tamanho
    
    def salvar(self, arquivo):
        saida = open(arquivo, "w", encoding="utf-8")
        atual = self._cabeca
        while atual is not None:
            f = atual.figurinha
            saida.write("A;" + str(f.id) + ";" + f.nome + ";" + f.pais + ";" + f.posicao + ";" + f.raridade + "\n")
            atual = atual.proximo
        atual = self._repetidas_cabeca
        while atual is not None:
            f = atual.figurinha
            saida.write("R;" + str(f.id) + ";" + f.nome + ";" + f.pais + ";" + f.posicao + ";" + f.raridade + "\n")
            atual = atual.proximo
        saida.close()

    def carregar(self, arquivo):
        try:
            entrada = open(arquivo, "r", encoding="utf-8")
        except FileNotFoundError:
            return False
        linha = entrada.readline()
        while linha != "":
            linha = linha.strip()
            if linha != "":
                partes = linha.split(";")
                if len(partes) == 6:
                    figurinha = Figurinha(int(partes[1]), partes[2], partes[3], partes[4], partes[5])
                    if partes[0] == "A":
                        self.adicionar(figurinha)
                    else:
                        self._adicionar_repetida(figurinha)
            linha = entrada.readline()
        entrada.close()
        return True
    
class Historico:
    def __init__(self):
        self._fila = Fila()

    def registrar(self, figurinha):
        self._fila.enqueue(figurinha)

    def listar(self):
        if self._fila.esta_vazia():
            print("Nenhuma troca registrada.")
            return
        atual = self._fila._inicio
        while atual is not None:
            print(atual.figurinha)
            atual = atual.proximo

    def quantidade(self):
        return self._fila.tamanho()