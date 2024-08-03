# Bibliotecas utilizadas
import pandas as pd
import os
from datetime import datetime
from menu import menu_de_opcoes
import sqlite3
from time import sleep
from log import *

# variavel global temporaria
df_global = None

class GerenciadorTarefas:
    # função para iniciar o programa
    def __init__(self) -> None:
        self.main()

    # Criar conexão no banco de dados
    def criar_conectar_banco(self):
        conexao = sqlite3.connect('tarefas.db')
        cursor = conexao.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT NOT NULL,
            tarefa TEXT NOT NULL,
            status TEXT NOT NULL
        )
        ''')
        conexao.commit()
        return conexao

    # Adicionar Tarefas:
    def adicionar_tarefas(self):
        global df_global

        conexao = self.criar_conectar_banco()
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
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f'Tarefas Adicionadas com Sucesso: \n{nova_tarefa}')
            else:
                novas_tarefas_df = pd.DataFrame({
                    'data': [hoje],
                    'tarefa': [nova_tarefa],
                    'status': [status]
                })
                df_global = pd.concat([df_global, novas_tarefas_df], ignore_index=True)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'Tarefa Adicionada com Sucesso: \n{nova_tarefa}')
        
        conexao.close()

    # Visualizar Tarefas
    def visualizar_tarefas(self):
        global df_global

        if df_global.empty:
            print('Não há tarefas em andamento')
        else:
            print(menu_de_opcoes()[2])
            print(df_global)
            print('#############################################')
        while True:
            escolha = input('Digite "sair" para voltar ao menu: ').strip()
            if escolha.lower() == 'sair' or escolha.lower() == '"sair"':
                break
    
    # Apresentar a resposta da função de alterar status
    def apresentar_resposta_da_funcao_status(self, tarefa, encontrado):
        if encontrado == 'sim':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'Status da Tarefa {tarefa} alterado com sucesso')
            print(menu_de_opcoes()[2])
            print(df_global)
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'Tarefa {tarefa} não encontrada.')
            print(menu_de_opcoes()[2])
            print(df_global)

    # Alterar status das tarefas
    def alterar_status_tarefas(self):
        global df_global

        df_comparacao = df_global.copy()
        df_comparacao['tarefa'] = df_comparacao['tarefa'].str.lower()

        if len(df_global) == 0:
            print('Não há tarefas em andamento')
        else:
            print('--- Tarefas Disponíveis Para Alterar o Status ---')
            print(df_global)
        while True:
            print(menu_de_opcoes()[3])
            print('#############################################')
            escolha = input('Digite o nome da tarefa: ').strip()
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
                                self.apresentar_resposta_da_funcao_status(tarefa_encontrada, 'sim')
                            if tarefa_nao_encontrada:
                                self.apresentar_resposta_da_funcao_status(tarefa_nao_encontrada, 'nao')
                        else:
                            if escolha.lower() not in df_global['tarefa'].str.lower().tolist():
                                self.apresentar_resposta_da_funcao_status(escolha, 'nao')
                            else: 
                                df_global.loc[df_comparacao['tarefa'] == escolha, 'status'] = novo_status
                                self.apresentar_resposta_da_funcao_status(escolha, 'sim')
                        break
                    else:
                        print('Status não aceito, tente novamente!')

    # Remover Tarefas
    def remover_tarefas(self):
        global df_global

        df_comparacao = df_global.copy()
        df_comparacao['tarefa'] = df_comparacao['tarefa'].str.lower()

        if len(df_global) == 0:
            print('Não há tarefas em andamento')
        else:
            print('--- Tarefas Disponíveis Para Remover ---')
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

    # Salvar e Carregar Tarefas
    def salvar_e_carregar_tarefas(self):
        global df_global
        conn = self.criar_conectar_banco()
        print("Salvando dados no banco...")
        loading_bar(5)
        try:
            df_global.to_sql('tarefas', conn, if_exists='replace', index=False)
            print("Dados salvos no banco de dados com sucesso.")
            sleep(2)
            print('Redirecionando ao Menu Principal')
            sleep(2)
        except Exception as e:
            print(f"Erro ao salvar no banco de dados: {e}")
        finally:
            conn.close()

    # Função principal que chama todas as outras
    def main(self):
        global df_global
        resetar_cor = '\033[0m'
        conexao = self.criar_conectar_banco()
        if df_global is None:
            df_global = pd.read_sql_query('SELECT * FROM tarefas', conexao)
        menu = menu_de_opcoes()[0]
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(menu)
            escolha = str(input(f'Digite a opção da sua escolha (\033[94m1{resetar_cor},\033[92m2{resetar_cor},\033[91m3{resetar_cor},\033[93m4{resetar_cor},\033[95m5{resetar_cor} ou \033[96m6{resetar_cor}): ')).strip()
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
                os.system('cls' if os.name == 'nt' else 'clear')
                self.salvar_e_carregar_tarefas()

            elif escolha == '6':
                os.system('cls' if os.name == 'nt' else 'clear')
                self.salvar_e_carregar_tarefas()
                print('Programa Finalizado com Sucesso!')
                break
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Opção inválida, tente novamente!!!\n')
                pass
        
gerenciador = GerenciadorTarefas()