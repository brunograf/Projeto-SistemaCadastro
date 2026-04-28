from interface import menu, cabecalho, leiaInt, leiaFloat, leiaSexo, leiaAtividade, calcularCalorias
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
        sexo = leiaSexo('Sexo [H/M]: ')
        idade = leiaInt('Idade: ')
        peso = leiaFloat('Peso (kg): ')
        altura = leiaFloat('Altura (m): ')
        atividade = leiaAtividade ('Nível de atividade física [1-4]: ')
        objetivo = str(input('Objetivo: '))
        calorias = f'{calcularCalorias(idade, sexo, peso, altura, atividade):.2f}'
        cadastrar(arquivo, nome, sexo, idade, peso, altura, atividade, objetivo, calorias)
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        cabecalho('\033[31mERRO: Digite uma opção válida.\033[m')
    sleep(1)