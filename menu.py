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

def remover_figurinha(album):
    id = ler_inteiro("Numero da figurinha para remover: ")
    if album.remover(id):
        print("Figurinha removida.")
    else:
        print("Figurinha nao encontrada.")


def consultar_figurinha(album):
    id = ler_inteiro("Numero da figurinha: ")
    figurinha = album.buscar(id)
    if figurinha is None:
        print("Figurinha nao encontrada.")
    else:
        print(figurinha)

def menu():
    album_voce = Album(TOTAL_ALBUM)

    while True:
        print("")
        print("===== ALBUM DA COPA =====")
        print("1 - Inserir figurinha")
        print("2 - Remover figurinha")
        print("3 - Consultar figurinha")
        print("4 - Ver album completo")
        print("5 - Ver porcentagem concluida")
        print("6 - Ver figurinhas repetidas")
        print("7 - Contar repetidas")
        print("0 - Sair")
        opcao = ler_texto("Escolha uma opcao: ")

        if opcao == "1":
            inserir_figurinha(album_voce)
        elif opcao == "2":
            remover_figurinha(album_voce)
        elif opcao == "3":
            consultar_figurinha(album_voce)
        elif opcao == "4":
            album_voce.listar()
        elif opcao == "5":
            print("Album " + str(round(album_voce.porcentagem(), 2)) + "% concluido.")
        elif opcao == "6":
            album_voce.mostrar_repetidas()
        elif opcao == "7":
            print("Voce tem " + str(album_voce.contar_repetidas()) + " repetidas.")
        elif opcao == "0":
            print("Ate logo!")
            break
        else:
            print("Opcao invalida.")


menu()