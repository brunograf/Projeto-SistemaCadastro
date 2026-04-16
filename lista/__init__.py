from interface import cabecalho

def arquivoExiste(nome):
    '''
    Verifica se um arquivo existe.

    Parâmetros:
    nome : Nome do arquivo a ser verificado.

    Retorna:
    bool : True se o arquivo existe, False caso contrário.
    '''
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    '''
    Cria um arquivo com o nome especificado.

    Parâmetros:
    nome : Nome do arquivo a ser criado.
    '''
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print(f'\033[31mHouve um erro na criação do arquivo {nome}.\033[m')
    else:
        print(f'\033[32mArquivo {nome} criado com sucesso!\033[m')

def lerArquivo(nome):
    '''
    Lê o conteúdo de um arquivo e imprime as linhas.

    Parâmetros:
    nome : Nome do arquivo a ser lido.
    '''
    try:
        a = open(nome, 'rt')
    except:
        print(f'\033[31mErro ao ler o arquivo!\033[m')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<20}{dado[1]:>3} anos{dado[2]:>10}kg{dado[3]:>10}m{dado[4]:>20}')
    finally:
        a.close()

def cadastrar(arquivo, nome, idade, peso, altura, objetivo):
    '''
    Cadastra um novo paciente no arquivo.

    Parâmetros:
    arquivo : Nome do arquivo onde os dados serão gravados.
    nome : Nome do paciente.
    idade : Idade do paciente em anos.
    peso : Peso do paciente em quilogramas.
    altura : Altura do paciente em metros.
    objetivo : Objetivo do paciente.
    '''
    try:
        a = open(arquivo, 'at')
    except:
        print(f'\033[31mHouve um erro ao abrir o arquivo {arquivo}.\033[m')
    else:
        try:
            a.write(f'{nome};{idade};{peso};{altura};{objetivo}\n')
        except:
            print(f'\033[31mHouve um erro ao escrever os dados no arquivo.\033[m')
        else:
            print(f'\033[32mNovo paciente {nome} adicionado com sucesso!\033[m')
        finally:
            a.close()