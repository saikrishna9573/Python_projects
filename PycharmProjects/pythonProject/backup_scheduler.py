import os
import shutil
import datetime
import schedule
import time
import logging
from pathlib import Path
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuration
source_dir = "C:/Users/saima/Documents/GitHub/Sample"
destination_dir = "C:/Users/saima/Desktop/Backups"
log_file = "backup_log.txt"
backup_time = "13:26"  # Change this to your preferred time
email_enabled = False
email_config = {
    "smtp_server": "smtp.gmail.com",
    "smtp_port": 587,
    "sender_email": "saikrish9573@gmail.com",
    "receiver_email": "saikrish9573@gmail.com",
    "password": "saikrishna.95"
}

# Logging setup
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def send_email(subject, body):
    if not email_enabled:
        return

    msg = MIMEMultipart()
    msg['From'] = email_config["sender_email"]
    msg['To'] = email_config["receiver_email"]
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(email_config["smtp_server"], email_config["smtp_port"])
        server.starttls()
        server.login(email_config["sender_email"], email_config["password"])
        text = msg.as_string()
        server.sendmail(email_config["sender_email"], email_config["receiver_email"], text)
        server.quit()
        logging.info("Email notification sent.")
    except Exception as e:
        logging.error(f"Failed to send email: {e}")


def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))

    # Create destination directory if it doesn't exist
    Path(dest).mkdir(parents=True, exist_ok=True)

    try:
        shutil.copytree(source, dest_dir)
        logging.info(f"Folder copied to: {dest_dir}")
        send_email("Backup Successful", f"Folder copied to: {dest_dir}")
    except FileExistsError:
        logging.warning(f"Folder already exists in: {dest}")
        send_email("Backup Skipped", f"Folder already exists in: {dest}")
    except Exception as e:
        logging.error(f"Error copying folder: {e}")
        send_email("Backup Failed", f"Error copying folder: {e}")


# Schedule the backup
schedule.every().day.at(backup_time).do(lambda: copy_folder_to_directory(source_dir, destination_dir))


def main():
    logging.info("Backup scheduler started.")
    while True:
        schedule.run_pending()
        time.sleep(60)


if __name__ == "__main__":
    main()
