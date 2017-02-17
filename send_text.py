from twilio.rest import TwilioRestClient

account_sid = "ACb991e402b3fefdd74c353c0f0ef82019" # Your Account SID from www.twilio.com/console
auth_token  = "48027f4f5c8ce12638e1716933331f7b"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from Python",
    to="+14168193643",    # Replace with your phone number
    from_="+16474962295 ") # Replace with your Twilio number

print(message.sid)
