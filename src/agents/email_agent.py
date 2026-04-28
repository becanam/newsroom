import smtplib
import os
import re
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from .gate import call_llm

EMAIL_FORMAT_SYSTEM = """
Format the following news analysis as a clean daily digest email.
Use these sections:
📰 Today's Story
🌍 Why It Matters
🔑 Key Context
Keep it under 300 words. Friendly but informative tone.
Do NOT use markdown symbols like **, ##, --, or *. Write in plain text only.
"""

def strip_markdown(text: str) -> str:
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)  # **bold**
    text = re.sub(r'\*(.*?)\*', r'\1', text)        # *italic*
    text = re.sub(r'#{1,6}\s*', '', text)           # ## headers
    text = re.sub(r'---+', '─' * 30, text)          # --- dividers
    text = re.sub(r'^\s*[-•]\s*', '• ', text, flags=re.MULTILINE)  # - bullets
    return text.strip()

def format_digest(analysis: str) -> str:
    raw = call_llm(EMAIL_FORMAT_SYSTEM, analysis)
    return strip_markdown(raw)

def send_email(to_addr: str, subject: str, body: str) -> bool:
    gmail_user = os.getenv("GMAIL_USER")
    gmail_pass = os.getenv("GMAIL_PASS")

    if not gmail_user or not gmail_pass:
        raise ValueError("GMAIL_USER and GMAIL_PASS must be set in environment")

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = gmail_user
    msg["To"] = to_addr

    # Plain text version
    msg.attach(MIMEText(body, "plain", "utf-8"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(gmail_user, gmail_pass)
            server.sendmail(gmail_user, [to_addr], msg.as_string())
        return True
    except Exception as e:
        print(f"Email send failed: {e}")
        return False