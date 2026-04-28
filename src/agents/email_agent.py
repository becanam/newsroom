import smtplib
import os
from email.mime.text import MIMEText
from .gate import call_llm

EMAIL_FORMAT_SYSTEM = """
Format the following news analysis as a clean daily digest email.
Use these sections:
📰 Today's Story
🌍 Why It Matters
🔑 Key Context
Keep it under 300 words. Friendly but informative tone.
"""

def format_digest(analysis: str) -> str:
    return call_llm(EMAIL_FORMAT_SYSTEM, analysis)

def send_email(to_addr: str, subject: str, body: str) -> bool:
    gmail_user = os.getenv("GMAIL_USER")
    gmail_pass = os.getenv("GMAIL_PASS")

    if not gmail_user or not gmail_pass:
        raise ValueError("GMAIL_USER and GMAIL_PASS must be set in environment")

    msg = MIMEText(body, "plain", "utf-8")
    msg["Subject"] = subject
    msg["From"] = gmail_user
    msg["To"] = to_addr

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(gmail_user, gmail_pass)
            server.sendmail(gmail_user, [to_addr], msg.as_string())
        return True
    except Exception as e:
        print(f"Email send failed: {e}")
        return False