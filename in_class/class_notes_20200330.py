class Employee:
    """An abstract representation of a employee.

    Attributes:
        employee_count: A running tally of employees.
        employee_list: A list of the names of all employees.
        salary_list: A list of salaries for all employees.
        mean_salary: The average salary for all employees.
        name: The name of a specific employee
        salary: The salary of a specific employee
    """
    # Class variables
    # acessible by classes and their instances
    employee_count = 0
    employee_list = []
    salary_list = []
    mean_salary = 0

    def __init__(self, name, salary): #should always start with self--self represents the instance
        # Instance attributes
        self.name = name
        self.salary = salary
        # Modifying class attributes
        self.__class__.employee_count += 1
        self.__class__.employee_list.append(name)
        self.__class__.salary_list.append(salary)
        self.__class__.mean_salary = (
                sum(self.__class__.salary_list) /
                len(self.__class__.salary_list)
        )

will = Employee("William", salary=10000)
martin = Employee("Martin", salary=30000)

will.salary

Employee.salary_list

# Instances also have access to the class variables
will.salary_list

# It doesn't make sense that we need to calculate mean salary every time we intialize since it uses the salary_list
# So let's write a better version of the class definition
class Employee:
    """An abstract representation of a employee.

    Attributes:
        employee_count: A running tally of employees.
        employee_list: A list of the names of all employees.
        salary_list: A list of salaries for all employees.
        mean_salary: The average salary for all employees.
        name: The name of a specific employee
        salary: The salary of a specific employee
    """
    # Class variables
    # acessible by classes and their instances
    employee_count = 0
    employee_list = []
    salary_list = []
    mean_salary = 0

    def __init__(self, name, salary): #should always start with self--self represents the instance
        # Instance attributes
        self.name = name
        self.salary = salary
        # Modifying class attributes
        self.__class__.employee_count += 1
        self.__class__.employee_list.append(name)
        self.__class__.salary_list.append(salary)
    def get_mean_salary(self):
        self.__class__.mean_salary = (
                sum(self.__class__.salary_list) /
                len(self.__class__.salary_list)
        )
        return self.__class__.mean_salary

# Now get_mean_salary is a method

will = Employee("William", salary=10000)
martin = Employee("Martin", salary=30000)

# Can call it from an instance
will.get_mean_salary()

# But not from the class
Employee.get_mean_salary()

# Could also set up the mean salary as a property not a method
# Probably the best way to do it in this case
class Employee:
    """An abstract representation of a employee.

    Attributes:
        employee_count: A running tally of employees.
        employee_list: A list of the names of all employees.
        salary_list: A list of salaries for all employees.
        mean_salary: The average salary for all employees.
        name: The name of a specific employee
        salary: The salary of a specific employee
    """
    # Class variables
    # acessible by classes and their instances
    employee_count = 0
    employee_list = []
    salary_list = []
    mean_salary = 0

    def __init__(self, name, salary): #should always start with self--self represents the instance
        # Instance attributes
        self.name = name
        self.salary = salary
        # Modifying class attributes
        self.__class__.employee_count += 1
        self.__class__.employee_list.append(name)
        self.__class__.salary_list.append(salary)
    @property
    def mean_salary(self):
        """Docstring"""
        return (
                sum(self.__class__.salary_list) /
                len(self.__class__.salary_list)
        )

# Now get_mean_salary is a propoerty

will = Employee("William", salary=10000)
martin = Employee("Martin", salary=30000)

# Can call it from an instance
will.mean_salary
# No error now
Employee.mean_salary

# A class method has access to the class of an instance only
# Also can have a static method. Review this next time.