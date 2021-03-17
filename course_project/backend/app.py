from flask import Flask, json, g, request
from flask import jsonify

# from werkzeug.security import check_password_hash, generate_password_hash

# from course import CourseCreationManager, CourseSearchManager
import time
from repository import Repository
from repository.dbMysql import Database as sqldb
from section import SectionRequestManager
app = Flask(__name__)


@app.route('/api/time')
def get_current_time():
    return {'time': time.time()}


@app.route('/api/view_course', methods=["POST"])
def get_course():
    if request.method == 'POST':
        data = request.form.to_dict(flat=False)
        cleaned_data = {}
        for key, value in data.items():
            if value[0] != "":
                cleaned_data[key] = value
        # Convert data into sth section request manager can understand
        r_manager = SectionRequestManager(Repository(sqldb()))
        results, field_names = r_manager.read(cleaned_data)
        # print(cleaned_data)
        rv = convert_sql(results, field_names)
        return jsonify(results = rv)
# [(1, 'Introduction to Computer Science', 100, 'Learn how to code "Hello World!"', 'Computer Science', 1, 1, 123, 352, 142, 1, 1, 1, 2021, 'Fall', 20, 1, 123, 'Dali', 'Smith', 1, 142, 1, 40, 1)]


@app.route('/api/create_course', methods=["POST"])
def create_course():
    if request.method == "POST":
        new_data = request.form.to_dict()
        print(new_data)
        return new_data


def convert_sql(results, field_names):
    rv = [{} for _ in range(len(results))]
    for j in range(len(results)):
        for i in range(len(field_names)):
            if field_names[i] not in rv[j]:
                rv[j][field_names[i]] = results[j][i]
    return rv