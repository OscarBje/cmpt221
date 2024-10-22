"""professor.py: create a table named professors in the marist database"""
from db.db import db

class Professor(db.Model):
    __tablename__ = 'Professors'
    ProfessorID = db.Column(db.Integer,primary_key=True, autoincrement=True)
    ProfessorFirstName = db.Column(db.String(40))
    ProfessorLastName = db.Column(db.String(40))
    ProfessorEmail = db.Column(db.String(40))

    # create relationship with courses table. assoc table name = ProfessorCourse
    course = db.relationship('Courses', secondary = 'ProfessorCourse', back_populates = 'Professors')
    def __init__(self, name):
        self.ProfessorFirstName = self.ProfessorFirstName
        self.ProfessorLastName = self.ProfessorLastName
        self.ProfessorEmail = ProfessorEmail

        # remove pass and then initialize attributes
    

    def __repr__(self):
        # add text to the f-string
        return f"""
            "FIRST NAME: {self.ProfessorFirstName},
             LAST NAME: {self.ProfessorLastName},
             EMAIL: {self.ProfessorEmail},
        """
    
    def __repr__(self):
        return self.__repr__()