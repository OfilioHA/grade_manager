from database.seeders.student import StudentSeeder
from app.extensions.alchemy import alchemy
from bootstrap import create_app

class DatabaseSeeder:

    def __init__(self, db_connection):
        self.db_connection = db_connection

    def seed(self):
        student_seeder = StudentSeeder(self.db_connection)
        student_seeder.seed(10)


def main():
    app = create_app()
    with app.app_context():
        database_seeder = DatabaseSeeder(alchemy)
        database_seeder.seed()


if __name__ == "__main__":
    main()