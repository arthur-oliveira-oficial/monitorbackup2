from watchdog.observers import Observer  # Importa a classe Observer do pacote watchdog
from time import sleep  # Importa a função sleep do pacote time

class FolderWatchDog:
    def __init__(self, handler, watch_path):
        """
        Construtor
        :param handler: Quem irá lidar com o que acontece em nosso watch_path.
        """
        self.handler = handler  # Define quem irá lidar com eventos na pasta
        self.watch_path = watch_path  # Define o caminho da pasta que será monitorada
        self.observer = Observer()  # Inicializa o observador de eventos

    def start(self):
        self.observer.schedule(self.handler, self.watch_path, recursive=True)  # Configura o observador para monitorar o caminho recursivamente

        try:
            print(f"Iniciando monitoramento da pasta: {self.watch_path}")
            self.observer.start()  # Inicia o monitoramento
            while True:
                sleep(5)  # Aguarda por 5 segundos

        except KeyboardInterrupt:
            self.stop()  # Encerra o monitoramento se houver interrupção pelo usuário
        except Exception as e:
            print(f"Algo deu errado...")
            print(e)  # Exibe detalhes se ocorrer um erro inesperado

        finally:
            self.stop()  # Garante que o monitoramento seja encerrado ao finalizar

    def stop(self):
        self.observer.stop()  # Para o observador
        self.observer.join()  # Aguarda até que o observador finalize completamente
