import sqlite3

class Database:
    def __init__(self, db_name="hospital.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            gender TEXT NOT NULL,
            phone TEXT NOT NULL,
            disease TEXT NOT NULL,
            doctor TEXT NOT NULL,
            status TEXT DEFAULT 'Admitted'
        )
        """
        self.cursor.execute(query)
        self.conn.commit()

    def add_patient(self, name, age, gender, phone, disease, doctor):
        query = """
        INSERT INTO patients (name, age, gender, phone, disease, doctor)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        self.cursor.execute(query, (name, age, gender, phone, disease, doctor))
        self.conn.commit()

    def get_all_patients(self):
        self.cursor.execute("SELECT * FROM patients")
        return self.cursor.fetchall()

    def search_patient_by_id(self, patient_id):
        self.cursor.execute("SELECT * FROM patients WHERE id = ?", (patient_id,))
        return self.cursor.fetchone()

    def update_patient(self, patient_id, name, age, gender, phone, disease, doctor):
        query = """
        UPDATE patients 
        SET name = ?, age = ?, gender = ?, phone = ?, disease = ?, doctor = ?
        WHERE id = ?
        """
        self.cursor.execute(query, (name, age, gender, phone, disease, doctor, patient_id))
        self.conn.commit()

    def update_status(self, patient_id, status):
        query = "UPDATE patients SET status = ? WHERE id = ?"
        self.cursor.execute(query, (status, patient_id))
        self.conn.commit()

    def delete_patient(self, patient_id):
        self.cursor.execute("DELETE FROM patients WHERE id = ?", (patient_id,))
        self.conn.commit()

    def close(self):
        self.conn.close()
