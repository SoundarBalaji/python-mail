import smtplib

# def send_mail():
# try:
FROM = '---mail id---'

TO = '---to mail id----'

SUBJECT = "meeting subject"

TEXT = "this is the message for you"

# message body
message = """\
From: %s
To: %s
Subject: %s

%s
""" % (FROM, TO, SUBJECT, TEXT)

# send the mail
# s = smtplib.SMTP('localhost')
s = smtplib.SMTP('smtp.gmail.com', 587)
s.ehlo()
s.starttls()

user = '---- from mail id---'
password = ''
s.login(user, password)
s.sendmail(FROM, TO, message)
s.quit()
print("mailed successfully")

# except:
#     print("failed")
