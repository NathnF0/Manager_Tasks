# ⚡ DIRECT TASKS : CORE SYSTEM

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Terminal](https://img.shields.io/badge/CLI-Terminal-000?style=for-the-badge&logo=gnumetadata&logoColor=white)

**Direct Tasks** é um gerenciador de tarefas via terminal (CLI) desenvolvido para alta performance e organização modular. Esqueça interfaces pesadas; aqui o foco é **velocidade, diretrizes claras e controle total.**

---

## 🖥️ INTERFACE OPERACIONAL

O sistema conta com um dashboard dinâmico que oferece:
* **Barra de Progresso Visual:** Acompanhe sua produtividade em tempo real.
* **Priorização por Cores:** Identifique o que é crítico instantaneamente.
* **Filtros Avançados:** Alterne entre tarefas pendentes, concluídas ou visão geral.
* **Logs de Feedback:** Confirmações de ações e alertas de falhas críticas.

---

## 🛠️ ARQUITETURA DO PROJETO

O núcleo do sistema é dividido em três pilares fundamentais:

| Módulo | Função |
| :--- | :--- |
| **`main.py`** | Controlador central, gerencia o loop de eventos e comandos. |
| **`interface.py`** | Engine visual, cuida das cores, molduras e barras de progresso. |
| **`manager.py`** | Cérebro lógico, processa dados, usuários e persistência em JSON. |

---

## 🚀 COMO EXECUTAR

1. **Requisitos:** Certifique-se de ter o Python 3.x instalado.
2. **Clone o repositório:**
   ```bash
   git clone [https://github.com/NathnF0/Manager_Tasks.git](https://github.com/NathnF0/Manager_Tasks.git)
3. Inicie o Núcleo:

Bash
python main.py
📑 DIRETRIZES DE COMANDO
Dentro do terminal, utilize os atalhos rápidos:

(A) Add: Registra uma nova diretriz no banco.

(C) Concluir: Alterna o status de conclusão de uma tarefa.

(D) Deletar: Remove um registro permanentemente.

(F) Filtro: Muda a perspectiva de visualização.

`(S)air**: Encerra a sessão atual do operador.

🛡️ SEGURANÇA E DADOS
Os dados são persistidos de forma estruturada no arquivo tasks.json. Cada operador possui seu próprio espaço isolado, garantindo que suas tarefas não se misturem com as de outros perfis registrados no mesmo sistema.

---
## 👤 AUTOR

<table align="left">
  <tr>
    <td align="center">
      <a href="https://github.com/NathnF0">
        <img src="https://github.com/NathnF0.png" width="100px;" alt="Galaxy Profile Picture"/><br />
        <sub><b>Nathn (NathnF0)</b></sub>
      </a>
    </td>
    <td>
      <b>Desenvolvedor Principal</b><br>
      Responsável pela arquitetura do sistema, engine de interface e lógica de persistência de dados.
    </td>
  </tr>
</table>
