import os
import csv 
import Pesquisar

def Emitir_Ata():
    resposta = "s"
    
    Inter_Exter = input("Membro Interno/Externo?")
    id = input("Qual o seu id? ")
    if Inter_Exter == "Interno":
        Retorno = Pesquisar.pesquisar_Interno(id)
    else:
        Retorno = Pesquisar.pesquisar_Externo(id)

    os.system('cls') or None
    print("---------------- Emitir Ata ---------------")
    Inicio = input("Horario de início")
    Fim = input("Horario de encerramento:")
    Titulo = input("Título:")
    Pauta = input("Pauta:")
    Descricao = input("Descrição:")
    Tipo = input("Tipo(Publica/Privada):")
    Palavra_chave = input("Palavra-chave")
    Menbro_Externo = Retorno[2]
    Opcao = 1
    id = input("Qual o id do participante?")
    Inter_Exter = input("Membro Interno/Externo?")
    if Inter_Exter == "Interno":
        Retorno = Pesquisar.pesquisar_Interno(id)
    else:
        Retorno = Pesquisar.pesquisar_Externo(id)
    while(Opcao == 1):

        Participantes = Retorno[0]
        Opcao = input("1-Incluir\n2-Salvar\n3-Excluir")

    

    colunas = ['Inicio', 'Fim', 'Titulo', 'Pauta', 'Descricao', 'Tipo', 'Palavra_chave', 'Menbro_Externo', 'Participantes']
    files_exists = os.path.isfile('EmitirAta.csv')

    with open('EmitirAta.csv', 'a', newline='', encoding='utf-8') as EmitirAta_csv:
        Ata = csv.DictWriter(EmitirAta_csv, fieldnames=colunas, delimiter=";", lineterminator="\r\n")
        if not files_exists:
            Ata. writeheader()
        Ata.writerow({'Inicio':Inicio, 'Fim':Fim, 'Titulo':Titulo, 'Pauta':Pauta, 'Descricao':Descricao, 'Tipo':Tipo, 'Palavra_chave':Palavra_chave, 'Menbro_Externo':Menbro_Externo, 'Participantes': Participantes})
    print("Emissão de Ata realizada com sucesso!")
    
    


def Emitir_Sugestao():
    os.system('cls') or None
    print("---------------- Emitir Sugestão ---------------")
    titulo = input("Qual o titulo da Ata a dar sugestão? ")
    Retorno = Pesquisar.pesquisar_Ata(titulo)
    print("Inicio: " + Retorno[0])
    print("Final: " + Retorno[1])
    print("Titulo: " + Retorno[2])
    print("Pauta: " + Retorno[3])
    print("Palavra-Chave: " + Retorno[4])

    sugestao = input("Diga sua sugestão:")

    colunas = ['Sugestao']
    files_exists = os.path.isfile('Sugestao.csv')

    with open('Sugestao.csv', 'a', newline='', encoding='utf-8') as Sugestao_csv:
        EmitirSugestao = csv.DictWriter(Sugestao_csv, fieldnames=colunas, delimiter=";", lineterminator="\r\n")
        if not files_exists:
            EmitirSugestao. writeheader()
        EmitirSugestao.writerow({'Sugestao':sugestao})
    print("Sugestão realizada com sucesso!")



