import smtplib
import ssl

smtPort = 587
smptServer = "smtp.gmail.com"
emailFrom = "petals.shshacks.2023@gmail.com"
emailTo = "unifiedummy@gmail.com"  #change to user email
pas = "zvgmfnhechrxjboy"
message = "Hello billy"         #put in the input value from the user

simpleEmailContext = ssl.create_default_context()

tserver = smtplib.SMTP(smptServer, smtPort)
tserver.starttls(context=simpleEmailContext)
tserver.login(emailFrom, pas)
tserver.sendmail(emailFrom, emailTo, message)

tserver.quit()
