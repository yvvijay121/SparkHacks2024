#Email notification system Hackathon
import smtplib
import ssl

def emailNotif(emailTo, pFname, pLname, dName, dVolume, dType, startRange, endRange):
  smtPort = 587
  smptServer = "smtp.gmail.com"
  emailFrom = "petals.shshacks.2023@gmail.com"
  pas = "zvgmfnhechrxjboy"
  # Actual formatting of the message:
  mes = "Hello " + pFname + " " + pLname + ",\n" + "Please take " + dVolume + " of the drug " + dName
  mes2 = mes +" via "+dType+" between the times of "+startRange+" and "+endRange
  message = mes2+"\nSincerely,\nThe aegisRX Team"
  
  
  simpleEmailContext = ssl.create_default_context()
  tserver = smtplib.SMTP(smptServer, smtPort)
  tserver.starttls(context=simpleEmailContext)
  tserver.login(emailFrom, pas)
  tserver.sendmail(emailFrom, emailTo, message)
  tserver.quit()


  #Use the code at the bottom to test
# pFname = input("Please enter your first name: ")
# pLname = input("Please enter your last name: ")
# dName = input("Please enter the drug name: ")
# dType = input("Please enter the type of ingestion method: ")
# dVol = input("Please enter the drug volume: ")
# pStart = input("Please enter the start range: ")
# pEnd = input("Please enter the end range: ")
# emailT = input("Please enter your email: ")
# emailNotif(emailT, pFname, pLname, dName, dVol, dType, pStart, pEnd)
