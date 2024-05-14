from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

class SMTPServer:
    def __init__(self):
        self.server = {
            'subject': "Test SMTP Usage",
            'to_email': ["youremail@gmail.com", "example1@company.co.za", "example2@icloud.com"],
            'cc_email': ["example3@gmail.com", "example4@outlook.com"],
            'from_email': os.getenv('from_email'),
            'smtp_server': os.getenv('smtp_server'),
            'smtp_port': os.getenv('smtp_port'),
            'smtp_password' : os.getenv('smtp_password')
        }
    
    # Getter methods for each variable
    @property
    def subject(self):
        return self.server['subject']
    @property
    def to_email(self):
        return self.server['to_email']
    @property
    def cc_email(self):
        return self.server['cc_email']
    @property
    def from_email(self):
        return self.server['from_email']
    @property
    def smtp_server(self):
        return self.server['smtp_server']

    @property
    def smtp_port(self):
        return self.server['smtp_port']
    
    @property
    def smtp_password(self):
        return self.server['smtp_password']