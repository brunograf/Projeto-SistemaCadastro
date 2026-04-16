def cabecalho (txt):
    '''
    Imprime um cabeçalho com o texto centralizado.

    Parâmetros:
    txt : Texto a ser impresso no cabeçalho.
    '''
    print('-' * 42)
    print(txt.center(42))
    print('-' * 42)

def leiaInt(msg):
    '''
    Lê um valor inteiro e retorna o valor lido.

    Caso o valor lido não seja um inteiro, é impresso um erro
    e é solicitado novamente o valor.

    Parâmetros:
    msg : Mensagem a ser impressa para solicitar o valor.

    Retorna:
    int : O valor inteiro lido.
    '''
    while True:
        n = input(msg)
        try:
            return int(n)
        except ValueError:
            cabecalho(f'\033[31mERRO: Digite um número inteiro válido.\033[m')

def leiaFloat(msg):
    '''
    Lê um valor real e retorna o valor lido.

    Caso o valor lido não seja um real, é impresso um erro
    e é solicitado novamente o valor.

    Parâmetros:
    msg : Mensagem a ser impressa para solicitar o valor.

    Retorna:
    float : O valor real lido.
    '''
    while True:
        n = input(msg)
        try:
            return float(n)
        except ValueError:
            cabecalho(f'\033[31mERRO: Digite um número real válido.\033[m')

def menu (lista):
    '''
    Imprime um menu com as opções passadas na lista.

    Parâmetros:
    lista : Lista com as opções do menu.

    Retorna:
    int : A opção escolhida pelo usuário.
    '''
    cabecalho('SISTEMA DE CADASTRO DE PESSOAS')
    for i, item in enumerate(lista):
        print(f'\033[33m{i+1}\033[m - \033[34m{item}\033[m')
    print('-' * 42)
    opc = leiaInt('Sua opção: ')
    return opc