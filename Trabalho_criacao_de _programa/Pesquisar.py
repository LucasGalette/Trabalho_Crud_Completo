import csv

def pesquisar_Interno(id):
    CadInter_csv = open('CadInter.csv')
    dados_Funcionarios = csv.DictReader(CadInter_csv, delimiter=";")

    for Funcionarios in dados_Funcionarios:
        if(Funcionarios["id"] == id):
            nome =  (Funcionarios["nome"])
            inter_exter =  (Funcionarios["inter_exter"])
            setor = (Funcionarios["setor"])

            return nome, inter_exter, setor
            break
    return False

def pesquisar_Externo(id):
    CadExter_csv = open('CadExter.csv')
    dados_Exter = csv.DictReader(CadExter_csv, delimiter=";")

    for Funcionarios in dados_Exter:
        if(Funcionarios["id"].lower() == id):
            nome =  (Funcionarios["nome"])
            inter_exter =  (Funcionarios["inter_exter"])

            return nome, inter_exter
            break
    return False

def pesquisar_Ata(titulo):
    EmitirAta_csv = open('EmitirAta.csv')
    AtaLida = csv.DictReader(EmitirAta_csv, delimiter=";")

    for Ata in AtaLida:
        if(Ata["Titulo"] == titulo):
            Inicio =  (Ata["Inicio"])
            Final =  (Ata["Fim"])
            Titulo =  (Ata["Titulo"])
            Pauta =  (Ata["Pauta"])
            Palavra_chave =  (Ata["Palavra_chave"])

            return Inicio, Final, Titulo, Pauta, Palavra_chave
            break
    return False

def pesquisar_Sugestao():
    Sugestao_csv = open('Sugestao.csv')
    Sugestao = csv.DictReader(Sugestao_csv, delimiter=";")

    for sugest in Sugestao:
        sugestao = (sugest["Sugestao"])
        return sugestao
        break
    return False
