import os
import csv 

inter_exter = ""

def Cadastrar_Interno():
    print("-------------- Cadastrar Funcionario -------------")

    id = input("Declare um id!")
    inter_exter = "interno"
    nome = input("Qual seu nome?")
    sexo = input("Qual seu sexo?(H/M)")
    data_nascimento = input("Qual seu ano de nascença?")
    email = input("Qual seu email?")
    setor = input("Qual seu setor?")

    colunas = ['inter_exter','nome', 'sexo', 'data_nascimento', 'email', 'setor', 'id']
    files_exists = os.path.isfile('CadInter.csv')

    with open('CadInter.csv', 'a', newline='', encoding='utf-8') as CadInter_csv:
        cadastrar = csv.DictWriter(CadInter_csv, fieldnames=colunas, delimiter=";", lineterminator="\r\n")
        if not files_exists:
            cadastrar. writeheader()
        cadastrar.writerow({'inter_exter':inter_exter, 'nome':nome, 'sexo':sexo, 'data_nascimento':data_nascimento, 'email':email, 'setor':setor, 'id':id})
    print("Cadastro realizado com sucesso!")

def Cadastrar_Externo():
    print("-------------- Cadastrar Visitante Externo -------------")

    id = input("Declare um id!")
    inter_exter = "externo"
    nome = input("Qual seu nome?")
    empresa = input("Qual o nome da sua empresa?")
    email = input("Qual seu email?")

    colunas = ['inter_exter', 'nome', 'empresa', 'email', 'id']
    files_exists = os.path.isfile('CadExter.csv')

    with open('CadExter.csv', 'a', newline='', encoding='utf-8') as CadExter_csv:
        cadastrar = csv.DictWriter(CadExter_csv, fieldnames=colunas, delimiter=";", lineterminator="\r\n")
        if not files_exists:
            cadastrar. writeheader()
        cadastrar.writerow({'inter_exter':inter_exter, 'nome':nome, 'empresa':empresa, 'email':email, 'id':id})
    print("Cadastro realizado com sucesso!")