import uuid

itemCadastrado = []

# FUNÇÕES REUTILIZAVEIS ->>>

def sair():
    escolhaSair = """
    ============= DESEJA SAIR? ===============
    
    [1] \tNão
    [0] \tSair
    
    => """
    
    return input(escolhaSair)


# MENUS ->>>

def escolhaMenu():
    escolhaDoMenu = """
    ============= ESCOLHA O MENU ===============
    
    [1] \tMenu de Itens
    [2] \tMenu de Pedidos
    [0] \tSair
    
    => """
    
    return input(escolhaDoMenu)

def menuItens():
    menu = """
    ================== MENU ITENS ==================
    
    [1] \tCadastrar Item 
    [2] \tAtualizar Item
    [3] \tConsultar Itens
    [4] \tDetalhes do Item
    [0] \tSair

    => """
    return input(menu)

def menuPedidos():
    menu = """
    ================= MENU PEDIDOS =================
    
    [1] \tCriar Pedido 
    [2] \tProcessar Pedidos Pendentes
    [3] \tAtualizar Status de Pedido
    [4] \tCacelar Pedido
    [0] \tSair

    => """
    return input(menu)


# FUNÇÕES DE MENU ITENS ->>>

def novoItem():
    while True:
        print("\nEscolha o próximo passo\n")
        print("1 - Cadastrar novo produto.")
        print("2 - Listar produtos cadastrados.")
        print("3 - Voltar ao menu de itens.")
        
        opcao = input("\n>>: ")
    
        match opcao:
            case "1":
                cadastrarItem()
            case "2":
                if itemCadastrado:
                    print("\nProdutos cadastrados:\n")
                    for item in itemCadastrado:
                        print(item)
                else: 
                    print("\nNenhum produto cadastrado.")
            case "3":
                print("\nRetornando ao menu de itens...\n")
                break
            case _:
                print("Opção inválida. Tente novamente.")
            
def cadastrarItem():
    nome = input("Digite o nome do produto: ")
    descricao = (input("Digite a descrição do produto: "))
    preco = (input("Digite o preço do produto: "))
    estoque = (input("Digite a quantidade do estoque: "))
    
    numero = int(uuid.uuid4().int %100000)
    codigo = f"PRO{numero:04d}"
    
    item = (nome, descricao, codigo, preco, estoque)
    itemCadastrado.append(item)
    
    print("\nProduto cadastrado com sucesso!\n")
    return
     
def atualizarItens():
    if not itemCadastrado: 
        print("\nO sistema ainda não possui um item cadastrado.")
        return


    print("\n=== ITENS CADASTRADOS ===")
    for i, item in enumerate(itemCadastrado):
        print(f"[{i}] {item[0]} (R${item[3]} - estoque: {item[4]})")

    try: 
        indice = int(input("\nDigite o número do item que será atualizado:"))
        if indice < 0 or indice >= len(itemCadastrado):
            print("Item inválido.")
            return
    except ValueError:
        print("Digite um item já cadastrado")
        return
    
    nome, descricao, codigo, preco, estoque = itemCadastrado[indice]

    print("\nDeixe em branco apenas o campo que não será alterado.")

    nome_atual = input(f"Nome atual [{nome}]: ") or nome
    descricao_atual = input(f"Descrição atual [{descricao}]: ") or descricao
    preco_atual = input(f"Preço atual [{preco}]:") or preco
    estoque_atual = input(f"Estoque atual [{estoque}]:") or estoque

    # ITENS ATUALIZADOS
    itemCadastrado[indice]= (nome_atual, descricao_atual, codigo, preco_atual, estoque_atual)

    print("\nItens atualizados!")


def consultarItens():
    if itemCadastrado:
        print("\n===== Itens Disponíveis =====")
        for i, item in enumerate(itemCadastrado):
            print(f"[{i}] {item[0]} (R${item[3]} - Descrição: {item[1]})")
    else:
        print("\nNenhum item cadastrado.")


def detalhesItens():

    if itemCadastrado:
        print("\n===== Detalhes do Item =====\n")
        for item in itemCadastrado:
            print(f"Nome: {item[0]}")
            print(f"Descrição: {item[1]}")
            print(f"Código: {item[2]}")
            print(f"Preço: R$ {float(item[3].replace(',', '.')):.2f}")
            print(f"Estoque: {item[4]}\n")           
    else:
        print("\nNenhum item cadastrado.")
            

