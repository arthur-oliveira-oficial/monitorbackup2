from watchdog.events import FileSystemEventHandler  # Importa a classe FileSystemEventHandler do pacote watchdog.events
import smtplib  # Importa o módulo smtplib para enviar e-mails
from email.mime.text import MIMEText  # Importa MIMEText do pacote email.mime.text para construir o corpo do e-mail

class BackupHandler(FileSystemEventHandler):
    def send_email(self, subject, body, to):
        """
        Envia um e-mail com os detalhes fornecidos.
        :param subject: Assunto do e-mail.
        :param body: Corpo do e-mail.
        :param to: Endereço de e-mail de destino.
        """
        msg = MIMEText(body)  # Cria um objeto MIMEText com o corpo do e-mail
        msg['Subject'] = subject  # Define o assunto do e-mail
        msg['From'] = "testeapi@agenciaclickone.com.br"  # Define o remetente do e-mail
        msg['To'] = to  # Define o destinatário do e-mail

        # Conecta-se ao servidor SMTP e envia o e-mail
        with smtplib.SMTP('seusmtp.com.br', 587) as server:
            server.starttls()  # Inicia a conexão TLS (Transport Layer Security)
            server.login("testeapi@seuemail", "suasenha")  # Faz login no servidor SMTP
            server.sendmail("testeapi@seuemail", to, msg.as_string())  # Envia o e-mail

    def on_created(self, event):
        """Chamado quando um arquivo ou pasta é criado."""
        print(f"Arquivo criado: {event.src_path}")
        self.send_email("Backup Criado", f"Arquivo criado: {event.src_path}", "emailderecebimento@mail.com")

    def on_modified(self, event):
        """Chamado quando algo é modificado."""
        print(f"Arquivo modificado: {event.src_path}")
        self.send_email("Backup Modificado", f"Arquivo modificado: {event.src_path}", "emailderecebimento@mail.com")

    def on_deleted(self, event):
        """Chamado quando um arquivo ou pasta é removido."""
        print(f"Arquivo deletado: {event.src_path}")
        self.send_email("Backup Deletado", f"Arquivo deletado: {event.src_path}", "emailderecebimento@mail.com")

    def on_moved(self, event):
        """Chamado quando um arquivo ou pasta é movido."""
        print(f"Arquivo movido: De: {event.src_path} | Para: {event.dest_path}")
        self.send_email("Backup Movido", f"Arquivo movido: De: {event.src_path} Para: {event.dest_path}", "emailderecebimento@mail.com")
