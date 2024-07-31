# Funcionalidades que o projeto deve possuir:
# 1. Menu de opções
# ○ Ao inicializar o programa, deve ser exibido um menu de opções com as escolhas
# de o que pode ser feito
# 2. Adicionar Tarefas:
# ○ Permitir ao usuário adicionar uma nova tarefa com uma descrição.
# 3. Visualizar Tarefas:
# ○ Exibir todas as tarefas, indicando quais estão concluídas e quais ainda estão
# pendentes.
# 4. Marcar Tarefas como Concluídas:
# ○ Permitir ao usuário marcar uma tarefa específica como concluída.
# 5. Remover Tarefas:
# ○ Permitir ao usuário remover uma tarefa específica da lista.
# 6. Salvar e Carregar Tarefas:
# ○ Salvar a lista de tarefas em um arquivo para que elas possam ser carregadas na
# próxima execução do programa.
# 7. Ter a Persistência de dados
# ○ Todos os dados que foram inseridos ou modificados pelo usuário devem ser
# persistidos(ou seja, devem ser armazenados em algum local que não irá sumir
# após o programa fechar)
# ○ Recomendo que use um banco de dados SQLite3(por ser o mais simples de
# começar), deixei o link das aulas recomendadas abaixo)
# 8. Ser entregue como um executável
# ○ O programa deve ser entregue como um executável, para que o usuário possa o
# utilizar, sem a necessidade de instalar ferramentas no seu computador.
# 9. (bônus) - Personalização
# ○ Customize

import os
from time import sleep

tarefas_global = []

class GerenciadorTarefas:
    def __init__(self) -> None:
        self.main()

    # 1. Menu de opções
    def menu_de_opcoes(self):
        menu = '''############################################################
  ------------ ESCOLHA UMA DAS OPÇÕES ABAIXO ------------
1 - Adicionar Tarefas (Adicione uma nova tarefa)
2 - Visualizar Tarefas (Visualize todas as tarefas)
3 - Marcar Tarefas (Marcar como concluído alguma tarefa)
4 - Remover Tarefas (Remover tarefa criada)
5 - Salvar Tarefas (Salvar as tarefas em um Banco de Dados)
6 - Fechar Programa (Salva as tarefas e desliga o programa)
############################################################'''

        adicionar_tarefas = ('''---- Para Adicionar uma Nova Tarefa Escreva ela e aperte enter ---
Exemplos: Arrumar a Cama, Estudar Inglês, Ir a Igreja
----> Para sair basta digitar "Sair"''')
        
        visualizar_tarefas = '''--------- Tarefas Em Andamento ---------'''
        return menu, adicionar_tarefas, visualizar_tarefas

    # 2. Adicionar Tarefas:
    def adicionar_tarefas(self):

        while True:
            print(self.menu_de_opcoes()[1])
            nova_tarefa = input('Tarefa: ').strip()
            if nova_tarefa.lower() == 'sair' or nova_tarefa.lower() == '"sair"':
                break
            elif ',' in nova_tarefa:
                tarefas = nova_tarefa.split(',')
                for tarefa in tarefas:
                    tarefas_global.append(tarefa.strip())
            else:
                tarefas_global.append(nova_tarefa)
            print(f'\nTarefas Adicionada com Sucesso!: {tarefas_global}')
            

    # 3. Visualizar Tarefas:
    def visualizar_tarefas(self):
        if len(tarefas_global) == 0:
            print('Não há tarefas em andamento')
        else:
            print(self.menu_de_opcoes()[2])
            for i, tarefa in enumerate(tarefas_global, start=1):
                print(f"Tarefa: {i} {tarefa}")
        while True:
            escolha = input('Digite sair para voltar ao menu principal: ').strip()
            if escolha.lower() == 'sair' or escolha.lower() == '"sair"':
                break


    # 4. Marcar Tarefas como Concluídas:
    def marcar_tarefas(self):
        ''

    # 5. Remover Tarefas:
    def remover_tarefas(self):
        ''

    # 6. Salvar e Carregar Tarefas:
    def salvar_e_carregar_tarefas(self):
        ''

    def main(self):
        menu = self.menu_de_opcoes()[0]
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(menu)
            escolha = str(input('Digite a opção da sua escolha (1,2,3,4,5 ou 6): ')).strip()
            if escolha == '1':
                os.system('cls' if os.name == 'nt' else 'clear')
                self.adicionar_tarefas()
                
            elif escolha == '2':
                os.system('cls' if os.name == 'nt' else 'clear')
                self.visualizar_tarefas()
                
            elif escolha == '3':
                self.marcar_tarefas()
                
            elif escolha == '4':
                self.remover_tarefas()
                
            elif escolha == '5':
                self.salvar_e_carregar_tarefas()

            elif escolha == '6':
                break
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Opção inválida, tente novamente!!!\n')
                pass
        

gerenciador = GerenciadorTarefas()