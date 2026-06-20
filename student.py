from datetime import datetime

class Student:
    def __init__(self, mssv, name, dob, email, phone, address):
        self.mssv = mssv
        self.name = name
        # Chuyển đổi dob từ string sang datetime nếu cần
        if isinstance(dob, str):
            self.dob = datetime.strptime(dob, "%Y-%m-%d").date()
        else:
            self.dob = dob
        self.email = email
        self.phone = phone
        self.address = address

    def add_student(self, db):
        query = "INSERT INTO students (mssv, name, dob, email, phone, address) VALUES (?, ?, ?, ?, ?, ?)"
        params = (self.mssv, self.name, str(self.dob), self.email, self.phone, self.address)
        try:
            db.execute_query(query, params)
            print(f"✓ Thêm sinh viên {self.mssv} thành công!")
        except Exception as e:
            print(f"✗ Lỗi khi thêm sinh viên: {e}")

    def update_student(self, db):
        query = "UPDATE students SET name = ?, dob = ?, email = ?, phone = ?, address = ? WHERE mssv = ?"
        params = (self.name, str(self.dob), self.email, self.phone, self.address, self.mssv)
        try:
            db.execute_query(query, params)
            print(f"✓ Cập nhật sinh viên {self.mssv} thành công!")
        except Exception as e:
            print(f"✗ Lỗi khi cập nhật sinh viên: {e}")

    @staticmethod
    def search_student(db, mssv):
        query = "SELECT * FROM students WHERE mssv = ?"
        result = db.fetch_all(query, (mssv,))
        formatted_students = []
        for student in result:
            mssv, name, dob, email, phone, address = student
            formatted_dob = dob  # SQLite trả về string
            formatted_students.append((mssv, name, formatted_dob, email, phone, address))
        
        return formatted_students if formatted_students else []

    @staticmethod
    def get_all_students(db):
        query = "SELECT * FROM students"
        result = db.fetch_all(query)
        
        formatted_students = []
        for student in result:
            mssv, name, dob, email, phone, address = student
            formatted_dob = dob  # SQLite trả về string
            formatted_students.append((mssv, name, formatted_dob, email, phone, address))
        
        return formatted_students if formatted_students else []
