import json
import os

# Configurar caminho do arquivo JSON
pasta = os.path.dirname(os.path.abspath(__file__))
caminho_arquivo = os.path.join(pasta, "tasks.json")

# Dicionário para armazenar todas as tarefas de todos os usuários
dados = {"usuarios": {}}

# Variável para rastrear qual usuário está logado
usuario_logado = None


# ========== FUNÇÕES DE CARREGAMENTO E SALVAMENTO ==========

def dados_iniciais():
    """Retorna dados de demo para primeira execução."""
    return {
        "usuarios": {
            "demo1": [
                {"nome": "Estudar Python", "feito": False},
                {"nome": "Fazer exercício de loop", "feito": True},
                {"nome": "Implementar projeto", "feito": False}
            ],
            "demo2": [
                {"nome": "Ler documentação", "feito": True},
                {"nome": "Praticar funções", "feito": False},
                {"nome": "Review de código", "feito": False}
            ]
        }
    }


def carregar_dados():
    """Carrega os dados do arquivo JSON. Se não existir, cria com dados de demo."""
    global dados
    if not os.path.exists(caminho_arquivo):
        # Se o arquivo não existe, cria com dados de exemplo
        dados = dados_iniciais()
        salvar_dados()
        print("📝 Arquivo criado com usuários de demo: demo1 e demo2")
    else:
        try:
            with open(caminho_arquivo, "r") as arquivo:
                dados = json.load(arquivo)
        except json.JSONDecodeError:
            # Se o arquivo está corrompido, reinicia com dados de demo
            dados = dados_iniciais()
            salvar_dados()
            print("⚠️ Arquivo corrompido. Restaurado com dados de demo.")


def salvar_dados():
    """Salva os dados no arquivo JSON."""
    with open(caminho_arquivo, "w") as arquivo:
        json.dump(dados, arquivo, indent=2)


# ========== FUNÇÕES DE USUÁRIO ==========

def criar_usuario(nome_usuario):
    """Cria um novo usuário no sistema."""
    if nome_usuario in dados["usuarios"]:
        print(f"❌ Usuário '{nome_usuario}' já existe!")
        return False
    else:
        # Cria um novo usuário com lista de tarefas vazia
        dados["usuarios"][nome_usuario] = []
        salvar_dados()
        print(f"✅ Usuário '{nome_usuario}' criado com sucesso!")
        return True


def fazer_login(nome_usuario):
    """Faz login de um usuário existente."""
    if nome_usuario in dados["usuarios"]:
        return True
    else:
        print(f"❌ Usuário '{nome_usuario}' não encontrado.")
        return False


def listar_usuarios():
    """Lista todos os usuários cadastrados."""
    if not dados["usuarios"]:
        print("Nenhum usuário cadastrado.")
        return
    print("\nUsuários cadastrados:")
    for i, usuario in enumerate(dados["usuarios"].keys(), 1):
        total_tarefas = len(dados["usuarios"][usuario])
        print(f"{i}. {usuario} ({total_tarefas} tarefas)")


# ========== FUNÇÕES DE TAREFA ==========

def listar_tarefas(usuario):
    """Lista todas as tarefas do usuário logado."""
    tarefas = dados["usuarios"][usuario]
    if not tarefas:
        print("📋 Você não tem tarefas!")
        return

    print("\n📋 Suas tarefas:")
    for i, tarefa in enumerate(tarefas, 1):
        status = "✅" if tarefa["feito"] else "⏳"
        print(
            f"{i}. {status} {tarefa['nome']} - {'Feito' if tarefa['feito'] else 'Pendente'}")


def adicionar_tarefa(usuario, nome_tarefa):
    """Adiciona uma nova tarefa para o usuário."""
    if not nome_tarefa.strip():
        print("❌ Nome da tarefa não pode ser vazio!")
        return

    # Adiciona tarefa à lista do usuário
    dados["usuarios"][usuario].append({"nome": nome_tarefa, "feito": False})
    salvar_dados()
    print(f"✅ Tarefa '{nome_tarefa}' adicionada com sucesso!")


def marcar_feita(usuario):
    """Marca uma tarefa como feita."""
    tarefas = dados["usuarios"][usuario]

    if not tarefas:
        print("📋 Você não tem tarefas!")
        return

    listar_tarefas(usuario)

    try:
        numero_tarefa = int(
            input("\nDigite o número da tarefa que deseja marcar como feita: "))
        if 0 < numero_tarefa <= len(tarefas):
            tarefas[numero_tarefa - 1]["feito"] = True
            salvar_dados()
            print(
                f"✅ Tarefa '{tarefas[numero_tarefa - 1]['nome']}' marcada como feita!")
        else:
            print("❌ Número de tarefa inválido.")
    except ValueError:
        print("❌ Por favor, digite um número válido.")


