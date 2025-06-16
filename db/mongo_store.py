from pymongo import MongoClient
from models.student import Student

client = MongoClient('mongodb://localhost:27017/')
db = client['nosql_lab']
collection = db['students']

def save_student(student):
    collection.replace_one({"student_no": student.student_no}, student.to_dict(), upsert=True)

def get_student(student_no):
    data = collection.find_one({"student_no": student_no})
    return Student.from_dict(data) if data else None
