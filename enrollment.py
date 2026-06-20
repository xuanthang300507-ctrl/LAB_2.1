from datetime import datetime

class Enrollment:
    def __init__(self, mssv, course_id, registration_date):
        self.mssv = mssv
        self.course_id = course_id
        self.registration_date = registration_date

    def enroll(self, db):
        query = "INSERT INTO enrollment (mssv, course_id, registration_date) VALUES (?, ?, ?)"
        params = (self.mssv, self.course_id, self.registration_date)
        try:
            db.execute_query(query, params)
            print(f"✓ Đăng ký khóa học {self.course_id} cho sinh viên {self.mssv} thành công!")
        except Exception as e:
            print(f"✗ Lỗi khi đăng ký: {e}")

    @staticmethod
    def search_enrollment(db, mssv, course_id):
        query = "SELECT * FROM enrollment WHERE mssv = ? AND course_id = ?"
        result = db.fetch_all(query, (mssv, course_id))
        return result
