import re

class Student:
    def __init__(self, name, age=13, grade="12th") -> None:
        self._name = name
        self._age = age
        self._grade = grade
    
    @property
    def get_name(self):
        return self._name
    
    @get_name.setter
    def set_name(self, new_name):
        if isinstance(new_name, str) and len(new_name) >= 3:
            new_name = re.sub(r'[^a-zA-Z]', "", new_name)
            self._name = new_name.title()
        else:
            print("Name must have at least three characters")
    
    @property
    def get_age(self):
        return self._age
    
    @get_age.setter
    def set_age(self, new_age):
        if isinstance(new_age, int) and 11 <= new_age <= 18:
            self._age = new_age
        else:
            print("Age must be a number between 11 and 18")

    @property
    def get_grade(self):
        return self._grade
    
    @get_grade.setter
    def set_grade(self, new_grade):
        try:
            grade = int(re.sub(r'[^\d]', '', new_grade))
            if 9 <= grade <= 12:
                self._grade = f"{grade}th"
            else:
                print("Grade must be formatted as between 9th and 12th grade")
        except ValueError:
            print("Invalid grade format. Please use numeric format (e.g., '12th').")


    def __str__(self):
        return f"Name: {self._name}\nAge: {self._age}\nGrade: {self._grade}"
    
    def advance(self, years_advanced):
        current_grade = int(re.sub(r'[th]', "", self.get_grade))
        print(current_grade)
        new_grade = current_grade + years_advanced
        print(new_grade)
        self.set_grade = f'{new_grade}th'
        # self._grade = f"{new_grade}th"
        
        # self.set_grade(new_grade)



    def study(self, subject):
        return f"{self._name} is studying {subject}"