# FUNÇÕES DE MENU PEDIDOS ->>>

def adicionarPedido():
    escolhaPedido = """
    ============= ESCOLHA ===============
    
    [1] \tAdicionar mais produtos
    [0] \tSair
    
    => """
    
    return input(escolhaPedido)

pedidosPendentes = []

def criarPedido():
    if itemCadastrado:
        consultarItens()
        pedido_usuario = {
            "produtos": [],   # lista de produtos desse pedido
            "status": "Aguardando Aprovação" # status inicial
        }
        qtd_produto = True
        while qtd_produto == True:
            try:
                indice = int(input("\nDigite o número do produto que deseja: "))
            except ValueError:
                print("Digite um número válido.")
                continue
            
            if 0 <= indice < len(itemCadastrado):
                pedido = {
                    "nome": itemCadastrado[indice][0],
                    # "descricao": itemCadastrado[indice][1],
                    "codigo": itemCadastrado[indice][2],
                    # "preco": itemCadastrado[indice][3],
                    # "estoque": itemCadastrado[indice][4],
                }
                pedido_usuario["produtos"].append(pedido)

                print("\nSua lista atual de pedidos:")
                for p in pedido_usuario["produtos"]:
                    print(f"- {p['nome']}")

                controle = True
                while controle == True:
    
                    match adicionarPedido():
                        case '1':
                            consultarItens()
                            controle = False
                        case '0':
                            qtd_produto = False
                            controle = False 
                        case _:
                            print("\nOpção inválida")
            else:
                print("\nÍndice inválido.")
                controle2=True
                while controle2 == True:
                    match sair():
                        case '1':
                            break
                        case '0':
                            controle2=False
                            qtd_produto = False
                        case _:
                            print("\nOpção inválida")
        
        if pedido_usuario["produtos"]:
            pedidosPendentes.append(pedido_usuario)
            print(f"\nPedido enviado para aprovação!")
            print(pedidosPendentes)
        else:
            print("\nNenhum produto adicionado, pedido não criado.")
    else:
        print("\nNenhum produto no sistema.")

filaPreparo = []

cancelados = []

def ProcessarPedidos():
    if pedidosPendentes:
        while pedidosPendentes:
            pedido = pedidosPendentes[0]
            print("\n===== Pedidos pendentes =====")
            print(f"Código - {pedido['produtos'][0]['codigo']} ({pedido['produtos'][0]['nome']} - Status: {pedido['status']})")
            print(f"\n===== Pedido {pedido['produtos'][0]['codigo']} =====")
            print("[1] Aceitar")
            print("[2] Rejeitar")
            print("[0] Sair")
            opcao = input("\n>>: ")

            if opcao == '1':  
                pedido['status'] = "Aprovado"
                linha = pedidosPendentes.pop(0)
                filaPreparo.append(linha)
                print("\nPedido aceito!")
            elif opcao == '2':
                pedido['status'] = "Cancelado"
                linha = pedidosPendentes.pop(0)
                cancelados.append(linha)
                print("\nPedido cancelado!")
            elif opcao == '0':
                return
            else:
                print("\nOpção inválida")
    else:
        print("\nNenhum pedido novo no sistema.")

def atualizarStatusPedido():
    print('oi')

def cancelarPedido():
    print('oi')
    

# LOOPING DO SISTEMA ->>>

controle = True

while controle == True:
    
    match escolhaMenu():
        case '1':
            while True:
                escolha = menuItens()
                match escolha:
                    case '1':
                        cadastrarItem()
                        novoItem()
                    case '2':
                        atualizarItens()
                    case '3':
                        consultarItens()
                    case '4':
                        detalhesItens()
                    case '0':
                        break
                    case _:
                        print("Opção inválida")
        case '2':
            while True:
                escolha = menuPedidos()
                match escolha:
                    case '1':
                        criarPedido()
                    case '2':
                        ProcessarPedidos()
                    case '3':
                        atualizarStatusPedido()
                    case '4':
                        cancelarPedido()
                    case '0':
                        break
                    case _:
                        print("Opção inválida")
        case '0':
            controle = False
        case _:
            print("Opção inválida")

    
