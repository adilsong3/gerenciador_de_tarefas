[![author](https://img.shields.io/badge/author-Adilsong-red.svg)](https://www.linkedin.com/in/adilson-gustavo-marcondes-barreto-de-souza-a74b98133/) [![](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/release/python-365/) [![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://perso.crans.org/besson/LICENSE.html)

<h1 align="center">Gerenciador de Tarefas</h1>

<sub>*Graduando em Ciência de Dados na Uninter e Cursando Mestres da Automação*</sub>

Este é um projeto de um Gerenciador de Tarefas desenvolvido em Python.

<h2 align="left">Guia Prático de Como Baixar o Executável</h3>

<h3 align="left">Passo 1: Baixar o Executável</h3>

1. **Acesse o link para download do executável**: [Link para o Executável](https://github.com/adilsong3/gerenciador_de_tarefas/tree/main/executavel). 

2. **Baixe o arquivo executável**: Clique no link e salve o arquivo em um local de sua preferência no seu computador.

<h3 align="left">Passo 2: Executar o Executável</h3>

1. **Navegue até a pasta onde o executável foi salvo**: 
    - Abra o **Explorador de Arquivos** e vá para a pasta onde você baixou o arquivo `gerenciador_de_tarefas.exe`.

2. **Execute o programa**:
   - Clique duas vezes no arquivo `gerenciador_de_tarefas.exe` para iniciar o programa.
   - Certifique que você tem permissão para executar arquivos externos.

---

<h2 align="left">Explicando o Projeto por Dentro</h3>

O projeto está dívidido em 7 principais funções que estão descritas abaixo.

<h3 align="left">Criar e Conectar ao Banco de Dados:</h3>

- Função conecta ao banco tarefas, caso não exista ela cria.

<h3 align="left">Adicionar Novas Tarefas:</h3>

- Função usada para criar novas tarefas, a mesma aceita criar um por vez ou passar mais de uma separado por vírgula.

- Exemplo: Arrumar a Cama, Estudar Python, Ir a Igreja

<h3 align="left">Visualizar Tarefas:</h3>

- Função simples que exibe todas as tarefas criadas até o momento indepente do dia.

<h3 align="left">Alterar Status das Tarefas:</h3>

- Função permite ao usuário alterar o status das tarefas que inicialmente começam com Em Andamento. Porém com essa função o usuário pode escolher mudar para Concluído ou Pausado.

<h3 align="left">Remover Tarefas:</h3>

- Função permite ao usuário remover uma ou mais tarefas, apenas digitando o nome da tarefa separado por virgula.

- Exemplo: Arrumar a Cama, Estudar Python

<h3 align="left">Salvar e Carregar Tarefas:</h3>

- Função permite ao usuário salvar todas as tarefas criadas em um banco de dados persistente, ou seja, se no dia seguinte quiser ver as tarefas em andamento é possível.

<h3 align="left">Principal (Main):</h3>

- Função que executa as demais funções com base na iteração do usuário com o terminal.

---

<h3 align="left">Imagem do Menu Principal:</h3>

![Exemplo da Interface do Gerenciador de Tarefas](menu_principal.png)