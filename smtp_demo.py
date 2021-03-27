import smtplib
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("smtptestmcc2021@gmail.com", "mcc@123!")
print(dir(smtplib.SMTP_SSL))
server.sendmail("smtptestmcc2021@gmail.com", "smtptestmcc2021@gmail.com", "Hello!!! How are MSC classes going?")
server.quit() # mcc@123!