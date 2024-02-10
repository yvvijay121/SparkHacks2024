DROP TABLE IF EXISTS patients;
DROP TABLE IF EXISTS logs;
DROP TABLE IF EXISTS drugs;

CREATE TABLE patients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    user_name TEXT NOT NULL,
    phone TEXT NOT NULL,
    drugs TEXT NOT NULL
);

CREATE TABLE drugs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    generic_name TEXT NOT NULL,
    dosage TEXT NOT NULL,
    drug_route TEXT NOT NULL,
    instructions TEXT NOT NULL,
    start_date TEXT NOT NULL,
    end_date TEXT NOT NULL,
    frequency INTEGER NOT NULL,
    unii TEXT NOT NULL
);


CREATE TABLE logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    drug_id INTEGER NOT NULL,
    patient_id INTEGER NOT NULL,
    start_time INTEGER NOT NULL,
    end_time INTEGER NOT NULL,
    dose_time INTEGER,
    taken TEXT,
    FOREIGN KEY (patient_id) REFERENCES patients(id),
    FOREIGN KEY (drug_id) REFERENCES drugs(id)
);
