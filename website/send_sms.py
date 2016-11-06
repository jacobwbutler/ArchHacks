from twilio.rest import TwilioRestClient

account_sid = "ACbd9fe5bc5d6de75200a8f627ead10fb4"
auth_token = "764e7c8cc7c1be9ebf916a74f0d30beb"
client = TwilioRestClient(account_sid, auth_token)

def send_sms(to_num, med, dose, reply_code):
    message = client.messages.create(to= to_num,from_="(913) 735-1407",
    body = "Reminder to take " + dose + " dose(s) of " + med + ".  Please reply with "
    + reply_code + " to confirm adherence.")