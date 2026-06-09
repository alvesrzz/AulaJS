import socket  # Importa o módulo de sockets para comunicação em rede

HOST = 'localhost'  # Define que o servidor vai rodar na própria máquina
PORT = 5000         # Define a porta que o servidor vai escutar

# Dicionário com os alunos já cadastrados (nome -> nota)
alunos = {
    'Ana': 8.5,
    'Carlos': 7.0,
    'Julia': 9.0,
}


def processar_requisicao(mensagem):
    # Divide a mensagem recebida pelo separador ':' (ex: "CONSULTA:Ana" -> ['CONSULTA', 'Ana'])
    partes = mensagem.strip().split(':')
    comando = partes[0]  # O primeiro trecho é sempre o comando

    print(f"Servidor processando requisicao: {mensagem.strip()}")

    if comando == 'CONSULTA':
        nome = partes[1]  # O segundo trecho é o nome do aluno
        if nome in alunos:
            return f"Nota encontrada: {alunos[nome]}"  # Retorna a nota se o aluno existir
        else:
            return "Aluno nao encontrado."  # Retorna erro se o aluno não existir

    elif comando == 'CADASTRO':
        nome = partes[1]        # Nome do aluno a cadastrar
        nota = float(partes[2]) # Converte a nota de texto para número decimal
        alunos[nome] = nota     # Salva o aluno no dicionário
        return f"Aluno {nome} cadastrado com nota {nota}."

    elif comando == 'MEDIA':
        if not alunos:
            return "Nenhum aluno cadastrado."  # Evita divisão por zero se não houver alunos
        media = sum(alunos.values()) / len(alunos)  # Soma todas as notas e divide pela quantidade
        return f"Media da turma: {media:.2f}"  # Retorna a média com 2 casas decimais

    elif comando == 'LISTA':
        if not alunos:
            return "Nenhum aluno cadastrado."
        # Cria uma linha "nome: nota" para cada aluno e junta tudo com quebra de linha
        linhas = [f"{nome}: {nota}" for nome, nota in alunos.items()]
        return "Alunos cadastrados:\n" + "\n".join(linhas)

    else:
        return "Comando desconhecido."  # Resposta padrão para comandos inválidos


def iniciar_servidor():
    # Cria um socket TCP/IP (AF_INET = IPv4, SOCK_STREAM = TCP)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
        # Permite reusar o endereço imediatamente após reiniciar o servidor
        servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        servidor.bind((HOST, PORT))  # Associa o socket ao endereço e porta definidos
        servidor.listen()            # Coloca o socket em modo de escuta, aguardando conexões
        print(f"Servidor aguardando conexoes em {HOST}:{PORT}...")

        while True:
            # Bloqueia até um cliente se conectar; retorna a conexão e o endereço do cliente
            conexao, endereco = servidor.accept()
            with conexao:
                print(f"Cliente conectado: {endereco}")
                while True:
                    dados = conexao.recv(1024)  # Recebe até 1024 bytes de dados do cliente
                    if not dados:
                        break  # Se não receber nada, o cliente desconectou
                    mensagem = dados.decode('utf-8')         # Converte os bytes recebidos para texto
                    resposta = processar_requisicao(mensagem) # Processa e obtém a resposta
                    conexao.sendall(resposta.encode('utf-8')) # Envia a resposta de volta ao cliente
                print(f"Cliente desconectado: {endereco}")


if __name__ == '__main__':
    iniciar_servidor()  # Inicia o servidor quando o arquivo é executado diretamente
