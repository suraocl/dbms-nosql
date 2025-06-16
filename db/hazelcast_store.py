import hazelcast
from models.student import Student
import json

client = hazelcast.HazelcastClient()
student_map = client.get_map("students").blocking()

def save_student(student):
    student_map.put(student.student_no, json.dumps(student.to_dict()))

def get_student(student_no):
    data = student_map.get(student_no)
    return Student.from_dict(json.loads(data)) if data else None
