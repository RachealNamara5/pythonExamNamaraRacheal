from flask import Blueprint, request, jsonify
from app.models.student import Student, db

student_blueprint = Blueprint('student', __name__, url_prefix='/api/v1/student')

@student_blueprint.route('/register', methods=['POST'])
def register_student():
    try:
        
        data = request.json
        firstname = data.get('firstname')
        lastname = data.get('lastname')
        origin = data.get('origin')
        course = data.get('course')

        # Basic input validation
        if not all([firstname, lastname, origin]):
            return jsonify({"error": 'All fields are required'}), 400

        # Creating a new student
        new_student = Student(
            firstname=firstname,
            lastname=lastname,
            origin=origin,
            course=course,
        )

        db.session.add(new_student)
        db.session.commit()

        # Building a response message
        message = f"Student '{new_student.firstname}' with ID '{new_student.id}' has been registered"
        return jsonify({"message": message}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@student_blueprint.route('/update/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    try:
        
        student = Student.query.get(student_id)
        
        if not student:
            return jsonify({"error": f"Student with ID {student_id} not found"}), 404

        
        data = request.json
        firstname = data.get('firstname', student.firstname)
        lastname = data.get('lastname', student.lastname)
        origin = data.get('origin', student.origin)
        course = data.get('course', student.course)

        
        student.firstname = firstname
        student.lastname = lastname
        student.origin = origin
        student.course = course

        db.session.commit()

        message = f"Student '{student.firstname}' with ID '{student.id}' has been updated"
        return jsonify({"message": message}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    

# to retrieve details about a specific user from database
@student_blueprint.route('/<int:student_id>', methods=['GET'])
def get_student(student_id):
    try:
        
        student = Student.query.get(student_id)
        
        if not student:
            return jsonify({"error": f"Student with ID {student_id} not found"}), 404

      
        student_data = {
            "id": student.id,
            "firstname": student.firstname,
            "lastname": student.lastname,
            "origin": student.origin,
            "course": student.course
        }

        return jsonify(student_data), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
