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

#fução reutilizavel de escolha
def pergunta(val):
    opcao = f"""
    ============= ESCOLHA ===============
    
    [1] \t{val}
    [0] \tSair
    
    => """
    
    return input(opcao)

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

def menuConsultas():
    menu = """
    ================== MENU CONSULTAS ==================
    
    [1] \tExibir Pedidos 
    [2] \tFiltro por Status
    [3] \tRelatório de Vendas
    [0] \tSair

    => """
    return input(menu)

def menuPedidos():
    menu = """
    ================= MENU PEDIDOS =================
    
    [1] \tCriar Pedido 
    [2] \tProcessar Pedidos Pendentes
    [3] \tAtualizar Status de Pedido
    [4] \tCancelar Pedido
    [5] \tConsultas
    [0] \tSair

    => """
    return input(menu)

# FUNÇÃO DE CRIAR CLIENTE ->>>

clientes = []
def criarCliente():
    if clientes:
        print("\nEscolha o usuário\n")
        for i, cliente in enumerate(clientes):
            print(f"[{i}] - {cliente}")
        print(f"[{len(clientes)}] - Criar novo cliente")  # opção extra

        try:
            opcao = int(input("\n>>: "))
        except ValueError:
            print("Digite um número válido!")
            return

        # Se escolheu cliente existente
        if 0 <= opcao < len(clientes):
            print(f"Bem-vindo {clientes[opcao]}!")
        
        # Se escolheu criar novo
        elif opcao == len(clientes):
            nome = input("Digite seu nome de usuário: ")
            clientes.append(nome)
            print(f"Bem-vindo {nome}!")
        
        else:
            print("Opção inválida!")

    else:
        print("\nAinda não existem clientes cadastrados.")
        menu = pergunta("Criar cliente")
        while True:
            match menu:
                case '1':
                    nome = input("\nDigite seu nome de usuário: ")
                    clientes.append(nome)
                    print(f"Bem vindo {clientes[0]}!")
                    return
                case '0':
                    return
                case _:
                        print("Opção inválida")

# FUNÇÕES DE MENU ITENS ->>>

def novoItem():
    while True:
        print("\nEscolha o próximo passo\n")
        print("[1] - Cadastrar novo produto.")
        print("[2] - Listar produtos cadastrados.")
        print("[0] - Voltar ao menu de itens.")
        
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
            case "0":
                print("\nRetornando ao menu de itens...\n")
                break
            case _:
                print("Opção inválida. Tente novamente.")
            
def cadastrarItem():
    nome = input("Digite o nome do produto: ")
    descricao = (input("Digite a descrição do produto: "))
    while True:
        try:
            preco = float(input("Digite o preço do produto (use '.' para decimais): "))
            break
        except ValueError:
            print("Digite o valor usando '.'(ponto)")
            continue
    estoque = int(input("Digite a quantidade do estoque: "))
    
    numero = int(uuid.uuid4().int %100000)
    codigo = f"PRO{numero:04d}"
    
    item = [nome, descricao, codigo, preco, estoque]  # <-- lista
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
        indice = int(input("\nDigite o número do item que será atualizado: "))
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
    itemCadastrado[indice]= [nome_atual, descricao_atual, codigo, preco_atual, estoque_atual]

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
            print(f"Preço: R$ {item[3]:.2f}")
            print(f"Estoque: {item[4]}\n")           
    else:
        print("\nNenhum item cadastrado.")
            

# FUNÇÕES DE MENU PEDIDOS ->>>


pedidosPendentes = []

