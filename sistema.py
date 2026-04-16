from interface import menu, cabecalho, leiaInt, leiaFloat
from lista import arquivoExiste, criarArquivo, lerArquivo, cadastrar
from time import sleep

arquivo = 'pacientes.txt'
if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:
    resposta = menu(['Ver pacientes cadastrados', 'Cadastrar novo paciente', 'Sair do sistema'])
    if resposta == 1:
        lerArquivo(arquivo)
    elif resposta == 2:
        cabecalho('Novo paciente')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        peso = leiaFloat('Peso (kg): ')
        altura = leiaFloat('Altura (m): ')
        objetivo = str(input('Objetivo: '))
        cadastrar(arquivo, nome, idade, peso, altura, objetivo)
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        cabecalho('\033[31mERRO: Digite uma opção válida.\033[m')
    sleep(1)