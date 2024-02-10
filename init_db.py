import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO patients (first_name, last_name, phone, drugs, user_name) VALUES (?, ?, ?, ?, ?)",
            ('Yash', 'Vijay', '2244751005', '804826J2HU,786Z46389E,362O9ITL9D,4B3SC438HI', 'yvvijay')
)

drugs_data = [
    ('Amoxicillin', '500', 'Oral', 'Take one capsule by mouth three times a day for 7 days.', '2024-02-10', '2024-02-17', '3', '804826J2HU'),
    ('Metformin', '500', 'Oral', 'Take one tablet by mouth daily with food.', '2024-01-01', '2024-12-31', '2', '786Z46389E'),
    ('Acetaminophen', '500', 'Oral', 'Take two caplet every 6 hours for a maximum of 10 days.', '2024-02-05', '2024-02-15', '4', '362O9ITL9D'),
    ('Methylphenidate', '20', 'Oral', 'If paradoxical aggravation of symptoms or other adverse effects occur, reduce dosage.', '2024-01-01', '2024-12-31', '2', '4B3SC438HI')
]

cur.executemany("INSERT INTO drugs (generic_name, dosage, drug_route, instructions, start_date, end_date, frequency, unii) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", drugs_data)
connection.commit()
connection.close()