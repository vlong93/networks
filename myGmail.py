import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)

server.ehlo()
server.starttls()

#Next, log in to the server
server.login("cs380project1@gmail.com", "HelloWorld!")

#Send the mail
msg = "This is a test message." 
recipient = input("Enter the e-mail of the recipient: ")
server.sendmail("cs380project1@gmail.com", recipient, msg)

server.close()