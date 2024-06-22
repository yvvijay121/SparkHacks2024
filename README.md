SpakHacks 2024 project with Yash Vijay, Trenton Coleman, Aditya Dalal and Rohith Komati 

Overall Project:
Drug tracker application that allows used to manage and be notified of the drugs that they are taking 

Flask backend:

Database Categories:
Table
Name
Phone number
Patient ID#
Drug Table
Name of drug and other related information, such as:
Whatever we need to access both openFDA API (generic name)
Whatever we need to search through drug interactions CSV
Dosage Schedule:
Time interval between dosages
How many times per day
Times that they missed the dosage (list of ISO timestamps)


Dosage Table:
Dosage UUID
Drug ID, 
Patient ID
Start of Time Range (ISO)
End of Time Range (ISO)
Actual Taking of Drug (ISO)
Enum for yet to be taken/not taken/taken

Basic Features
Gantt chart in middle to track how drugs are taken
Simple card list of drugs that are being taken & picture of drug along with drug info (dosage, how long, complications, etc.)
Color coding
Listing symptoms
Medical history

New features
SMS/phone call notifications for taking medicine
Notify emergency contact is medicine isn’t being taken for certain period
Complications - search bar for when people are having trouble with drugs (Ex. On a scale, 1-10 how bad are you feeling, how big is your rash)
Period tracker like - analyzes your mood for certain days of period --> analysing mood for how long you’re taking and can display effects better of psychiatric
Labels for settings within app
Family account system for app
Previous medications (how long were you taking, WHY you stopped taking it)

[Dev Docs](https://docs.google.com/document/d/17XwLa5vnaRyn055X1fiz8kVhpMb4cP5uQixNE5NjAGY/edit?usp=sharing)
