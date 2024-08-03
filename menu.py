cores = {
    'azul': '\033[94m',
    'verde': '\033[92m',
    'vermelho': '\033[91m',
    'amarelo': '\033[93m',
    'magenta': '\033[95m',
    'ciano': '\033[96m',
    'resetar': '\033[0m'
}

def menu_de_opcoes():
        menu = f'''############################################################
  ------------ ESCOLHA UMA DAS OPÇÕES ABAIXO ------------
{cores['azul']}1 - Adicionar Tarefas (Adicione uma nova tarefa){cores['resetar']}
{cores['verde']}2 - Visualizar Tarefas (Visualize todas as tarefas){cores['resetar']}
{cores['amarelo']}3 - Marcar Tarefas (Alterar o status das tarefas){cores['resetar']}
{cores['vermelho']}4 - Remover Tarefas (Remover tarefas criadas){cores['resetar']}
{cores['magenta']}5 - Salvar Tarefas (Salvar as tarefas em um Banco de Dados){cores['resetar']}
{cores['ciano']}6 - Fechar Programa (Salvar as tarefas e desligar o programa){cores['resetar']}
############################################################'''

        adicionar_tarefas = (f'''############################################################
{cores['azul']}--- Menu Para Adicionar uma Nova Tarefa ---{cores['resetar']} 
Para Adicionar uma Nova Tarefa Escreva ela e aperte enter.
Exemplos: Arrumar a Cama, Estudar Inglês, Ir a Igreja
----> Para voltar ao menu basta digite "Sair"
############################################################''')
        
        visualizar_tarefas = f'''#############################################
{cores['verde']}--- Menu Para Apresentar as Tarefas Em Andamento ---{cores['resetar']}'''

        marcar_concluido = f'''\n#############################################
{cores['amarelo']}--- Menu de Alteração dos Status das Tarefas ---{cores['resetar']}
Para alterar o status de uma tarefa, basta digitar uma das opções abaixo:
-> Concluido
-> Pausado
----> Para voltar ao menu basta digite "Sair"'''

        remover_tarefas = f'''\n#############################################
{cores['vermelho']}--- Menu Para Remover Tarefas ---{cores['resetar']} 
Para remover uma tarefa, basta digitar o nome dela e apertar enter.
Exemplos: Estudar Inglês, Estudar Python
----> Para voltar ao menu basta digite "Sair"
#############################################'''

        return menu, adicionar_tarefas, visualizar_tarefas, marcar_concluido, remover_tarefas