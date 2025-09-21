import uuid

itemCadastrado = []

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
        print("3 - Voltar ao menu inicial")
        
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
                print("Retornando ao menu inicial...\n")
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
    print('oi')


def consultarItens():
    if itemCadastrado:
        print(itemCadastrado[0][0])
    else:
        print("Nenhum item cadastrado.")


def detalhesItens():
    print("\n===== DetalheS do Item =====\n")
    for item in itemCadastrado:
        print(f"Nome: {item[1]}")
        print(f"Descrição: {item[2]}")
        print(f"Código: {item[0]}")
        print(f"Preço: R$ {float(item[3]):.2f}")
        print(f"Estoque: {item[4]}\n")           
        
            

# FUNÇÕES DE MENU PEDIDOS ->>>

def criarPedido():
    print('oi')
    
def ProcessarPedidos():
    print('oi')

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

    
