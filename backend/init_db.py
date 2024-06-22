import sqlite3
from datetime import datetime, timedelta
import random

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

users = [
    ('John', 'Doe', '1234564738', '804826J2HU,786Z46389E,362O9ITL9D,4B3SC438HI', 'johndoe'),
    ('Jane', 'Deer', '5679480035', 'L6UH7ZF8HC,QWB9JQZ4F1,7CUC9DDI9F,7AJO3BO7QN', 'janedoe'),
]

cur.executemany("INSERT INTO patients (first_name, last_name, phone, drugs, user_name) VALUES (?, ?, ?, ?, ?)",
                users
)

drugs_data = [
    ('Amoxicillin', '500', 'Oral', 'Take one capsule by mouth three times a day for 7 days.', '2024-02-10', '2024-02-17', '3', '804826J2HU'),
    ('Metformin', '500', 'Oral', 'Take one tablet by mouth daily with food.', '2024-01-01', '2024-12-31', '2', '786Z46389E'),
    ('Acetaminophen', '500', 'Oral', 'Take two caplet every 6 hours for a maximum of 10 days.', '2024-02-05', '2024-02-15', '4', '362O9ITL9D'),
    ('Methylphenidate', '20', 'Oral', 'If paradoxical aggravation of symptoms or other adverse effects occur, reduce dosage.', '2024-01-01', '2024-12-31', '2', '4B3SC438HI'),
    ('Risperidone', '1', 'Oral', 'Take one tablet by mouth two times a day.', '2024-01-01', '2024-08-31', '1', 'L6UH7ZF8HC'),
    ('Hydroxyzine', '25', 'Oral', 'Take one tablet by mouth daily.', '2024-01-01', '2024-4-01', '1', 'QWB9JQZ4F1'),
    ('Pseudoephedrine', '120', 'Oral', 'Take one capsule by mouth daily.', '2023-11-01', '2024-01-01', '1', '7CUC9DDI9F'),
    ('Loratadine', '10', 'Oral', 'Take one tablet by mouth daily.', '2024-01-01', '2024-12-31', '1', '7AJO3BO7QN'),
]

cur.executemany("INSERT INTO drugs (generic_name, dosage, drug_route, instructions, start_date, end_date, frequency, unii) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", drugs_data)

for drug in drugs_data:
    date_format = "%Y-%m-%d"
    start = datetime.strptime(drug[4], date_format)
    end = datetime.strptime(drug[5], date_format)

    number_of_days = (end - start).days

    for k in range(number_of_days):
        start_of_day = start + timedelta(days=k)
        for j in range(int(drug[6])):
            if drug[7] in users[0][3]:
                patient_username = 'johndoe'
            else:
                patient_username = 'janedoe'
            taken = 'true' if random.random() > 0.2 else 'false' 
            cur.execute("INSERT INTO logs (drug_id, patient_username, start_time, end_time, dose_time, taken) VALUES (?, ?, ?, ?, ?, ?)",
                       (drug[7],
                        patient_username,
                        start_of_day + j * timedelta(hours=24 / int(drug[6])) - timedelta(minutes=15),
                        start_of_day + j * timedelta(hours=24 / int(drug[6])) + timedelta(minutes=15),
                        start_of_day + j * timedelta(hours=24 / int(drug[6])),
                        taken))

connection.commit()
connection.close()