from flask import Flask, jsonify
from db import redis_store, mongo_store, hazelcast_store

app = Flask(__name__)

@app.route("/nosql-lab-rd/student_no=<student_no>")
def get_redis(student_no):
    student = redis_store.get_student(student_no)
    return jsonify(student.to_dict() if student else {})

@app.route("/nosql-lab-mon/student_no=<student_no>")
def get_mongo(student_no):
    student = mongo_store.get_student(student_no)
    return jsonify(student.to_dict() if student else {})

@app.route("/nosql-lab-hz/student_no=<student_no>")
def get_hazelcast(student_no):
    student = hazelcast_store.get_student(student_no)
    return jsonify(student.to_dict() if student else {})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

