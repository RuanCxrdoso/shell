import os
import sys

def shell_print(mensagem):
    os.write(1, mensagem.encode('utf-8'))

def shell_read():
    try:
        entrada_bytes = os.read(0, 1024)
        
        if not entrada_bytes:
            return ""
            
        entrada_str = entrada_bytes.decode('utf-8').strip()
        return entrada_str
    except OSError as e:
        shell_print(f"Erro ao ler entrada: {e}\n")
        return ""

# --- LÓGICA DO SHELL ---

def ler_e_analisar_comando():
    shell_print("> ")
    
    comando_bruto = shell_read()
    
    if not comando_bruto:
        return []
    
    argumentos = comando_bruto.split()
    return argumentos

def executar_comando(args):
    if args[0] == "exit":
        shell_print("Encerrando o shell...\n")
        sys.exit(0)

    pid = os.fork()

    if pid < 0:
        shell_print("Erro ao criar processo filho (fork falhou).\n")
        
    elif pid == 0:
        try:
            os.execvp(args[0], args)
        except OSError:
            shell_print(f"Erro: comando '{args[0]}' não encontrado.\n")

            os._exit(1)

    else:
        pid_filho, status = os.wait()

# --- LOOP PRINCIPAL ---

def main():
    shell_print("--- Shell - SO ---\n")
    shell_print("Digite 'exit' para sair.\n")

    while True:
        try:
            args = ler_e_analisar_comando()

            if not args:
                continue
                
            executar_comando(args)
            
        except KeyboardInterrupt:
            shell_print("\nPara sair, digite 'exit'.\n")

if __name__ == "__main__":
    main()