import smtplib, ssl
import os


mail_list={
'pratyakshchauhan':'pratyaksh_chauhan@fosteringlinux.com',
'GithubLearningrepository':'anjali_manocha@fosteringlinux.com'
}


port = 465
smtp_server = "smtp.gmail.com"
USER_EMAIL = os.environ.get("USER_EMAIL")
USER_PASSWORD = os.environ.get("USER_PASSWORD")
ISSUE = os.environ.get("ISSUE_TITLE")
RECIVERS_MAIL = os.environ.get("RECIEVERS_MAIL")
TEXT = os.environ.get("ISSUE_DESC")


to_address = [RECIVERS_MAIL, RECIVERS_MAIL1]
actor = os.environ.get("ISSUE_CREATOR")
for i in mail_list:
  if actor == i:
    mailto = mail_list[i]
    to_address.append(mailto)



SUBJECT = "Issue: " + ISSUE

body = "The following issue has been encountered: " + TEXT + ", and has been assigned to " + actor +"."
message = 'Subject: {}\n\n{}'.format(SUBJECT, body)
context = ssl.create_default_context()

server = smtplib.SMTP_SSL(smtp_server, port, context=context)

server.login(USER_EMAIL, USER_PASSWORD)
server.sendmail(USER_EMAIL, to_address, message)
