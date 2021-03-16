from postmarker.core import PostmarkClient


FROM = 'soundar@thinkbridge.in'

TO = ['soundar@thinkbridge.in']

SUBJECT = "meeting subject"

TEXT = "this is the message for you"

# send the mail
s = PostmarkClient(server_token='c5aa6dc8-1eac-42bc-a759-e30315aeae6d')
s.emails.send(
  From=FROM,
  To=TO,
  Subject=SUBJECT,
  HtmlBody=TEXT
)

print("mailed successfully")
