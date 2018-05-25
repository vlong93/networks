import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)

server.ehlo()
server.starttls()

#Next, log in to the server
server.login("your gmail address", "your password")

#Send the mail
msg = "Hello!Here is Jinjing!" 
server.sendmail("from email address", "destination email address", msg)

server.close()	