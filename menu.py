def menu_de_opcoes():
        menu = '''############################################################
  ------------ ESCOLHA UMA DAS OPÇÕES ABAIXO ------------
1 - Adicionar Tarefas (Adicione uma nova tarefa)
2 - Visualizar Tarefas (Visualize todas as tarefas)
3 - Marcar Tarefas (Marcar como concluído alguma tarefa)
4 - Remover Tarefas (Remover tarefa criada)
5 - Salvar Tarefas (Salvar as tarefas em um Banco de Dados)
6 - Fechar Programa (Salva as tarefas e desliga o programa)
############################################################'''

        adicionar_tarefas = ('''------------------------------------------------------------------
-- Para Adicionar uma Nova Tarefa Escreva ela e aperte enter --
Exemplos: Arrumar a Cama, Estudar Inglês, Ir a Igreja
----> Para voltar ao menu basta digite "Sair"
------------------------------------------------------------------''')
        
        visualizar_tarefas = '''--------- Tarefas Em Andamento ---------'''

        marcar_concluido = ''''''

        remover_tarefas = '''------------------------------------------------------------------
-- Para remover uma tarefa, basta digitar o nome dela e apertar enter --
Exemplos: Estudar Inglês, Estudar Python
----> Para voltar ao menu basta digite "Sair"
------------------------------------------------------------------'''

        return menu, adicionar_tarefas, visualizar_tarefas, marcar_concluido, remover_tarefas