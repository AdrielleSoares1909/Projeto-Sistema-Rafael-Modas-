



def registrar_venda(roupas, vendas):

    venda_roupa = input("Qual item do estoque foi vendido: ")

    venda_tamanho = input("Qual tamanho do item  do estoque foi vendido: ")

    quantidade_vendida = int(input("Qual quantidade  do item  do estoque foi vendido: "))

    

    roupa_encontrada = False

    for roupa in roupas:

        

        if roupa["nome"] == venda_roupa and roupa["tamanho"] == venda_tamanho.strip().lower():

                roupa_encontrada = True

                if roupa["estoque"] >= quantidade_vendida:

                    nome_do_cliente = input("Qual o nome do cliente: ")

                    data_da_venda = input("Qual a data da venda: ")

                    roupa["estoque"] = roupa["estoque"] - quantidade_vendida

                    
                    historico_vendas(vendas,roupa,nome_do_cliente,data_da_venda,quantidade_vendida)

                    print("Compra realizada com sucesso.")

                else:

                    print("QUANTIDADE INDISPONIVEL!!!")
                
                

                return
        
    if not roupa_encontrada:
        print("ROUPA NÃO ENCONTRADA!")


def historico_vendas(vendas,roupa,nome_do_cliente,data_da_venda,quantidade_vendida):

    
        
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


def listar_historico_vendas(vendas):

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