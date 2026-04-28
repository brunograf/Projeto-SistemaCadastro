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

def leiaSexo (msg):
    '''
    Lê um sexo e retorna o sexo lido.

    Caso o sexo lido seja diferente de H ou M, é impresso um erro
    e é solicitado novamente o sexo.

    Parâmetros:
    msg : Mensagem a ser impressa para solicitar o sexo.

    Retorna:
    str : O sexo lido.
    '''
    while True:
        sexo = input(msg).upper().strip()[0]
        if sexo == 'H':
            return 'Homem'
        elif sexo == 'M':
            return 'Mulher'
        else:
            cabecalho(f'\033[31mERRO: Digite um sexo válido.\033[m')

def leiaAtividade (msg):
    '''
    Lê um nível de atividade física e retorna o nível lido.

    Caso o nível de atividade física lido seja diferente de 1, 2, 3 ou 4,
    é impresso um erro e é solicitado novamente o nível de atividade física.

    Parâmetros:
    msg : Mensagem a ser impressa para solicitar o nível de atividade física.

    Retorna:
    str : O nível de atividade física lido.
    '''
    while True:
        nivel = leiaInt(msg)
        if nivel == 1:
            return 'Sedentario'
        elif nivel == 2:
            return 'Leve'
        elif nivel == 3:
            return 'Moderado'
        elif nivel == 4:
            return 'Alto'
        else:
            cabecalho(f'\033[31mERRO: Digite um nível de atividade física válido.\033[m')

def calcularCalorias(idade, sexo, peso, altura, atividade):
    '''
    Calcula as calorias diárias recomendadas para um paciente.

    Parâmetros:
    idade : Idade do paciente em anos.
    sexo : Sexo do paciente.
    peso : Peso do paciente em quilogramas.
    altura : Altura do paciente em metros.
    atividade : Nível de atividade física do paciente.

    Retorna:
    float : As calorias diárias recomendadas para o paciente.
    '''
    if sexo == 'Homem':
        tmb = (10 * peso) + (6.25 * altura * 100) - (5 * idade) + 5
    else:
        tmb = (10 * peso) + (6.25 * altura * 100) - (5 * idade) - 161

    if atividade == 'Sedentario':
        return tmb * 1.2
    elif atividade == 'Leve':
        return tmb * 1.375
    elif atividade == 'Moderado':
        return tmb * 1.55
    elif atividade == 'Alto':
        return tmb * 1.725

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