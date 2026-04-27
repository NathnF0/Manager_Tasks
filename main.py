from manager import TaskManager
from interface import Cores, exibir_cabecalho, exibir_barra_progresso
from datetime import datetime
import os
import time

def renderizar_divisor():
    print(f"{Cores.AZUL}─" * 65 + f"{Cores.RESET}")

def mensagem_sistema(texto, cor=Cores.AMARELO):
    """Exibe um aviso rápido no terminal."""
    print(f"\n {cor}>> {texto}{Cores.RESET}")
    time.sleep(1.2)

def main():
    app = TaskManager()
    filtro_ativo = "todas" 

    while True:
        # --- TELA DE ACESSO ---
        if not app.usuario_logado:
            exibir_cabecalho(" DIRECT TASKS : CORE SYSTEM ")
            
            print(f"\n          {Cores.NEGRITO}{Cores.BRANCO}CONTROLE DE DIRETRIZES E FLUXO{Cores.RESET}")
            print(f"          {Cores.CIANO}Status: {Cores.VERDE}Terminal pronto para entrada.{Cores.RESET}\n")
            
            renderizar_divisor()
            
            opcoes = [
                ("1", "AUTENTICAR", "Acessar terminal de operador"),
                ("2", "CRIAR PERFIL", "Registrar nova credencial no banco"),
                ("3", "BANCO DE DADOS", "Listar usuários ativos no sistema"),
                ("4", "ENCERRAR NÚCLEO", "Finalizar execução do software")
            ]

            for num, titulo, desc in opcoes:
                print(f"  {Cores.AMARELO}[{num}]{Cores.RESET} {Cores.NEGRITO}{titulo:<20}{Cores.RESET} {Cores.AZUL}│{Cores.RESET} {Cores.BRANCO}{desc}{Cores.RESET}")

            renderizar_divisor()
            
            # PROMPT CORRIGIDO: Limpo e sem o "root@system"
            op = input(f"\n{Cores.CIANO} comando > {Cores.RESET}")

            if op == "1":
                nome = input(f"{Cores.AMARELO} Inserir Credencial: {Cores.RESET}").strip()
                if app.login(nome):
                    mensagem_sistema(f"Bem-vindo, {nome}.", Cores.VERDE)
                else:
                    mensagem_sistema("FALHA: Credencial não localizada.", Cores.VERMELHO)
            
            elif op == "2":
                nome = input(f"{Cores.AMARELO} Novo ID de perfil: {Cores.RESET}").strip()
                if app.criar_usuario(nome):
                    mensagem_sistema(f"Usuário '{nome}' registrado.", Cores.VERDE)
                else:
                    mensagem_sistema("FALHA: Nome indisponível.", Cores.VERMELHO)
            
            elif op == "3":
                print(f"\n {Cores.NEGRITO}USUÁRIOS CADASTRADOS:{Cores.RESET}")
                if not app.dados["usuarios"]:
                    print(f"  {Cores.VERMELHO}[BANCO VAZIO]{Cores.RESET}")
                for user in app.dados["usuarios"].keys():
                    print(f"  {Cores.AZUL}# {Cores.RESET}{Cores.CIANO}{user}{Cores.RESET}")
                input(f"\n {Cores.AMARELO}Pressione Enter para voltar...{Cores.RESET}")
            
            elif op == "4":
                print(f"\n{Cores.VERMELHO}Desativando protocolos...{Cores.RESET}")
                break
        
        # --- DASHBOARD LOGADO ---
        else:
            exibir_cabecalho(" DASHBOARD OPERACIONAL ", app.usuario_logado)
            todas_tarefas = app.dados["usuarios"][app.usuario_logado]["tarefas"]
            
            if filtro_ativo == "pendentes":
                tarefas_exibidas = [t for t in todas_tarefas if not t["feito"]]
            elif filtro_ativo == "concluidas":
                tarefas_exibidas = [t for t in todas_tarefas if t["feito"]]
            else:
                tarefas_exibidas = todas_tarefas

            total = len(todas_tarefas)
            concluidas = sum(1 for t in todas_tarefas if t["feito"])
            
            exibir_barra_progresso(concluidas, total)
            print(f" {Cores.BRANCO}VISUALIZAÇÃO: {Cores.MAGENTA}{filtro_ativo.upper()}{Cores.RESET}")
            renderizar_divisor()

            print(f"{Cores.NEGRITO}{'ID':<4} {'PRIORIDADE':<12} {'STATUS':<5} {'TAREFA':<25} {'DATA':<10}{Cores.RESET}")
            renderizar_divisor()

            if not tarefas_exibidas:
                print(f"\n          {Cores.AMARELO}Nenhuma diretriz ativa.{Cores.RESET}\n")
            else:
                for i, t in enumerate(tarefas_exibidas, 1):
                    prio = t.get("prioridade", "MÉDIA")
                    cor_prio = Cores.VERMELHO if prio == "ALTA" else (Cores.AMARELO if prio == "MÉDIA" else Cores.CIANO)
                    status_ic = f"{Cores.VERDE}✔{Cores.RESET}" if t["feito"] else f"{Cores.BRANCO}○{Cores.RESET}"
                    nome_txt = f"{Cores.RESET}{t['nome']}" if t["feito"] else f"{Cores.NEGRITO}{t['nome']}{Cores.RESET}"
                    print(f"{i:<4} {cor_prio}{prio:<12}{Cores.RESET} {status_ic:<5} {nome_txt:<25} {t['data']:<10}")

            renderizar_divisor()
            print(f" {Cores.NEGRITO}AÇÕES:{Cores.RESET}  {Cores.VERDE}(A)dd{Cores.RESET} | {Cores.CIANO}(C)oncluir{Cores.RESET} | {Cores.VERMELHO}(D)eletar{Cores.RESET} | {Cores.MAGENTA}(F)iltro{Cores.RESET} | {Cores.AMARELO}(S)air{Cores.RESET}")
            
            # PROMPT LOGADO CORRIGIDO
            cmd = input(f"\n{Cores.CIANO} {app.usuario_logado} > {Cores.RESET}").lower()

            if cmd == 'a':
                desc = input(f" {Cores.AMARELO}Tarefa: {Cores.RESET}")
                print(f" {Cores.BRANCO}Urgência: {Cores.VERMELHO}1.Alta{Cores.RESET} | {Cores.AMARELO}2.Média{Cores.RESET} | {Cores.CIANO}3.Baixa{Cores.RESET}")
                p_op = input(" Selecione (1-3): ")
                p_map = {"1": "ALTA", "2": "MÉDIA", "3": "BAIXA"}
                if desc:
                    app.adicionar_tarefa(desc, datetime.now().strftime("%d/%m"), p_map.get(p_op, "MÉDIA"))
                    mensagem_sistema("Diretriz registrada.", Cores.VERDE)
            
            elif cmd == 'f':
                print(f"\n {Cores.AZUL}1. Todas | 2. Pendentes | 3. Concluídas{Cores.RESET}")
                f_op = input(" Modo: ")
                filtro_ativo = {"1": "todas", "2": "pendentes", "3": "concluidas"}.get(f_op, "todas")
            
            elif cmd == 'c':
                try:
                    idx = int(input(f" {Cores.CIANO}ID da tarefa: {Cores.RESET}")) - 1
                    tarefas_exibidas[idx]["feito"] = not tarefas_exibidas[idx]["feito"]
                    app.salvar()
                except:
                    mensagem_sistema("Erro: ID inválido.", Cores.VERMELHO)
            
            elif cmd == 'd':
                try:
                    idx = int(input(f" {Cores.VERMELHO}ID para exclusão: {Cores.RESET}")) - 1
                    alvo = tarefas_exibidas[idx]
                    todas_tarefas.remove(alvo)
                    app.salvar()
                    mensagem_sistema("Registro removido.", Cores.VERMELHO)
                except:
                    mensagem_sistema("Erro: Falha na exclusão.", Cores.VERMELHO)
            
            elif cmd == 's':
                app.logout()
                mensagem_sistema("Logout efetuado.", Cores.AZUL)

if __name__ == "__main__":
    main()