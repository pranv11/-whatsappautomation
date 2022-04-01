import os
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

from_whatsapp_number = 'whatsapp:+<13413140599>'
to_whatsapp_number = 'whatsapp:+<14083688187>'

message = client.messages.create(body='hello this is a test',
                       media_url='https://raw.githubusercontent.com/dianephan/flask_upload_photos/main/UPLOADS/DRAW_THE_OWL_MEME.png',
                       from_=from_whatsapp_number,
                       to=to_whatsapp_number)

print(message.sid)