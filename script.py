import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def confirm_choice():
    confirm = input("Do you wish to send a file? [Y]Yes or [N]No: ")
    if confirm != "Y" and confirm != "N":
        print("\n Invalid Option. Please Enter a Valid Option.")
        return confirm_choice() 
    return confirm

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

msg = MIMEMultipart()

email_login = input("Enter your gmail login: ")
email_password = input("Enter your gmail password: ")

server.login(email_login, email_password)

receiver_email = input("Enter receiver email: ")

msg["From"] = email_login
msg["To"] = receiver_email
msg["Subject"] = "From Python"

message_text = input("Enter message: ")
 
answer = confirm_choice()

if answer: 
	filename = input("Enter a file name with extension: ")
	path = input("Drag the file into console to copy path: ")
	attachment = open(path, "rb")

	part = MIMEBase('application', 'octet-stream')
	part.set_payload((attachment).read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

	msg.attach(part)
	msg.attach(MIMEText(message_text, "plain"))

	text = msg.as_string()

	server.sendmail(email_login, receiver_email, text)
else: 
	text = msg.as_string()
	server.sendmail(email_login, receiver_email, text)

server.quit()

print("message was sended successful")

