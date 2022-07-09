from twilio.rest import Client
from datetime import datetime

account_sid ="AC4724897becf2b0169714953990035adf"
auth_token ="27c344f841ad67e649b6243e0920a980"

client = Client(account_sid, auth_token)

message = client.api.account.messages.create(
    to="+18177743112",
    from_="+12395109123",
    body="Script ran at {}".format(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
)
