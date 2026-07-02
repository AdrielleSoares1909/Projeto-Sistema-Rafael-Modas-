""" 

    📦 Projeto: Sistema Rafael Modas 

    Etapas do projeto: 
    -----------------------------
    Etapa 1 (CRUD)

    ✅ Cadastrar roupa
    ✅ Listar roupas
    ✅ Buscar roupa
    🔜 Remover roupa
    ------------------------------
    Etapa 2

    Alterar preço
    Alterar estoque
    Registrar venda
    Repor estoque
    ------------------------------
    Etapa 3

    Calcular valor total do estoque
    Produto mais caro
    Produto mais barato
    -----------------------------
    Etapa 4

    Salvar em arquivo .txt
    Ler arquivo .txt
    ----------------------------------
    Etapa 5

    Organizar tudo em funções
    Deixar o código limpo

---------------------------------------------------------------------------------------
    OBS:::: >>> # break,ele realmente interrompe alguma coisa. 
                #Só que ele interrompe apenas loops (for e while). Sai do for.

# Mas a função continua executando o restante do código depois do for. 
# Para sair da função.Quando o Python encontra o return, 
# ele para de executar a função e volta para quem a chamou (no seu caso, o menu).
# >>>> Resumindo<<<<<
# break → sai de um for ou while.
# return → sai de uma função.
    
"""


roupas = []

vendas = []

opcao = "0"

def cadastrar_roupas():

    nome = input("Digite o nome da peça de roupa a ser cadastrada: ")
    preco = float(input("Digite o preço da peca de roupa a ser cadastrada: "))
    estoque = float(input("Digite a quantidade em estoque disponivel : "))
    tamanho = input("Digite o tamanho da peca de roupa a ser cadastrada: ")

    roupa = {

        "nome": nome,
        "preco" : preco,
        "estoque" : estoque,
        "tamanho": tamanho
    }

    roupas.append(roupa) #Alterar a lista





def listar_roupas():

    if not roupas:

        print("LISTA VAZIA")
        return # usando para sair da função

    for roupa in roupas:
        print("-------------------")
        print(f"Nome: {roupa['nome']}")
        print(f"Preço: R${roupa['preco']}")
        print(f"Estoque: {roupa['estoque']}")
        print(f"Tamanho: {roupa['tamanho']}")
        print("-------------------")


def buscar_roupa():

    localizar_roupa = input("Qual roupa deseja localizar:  ")

    localizar_tamanho = input("Digite o tamanho da roupa a ser localizada: ")

    encontrei_roupa = False

    for roupa in roupas:

        if roupa["nome"]  == localizar_roupa and roupa["tamanho"] == localizar_tamanho:

            encontrei_roupa = True

            print(f"Nome: {roupa['nome']}")
            print(f"Preço: R${roupa['preco']}")
            print(f"Estoque: {roupa['estoque']}")
            print(f"Tamanho: {roupa['tamanho']}")

    if not encontrei_roupa:
        print("ROUPA NÃO LOCALIZADA NO SISTEMA!")


def remover_roupa():

    excluir_roupa = input("Qual roupa deseja excluir do sistema: ")

    excluir_tamanho = input("Qual tamanho  deseja excluir do sistema: ")

    roupa_encontrada = False

    for roupa in roupas:

        if roupa["nome"] == excluir_roupa and roupa["tamanho"] == excluir_tamanho:

            roupa_encontrada = True

            roupas.remove(roupa) #Alterar a lista

            print("ROUPA EXCLUIDA DO SISTEMA COM SUCESSO.")

            return
    
    if not roupa_encontrada:
        print("ROUPA NÃO ENCONTRADA!")


def alterar_preco():

    alterar_roupa = input("Qual roupa deseja alterar no sistema: ")

    alterar_tamanho = input("Qual tamanho  deseja alterar no sistema: ")

    novo_preco = float(input("Qual sera o novo preco a ser cadastrado no sistema: "))

    roupa_encontrada = False

    for roupa in roupas:

        if roupa["nome"] == alterar_roupa and roupa["tamanho"] == alterar_tamanho:

                roupa_encontrada = True

                roupa["preco"] = novo_preco #Alterar um item da lista

                print("PRECO ATUALIZADO NO  SISTEMA COM SUCESSO.")

                return
    
    if not roupa_encontrada:
        print("ROUPA NÃO ENCONTRADA!")
    

