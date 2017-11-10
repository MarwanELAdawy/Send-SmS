import os
from twilio.rest import Client

account_sid = "AC###############################"
auth_token = "8d##############################"
client = Client(account_sid, auth_token)

client.messages.create(
	to="+2 The Phone of Yours",
	from_="+ Your Phone in twilio",
	body=" Your Message "
	)
