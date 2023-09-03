import os
import csv 
import Pesquisar

def Consultar_Ata():
    os.system('cls') or None
    print("---------------- Emitir Sugestão ---------------")
    titulo = input("Qual o nome da Ata a ser consultada? ")
    Retorno = Pesquisar.pesquisar_Ata(titulo)
    print("Inicio: " + Retorno[0])
    print("Final: " + Retorno[1])
    print("Titulo: " + Retorno[2])
    print("Pauta: " + Retorno[3])
    print("Palavra-Chave: " + Retorno[4])

    colunas = ['Inicio', 'Fim', 'Titulo', 'Pauta', 'Descricao', 'Tipo', 'Palavra_chave', 'Menbro_Externo', 'Participantes']
    files_exists = os.path.isfile('ConsultarAta.csv')

    with open('ConsultarAta.csv', 'a', newline='', encoding='utf-8') as ConsultarAta_csv:
        AtaConsulta = csv.DictWriter(ConsultarAta_csv, fieldnames=colunas, delimiter=";", lineterminator="\r\n")
        if not files_exists:
            AtaConsulta. writeheader()
        AtaConsulta.writerow({'Inicio':Retorno[0], 'Fim':Retorno[1], 'Titulo':Retorno[2], 'Pauta':Retorno[3], 'Descricao':"...", 'Tipo':"Publico", 'Palavra_chave':Retorno[4], 'Menbro_Externo':"Interno", 'Participantes': "Participantes"})
    print("Consulta de Ata realizada com sucesso!")

Consultar_Ata()