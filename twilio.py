from twilio.rest import Client


account_sid = "ACf03aeff7f1ca60a5e46c527f7faa71b1"

auth_token  = "afd75c7d3c22c1dcb8db01b0eacd019e"

client = Client(account_sid, auth_token)

mes=['from akash kumar with twilio api\n 'for x in range(10) ]
message = client.messages.create(
    to="+918437417877", 
    from_="+17372002622",
    body=mes)
print(message)

