from flask import Flask, request
import sqlite3

app = Flask(__name__)

def get_database_connection():
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    return connection

@app.route('/get_user/<username>')
def get_user(username):
    with get_database_connection() as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM patients WHERE user_name = ?", (username,))
        user = cursor.fetchone()
        return {
            "user": dict(user) if user else None
        }

@app.route('/get_drugs/<username>')
def get_drugs(username):
    with get_database_connection() as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT drugs FROM patients WHERE user_name = ?", (username,))
        drugs = cursor.fetchone()
        return {
            "drugs": dict(drugs)["drugs"].split(',') if drugs else None
        }

@app.route('/get_drug/<unii>')
def get_drug(unii):
    with get_database_connection() as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM drugs WHERE unii = ?", (unii,))
        drug = cursor.fetchone()
        return {
            "drug": dict(drug) if drug else None
        }

@app.route('/remove_drug/<username>/<unii>')
def remove_drug(username, unii):
    with get_database_connection() as connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM drugs WHERE unii = ?", (unii,))
        cursor.execute("SELECT drugs FROM patients WHERE user_name = ?", (username,))
        drugs = cursor.fetchone()
        drugs = dict(drugs)["drugs"].split(',') if drugs else []
        drugs.remove(unii)
        cursor.execute("UPDATE patients SET drugs = ? WHERE user_name = ?", (','.join(drugs), username))
        connection.commit()
        return {
            "status": "success"
        }
    
@app.route('/add_drug/<username>/', methods=['POST'])
def add_drug(username):
    with get_database_connection() as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT drugs FROM patients WHERE user_name = ?", (username,))
        drugs = cursor.fetchone()
        drugs = dict(drugs)["drugs"].split(',') if drugs else []
        drugs.append(request.json["unii"])
        cursor.execute("UPDATE patients SET drugs = ? WHERE user_name = ?", (','.join(drugs), username))
        cursor.execute("INSERT INTO drugs (generic_name, dosage, drug_route, instructions, start_date, end_date, frequency, unii) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (request.json["generic_name"], request.json["dosage"], request.json["drug_route"], request.json["instructions"], request.json["start_date"], request.json["end_date"], request.json["frequency"], request.json["unii"]))
        connection.commit()
        return {
            "status": "success"
        }

@app.route('/update_drug/<unii>/', methods=['POST'])
def update_drug(unii):
    with get_database_connection() as connection:
        cursor = connection.cursor()
        cursor.execute("UPDATE drugs SET generic_name = ?, dosage = ?, drug_route = ?, instructions = ?, start_date = ?, end_date = ?, frequency = ? WHERE unii = ?", (request.json["generic_name"], request.json["dosage"], request.json["drug_route"], request.json["instructions"], request.json["start_date"], request.json["end_date"], request.json["frequency"], unii))
        connection.commit()
        return {
            "status": "success"
        }


if __name__ == '__main__':
    app.run()