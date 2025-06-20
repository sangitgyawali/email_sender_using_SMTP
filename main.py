# This script sends an email using Python's smtplib module.
# Make sure to replace the SMTP server, port, and login credentials with your own.

import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Your Name'
email['to'] = 'recipient@example.com'
email['subject'] = 'Test Email'

email.set_content('This is a test email sent using Python.')

smtp_server = 'smtp.example.com'
smtp_port = 587

with smtplib.SMTP(smtp_server, smtp_port) as smtp:
    smtp.ehlo()
    smtp.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
    smtp.login('your_email@example.com', 'your_password')
    smtp.send_message(email)

print('Email sent successfully!')