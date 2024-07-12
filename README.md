Backup Monitor
Este projeto é uma ferramenta de monitoramento de diretórios que envia notificações por e-mail sempre que um arquivo é criado, modificado, deletado ou movido em uma pasta específica.

Estrutura do Projeto
O projeto é dividido em três arquivos principais:

backup_handler.py: Contém a classe BackupHandler, que lida com eventos de sistema de arquivos e envia e-mails sobre as mudanças detectadas.

folder_watchdog.py: Contém a classe FolderWatchDog, responsável por monitorar a pasta especificada e notificar o manipulador (BackupHandler) sobre as alterações.

main.py: O ponto de entrada do programa, que inicializa o monitoramento com base no caminho fornecido como argumento de linha de comando.

Pré-requisitos
Antes de executar o projeto, você precisa ter as seguintes bibliotecas instaladas:

pip install watchdog

Configuração do E-mail
No arquivo backup_handler.py, você precisará configurar as credenciais do seu servidor SMTP:

server.login("testeapi@seuemail", "suasenha")

Substitua "testeapi@seuemail" e "suasenha" pelas suas credenciais reais. Além disso, modifique seusmtp.com.br para o domínio do seu servidor SMTP.

Uso
Para executar o programa, utilize o seguinte comando no terminal:
Substitua "testeapi@seuemail" e "suasenha" pelas suas credenciais reais. Além disso, modifique seusmtp.com.br para o domínio do seu servidor SMTP.

Uso
Para executar o programa, utilize o seguinte comando no terminal:
python main.py <caminho_para_monitorar>
Por exemplo, para monitorar a pasta C:\Users\arthur\Downloads\backup\imp, você deve executar:
python main.py C:\Users\arthur\Downloads\backup\imp

Eventos Monitorados
O programa monitora os seguintes eventos:

Arquivo criado: Envia um e-mail quando um novo arquivo é criado.
Arquivo modificado: Envia um e-mail quando um arquivo existente é modificado.
Arquivo deletado: Envia um e-mail quando um arquivo é removido.
Arquivo movido: Envia um e-mail quando um arquivo é movido para outra localização.

Exemplo de Saída
Durante a execução, o programa imprime no console as ações realizadas:
Iniciando monitoramento da pasta: C:\Users\arthur\Downloads\backup\imp
Arquivo criado: C:\Users\arthur\Downloads\backup\imp\novo_arquivo.txt
Arquivo modificado: C:\Users\arthur\Downloads\backup\imp\arquivo_existente.txt
Arquivo deletado: C:\Users\arthur\Downloads\backup\imp\arquivo_deletado.txt
Arquivo movido: De: C:\Users\arthur\Downloads\backup\imp\arquivo_mover.txt | Para: C:\Users\arthur\Downloads\backup\imp\destino\arquivo_mover.txt

Interrompendo o Monitoramento
Para parar o monitoramento, você pode usar Ctrl + C no terminal. O programa garantirá que o monitoramento seja encerrado corretamente.

Licença
Este projeto é distribuído sob a licença MIT. Sinta-se à vontade para modificar e usar conforme necessário.
