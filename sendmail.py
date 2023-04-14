import smtplib, ssl
import os

port = 465
smtp_server = "smtp.gmail.com"
USER_EMAIL = os.environ.get("USER_EMAIL")
USER_PASSWORD = os.environ.get("USER_PASSWORD")
ISSUE = os.environ.get("ISSUE_TITLE")
RECIVERS_MAIL = os.environ.get("RECIEVERS_MAIL")
to_addr = [USER_EMAIL, RECIVERS_MAIL]
message = ISSUE
context = ssl.create_default_context()

server = smtplib.SMTP_SSL(smtp_server, port, context=context)

server.login(USER_EMAIL, USER_PASSWORD)
server.sendmail(to_addr, USER_EMAIL, message)
