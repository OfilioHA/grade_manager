from database.factories.students import StudentFactory
from app.models import Student

class StudentSeeder:

    def __init__(self, db_connection):
        self.db_connection = db_connection

    def seed(self, amount):
        students = StudentFactory().create(amount)
        for student in students:
            new_student = Student(**student)
            self.db_connection.session.add(new_student)
        self.db_connection.session.commit()

