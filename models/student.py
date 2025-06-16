class Student:
    def __init__(self, student_no, name, department):
        self.student_no = student_no
        self.name = name
        self.department = department

    def to_dict(self):
        return {
            "student_no": self.student_no,
            "name": self.name,
            "department": self.department
        }

    @staticmethod
    def from_dict(data):
        return Student(data["student_no"], data["name"], data["department"])
