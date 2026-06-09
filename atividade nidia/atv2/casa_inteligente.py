from datetime import datetime


# Barramento central da arquitetura Publish/Subscribe.
# Componentes se registram para ouvir eventos (assinar) sem precisar se conhecer diretamente,
# o que garante o baixo acoplamento entre eles.
class BarramentoEventos:
    def __init__(self):
        # Dicionário que mapeia nome do evento para lista de funções inscritas
        self._assinantes = {}

    def assinar(self, evento, callback):
        # Se o evento ainda não existe no dicionário, cria uma lista vazia para ele
        if evento not in self._assinantes:
            self._assinantes[evento] = []
        # Adiciona a função (callback) à lista de assinantes daquele evento
        self._assinantes[evento].append(callback)

    def publicar(self, evento, dados=None):
        # Percorre todos os assinantes do evento e chama cada função registrada
        for callback in self._assinantes.get(evento, []):
            callback(dados)


# Componente PUBLICADOR — lê a temperatura digitada pelo usuário e gera o evento correspondente.
class SensorTemperatura:
    def __init__(self, barramento: BarramentoEventos):
        # Guarda a referência ao barramento para publicar eventos
        self._barramento = barramento

    def ler_temperatura(self):
        # Recebe a temperatura digitada pelo usuário via teclado
        temperatura = float(input("Digite a temperatura: "))
        print(f"Temperatura simulada: {temperatura}°C")

        # Publica evento diferente dependendo se a temperatura é alta ou normal
        if temperatura > 30:
            self._barramento.publicar("temperatura_alta", {"temperatura": temperatura})
        else:
            self._barramento.publicar("temperatura_normal", {"temperatura": temperatura})


# Componente ASSINANTE — reage aos eventos de temperatura ligando ou desligando o ar-condicionado.
class ArCondicionado:
    def __init__(self, barramento: BarramentoEventos):
        # Se inscreve nos dois eventos para poder reagir a qualquer mudança de temperatura
        barramento.assinar("temperatura_alta", self._ao_receber_evento)
        barramento.assinar("temperatura_normal", self._ao_receber_evento)

    def _ao_receber_evento(self, dados):
        # Liga se temperatura alta, desliga se temperatura normal
        if dados["temperatura"] > 30:
            print("Ar-condicionado ligado automaticamente.")
        else:
            print("Ar-condicionado desligado.")


# Componente ASSINANTE — exibe alertas na tela conforme o evento recebido.
class Alarme:
    def __init__(self, barramento: BarramentoEventos):
        barramento.assinar("temperatura_alta", self._ao_receber_evento)
        barramento.assinar("temperatura_normal", self._ao_receber_evento)

    def _ao_receber_evento(self, dados):
        if dados["temperatura"] > 30:
            print("ALERTA: temperatura muito alta!")
        else:
            print("Temperatura dentro do normal.")


#Componente ASSINANTE que ajusta a cor da luz conforme a temperatura.
class LuzInteligente:
    def __init__(self, barramento: BarramentoEventos):
        barramento.assinar("temperatura_alta", self._ao_receber_evento)
        barramento.assinar("temperatura_normal", self._ao_receber_evento)

    def _ao_receber_evento(self, dados):
        if dados["temperatura"] > 30:
            print("Luz inteligente: modo frio ativado (luz azul).")
        else:
            print("Luz inteligente: modo normal.")


#Componente ASSINANTE que simula o envio de notificações ao usuário.
class SistemaNotificacoes:
    def __init__(self, barramento: BarramentoEventos):
        barramento.assinar("temperatura_alta", self._ao_receber_evento)
        barramento.assinar("temperatura_normal", self._ao_receber_evento)

    def _ao_receber_evento(self, dados):
        temp = dados["temperatura"]
        if temp > 30:
            print(f"[NOTIFICACAO] Temperatura critica detectada: {temp}°C. Acao automatica iniciada.")
        else:
            print(f"[NOTIFICACAO] Sistema em operacao normal. Temperatura: {temp}°C.")


#Componente ASSINANTE que armazena todos os eventos com horário para consulta posterior.
class HistoricoEventos:
    def __init__(self, barramento: BarramentoEventos):
        # Lista interna onde cada entrada é um dicionário com horário, tipo e temperatura
        self._historico = []
        barramento.assinar("temperatura_alta", self._registrar)
        barramento.assinar("temperatura_normal", self._registrar)

    def _registrar(self, dados):
        # Determina o tipo do evento com base no valor da temperatura
        tipo = "temperatura_alta" if dados["temperatura"] > 30 else "temperatura_normal"
        registro = {
            "horario": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "evento": tipo,
            "temperatura": dados["temperatura"],
        }
        self._historico.append(registro)

    def exibir(self):
        # Exibe todos os registros salvos ao final da execução
        print("\n--- Historico de Eventos ---")
        if not self._historico:
            print("Nenhum evento registrado.")
        else:
            for r in self._historico:
                print(f"[{r['horario']}] {r['evento']} | {r['temperatura']}°C")
        print("----------------------------\n")


def main():
    # Cria o barramento compartilhado por todos os componentes
    barramento = BarramentoEventos()

    # Instancia todos os componentes passando o barramento — cada um se registra automaticamente
    sensor = SensorTemperatura(barramento)
    ArCondicionado(barramento)
    Alarme(barramento)
    LuzInteligente(barramento)
    SistemaNotificacoes(barramento)
    historico = HistoricoEventos(barramento)

    print("=== Casa Inteligente - Sistema de Monitoramento ===\n")

    while True:
        try:
            sensor.ler_temperatura()
        except ValueError:
            # Captura entradas inválidas (letras, símbolos) sem encerrar o programa
            print("Valor invalido. Digite um numero.")
            continue

        print()
        opcao = input("Deseja registrar outra temperatura? (s/n): ").strip().lower()
        print()
        if opcao != "s":
            break

    # Exibe o histórico completo ao encerrar
    historico.exibir()


# Garante que main() só executa quando o arquivo é rodado diretamente,
# não quando importado por outro módulo
if __name__ == "__main__":
    main()
