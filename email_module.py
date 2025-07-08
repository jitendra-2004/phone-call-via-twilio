import smtplib

def send_email():
    sender_email = "jb303302@gmail.com"
    app_password = "osrs mjyd rqge jbhj"
    receiver_email = input("Enter receiver email: ")
    subject = input("Enter subject: ")
    message = input("Enter message: ")

    email_body = f"Subject: {subject}\n\n{message}"

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, app_password)
        server.sendmail(sender_email, receiver_email, email_body)
        server.quit()
        print(f"Email sent to {receiver_email}")
    except Exception as e:
        print("Failed to send email:", e)

if __name__ == "__main__":
    send_email()
