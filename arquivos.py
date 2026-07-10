



def salvar_arquivo(roupas):

    
    arquivo = open("estoque.txt","w") # w escreve na lista

    for roupa in roupas:

        arquivo.write(f'{roupa ["nome"]};{roupa ["preco"]};{roupa["estoque"]};{roupa ["tamanho"]}\n')

    arquivo.close()


def carregar_arquivo(roupas):

    arquivo = open("estoque.txt", "r")

    for linha in arquivo:

        if linha.strip() == "":
            continue

        dados = linha.split(";")

        roupa = {
            "nome": dados[0],
            "preco": float(dados[1]),
            "estoque": int(float(dados[2])),
            "tamanho": dados[3].strip()
        }

        roupas.append(roupa)

    arquivo.close()








def salvar_historico(vendas):

    historico = open("historico_vendas.txt","w") # w escreve na lista

    for venda in vendas:

        historico.write(f'{venda ["nome"]};{venda ["tamanho"]};{venda["quantidade_vendida"]};{venda ["preco"]};{venda["valor_total"]};{venda ["nome_do_cliente"]};{venda ["data_da_venda"]}\n')

    historico.close()


def carregar_historico(vendas):

    historico = open("historico_vendas.txt","r") # Abrir arquivo

    for linha in historico: # percorre a lista 

        if linha.strip() == "":
            continue

        dados = linha.split(";") # split =  transformar a linha do arquivo em uma lista e seprar por ;

        venda = { # Cria o dicionário

            "nome": dados[0],
            "tamanho": dados[1],
            "quantidade_vendida" : dados[2],
            "preco": float(dados[3]),# converter tipo para float como se trata do preco
            "valor_total": float(dados[4]), # converter para int pois se trata de uma numero inteiro
            "nome_do_cliente": dados[5],
            "data_da_venda" : dados[6].strip() # O strip() remove o \n do final da linha.
        }

        vendas.append(venda)

    historico.close() # fecha o arquivo