class Course:
    def __init__(self, course_id, course_name, description, credits):
        self.course_id = course_id
        self.course_name = course_name
        self.description = description
        self.credits = credits

    def add_course(self, db):
        query = "INSERT INTO courses (course_id, course_name, description, credits) VALUES (?, ?, ?, ?)"
        params = (self.course_id, self.course_name, self.description, self.credits)
        try:
            db.execute_query(query, params)
            print(f"✓ Thêm khóa học {self.course_id} thành công!")
        except Exception as e:
            print(f"✗ Lỗi khi thêm khóa học: {e}")

    def update_course(self, db):
        query = "UPDATE courses SET course_name = ?, description = ?, credits = ? WHERE course_id = ?"
        params = (self.course_name, self.description, self.credits, self.course_id)
        try:
            db.execute_query(query, params)
            print(f" Cập nhật khóa học {self.course_id} thành công!")
        except Exception as e:
            print(f" Lỗi khi cập nhật khóa học: {e}")

    @staticmethod
    def delete_course(db, course_id):
        query = "DELETE FROM courses WHERE course_id = ?"
        db.execute_query(query, (course_id,))

    @staticmethod
    def search_course(db, course_id):
        query = "SELECT * FROM courses WHERE course_id = ?"
        result = db.fetch_one(query, (course_id,))
        return result

    @staticmethod
    def get_all_courses(db):
        query = "SELECT * FROM courses"
        result = db.fetch_all(query)
        return result if result else []
