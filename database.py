import sqlite3
from datetime import datetime
import os

class Database:
    def __init__(self):
        db_path = "course_registration.db"
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.conn.row_factory = sqlite3.Row
        self._init_schema()

    def _init_schema(self):
        """Tạo schema nếu chưa tồn tại"""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                mssv TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                dob TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                phone TEXT UNIQUE NOT NULL,
                address TEXT NOT NULL
            )
        ''')
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS courses (
                course_id TEXT PRIMARY KEY,
                course_name TEXT NOT NULL,
                description TEXT,
                credits INTEGER CHECK(credits > 0)
            )
        ''')
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS enrollment (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                mssv TEXT NOT NULL,
                course_id TEXT NOT NULL,
                registration_date TEXT DEFAULT CURRENT_DATE,
                FOREIGN KEY (mssv) REFERENCES students(mssv) ON DELETE CASCADE,
                FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE
            )
        ''')
        self.conn.commit()

    def execute_query(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.conn.commit()
        except sqlite3.IntegrityError as e:
            print(f"Lỗi: Dữ liệu bị trùng lặp hoặc vi phạm ràng buộc - {e}")
            self.conn.rollback()

    def fetch_all(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        return self.cursor.fetchall()

    def fetch_one(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        return self.cursor.fetchone()
