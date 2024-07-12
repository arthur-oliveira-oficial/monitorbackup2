from backup_handler import BackupHandler  # Importa a classe BackupHandler do módulo backup_handler
from folder_watchdog import FolderWatchDog  # Importa a classe FolderWatchDog do módulo folder_watchdog
import sys  # Importa o módulo sys para acessar argumentos de linha de comando

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Uso: python main.py <caminho_para_monitorar>")
        sys.exit(1)  # Encerra o programa se o número de argumentos não for igual a 2

    path_to_watch = sys.argv[1]  # Obtém o caminho a ser monitorado a partir do argumento de linha de comando
    w_dog = FolderWatchDog(handler=BackupHandler(), watch_path=path_to_watch)  # Cria uma instância de FolderWatchDog com BackupHandler como manipulador e o caminho fornecido
    w_dog.start()  # Inicia o monitoramento do caminho especificado
