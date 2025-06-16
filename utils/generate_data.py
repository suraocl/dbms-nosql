from models.student import Student
from db import redis_store, mongo_store, hazelcast_store

def generate_students():
    for i in range(1, 10001):
        # 00001 → 2025000001 gibi ID üret
        padded = f"{i:05d}"
        student_no = f"2025{padded}"

        name = f"Student {i}"
        department = "Department " + str(i % 10)

        student = Student(student_no, name, department)

        # DEBUG log (kontrol amaçlı)
        print(f"[✓] Saving student_no={student_no}")

        redis_store.save_student(student)
        mongo_store.save_student(student)
        hazelcast_store.save_student(student)

    print("✅ 10.000 öğrenci başarıyla kaydedildi.")

if __name__ == "__main__":
    generate_students()