def deletar_tarefa(usuario):
    """Deleta uma tarefa do usuário."""
    tarefas = dados["usuarios"][usuario]

    if not tarefas:
        print("📋 Você não tem tarefas!")
        return

    listar_tarefas(usuario)

    try:
        numero_tarefa = int(
            input("\nDigite o número da tarefa que deseja deletar: "))
        if 0 < numero_tarefa <= len(tarefas):
            tarefa_removida = tarefas.pop(numero_tarefa - 1)
            salvar_dados()
            print(
                f"✅ Tarefa '{tarefa_removida['nome']}' deletada com sucesso!")
        else:
            print("❌ Número de tarefa inválido.")
    except ValueError:
        print("❌ Por favor, digite um número válido.")


def editar_tarefa(usuario):
    """Edita o nome de uma tarefa existente."""
    tarefas = dados["usuarios"][usuario]

    if not tarefas:
        print("📋 Você não tem tarefas!")
        return

    listar_tarefas(usuario)

    try:
        numero_tarefa = int(
            input("\nDigite o número da tarefa que deseja editar: "))
        if 0 < numero_tarefa <= len(tarefas):
            novo_nome = input("Digite o novo nome para a tarefa: ").strip()
            if novo_nome:
                tarefas[numero_tarefa - 1]["nome"] = novo_nome
                salvar_dados()
                print(f"✅ Tarefa editada com sucesso para '{novo_nome}'!")
            else:
                print("❌ Nome da tarefa não pode ser vazio!")
        else:
            print("❌ Número de tarefa inválido.")
    except ValueError:
        print("❌ Por favor, digite um número válido.")


# ========== MENU PRINCIPAL ==========

def menu_autenticacao():
    """Menu para login ou cadastro de novo usuário."""
    global usuario_logado

    while True:
        print("\n" + "="*40)
        print("🔐 GERENCIADOR DE TAREFAS - AUTENTICAÇÃO")
        print("="*40)
        print("1. Fazer login")
        print("2. Criar novo usuário")
        print("3. Ver todos os usuários")
        print("4. Sair")
        print()

        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            # Login de usuário existente
            nome_usuario = input("Digite seu nome de usuário: ").strip()
            if fazer_login(nome_usuario):
                usuario_logado = nome_usuario
                print(f"✅ Bem-vindo, {nome_usuario}!")
                return

        elif opcao == "2":
            # Criar novo usuário
            nome_usuario = input("Digite um nome de usuário: ").strip()
            if nome_usuario:
                criar_usuario(nome_usuario)

        elif opcao == "3":
            # Listar todos os usuários
            listar_usuarios()

        elif opcao == "4":
            # Sair do programa
            print("👋 Até mais!")
            exit()

        else:
            print("❌ Opção inválida. Por favor, tente novamente.")


def menu_principal():
    """Menu de tarefas do usuário logado."""
    global usuario_logado

    while True:
        print(f"\n{'='*40}")
        print(f"📝 GERENCIADOR DE TAREFAS - {usuario_logado.upper()}")
        print(f"{'='*40}")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Marcar tarefa como feita")
        print("4. Deletar tarefa")
        print("5. Editar tarefa")
        print("6. Trocar de usuário")
        print("7. Sair")
        print()

        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            nome_tarefa = input("Digite o nome da tarefa: ")
            adicionar_tarefa(usuario_logado, nome_tarefa)

        elif opcao == "2":
            listar_tarefas(usuario_logado)

        elif opcao == "3":
            marcar_feita(usuario_logado)

        elif opcao == "4":
            deletar_tarefa(usuario_logado)

        elif opcao == "5":
            editar_tarefa(usuario_logado)

        elif opcao == "6":
            # Voltar ao menu de autenticação para trocar de usuário
            print("👤 Voltando ao menu de login...")
            return

        elif opcao == "7":
            print("👋 Até mais!")
            exit()

        else:
            print("❌ Opção inválida. Por favor, tente novamente.")


# ========== PROGRAMA PRINCIPAL ==========

# Carregar dados ao iniciar o programa
carregar_dados()

# Loop principal - menu de autenticação e depois menu de tarefas
while True:
    menu_autenticacao()
    menu_principal()
