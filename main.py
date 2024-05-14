import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from link import SMTPServer



def prepare_email_body():
    body = (f'Email body test. You can add any information you would like to address. \n\n'
            f'Above I have sent an attachment from my Tweets on Twitter project in GitHub repos: \n'
            f'https://github.com/DonaldMod/Tweets \n'
            f'https://github.com/DonaldMod/Tweets_Airflow_Flow')
    return body

def send_email(subject, body, from_email, smtp_password, smtp_server, smtp_port, attachment_path, to_email  = None, cc_email = None):
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    if to_email:
        msg['To'] = ', '.join(to_email)
    if cc_email:
        msg['CC'] = ', '.join(cc_email)

    if attachment_path:
        with open(attachment_path, "rb") as attachment_file:
            attachment = MIMEBase('application', 'octet-stream')
            attachment.set_payload(attachment_file.read())
        encoders.encode_base64(attachment)
        attachment.add_header('Content-Disposition', f"attachment; filename= {attachment_path}")
        msg.attach(attachment)

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(from_email, smtp_password)
        text = msg.as_string()
        if cc_email != None:
            server.sendmail(from_email, to_email + cc_email, text)
        else:
            server.sendmail(from_email, to_email, text)
        server.quit()
        
        print("Email sent successfully.")
    except Exception as e:
        print(f"Email sending failed: {e}")


smtpDetails = SMTPServer()
subject = smtpDetails.subject
to_email = smtpDetails.to_email
cc_email = smtpDetails.cc_email
from_email = smtpDetails.from_email
smtp_server = smtpDetails.smtp_server
smtp_port = smtpDetails.smtp_port
smtp_password = smtpDetails.smtp_password

attachment_path = "katyperry_twitter_data.csv"

email_body = prepare_email_body()

send_email(subject, email_body, from_email, smtp_password, smtp_server, smtp_port, attachment_path, to_email, cc_email)