def registrar_venda():

    venda_roupa = input("Qual item do estoque foi vendido: ")

    venda_tamanho = input("Qual tamanho do item  do estoque foi vendido: ")

    quantidade_vendida = float(input("Qual quantidade  do item  do estoque foi vendido: "))

    

    roupa_encontrada = False

    for roupa in roupas:

        if roupa["nome"] == venda_roupa and roupa["tamanho"] == venda_tamanho:

                roupa_encontrada = True

                if roupa["estoque"] >= quantidade_vendida:

                    nome_do_cliente = input("Qual o nome do cliente: ")

                    data_da_venda = input("Qual a data da venda: ")

                    roupa["estoque"] = roupa["estoque"] - quantidade_vendida

                    
                    historico_vendas(roupa,nome_do_cliente,data_da_venda,quantidade_vendida)

                    print("Compra realizada com sucesso.")

                else:

                    print("QUANTIDADE INDISPONIVEL!!!")

                return
        
    if not roupa_encontrada:
        print("ROUPA NÃO ENCONTRADA!")
                
def valor_total_estoque():

    total_estoque = 0

    for roupa in roupas:

        total_estoque += roupa["estoque"] * roupa["preco"] 

    print(f"Valor total do estoque: R$ {total_estoque:.2f}")

def salvar_arquivo():

    arquivo = open("estoque.txt","w") # w escreve na lista

    for roupa in roupas:

        arquivo.write(f'{roupa ["nome"]};{roupa ["preco"]};{roupa["estoque"]};{roupa ["tamanho"]}\n')

    arquivo.close()

def carregar_arquivo():

    arquivo = open("estoque.txt","r") # Abrir arquivo

    for linha in arquivo: # percorre a lista 

        dados = linha.split(";") # split =  transformar a linha do arquivo em uma lista e seprar por ;

        roupa = { # Cria o dicionário

            "nome": dados[0],
            "preco": float(dados[1]),# converter tipo para float como se trata do preco
            "estoque": int(dados[2]), # converter para int pois se trata de uma numero inteiro
            "tamanho": dados[3]
        }

    
        roupas.append(roupa) # adiciona na lista

    arquivo.close() # fecha o arquivo


def historico_vendas(roupa,nome_do_cliente,data_da_venda,quantidade_vendida):

    
        
    venda = {

        "nome": roupa["nome"],

        "tamanho": roupa["tamanho"],

        "quantidade_vendida" : quantidade_vendida, # Se a informação já está em uma variável, use a variável.

        "preco" : roupa["preco"],

        "valor_total" : roupa["preco"] * quantidade_vendida, # Se a informação já está em uma variável, use a variável.

        "nome_do_cliente" : nome_do_cliente,

        "data_da_venda" : data_da_venda,

    }

    vendas.append(venda)


def listar_historico_vendas():

    for venda in vendas:


        print(f"----------------------")
        print(f"PRODUTO: {venda['nome']}")
        print(f"TAMANHO: {venda['tamanho']}")
        print(f"QUANTIDADE VENDIDA: {venda['quantidade_vendida']}")
        print(f"PREÇO DA UNIDADE: R${venda['preco']}")
        print(f"PREÇO TOTAL DA VENDA: R${venda['valor_total']}")
        print(f"CLIENTE: {venda['nome_do_cliente']}")
        print(f"DATA DA VENDA: {venda['data_da_venda']}")
        print(f"----------------------")


    if not vendas:
        print("Nenhuma venda registrada.")
    return



while opcao != "10":

    print("------- MENU --------")
    print("1 = CADASTRAR ROUPA ")
    print("2 = LISTAR ROUPAS ")
    print("3 = BUSCAR ROUPA ")
    print("4 = REMOVER ROUPA ")
    print("5 = ALTERAR PRECO ")
    print("6 = REGISTRAR VENDA ")
    print("7 = VALOR TOTAL DO ESTOQUE")
    print("8 = LISTAR HISTORICO DE VENDAS ")
    print("9 = SAIR ")

    opcao = input("Digite a opcao desejada: ")

    if opcao == "1":

        cadastrar_roupas()

    elif opcao == "2":

        listar_roupas()
    
    elif opcao == "3":

        buscar_roupa()

    elif opcao == "4":

        remover_roupa()

    elif opcao == "5":

        alterar_preco()

    elif opcao == "6":

        registrar_venda()

    elif opcao == "7":

        valor_total_estoque()

    elif opcao == "8":

        listar_historico_vendas()

    else:

        print("Sair do Sistema!")



