import os

class Cores:
    # Cores Vibrantes
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    VERMELHO = '\033[91m'
    AZUL = '\033[94m'
    CIANO = '\033[96m'
    MAGENTA = '\033[95m'
    BRANCO = '\033[97m'
    
    # Estilos
    RESET = '\033[0m'
    NEGRITO = '\033[1m'
    SUBRINHADO = '\033[4m'
    INVERSO = '\033[7m'

def exibir_cabecalho(titulo, usuario=None):
    """
    Gera um cabeçalho elegante e centralizado com moldura dupla.
    """
    largura = 60
    # Limpa a tela para o cabeçalho ser sempre o topo
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(f"{Cores.CIANO}╔" + "═" * (largura - 2) + "╗")
    
    # Centraliza o título
    espacos_titulo = (largura - 2 - len(titulo)) // 2
    print(f"║" + " " * espacos_titulo + f"{Cores.NEGRITO}{titulo.upper()}{Cores.RESET}{Cores.CIANO}" + " " * (largura - 2 - espacos_titulo - len(titulo)) + "║")
    
    # Se houver usuário, exibe uma linha secundária
    if usuario:
        sub = f"Sessão Ativa: {usuario}"
        espacos_sub = (largura - 2 - len(sub)) // 2
        print(f"║" + " " * espacos_sub + f"{Cores.AZUL}{sub}{Cores.RESET}{Cores.CIANO}" + " " * (largura - 2 - espacos_sub - len(sub)) + "║")
    
    # CORREÇÃO: Removi o {Cores.RESET} de dentro da string e coloquei como expressão f-string real
    print(f"╚" + "═" * (largura - 2) + f"╝{Cores.RESET}\n")

def exibir_barra_progresso(atual, total):
    """
    Uma barra de progresso visual para o Dashboard.
    Nomeada exatamente como o main.py solicita.
    """
    if total == 0:
        print(f" Progresso: [{Cores.AZUL}░░░░░░░░░░░░░░░░░░░░{Cores.RESET}] 0%")
        return
        
    largura_barra = 20
    progresso = int((atual / total) * largura_barra)
    barra = f"{Cores.VERDE}█{Cores.RESET}" * progresso + f"{Cores.AZUL}░{Cores.RESET}" * (largura_barra - progresso)
    porcentagem = (atual / total) * 100
    print(f" Progresso: [{barra}] {porcentagem:.0f}%")