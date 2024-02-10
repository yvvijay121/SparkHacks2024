from flask import Flask, request, jsonify
from tinydb import TinyDB
import uuid
import random
app = Flask(__name__)

db = TinyDB("database.json")


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/create_user", methods=["POST"])
def create_user():
    user_data = request.get_json()
    # Create a random UUID
    uuid = str(uuid.uuid4())

    # Create a new user in the TinyDB
    user_id = db.insert(
        {
            "first_name": user_data["first_name"],
            "last_name": user_data["last_name"],
            "phone": user_data["phone"],
            "UUID": uuid,
            "drugs": [],
        }
    )

    # Return the user ID as a response
    return jsonify({"user_id": user_id})


@app.route("/create_example_patient")
def create_example_patient():
    # Generate a random phone number
    phone_number = str(random.randint(1000000000, 9999999999))

    # Create a new example patient in the TinyDB
    patient_id = db.insert(
        {
            "first_name": "John",
            "last_name": "Doe",
            "phone": phone_number,
            "UUID": str(uuid.uuid4()),
            "drugs": [],
        }
    )

    # Return the patient ID as a response
    return jsonify({"patient_id": patient_id})

@app.route("/add_drug", methods=["POST"])
def add_drug():
    drug_data = request.get_json()
    patient_id = drug_data["patient_id"]
    drug_name = drug_data["drug_name"]
    drug_dosage = drug_data["drug_dosage"]

    # Get the patient from the TinyDB database
    patient = db.get(doc_id=patient_id)

    if patient is None:
        return jsonify({"error": "Patient not found"})

    # Add the new drug to the patient's drugs list
    patient["drugs"].append({"name": drug_name, "dosage": drug_dosage})

    # Update the patient in the TinyDB database
    db.update(patient, doc_ids=[patient_id])

    return jsonify({"message": "Drug added successfully"})


if __name__ == "__main__":
    app.run()
