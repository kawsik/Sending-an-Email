import smtplib

email = input("Sender email: ")
reciever_email = input("Reciever email: ")

subject = input("Subject: ")
message = input("Message: ")

text = f"Subject : {subject}\n\n{message}"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login(email, "")

server.sendmail(email, reciever_email, text)

print("Email has been sent")