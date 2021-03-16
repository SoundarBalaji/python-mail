from postmarker.core import PostmarkClient


FROM = '----from mail id---'

TO = ['--- to mail id---']

SUBJECT = "meeting subject"

TEXT = "this is the message for you"

# send the mail
s = PostmarkClient(server_token='--- server token---')
s.emails.send(
  From=FROM,
  To=TO,
  Subject=SUBJECT,
  HtmlBody=TEXT
)

print("mailed successfully")
