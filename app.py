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

import pandas as pd
import os
from datetime import datetime
from menu import menu_de_opcoes

df_global = pd.DataFrame(columns=['data', 'tarefa', 'status'])

class GerenciadorTarefas:
    def __init__(self) -> None:
        self.main()

    # 2. Adicionar Tarefas:
    def adicionar_tarefas(self):
        global df_global
        hoje = datetime.now().strftime('%Y-%m-%d')  # Formata a data como 'YYYY-MM-DD'
        status = 'Em andamento'

        while True:
            print(menu_de_opcoes()[1])
            nova_tarefa = input('Digite o nome da tarefa: ').strip()
            if nova_tarefa.lower() == 'sair' or nova_tarefa.lower() == '"sair"':
                break
            elif ',' in nova_tarefa:
                tarefas = nova_tarefa.split(',')
                novas_tarefas_df = pd.DataFrame({
                    'data': [hoje] * len(tarefas),
                    'tarefa': [t.strip() for t in tarefas],
                    'status': [status] * len(tarefas)
                })
                df_global = pd.concat([df_global, novas_tarefas_df], ignore_index=True)
                print(f'\nTarefas Adicionadas com Sucesso: \n{nova_tarefa}')
            else:
                novas_tarefas_df = pd.DataFrame({
                    'data': [hoje],
                    'tarefa': [nova_tarefa],
                    'status': [status]
                })
                df_global = pd.concat([df_global, novas_tarefas_df], ignore_index=True)
            print(f'\nTarefa Adicionada com Sucesso: \n{nova_tarefa}')

            

    # 3. Visualizar Tarefas:
    def visualizar_tarefas(self):
        global df_global
        
        if len(df_global) == 0:
            print('Não há tarefas em andamento')
        else:
            print(menu_de_opcoes()[2])
            print(df_global)
            print('############################################################')
        while True:
            escolha = input('Digite "sair" para voltar ao menu: ').strip()
            if escolha.lower() == 'sair' or escolha.lower() == '"sair"':
                break


    # 4. Marcar Tarefas como Concluídas:
    def alterar_status_tarefas(self):
        global df_global

        df_comparacao = df_global.copy()
        df_comparacao['tarefa'] = df_comparacao['tarefa'].str.lower()

        if len(df_global) == 0:
            print('Não há tarefas em andamento')
        else:
            print(menu_de_opcoes()[2])
            print(df_global)
        while True:
            print(menu_de_opcoes()[3])
            escolha = input('Digite o nome da tarefa: ').strip()
            os.system('cls' if os.name == 'nt' else 'clear')
            if escolha.lower() == 'sair' or escolha.lower() == '"sair"':
                break
            else:
                while True:
                    novo_status = input('Digite o novo status das tarefas: ').strip()
                    if novo_status.lower() in ('concluido','pausado'):
                        if ',' in escolha:
                            tarefa_escolhida = escolha.split(',')
                            tarefa_escolhida = [tarefa.strip() for tarefa in tarefa_escolhida]
                            tarefa_nao_encontrada = []
                            tarefa_encontrada = []
                            for tarefa in tarefa_escolhida:
                                if tarefa not in df_global['tarefa'].str.lower().tolist():
                                    tarefa_nao_encontrada.append(tarefa)
                                else:
                                    tarefa_encontrada.append(tarefa)

                            if tarefa_encontrada:
                                df_global.loc[df_comparacao['tarefa'].isin(tarefa_encontrada), 'status'] = novo_status
                                print(f'Status da Tarefa {tarefa_encontrada} alterado com sucesso')
                            if tarefa_nao_encontrada:
                                print(f'Tarefa {tarefa_nao_encontrada} não encontrada.')
                        else:
                            if escolha.lower() not in df_global['tarefa'].str.lower().tolist():
                                print(f'Tarefa "{escolha}" não encontrada.\n')
                                print(df_global)
                            else: 
                                df_global.loc[df_comparacao['tarefa'] == escolha, 'status'] = novo_status
                                print(f"Status da Tarefa '{escolha}' alterado com sucesso.")
                        break
                    else:
                        print('Status não aceito, tente novamente!')

    # 5. Remover Tarefas:
    def remover_tarefas(self):
        global df_global

        df_comparacao = df_global.copy()
        df_comparacao['tarefa'] = df_comparacao['tarefa'].str.lower()

        if len(df_global) == 0:
            print('Não há tarefas em andamento')
        else:
            print(menu_de_opcoes()[2])
            print(df_global)
            print(menu_de_opcoes()[4])
        while True:
            escolha = input('Digite o nome da tarefa: ').strip()
            if escolha.lower() == 'sair' or escolha.lower() == '"sair"':
                break
            elif ',' in escolha:
                tarefas_para_remover = escolha.split(',')
                tarefas_para_remover_sem_espacos = [tarefa.strip() for tarefa in tarefas_para_remover]
                tarefa_nao_encontrada = []
                tarefa_encontrada = []

                for tarefa in tarefas_para_remover_sem_espacos:
                    if tarefa not in df_global['tarefa'].str.lower().tolist():
                        tarefa_nao_encontrada.append(tarefa)
                    else:
                        tarefa_encontrada.append(tarefa)
                
                if tarefa_encontrada:
                    # Remove as tarefas especificadas
                    df_global = df_global[~df_comparacao['tarefa'].isin(tarefa_encontrada)]
                    print(f'Tarefa {tarefa_encontrada} removida com sucesso')
                if tarefa_nao_encontrada:
                    print(f'Tarefa {tarefa_nao_encontrada} não encontrada.')
                
            else:
                if escolha.lower() not in df_global['tarefa'].str.lower().tolist():
                    print(f'Tarefa "{escolha}" não encontrada.')
                else: 
                    df_global = df_global[df_comparacao['tarefa'] != escolha.lower()]
                    print(f"Tarefa '{escolha}' removida com sucesso.")


    # 6. Salvar e Carregar Tarefas:
    def salvar_e_carregar_tarefas(self):
        ''

    def main(self):
        global df_global
        menu = menu_de_opcoes()[0]
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
                os.system('cls' if os.name == 'nt' else 'clear')
                self.alterar_status_tarefas()
                
            elif escolha == '4':
                os.system('cls' if os.name == 'nt' else 'clear')
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