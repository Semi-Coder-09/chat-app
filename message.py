import smtplib
import os 
from dotenv import load_dotenv
load_dotenv()

EMAIL = os.getenv("GmailUser")
PASSWORD = os.getenv("GmailPass")

print(EMAIL)