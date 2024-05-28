import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(subject, body, to_email):
    smtp_server = "chirpn-com.mail.protection.outlook.com"  # Replace with the SMTP server for chirpn.com
    smtp_port = 587  # Typically 587 for TLS
    sender_email = "smallela@chirpn.com"  # Replace with your email address
    sender_password = "Probook@2024"  # Replace with your email password

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Upgrade the connection to secure TLS
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")


# Example usage
send_email("Test Subject", "This is a test email body.", "smallela@chirpn.com")
