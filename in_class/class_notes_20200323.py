import numpy as np
import pandas as pd

new_york = pd.DataFrame(
    {
        'first_name': ['Bill', 'Meghan', 'Peter', 'Carlos', 'Milton', 'Bob', 'Bob'],
        'last_name': ['Lumbergh', 'Elliott', 'Gibbons', 'Garcia', 'waddams', 'Porter', 'Slydell'],
        'job_title': ['Manager', 'Programmer', 'Programmer', 'Programmer', 'Collator', 'Consultant', 'Consultant'],
        'hire_date': [1985, 1989, 1989, 1974, 1989, 1974, 1999],
        'Contact_number': ['555-245', '544-235', '555-234', '988-224', '876-244', '874-244', '789-764'],
    }
)
washington = pd.DataFrame(
    {
        'first_name': ['Gerardo', 'Andrea', 'Pedro', 'Vicente', 'Luis', 'Ramon', 'Geral'],
        'last_name': ['Perez', 'Ramirez', 'Villamediana', 'Ostos', 'Escalante', 'Elliott', 'Shome'],
        'job_title': ['Manager', 'Programmer', 'Programmer', 'Programmer', 'Collator', 'Consultant', 'Consultant'],
        'hire_date': [1985, 1995, 1985, 1974, 1974, 1985, 1999],
        'Contact_number': ['563-245', '544-342', '555-849', '462-245', '246-234', '264-536', '246-245'],
    }
)

# in class notes ##############
new_york.head()
# Slicing with integers to get rows. Can't do columns and rows simultaneously (use iloc - below)
new_york[:3]
# Indexing with column names to get columns. Here I combined to get first three elements of a specific column
new_york['job_title'][:3]

# With iloc, slicing and indexing is just like usual in python. That way, we can use usual slicing type for both
# iloc, i is for index, loc is for location
# used to access dataframe columns and rows by position (index)
new_york.iloc[:5,2:4]

# With loc, slicing and indexing is almost like regular python
# For slicing the stop is INCLUSIVE rather than EXCLUSIVE (the usual way)
# Can acess columns and rows simultaneously
# Access dataframes by column and rows by label
new_york.loc[:3,"job_title"]

# Creating a class
class Student:
    """An abstract representation of a student.

    Attributes:
        student_count: A running tally of students.
        mean_gpa: Average GPA for all students.
        student_roster: A list of all of the students.
        gpa_list: A list of GPAs for all students
        name: The name of a specific student.
        gpa: The GPA of a specific student.
    """
    student_count = 0
    gpa_list = []
    mean_gpa = 0
    student_roster = []

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        self.__class__.student_count += 1
        self.__class__.gpa_list.append(gpa)
        self.__class__.student_roster.append(name)
        self.__class__.mean_gpa = (
                sum(self.__class__.gpa_list) /
                len(self.__class__.gpa_list)
        )

# The __init__ allows you to instantiate an instance of the class with 2 attributes.
# Then it calculates info for our class attributes (like student_roster)

# To access the doc string
print(Student.__doc__)

# Instantiate our first student
will = Student(name = "William", gpa = 4.0)

# Check type of will
type(will)
# He's in an instance of the class Student
will.name
will.gpa

# Check that our count increased by 1
Student.student_count

# Let's add another
martin = Student(name = "Martin", gpa = 3.2)

# Check that our count increased by 1
Student.student_count
Student.gpa_list
Student.mean_gpa
Student.student_roster


# Activity
# Write a MyList class so that we can instantiate and includes a head method that returns the first n elements

class MyList:
    """
    A class that build a list and allows users to get the first n elements.
    """

    def __init__(self,data):
        self.data = data

    def head(self, n=5):
        return self.data[:n]

    def tail(self, n=5):
        return self.data[-n:]

me = MyList(list(range(9)))
me.head(n = 6)
me.tail()

# Method chaining
me.head(5).count(2) # count instances of 2 in the first 5 elements of mylist

# If we want to have the class be iterable
# Add a __iter__

def search_col(df, colname, query):
    return df[df[colname].str.contains(query)]


search_col(washington, "job_title", "Prog")


def search_cols(df, query):
    return df[
        df.apply(
            lambda row: row.astype(str).str.contains(query).any(),
            axis=1
        )]


search_cols(washington, "Prog")