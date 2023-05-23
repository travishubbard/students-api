
import sqlite3
import json


from flask import *
import logging


app = Flask(__name__)

# set up our logging output file, level, and format
logging.basicConfig(filename='record.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

with app.app_context():
    app.logger.info("app startup")
    # if you have any init code you want to run once on startup, put it here


# ----------------------
# routes below this line

@app.route('/', methods=['GET'])
def main():
    app.logger.info("main route")
    return 'Welcome to the Students API!'

@app.route('/getStudents', methods=['GET'])
def get_students():
    c = sqlite3.connect("student.db").cursor()
    c.execute("SELECT * FROM STUDENTS")
    data = c.fetchall()
    return jsonify(data)

@app.route('/getStudentById/<student_id>', methods=['GET'])
def get_student_by_id(student_id):
    c = sqlite3.connect("student.db").cursor()
    c.execute("SELECT * FROM STUDENTS WHERE id=?", (student_id,))
    data = c.fetchone()
    return json.dumps(data)    

# routes above this line
# ----------------------

# last but not least, let's get this show on the road
if __name__ == '__main__':
    app.run(port=8888)

    