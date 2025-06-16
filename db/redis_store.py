import redis
import json
from models.student import Student

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

def save_student(student):
    print(f"[Redis] Saving student: {student.student_no}")
    r.set(student.student_no, json.dumps(student.to_dict()))

def get_student(student_no):
    data = r.get(student_no)
    print(f"[Redis] GET {student_no} -> {data}")
    return Student.from_dict(json.loads(data)) if data else None
