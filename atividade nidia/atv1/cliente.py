import socket  # Importa o módulo de sockets para comunicação em rede

HOST = 'localhost'  # Endereço do servidor ao qual o cliente vai se conectar
PORT = 5000         # Porta do servidor, deve ser a mesma definida no servidor.py


def enviar_requisicao(mensagem):
    # Cria um socket TCP/IP e conecta ao servidor
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
        cliente.connect((HOST, PORT))                      # Estabelece a conexão com o servidor
        cliente.sendall(mensagem.encode('utf-8'))          # Envia a mensagem convertida para bytes
        resposta = cliente.recv(1024).decode('utf-8')      # Recebe a resposta do servidor e converte para texto
        return resposta  # Retorna a resposta para quem chamou a função


def menu():
    # Exibe as opções disponíveis para o usuário
    print("\n=== Sistema de Consulta de Notas ===")
    print("1. Consultar nota de aluno")
    print("2. Cadastrar novo aluno")
    print("3. Consultar media da turma")
    print("4. Listar todos os alunos")
    print("5. Sair")
    return input("Escolha uma opcao: ").strip()  # Lê a opção digitada e remove espaços extras


def main():
    print("Bem-vindo ao sistema de notas!")

    while True:
        opcao = menu()  # Exibe o menu e aguarda a escolha do usuário

        if opcao == '1':
            nome = input("Digite o nome do aluno: ").strip()  # Lê o nome do aluno
            resposta = enviar_requisicao(f"CONSULTA:{nome}")   # Envia comando de consulta ao servidor
            print(resposta)  # Exibe a resposta recebida

        elif opcao == '2':
            nome = input("Digite o nome do aluno: ").strip()
            nota_str = input("Digite a nota (0.0 a 10.0): ").strip()
            try:
                nota = float(nota_str)  # Converte o texto digitado para número decimal
                if not 0.0 <= nota <= 10.0:
                    print("Nota invalida. Deve ser entre 0.0 e 10.0.")
                    continue  # Volta ao início do loop sem enviar ao servidor
                resposta = enviar_requisicao(f"CADASTRO:{nome}:{nota}")  # Envia comando de cadastro
                print(resposta)
            except ValueError:
                print("Nota invalida. Digite um numero.")  # Captura erro se o usuário digitar texto no lugar da nota

        elif opcao == '3':
            resposta = enviar_requisicao("MEDIA")  # Solicita ao servidor o cálculo da média da turma
            print(resposta)

        elif opcao == '4':
            resposta = enviar_requisicao("LISTA")  # Solicita ao servidor a lista de todos os alunos
            print(resposta)

        elif opcao == '5':
            print("Encerrando cliente.")
            break  # Encerra o loop e finaliza o programa

        else:
            print("Opcao invalida.")  # Informa ao usuário que digitou uma opção inexistente


if __name__ == '__main__':
    main()  # Inicia o cliente quando o arquivo é executado diretamente