def criarPedido():
    if itemCadastrado:
        consultarItens()
        pedido_usuario = {
            "id_pedido": str(uuid.uuid4()) [:6],
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
                # verifica o estoque
                if itemCadastrado[indice][4] > 0:
                    # decrementa do estoque
                    itemCadastrado[indice][4] -= 1
                    pedido = {
                        "nome": itemCadastrado[indice][0],
                        "codigo": itemCadastrado[indice][2],
                        "preco": itemCadastrado[indice][3],
                    }
                    pedido_usuario["produtos"].append(pedido)

                    print("\nSua lista atual de pedidos:")
                    for p in pedido_usuario["produtos"]:
                        print(f"- {p['nome']}")
                        
                    controle = True
                    while controle == True:
        
                        match pergunta("Adicionar mais produtos"):
                            case '1':
                                consultarItens()
                                controle = False
                            case '0':
                                qtd_produto = False
                                controle = False 
                            case _:
                                print("\nOpção inválida")
                else:
                    print(f"\n{itemCadastrado[indice][0]} está sem estoque.")
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
        else:
            print("\nNenhum produto adicionado, pedido não criado.")
    else:
        print("\nNenhum produto no sistema.")

filaPreparo = []

filaRejeitados = []

def ProcessarPedidos():
    if pedidosPendentes:
        while pedidosPendentes:
            pedido = pedidosPendentes[0]
            print("\n===== Pedido pendente =====")
            print(f"Código do pedido - {pedido['id_pedido']} (Status: {pedido['status']})")
            for produto in pedido['produtos']:
                print(f"   - {produto['nome']} (id: {produto['codigo']})")
            print(f"\n===== Pedido {pedido['produtos'][0]['codigo']} =====")
            print("[1] Aceitar (pagamento)")
            print("[2] Rejeitar")
            print("[0] Sair")
            opcao = input("\n>>: ")

            if opcao == '1':
                valor_total = 0
                for produto in pedido['produtos']:
                    valor_total = valor_total + produto['preco']
                valor_final_pago = valor_total
                while True:
                    try:
                        cupom = input("Deseja utilizar o cupom de desconto do dia?[s ou n]: ").lower()
                        break
                    except ValueError:
                        print("Digite 's' para sim, ou 'n' para não.")
                        continue
                if(cupom == 's'):
                    desconto = valor_total/10
                    valor_final_pago = valor_total - desconto
                    print(f"\nValor total pago: {valor_final_pago:.2f}")
                else:
                    print(f"\nValor total pago: {valor_total:.2f}")
                    valor_final_pago = valor_total
                pedido['valor_final_pago'] = valor_final_pago
                pedido['status'] = "Aceito"
                linha = pedidosPendentes.pop(0)
                filaPreparo.append(linha)
                print(f"\nPedido " + pedido['id_pedido'] + " aceito!")
            elif opcao == '2':
                pedido['status'] = "Rejeitado"
                linha = pedidosPendentes.pop(0)
                filaRejeitados.append(linha)
                print("\nPedido cancelado!")
            elif opcao == '0':
                return
            else:
                print("\nOpção inválida")
    else:
        print("\nNenhum pedido novo no sistema.")

def atualizarStatusPedido():
    fluxoStatus = [
        'Em preparo',
        'Pedido pronto!',
        'Aguardando o entregador!',
        'Seu pedido saiu para entrega!',
        'Pedido entregue!'
    ]
    print("\nPEDIDOS EM PROCESSO: \n")
    for pedido in (filaPreparo):
        print(f"ID do Pedido - {pedido['id_pedido']} (Status: {pedido['status']})")
        for produto in pedido['produtos']:
            print(f"   - {produto['nome']}")
        print("______________________________________________")

    if not filaPreparo:
        print("NENHUM PEDIDO A SER ATUALIZADO!")
        return
# Nesse input, o usuário deve escrever o ID gerado para o pedido        
    numeroPedido = (input(f"Nº ID do pedido que deseja atualizar: "))    
    for pedido in filaPreparo:
        if pedido['id_pedido'] == numeroPedido:
            print(f"\nPedido encontrado!")
            print(f"id_pedido: {pedido['id_pedido']}")
            # print("ITENS ADICIONADOS:\n" + pedido['produtos'] [0] ['nome'])
            
            if pedido['status'] in fluxoStatus:
                indice = fluxoStatus.index(pedido['status'])
                if indice < len(fluxoStatus) - 1:
                    pedido['status'] = fluxoStatus[indice + 1]
                else:
                    print("\nEste pedido já foi atualizado!")
                    return
            else:
                pedido['status'] = fluxoStatus [0]
                
            print(f"Status do pedido {pedido['id_pedido']} atualizado para: {pedido['status']}")
            return
        else:
            print("\nPedido não encontrado!")
    
filaCancelados =[]
def cancelarPedido():
    global pedidosPendentes, filaPreparo, filaCancelados
    # montando a lista de pedidos canceláveis
    cancelaveis = []
    for nome_lista, lista_pedidos in [("Pendentes", pedidosPendentes), ("Fila de Preparo", filaPreparo)]:
        for pedido in lista_pedidos:
            status = pedido.get("status", "")
            if status in ("Aguardando Aprovação", "Aceito"):
                cancelaveis.append((nome_lista, pedido))
    # se nao tiver nenhum pedido cancelável vai avisar e sair 
    if not cancelaveis:
            print("\nNão há pedidos canceláveis no momento.")
            return
    # mostrando os pedidos que podem ser cancelados 
    print("\n====== Pedidos Canceláveis ======")
    for i, (nome_lista, pedido) in enumerate(cancelaveis):
        nomes_produtos = ", ".join([produto['nome'] for produto in pedido['produtos']])
        print(f"[{i}] {nomes_produtos} | Status: {pedido['status']}")
    # lendo a escolha do usuário 
    try: 
        escolha = int(input("\nDigite o número do pedido para cancelar: "))
        nome_lista, pedido = cancelaveis[escolha]
    except (ValueError, IndexError):
        print("Opção inválida.")
        return
    # removendo pedido das listas originais 
    if pedido in pedidosPendentes:
        pedidosPendentes.remove(pedido)
    elif pedido in filaPreparo:
        filaPreparo.remove(pedido)
    # marcando como cancelado 
    pedido["status"] = "Cancelado"
    filaCancelados.append(pedido)
    print("\nPedido cancelado com sucesso!")

def exibirPedidos():
    print("oi")
def filtroStatus():
    print("oi")

def relatorioVendas():
    totalFaturamento = 0
    for pedido in filaPreparo:
        if pedido['status'] in ("Aceito", "Em preparo", "Pedido pronto!", "Aguardando o entregador!", "Seu pedido saiu para entrega!", "Pedido entregue!"):
            totalFaturamento += pedido['valor_final_pago']
    print("\n===== RELATÓRIO DE FATURAMENTO =====")
    print(f"\nFaturamento total: R$ {totalFaturamento:.2f}")

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
                        criarCliente()
                        criarPedido()
                    case '2':
                        criarCliente()
                        ProcessarPedidos()
                    case '3':
                        criarCliente()
                        atualizarStatusPedido()
                    case '4':
                        criarCliente()
                        cancelarPedido()
                    case '5':
                        criarCliente()
                        print(filaPreparo)
                        while True:
                            escolha = menuConsultas()
                            match escolha:
                                case '1':
                                    exibirPedidos()
                                case '2':
                                    filtroStatus()
                                case'3':
                                    relatorioVendas()
                                case '0':
                                    break
                                case _:
                                    print("Opção inválida")
                    case '0':
                        break
                    case _:
                        print("Opção inválida")
        case '0':
            controle = False
        case _:
            print("Opção inválida")
