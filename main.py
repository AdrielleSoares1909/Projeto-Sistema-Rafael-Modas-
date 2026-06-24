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

opcao = "0"

def cadastrar_roupas():

    nome = input("Digite o nome da peça de roupa a ser cadastrada: ")
    preco = float(input("Digite o preço da peca de roupa a ser cadastrada: "))
    estoque = int(input("Digite a quantidade em estoque disponivel : "))
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

    quantidade_vendida = int(input("Qual quantidade  do item  do estoque foi vendido: "))

    roupa_encontrada = False

    for roupa in roupas:

        if roupa["nome"] == venda_roupa and roupa["tamanho"] == venda_tamanho:

                roupa_encontrada = True

                if roupa["estoque"] >= quantidade_vendida:

                    roupa["estoque"] = roupa["estoque"] - quantidade_vendida

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



while opcao != "9":

    print("------- MENU --------")
    print("1 = CADASTRAR ROUPA ")
    print("2 = LISTAR ROUPAS ")
    print("3 = BUSCAR ROUPA ")
    print("4 = REMOVER ROUPA ")
    print("5 = ALTERAR PRECO ")
    print("6 = REGISTRAR VENDA ")
    print("7 = VALOR TOTAL DO ESTOQUE")
    print("8 = SAIR ")

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

    else:

        print("Sair do Sistema!")
    
