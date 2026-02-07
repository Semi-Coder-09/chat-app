import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("GmailUser")
PASSWORD = os.getenv("GmailPass")
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(EMAIL, PASSWORD)
    server.ehlo()
    
    server.sendmail(
        EMAIL,
        "bhabanismishra123@gmail.com",
        "Subject: Test\n\nHello from Python!"
    )

print("Email sent 🚀")
