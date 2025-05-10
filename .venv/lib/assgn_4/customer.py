import person
class Customer(person.Person):
    def __init__(self, first_name, last_name, email):
        person.Person.__init__(self, first_name, last_name)
        super().__init__(first_name, last_name)
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def __iter__(self):
        # Define how the object is iterated over
        return iter([self.first_name, self.last_name, self.email])
