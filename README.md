# Projeto Integrador - Mini Shell com Chamadas ao Sistema

**Universidade Federal da Bahia (UFBA) - Instituto de Computação**
**Disciplina:** Sistemas Operacionais
**Docente:** Prof. Dra. Larissa Barbosa Leôncio Pinheiro
**Alunos:** Ruan Cardoso dos Santos, Edilton Damasceno, Erlan Carvalho

---

## 📝 Descrição do Projeto
Este projeto consiste no desenvolvimento de um **Mini Shell** (interpretador de comandos) em Python. O objetivo principal é simular a execução de comandos em um terminal Linux, explorando conceitos fundamentais de sistemas operacionais como criação de processos e manipulação de entrada/saída de baixo nível.

O shell opera em um ciclo REPL (Read-Eval-Print Loop), exibindo um prompt, lendo comandos do usuário e executando-os através de chamadas ao sistema (system calls) diretas ao Kernel.

---

## 🚀 Como Compilar e Rodar

### Pré-requisitos
* **Sistema Operacional:** Linux (ou WSL no Windows).
* **Linguagem:** Python 3 instalado.

### Compilação
Como o projeto foi desenvolvido em **Python** (uma linguagem interpretada), **não é necessário realizar compilação** prévia do código fonte. O interpretador Python lê e executa o código diretamente.

### Execução
Para iniciar o Mini Shell, abra o terminal na pasta onde o arquivo foi salvo e execute o comando:

```bash
python3 shell.py
````

Para encerrar a execução do shell, digite o comando `exit` ou pressione `Ctrl+C`.

-----

## ⚙️ Chamadas ao Sistema Utilizadas

Para realizar a comunicação direta com o Kernel do Linux, utilizamos a biblioteca nativa `os`, que serve como *wrapper* para as seguintes System Calls:

1.  **`fork()`**: Utilizada para clonar o processo atual (Shell Pai). É a base da multiprogramação neste projeto, criando um processo Filho idêntico ao Pai para executar a tarefa solicitada.
2.  **`execvp()`**: Chamada dentro do processo Filho. Ela substitui a imagem de memória do processo Python pelo código do programa digitado pelo usuário (ex: substitui o script pelo binário do `ls`), preservando os argumentos passados.
3.  **`wait()`**: Utilizada pelo processo Pai. Faz com que o Shell suspenda sua execução (fique bloqueado) até que o processo Filho termine, garantindo que o prompt `>` só reapareça após o fim do comando.
4.  **`read()`**: Utilizada para ler a entrada do usuário diretamente do descritor de arquivo padrão (stdin / fd 0), capturando bytes brutos do teclado.
5.  **`write()`**: Utilizada para escrever bytes diretamente na saída padrão (stdout / fd 1), usada para exibir o prompt e mensagens de erro.
6.  **`_exit()`**: Utilizada em caso de erro no processo Filho (ex: comando não encontrado), garantindo que o clone seja destruído imediatamente sem interferir no processo Pai.

-----

## 💻 Exemplos de Comandos Testados

Abaixo estão os cenários de teste realizados para validar o funcionamento do Shell:

### 1\. Listagem de Diretórios (`ls`)

Verifica a capacidade de executar programas externos e passar argumentos.

  * **Comando:** `ls -la`
  * **Saída:** Exibe a lista completa de arquivos do diretório atual, incluindo permissões, datas e arquivos ocultos.

### 2\. Exibição de Mensagens (`echo`)

Verifica o tratamento de strings e argumentos múltiplos.

  * **Comando:** `echo Ola Mundo UFBA`
  * **Saída:** `Ola Mundo UFBA`

### 3\. Leitura de Arquivo (`cat`)

Verifica a interação com o sistema de arquivos.

  * **Comando:** `cat README.md`
  * **Saída:** Exibe o conteúdo de texto deste arquivo no terminal.

### 4\. Tratamento de Erro (Comando Inválido)

Verifica se o shell sobrevive a erros de execução.

  * **Comando:** `comando_que_nao_existe`
  * **Saída:** `Erro: comando 'comando_que_nao_existe' não encontrado.` (O shell retorna ao prompt `>` logo em seguida).

-----

## ⚠️ Limitações Conhecidas da Implementação

Devido ao escopo acadêmico e simplificado do projeto, existem as seguintes limitações em relação a um shell comercial (como Bash ou Zsh):

1.  **Navegação de Diretórios (`cd`):** O comando `cd` não persiste. Como os comandos rodam em um processo Filho, ao executar `cd pasta`, apenas o Filho muda de diretório e encerra. O Pai (o Shell em si) permanece no diretório original.
2.  **Histórico de Comandos:** Não há suporte para navegar pelos comandos anteriores usando as setas do teclado (Cima/Baixo), pois a leitura é feita byte a byte via `os.read`.
3.  **Redirecionamento e Pipes:** Não foram implementados os operadores de redirecionamento (`>`, `<`) ou pipes (`|`) para encadear a saída de um comando na entrada de outro.
4.  **Autocompletar:** A tecla `TAB` não completa nomes de arquivos ou comandos.
