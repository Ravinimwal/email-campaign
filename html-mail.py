import smtplib
import getpass
import jinja2
import datetime
import threading
import mysql.connector
import config
from flask import Flask, request, jsonify
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from getemails import getEmails
getEmails=getEmails()
app = Flask(__name__)
app.config.from_object(config)

mysql = mysql.connector.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    database=app.config['MYSQL_DB']
)

HOST = "smtp.gmail.com"
PORT = 25
FROM_EMAIL = <"Enter Sender Email">
TO_EMAIL = <"Enter Reciepient Email">
PASSWORD = getpass.getpass("Enter password: ")

template_loader = jinja2.FileSystemLoader(searchpath="./templates")
template_env = jinja2.Environment(loader=template_loader)
template = template_env.get_template("campaign_template.html")

subject = "Your Daily Newsletter"
preview_text = "Check out our latest news!"
article_url = "https://www.google.com"
published_date = "September 9, 2023"
html_content = "<p>Click on read more to go to article.</p>"
plain_text_content = "This is the plain text version of your email."

NUM_THREADS = 4

def send_email(to_email):
    try:
        email_content = template.render(
            subject=subject,
            preview_text=preview_text,
            article_url=article_url,
            published_date=published_date,
            html_content=html_content,
            plain_text_content=plain_text_content
        )

        message = MIMEMultipart("alternative")
        message['Subject'] = subject
        message['From'] = FROM_EMAIL
        message['To'] = to_email

        html_part = MIMEText(email_content, 'html')
        message.attach(html_part)

        smtp = smtplib.SMTP(HOST, PORT)

        status_code, response = smtp.ehlo()
        print(f"[*] Echoing the server: {status_code} {response}")

        status_code, response = smtp.starttls()
        print(f"[*] Starting TLS connection: {status_code} {response}")

        status_code, response = smtp.login(FROM_EMAIL, PASSWORD)
        print(f"[*] Logging in: {status_code} {response}")

        smtp.sendmail(FROM_EMAIL, to_email, message.as_string())
        smtp.quit()

        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Error sending email to {to_email}: {str(e)}")

emails_list= getEmails.getAllEmails()

threads = [threading.Thread(target=send_email, args=(email[0],))for email in emails_list ]

    
for thread in threads:
    thread.start()


print("All emails sent.")
