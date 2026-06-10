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