import os
import csv 
import Pesquisar

def Concluir_Ata():
    os.system('cls') or None
    sugestao = Pesquisar.pesquisar_Sugestao()
    print("---------------- Emitir Sugestão ---------------")
    titulo = input("Qual o nome da Ata a ser concluida? ")
    Retorno = Pesquisar.pesquisar_Ata(titulo)
    print("Inicio: " + Retorno[0])
    print("Final: " + Retorno[1])
    print("Titulo: " + Retorno[2])
    print("Pauta: " + Retorno[3])
    print("Palavra-Chave: " + Retorno[4])
    print("Sugestão: " + sugestao)

    colunas = ['Inicio', 'Fim', 'Titulo', 'Pauta', 'Descricao', 'Tipo', 'Palavra_chave', 'Menbro_Externo', 'Participantes', 'Sugestão']
    files_exists = os.path.isfile('ConcluirAta.csv')

    with open('ConcluirAta.csv', 'a', newline='', encoding='utf-8') as ConcluirAta_csv:
        AtaConcluida = csv.DictWriter(ConcluirAta_csv, fieldnames=colunas, delimiter=";", lineterminator="\r\n")
        if not files_exists:
            AtaConcluida. writeheader()
        AtaConcluida.writerow({'Inicio':Retorno[0], 'Fim':Retorno[1], 'Titulo':Retorno[2], 'Pauta':Retorno[3], 'Descricao':"...", 'Tipo':"Publico", 'Palavra_chave':Retorno[4], 'Menbro_Externo':"Interno", 'Participantes': "Participantes", 'Sugestão': sugestao})
    print("Conclusão de Ata realizada com sucesso!")