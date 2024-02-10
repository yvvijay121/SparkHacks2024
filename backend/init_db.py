import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

users = [
    ('John', 'Doe', '1234564738', '804826J2HU,786Z46389E,362O9ITL9D,4B3SC438HI', 'johndoe'),
    ('Jane', 'Deer', '5679480035', 'L6UH7ZF8HC,QWB9JQZ4F1,7CUC9DDI9F,7AJO3BO7QN', 'janedoe')
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
connection.commit()
connection.close()