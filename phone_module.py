from twilio.rest import Client

def make_call():
    account_sid = "enter your account sid"
    auth_token = "enter your auth token"
    client = Client(account_sid, auth_token)
    from_number = "+16169523624"
    to_number = input("Enter target phone number (with country code): ")
    message = input("Enter message to speak: ")

    try:
        call = client.calls.create(
            to=to_number,
            from_=from_number,
            twiml=f"<Response><Say>{message}</Say></Response>"
        )
        print("Call initiated:", call.sid)
    except Exception as e:
        print("Failed to call:", e)

if __name__ == "__main__":
    make_call()