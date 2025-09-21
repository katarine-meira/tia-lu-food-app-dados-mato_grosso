
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


def cadastrarItem():
    nome = input("Digite o nome do produto: ")
    descricao = (input("Digite a descrição do produto: "))
    preco = (input("Digite o preço do produto: "))
    estoque = (input("Digite a quantidade do estoque: "))

    return (nome, descricao, preco, estoque)

    # lista com os itens cadastrados ->
itemCadastrado = [cadastrarItem()]


def atualizarItens():
    print('oi')


def consultarItens():
    print(itemCadastrado[0][0])


def detalhesItens():
    print('oi')

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

    
