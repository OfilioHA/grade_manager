from faker import Faker

class StudentFactory:

    def create(self, amount):
        return  [self._generate_student() for _ in range(amount)]

    def _generate_student(self):
        fake = Faker()
        return {
            "identification": str(fake.unique.random_number(digits=10)),
            "email": fake.unique.email(),
            "phone": fake.unique.phone_number(),
            "firstname": fake.first_name(),
            "lastname": fake.last_name(),
            "address": fake.address(),
            "gender": fake.random_element(elements=("M", "F")),
            "date_of_birth": fake.date_of_birth(minimum_age=18, maximum_age=25),
        }

