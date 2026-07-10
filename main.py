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

from estoque import cadastrar_roupas
from  estoque import listar_roupas
from estoque import buscar_roupa
from estoque import encontrar_roupa
from estoque import remover_roupa
from estoque import alterar_preco
from estoque import valor_total_estoque
from vendas import registrar_venda
from vendas import historico_vendas
from vendas import listar_historico_vendas
from arquivos import salvar_arquivo
from arquivos import carregar_arquivo
from arquivos import salvar_historico
from arquivos import carregar_historico

roupas = []

vendas = []

opcao = "0"

carregar_arquivo(roupas)
carregar_historico(vendas)


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
    print("9 = ENCONTRAR ROUPA ")
    print("10 = SAIR ")

    opcao = input("Digite a opcao desejada: ")

    if opcao == "1":

        cadastrar_roupas(roupas)
        salvar_arquivo(roupas)

    elif opcao == "2":

        listar_roupas(roupas)
     
    
    elif opcao == "3":

        buscar_roupa(roupas)
        

    elif opcao == "4":

        remover_roupa(roupas)
        salvar_arquivo(roupas)

    elif opcao == "5":

        alterar_preco(roupas)
        salvar_arquivo(roupas)

    elif opcao == "6":

        registrar_venda(roupas, vendas)
        salvar_arquivo(roupas)
        salvar_historico(vendas)


    elif opcao == "7":

        valor_total_estoque(roupas)

    elif opcao == "8":

        listar_historico_vendas(vendas)
        
        

    elif opcao == "9":

        encontrar_roupa(roupas)

    elif opcao == "10":

        print("Sair do Sistema!")



