from figurinhas import Figurinha, Album, Historico, SELECOES_VALIDAS, selecao_valida

TOTAL_ALBUM = 20
ARQUIVO = "dados.csv"


def ler_inteiro(mensagem):
    while True:
        entrada = input(mensagem).strip()
        if entrada == "":
            print("Entrada vazia. Tente novamente.")
            continue
        valido = True
        i = 0
        if entrada[0] == "-":
            i = 1
        if i >= len(entrada):
            valido = False
        while i < len(entrada):
            if entrada[i] < "0" or entrada[i] > "9":
                valido = False
                break
            i = i + 1
        if valido:
            return int(entrada)
        print("Numero invalido. Digite apenas digitos.")


def ler_texto(mensagem):
    while True:
        entrada = input(mensagem).strip()
        if entrada == "":
            print("Entrada vazia. Tente novamente.")
            continue
        return entrada


def ler_selecao(mensagem):
    while True:
        entrada = ler_texto(mensagem)
        if selecao_valida(entrada):
            return entrada
        print("Selecao invalida. Selecoes validas:")
        for selecao in SELECOES_VALIDAS:
            print(" - " + selecao)


def inserir_figurinha(album):
    id = ler_inteiro("Numero da figurinha: ")
    if id < 1 or id > TOTAL_ALBUM:
        print("Numero fora do album (1 a " + str(TOTAL_ALBUM) + ").")
        return
    nome = ler_texto("Nome do jogador: ")
    pais = ler_selecao("Selecao: ")
    posicao = ler_texto("Posicao: ")
    raridade = ler_texto("Raridade (comum/rara/lendaria): ")
    figurinha = Figurinha(id, nome, pais, posicao, raridade)
    if album.adicionar(figurinha):
        print("Figurinha adicionada ao album.")
    else:
        print("Voce ja tinha essa figurinha. Foi para as repetidas.")