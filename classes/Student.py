class Student:
    def __init__(self, name, major, gwa, is_on_probation):
        self.name = name
        self.major = major
        self.gwa = gwa
        self.is_on_probation = is_on_probation

    def on_honor_roll(self):
        return self.gwa < 1.5
