

def cadastrar_roupas(roupas):

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

    

def listar_roupas(roupas):

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


def buscar_roupa(roupas):

    localizar_roupa = input("Qual roupa deseja localizar:  ")

    localizar_tamanho = input("Digite o tamanho da roupa a ser localizada: ")

    encontrei_roupa = False

    for roupa in roupas:

        if roupa["nome"]  == localizar_roupa and roupa["tamanho"] == localizar_tamanho.strip().lower():

            encontrei_roupa = True

            print(f"Nome: {roupa['nome']}")
            print(f"Preço: R${roupa['preco']}")
            print(f"Estoque: {roupa['estoque']}")
            print(f"Tamanho: {roupa['tamanho']}")

    if not encontrei_roupa:
        print("ROUPA NÃO LOCALIZADA NO SISTEMA!")


def encontrar_roupa(roupas):



    buscar_roupa = input("Digite o nome da roupa: ").strip().lower()

    roupa_encontrada = False

    for roupa in roupas:

        
        if roupa["nome"].strip().lower() == buscar_roupa:

            roupa_encontrada = True

            print("---------------------")
            print(f"Nome: {roupa['nome']}")
            print(f"Preço: R${roupa['preco']}")
            print(f"Estoque: {roupa['estoque']}")
            print(f"Tamanho: {roupa['tamanho']}")
            print("---------------------")

            
            
    if not roupa_encontrada:
        print("ROUPA NÃO ENCONTRADA!")






def remover_roupa(roupas):

    excluir_roupa = input("Qual roupa deseja excluir do sistema: ")

    excluir_tamanho = input("Qual tamanho  deseja excluir do sistema: ")

    roupa_encontrada = False

    for roupa in roupas:

        if roupa["nome"] == excluir_roupa and roupa["tamanho"] == excluir_tamanho.strip().lower():

            roupa_encontrada = True

            roupas.remove(roupa) #Alterar a lista

            print("ROUPA EXCLUIDA DO SISTEMA COM SUCESSO.")

            

            return
    
    if not roupa_encontrada:
        print("ROUPA NÃO ENCONTRADA!")


def alterar_preco(roupas):

    alterar_roupa = input("Qual roupa deseja alterar no sistema: ")

    alterar_tamanho = input("Qual tamanho  deseja alterar no sistema: ")

    novo_preco = float(input("Qual sera o novo preco a ser cadastrado no sistema: "))

    roupa_encontrada = False

    for roupa in roupas:

        if roupa["nome"] == alterar_roupa and roupa["tamanho"] == alterar_tamanho.strip().lower():

                roupa_encontrada = True

                roupa["preco"] = novo_preco #Alterar um item da lista

                print("PRECO ATUALIZADO NO  SISTEMA COM SUCESSO.")

                

                return
    
    if not roupa_encontrada:
        print("ROUPA NÃO ENCONTRADA!")

def valor_total_estoque(roupas):

    total_estoque = 0

    for roupa in roupas:

        total_estoque += roupa["estoque"] * roupa["preco"] 

    print(f"Valor total do estoque: R$ {total_estoque:.2f}")