import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

class Config:
    def __init__(self, smtp_server,smtp_port,sender):
        self.smtp_server=smtp_server
        self.smtp_port=smtp_port
        self.sender = sender

    def get_files_in_folders(folder_paths):
        file_paths = []
        file_names = []
        for folder_path in folder_paths:
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    file_paths.append(os.path.join(root, file))
                    file_names.append(file)
        return file_paths, file_names

    def send(self,recipients,recipients_cc,subject,message_header,message_footer, folder_paths):
        # Email details
        smtp_server = self.smtp_server
        smtp_port = self.smtp_prt
        sender = self.sender

        # Create a MIME text object
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = ';'.join(recipients)
        msg['CC'] = ';'.join(recipients_cc)

        table_html = ''
        if folder_paths != 'null':
            table_html = folder_paths
        
        # Create the email body as HTML
        message = message_header
        message += f'<html><body>{table_html}</body></html>'
        message += message_footer

        # Attach the email body
        msg.attach(MIMEText(message, 'html'))

        # Connect to the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            try:    
                server.sendmail(sender, recipients, msg.as_string())
                return 1
            except Exception as e:
                print('An error occurred:', str(e))
                return 0
            finally:
                # Disconnect from the SMTP server
                server.quit()