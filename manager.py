import json
import os

class TaskManager:
    def __init__(self):
        # Nome do arquivo onde os dados serão persistidos
        self.arquivo_dados = "data.json"
        self.usuario_logado = None
        # Estrutura inicial do banco de dados
        self.dados = self.carregar_dados()

    def carregar_dados(self):
        """Carrega os dados do arquivo JSON ou cria uma estrutura nova."""
        if os.path.exists(self.arquivo_dados):
            try:
                with open(self.arquivo_dados, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except (json.JSONDecodeError, Exception):
                # Se o arquivo estiver corrompido, inicia um novo
                return {"usuarios": {}}
        return {"usuarios": {}}

    def salvar(self):
        """Salva o estado atual dos dados no arquivo JSON."""
        try:
            with open(self.arquivo_dados, 'w', encoding='utf-8') as f:
                json.dump(self.dados, f, indent=4, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Erro ao salvar dados: {e}")
            return False

    def criar_usuario(self, nome):
        """Cria um novo perfil de usuário se ele não existir."""
        nome = nome.strip()
        if not nome:
            return False
        
        if nome not in self.dados["usuarios"]:
            self.dados["usuarios"][nome] = {
                "data_criacao": str(os.times()),
                "tarefas": []
            }
            self.salvar()
            return True
        return False

    def login(self, nome):
        """Realiza o login se o usuário existir no sistema."""
        nome = nome.strip()
        if nome in self.dados["usuarios"]:
            self.usuario_logado = nome
            return True
        return False

    def logout(self):
        """Desloga o usuário atual."""
        self.usuario_logado = None

    def adicionar_tarefa(self, nome_tarefa, data_tarefa, prioridade="MÉDIA", categoria="Geral"):
        """
        Adiciona tarefa com suporte a prioridade e categoria.
        """
        if self.usuario_logado:
            nova_tarefa = {
                "nome": nome_tarefa,
                "feito": False,
                "data": data_tarefa,
                "prioridade": prioridade,
                "categoria": categoria
            }
            self.dados["usuarios"][self.usuario_logado]["tarefas"].append(nova_tarefa)
            self.salvar()
            return True
        return False

    def remover_tarefa(self, tarefa_obj):
        """
        Remove uma tarefa específica da lista do usuário logado.
        """
        if self.usuario_logado:
            try:
                self.dados["usuarios"][self.usuario_logado]["tarefas"].remove(tarefa_obj)
                self.salvar()
                return True
            except ValueError:
                return False
        return False