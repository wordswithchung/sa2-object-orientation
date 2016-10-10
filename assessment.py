"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

The three main design advantages of OO:
- abstraction means you don't need to know info that a method uses internally,
saving you time from having to go through source code; you can just use it!
- encapsulation means that the data lives close to its functionality and you're
bundling behavior with data.
- polymorphism means it's easy to make different, interchangable types of
things that are customizable (e.g., dogs and cats are both of the animal class,
but they have different greetings for each subclass because its customized).

2. What is a class?

A class is a core part of object-oriented programming. It's something that the
programmer can customize -- what it is, what it means, its attributes, what it
can do -- depending on what she's looking to achieve in her program.

3. What is an instance attribute?

An instance attribute is an attribute or characteristic tied to a specific 
object (or instance). For example, if you have a class of math students and 
one instance is student Jane Chen, you can set Jane's grade attribute 
specifically to whatever her grade for the class is (presumably "A", because 
Jane is great at math!). The "A" is Jane Chen's (instance) attribute.

4. What is a method?

A method is similar to a function but is specifically tied to a class. This is 
an example of the encapsulation design advantage mentioned above.

5. What is an instance in object orientation?

An instance is one specific occurence / creation from a class. For example, 

    chung_nguyen = EnglishMajors("Chung", "Nguyen")

In this case, chung_nguyen is a specific instance of the EnglishMajors class 
and she has the first name "Chung" and last name "Nguyen", assigned at the 
point of instantiation (via the __init__ method).

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

A class attribute belongs to the entire class, whereas an instance attribute 
is specific to that instance / object. When returning attributes, Python will 
start at the instance level first and then move up to the class level if no 
such value exists. 

A great way to use this is to additionally customize your instances. For 
example:

class Fruits(object):
    delicious = True

durian = Fruits()
durian.delicious = False
durian.stinky = True

In this example, the class attribute (default for the class, basically) is that 
all fruits of the fruits class is truly delicious. Unfortunately, durian is 
not. (It's a very, very, very specifically acquired taste. And is generally, 
arguably NOT delicious.) Because of its lack of deliciousness, the instance 
attribute for durian has been set to False. 

"""


# Parts 2 through 5:
# Create your classes and class methods

class Student(object):
    """Student info including: first_name, last_name, and address."""

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):
    """Questions with answers: question and correct_answer."""

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        if raw_input(self.question + " > ") == self.correct_answer:
            return True
        else:
            return False


class Exam(object):
    """Exam for students: name (e.g., midterm) with list of questions."""

    def __init__(self, name):
        self.name = name
        self.questions = []

    def add_question(self, question, correct_answer):
        self.questions.append(Question(question, correct_answer))

    def administer(self):
        score = 0
        for question in self.questions:
            if question.ask_and_evaluate():
                score += 1
        return score


class Quiz(Exam):
    """Quiz inherits from Exam. Score is Pass or Fail."""

    def administer(self):
        score = super(Quiz, self).administer()
        return score >= (len(self.questions) / 2.0)


def take_test(exam, student):
    score = 0
    student.score = exam.administer()


def example():
    """Function does the following:

    - creates an exam
    - adds a few questions to the exam
    - creates a student
    - administers the test for that student
    """

    exam = Exam("Finals")
    exam.add_question("What's the largest lake in the US?", "Lake Superior")
    exam.add_question("What't the smallest country in the world?",
                      "Vatican City")
    exam.add_question("What's the most popular name in the world?", 
                      "Muhammad")
    student = Student("Chung", "Nguyen", "123 Main Street")
    take_test(exam, student)
    print student.score


example()


