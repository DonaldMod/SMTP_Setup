# Library

Used Libraries:
- import smtplib
    - A pre-installed library of Python
- from email.mime.multipart import MIMEMultipart 
  - Composes the email
- from email.mime.text import MIMEText
  - Email body content
- from email.mime.base import MIMEBase
  - Allows for attachments to be attached to the email.
- from email import encoders
  - Helps to encode and decode email content, such as Excel Workbooks