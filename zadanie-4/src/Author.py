class Author:
    def __init__(self, first_name, last_name, email):
        if type(first_name) is not str:
            raise ValueError("Podano błędne imię")
        if type(last_name) is not str:
            raise ValueError("Podano błędne nazwisko")
        if type(email) is not str:
            raise ValueError("Podano błędny email")
        self.first_name = first_name
        self.last_name = last_name
        self.email = email