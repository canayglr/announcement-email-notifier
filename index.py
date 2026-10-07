import os
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import requests as req
from bs4 import BeautifulSoup as bs

# Credentials come from environment variables, never from the source code.
sender = os.environ["MAIL_SENDER"]
password = os.environ["MAIL_PASSWORD"]
receiver = os.environ["MAIL_RECEIVER"]
subject = "Yeni Duyuru"

url = "https://erzurum.edu.tr/duyuru/index/1052/1/#gsc.tab=0"
CHECK_INTERVAL = 60  # seconds


def fetch_announcements():
    r = req.get(url, timeout=15)
    soup = bs(r.content, "lxml")
    return soup.find("div", attrs={"class": "list"}).select("div")


def send_mail(body):
    message = MIMEMultipart()
    message["From"] = sender
    message["To"] = receiver
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))
    with smtplib.SMTP("smtp.office365.com", 587) as server:
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receiver, message.as_string())
    print("Gönderim tamamlandı")


last_date = ""
while True:
    try:
        tablo = fetch_announcements()
        if last_date != tablo[0].text:
            body = "---\tDUYURULAR\t---\n"
            for i in range(0, 4):
                if i % 2 == 0:
                    body += f"Tarih: {tablo[i].text}\n"
                else:
                    body += f"Konu: {tablo[i].text.strip()}\n{'-' * 30}\n"
            last_date = tablo[0].text
            send_mail(body)
    except Exception as e:
        print("An error occurred:", e)
    time.sleep(CHECK_INTERVAL)
