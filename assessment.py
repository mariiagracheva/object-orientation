"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.
    
    1 Abstruction
        Use an class without knowledge how it works inside  

    2 Encapsulation
        Class can be changed without affecting other parts of code

    3 Polymorohism
        Several classes can have the same method which works different ways depending on class



2. What is a class?
    Class is a template structure with attributes and certain behaviors inside itself.
    Basically attributes and methods describe class

3. What is an instance attribute?
    Attribute of certain instanse. Two different instances from one class can have different attributes

4. What is a method?
    Method is a "function inside the class". It's a part of class definition. Method is invoked on its class 

5. What is an instance in object orientation?
    Certain item from the class. Like my-pet-cat-Fluffy from the class of all-my-pets

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
   Instance attribute does not have to be the same for all instances from that class.
   But it is possible to happen that the instance attribute is the same for some instances.
   Class attribute is always the same for all instances from this class.


"""


# Parts 2 through 5:
# Create your classes and class methods
class Student(object):
    
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):
    
    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = str(correct_answer)
    
    def ask_and_evaluate(self):
        print self.question
        answer = raw_input()
        if answer == self.correct_answer:
            return True
        else:
            return False


class Exam(object):
    
    def __init__(self, name):
        self.name = name
        self.questions = []
    
    def add_question(self, question, correct_answer):
        self.question = question
        self.correct_answer = str(correct_answer)
        self.questions.append(Question(self.question, self.correct_answer))
    
    def administer(self):
        score = 0.0
        for q in self.questions:
            if q.ask_and_evaluate() == True:
                score += 1
            else:
                score = score
        print score, len(self.questions)
        return score/len(self.questions)


class Quiz(Exam):
    def administer(self):
        score = super(Quiz, self).administer()
        if score > 0.5:
            return "Passed"
        else:
            return "Failed"


def take_test(exam, student):
    student.score = exam.administer()
    return student.score

def example():
    exam = Exam('exam')

    for i in range(3):
        exam.add_question('Can you tell me what is i*2?', i*2)

    student = Student('Grace', 'Hopper', 'US')

    take_test(exam, student)
    return "Wow, " + student.first_name + " " +student.last_name + ", "+ str(student.score)











