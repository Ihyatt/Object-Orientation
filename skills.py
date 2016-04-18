# Part 1: Discussion
# What are the three main design advantages that object orientation can provide?
"""Abstraction- Hiding details we don't need.
Encapsulation-Keeping everything together.
Polymorphism-Interchangibility of components"""


# 1. What is a class?
"""Classes are a core part of object-oriented programming, and allows for interactive programming"""

# 2. What is an instance attribute?
"""Instance attributes is a variable within a class that is binded to something when a class is initialized"""

# 3. What is a method?
"""A method is similar to a function but is able to alter and object and has an argument."""

# 4. What is an instance in object orientation?
"""An instance is what occurs when you initialize a class and set the instance to equal the class"""

# 5. How is a class attribute different than an instance attribute? Give an example of when you might use each.
"""A class attribute is defined within the class not a method and set to a default for ex. name = None. A class attibute is shared with the 
entire class ands subclassess. An instance attribute is only useable within its own class and is useful when you want to call code to a unique argument or situation. 
An example a class attribute being used is when we did the the domestic and international shipping project. 
A class attribute would be used when there was intersecting functions and an instance attribute would be used when there are unique functions"""

# Parts 2 through 5:
# Create your classes and class methods
"Part 2"
#1. Student Classes

class Student(object):
    def __init__(self, first_name, last_name, addr):
        self.first_name = first_name
        self.last_name = last_name
        self.addr = addr
        self.call()

    def call(self):
        student_info = {
        "name": self.first_name,
        "lastname": self.last_name,
        "address": self.addr
        }
        print student_info


class Question(object):
    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer
        self.call()

    def call(self):
        question_and_answer = {
        "question": self.question,
        "answer": self.correct_answer
        }
        print question_and_answer



class Exam(Question):
    def __init__(self, name):
        self.name = name
        questions = []
        self.call()

    def call(self):
        midterm = {
        self.name: "Midterm",
        "question": self.questions
        }
        print midterm

    def add_question(self, question, correct_answer):
        self.question_and_answer[self.question] = self.correct_answer

    def ask_and_evaluate(self):
        quest = self.question_and_answer.key()
        answer = raw_input(quest)
        count = 0 
        if answer == self.question_and_answer[quest]:
            return True
        else:
            return False

    def administer(self):
        score = 0 
        for question in self.question_and_answer:
            if ask_and_evaluate:
                score += 1

        return score

#Part 4












