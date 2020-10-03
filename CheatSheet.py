#if __name__=="__main__":
    
    #a.py
    print(__name__)
    def func1():
        print("function 1")
    def main():
        print("main function")	
    if __name__=="__main__":
        main()

    #b.py
    import a
    print(__name__)
    a.func1()


#################################################################################################

    '''
    This is a 
    multiline string

    '''

    sttr = "This is me"
    age = 21
    weight = 75.5
#################################################################################################
#Arithmetic operations

    print("The value of 3 + 5 = ", 3+5)
    print("The value of 3 - 5 = ", 3-5)
    print("The value of 3 * 5 = ", 3*5)
    print("The value of 3 / 5 = ", 3/5)
    print("The value of 3 ** 5 = ", 3**5)
    print("The value of 3 // 5 = ", 3//5)

    print("This is a \"")
    mls = ''' this is a multiline

    string and this will keep 
    going'''
    print(mls)
#################################################################################################
    print("%s to the right"%('this is a string'))
    print('this is print statement 1', end="")
    print('this is print statement 2')
    print("this "*50)
#################################################################################################
# Strings

    string_ = "this is me"
    
    print(string_[0:2])
    
    print(string_[-2:])
    
    print(string_[:-2])
    
    print(string_.capitalize())

    print(string_.replace("is", "are"))
    
    if string_.find("this")>=0:
        print("found")

    if string_.startswith("this")>=0:
        print(string_)

#################################################################################################
    
    print("My name is {} {}".format("Parth","Sharma"))

#################################################################################################
    
    print(" and ".join(list1))

#################################################################################################
# If else statements

    print("Enter Your Marks")
    number = int(input())
    print(number)

    if (number>90 or number<100):
        grade = 'A'
    elif (number>80 and number<100):
        grade = 'B'
    else:
        grade = 'Dont Know'

    print("The grade is", grade)
#################################################################################################
# loops

    print("How many times do you want to execute")
    no = int(input())
    for i in range(0,no):
        print(i)
    list1 =[[1,2,3], [4,5,6], [7,8,9]]
    for item in list1:
        for i in item:
            print(i)
#################################################################################################
# while loops

    print("Enter a number")
    number = int(input())

    while(number>4):
        print("Number is greater than 4")
        number = int(input())
        if (number ==9):
            break
        if number ==8:
            continue
        print("loop ended")

#################################################################################################
#iterators,iterables,genrators

    def gen(n):
        for i in range(n):
            yield(i)

    obj1=gen(10)
    while(obj1):
        print(next(obj1))

    num="harry"
    iter1=iter(num)
    print(next(iter1))
    print(next(iter1))


#################################################################################################
# Lists

    colleges = ['IIT', 'NIT', 'College of engineering']

    print(colleges[2])

    colleges[2] = "COE"

    print(colleges[2])
    print(colleges)
    print(colleges[1:3])
    list2 = ['table', 'chair', 'fan', 'clothes', 'bottle']

    # list2.append('microphone')
    list2.insert(3, 'microphone')
    print(list2)
    list2.remove('microphone')
    print(list2 + ['pillow', 'tubelight', 'bed'])
    print(list2)
    print(len(list2))
    print(max(list2))
    print(min(list2))
#################################################################################################
    list1=[0,1,2,3,4,5,6,7,8,9]
    print(list1[0::2])

#################################################################################################
    import bisect
    list1=[0,1,2,3,4,5,6,7,8,9]
    print(bisect.bisect(list1,3.5))
    print(bisect.insort(list1,3.5))
    print(list1)

#################################################################################################
#Enumerate
    list1=[0,1,2,3,4,5,6,7,8,9]
    for count,ele in enumerate(list1):
        print(count,ele)

#################################################################################################
# Tuples

    tup1 = (1, 2, 3)
    list1 = list(tup1)
    print(list1)
    print(tup1[0])
#################################################################################################
# Dictionaries

    names = {'Harry': 22,
            'Shubham': 41,
            'Jyoti': 19,
            'Ramdev': 82}

    for key,val in names.items():
        print(key,val)

    print(names['Ramdev'])
    names['Ramdev'] = 55
    print(names['Ramdev'])

    print(names.keys())
    print(names.values())
#################################################################################################
#List Comprehension, Dictionary Comprehension And Generator Comprehension

#List Comprehension
    list1=[0,1,2,3,4,5,6,7,8,9]
    print("list comprehensions",[item for item in list1 if(item%3==0)])

#Dictionary Comprehension
    list1=[0,1,2,3,4,5,6,7,8,9]
    list2=["a","b","c","d","e","f","g","h","i","j"]
    print({i:j for i in list1 for j in list2})

#Set Comprehension
    print(sorted( {i**2 for i in [1,1,1,2,4,7,3,3,5,7,8,2,9]} ))

# Generator Comprehensions:
    gen=(i for i in range(100) if(i%3==0))
    obj1=gen
    for i in obj1:
        print(i)


#################################################################################################
#Map, Filter and Reduce in Python

#Map
    list1=[0,1,2,3,4,5,6,7,8,9]
    def func1(n):
        return (n**2)+(2*n)+1
    print(list(map(func1,list1)))

#Filter
    list1=[0,1,2,3,4,5,6,-2,-3,-1]
    def func1(n):
        if(n>2):
            return True
        else:
            return False	
    print(list(filter(func1,list1)))

#Reduce
    from functools import reduce
    def func1(a, b):
        return a+b
    print(reduce(func1,[0,1,2,3,4,5,6,7,8,9]))


#################################################################################################
#*args and **kwargs

    def func1(*kuchbhi,**anokhi):
        for i in kuchbhi:
            print(i)
        for key,value in anokhi.items():
            print(key,value)
    a=[1,2,3]
    b={"d":4,"e":5,"f":6}
    func1(*a,**b)


#################################################################################################
# Functions and __doc__string

    def average(num1, num2):
        """this is program for average"""
        return (num1+num2)/2

    print(average(2, 3))
    print(average.__doc__)


#################################################################################################
#Decorators In Python
    def dec1(func1):
        def nowexec():
            print("Executing now")
            func1()
            print("Executed")
        return nowexec

    @dec1
    def who_is_harry():
        print("Harry is a good boy")

    # who_is_harry = dec1(who_is_harry)

    who_is_harry()


    def dec1(rule):
        print(rule)
        def nowexec(func1):
            print("Executing now")
            func1()
            print("Executed")
        return nowexec

    @dec1("/")
    def who_is_harry():
        print("Harry is a good boy")


#################################################################################################
#Lambda

    add= lambda x,y:x+y
    print(add(3,4))

    list1=[(1,2),(3,1),(4,5),(5,6)]
    list1.sort(key=lambda x: x[1])
    print(list1)


#################################################################################################
#Function Caching In Python
    import time
    from functools import lru_cache

    @lru_cache(maxsize=32)
    def some_work(n):
        #Some task taking n seconds
        time.sleep(n)
        return n

    if __name__ == '__main__':
        print("Now running some work")
        some_work(3)
        some_work(1)
        some_work(6)
        some_work(2)
        print("Done... Calling again")
        input()
        some_work(3)
        print("Called again")
    

#################################################################################################
# File IO

    #"r"= file for reading
    #"w"= file for writing
    #"x"= create if not exist
    #"a"= append
    #"t"= text mode
    #"b"= binary
    #"+"= read and write


    file1 = open("harry.txt", "wb")
    print(file1.mode)
    print(file1.name)
    file1.write(bytes("Write this to my file", "UTF-8"))
    file1.close()

# file io - reading the content of a file

    file1 = open('harry.txt', 'r+')
    text_to_read = file1.read()
    print(text_to_read)
    file1.close()

#file pointer

    print(file1.tell())
    print(file1.seek())

#Using With Block To Open Python Files

    # file1 = open("harry.txt", "wb")
    # print(file1.mode)
    # print(file1.name)
    # file1.write(bytes("Write this to my file", "UTF-8"))
    # file1.close()
    with open("harry.txt", "wb") as f:
        print(file1.mode)
        print(file1.name)
        file1.write(bytes("Write this to my file", "UTF-8"))


#################################################################################################
 # try/except blocks let you catch and we can 
 # manage exception or add custom exceptions.
 # Exceptions can be triggered by raise, assert, 
 # and a large number of errors such as trying 
 # to index an empty list or Integrity errors.

#try,except,else,finally

    try:
        print("try block")
        #open("ok.txt")
    except Exception as e:
        print("exception block ",e)
    else:
        print("else block")
    finally:
        print("finally block")

# assert
# assert - raise an 
# exception if a given condition is not met an error is raised
# used for testing

    list_ = ["a","b","c"]
    assert "x" in list_, "x is not in the list"
    print("passed")

#Raise In Python
    # a = input("What is your name")
    # b = input("How much do you earn")
    # if int(b)==0:
    #     raise ZeroDivisionError("b is 0 so stopping the program")
    # if a.isnumeric():
    #     raise Exception("Numbers are not allowed")
    #
    # print(f"Hello {a}")
    # 1000 lines taking 1 hour

    # Task - Write about 2 built in exception

    c = input("Enter your name")
    try:
        print(a)

    except Exception as e:

        if c =="harry":
            raise ValueError("Harry is blocked he is not allowed")

        print("Exception handled")


# assert vs raise : used when u want to stop the script rasie when u want a custom error


#################################################################################################
# Object oriented programming
    class Employee:

        def __init__(self, name, id, salary):
            self.__name = name   # __for private variable using name mangling
            self.__id = id
            self.__salary = salary


        def set_name(self, name):
            self.__name = name

        def get_name(self):
            return self.__name

        def set_id(self, id):
            self.__id = id

        def get_id(self):
            return self.__id

        def set_salary(self, salary):
            self.__id = salary

        def get_salary(self):
            return self.__salary

    harry = Employee('harry', 420, 70000000)
    print(harry._Employee__name)
    print(harry.get_salary())


#Class Methods and class variables In Python
    class Employee:
        no_of_employees=0

        def __init__(self,name,id,salary):
            self.name=name
            self.id=id
            self.salary=salary
            #Employee.no_of_employees+=1
            self.inc_employee()

        @classmethod
        def inc_employee(cls):
            cls.no_of_employees+=1
        
    parth=Employee("parth",21,1000000000000)
    harry=Employee("harry",21,1000000000000)
    smrati=Employee("smrati",21,1000000000000)
    print(smrati.no_of_employees,smrati.name,smrati.salary,smrati.id)


    class Employee:  
        def __init__(self, id,name,cost):
            self.name = name
            self.cost = cost
            Employee.identity=id

    jhk = Employee(1,'pyaaz',70)
    kjk = Employee(2,'kaju',20)
    hkk = Employee(3,'tamatar',50)
    print(hkk.identity,hkk.salary)
    print(kjk.identity,kjk.salary)
    print(jhk.identity,jhk.salary)


#Class Methods As Alternative Constructors and static methods
    from datetime import date 
    
    class Person: 
        def __init__(self, name, age): 
            self.name = name 
            self.age = age 
        
        # a class method to create a Person object by birth year. 
        @classmethod
        def fromBirthYear(cls, name, year): 
            return cls(name, date.today().year - year) 
        
        # a static method to check if a Person is adult or not. 
        @staticmethod
        def isAdult(age): 
            return age > 18

    person1 = Person('mayank', 21) 
    person2 = Person.fromBirthYear('mayank', 1996) 
    
    print person1.age 
    print person2.age 
    print Person.isAdult(22) 


#Super() and Overriding In Classes
    class A:
        classvar1 = "I am a class variable in class A"
        def __init__(self):
            self.var1 = "I am inside class A's constructor"
            self.classvar1 = "Instance var in class A"
            self.special = "Special"

    class B(A):
        classvar1 = "I am in class B"

        def __init__(self):
            self.var1 = "I am inside class B's constructor"
            self.classvar1 = "Instance var in class B"
            super().__init__()
            print(super().classvar1)

    a = A()
    b = B()
    print(b.special, b.var1, b.classvar1)


#Abstract Base Class & @abstractmethod
    from abc import ABCMeta,abstractclassmethod
    class shape(metaclass=ABCMeta):
        @abstractclassmethod
        def area():
            return 0

    class rectangle(shape):
        type="rectangle"
        sides=4
        def __init__(self):
            self.length=7
            self.breadth=4
        
    r=rectangle()


#Setters & Property Decorators
    class Employee:
        def __init__(self, fname, lname):
            self.fname = fname
            self.lname = lname
            # self.email = f"{fname}.{lname}@codewithharry.com"

        def explain(self):
            return f"This employee is {self.fname} {self.lname}"

        @property
        def email(self):
            if self.fname==None or self.lname == None:
                return "Email is not set. Please set it using setter"
            return f"{self.fname}.{self.lname}@codewithharry.com"

        @email.setter
        def email(self, string):
            print("Setting now...")
            names = string.split("@")[0]
            self.fname = names.split(".")[0]
            self.lname = names.split(".")[1]

        @email.deleter
        def email(self):
            self.fname = None
            self.lname = None
    hindustani_supporter = Employee("Hindustani", "Supporter")
    # nikhil_raj_pandey = Employee("Nikhil", "Raj")
    print(hindustani_supporter.email)
    hindustani_supporter.fname = "US"
    
    print(hindustani_supporter.email)
    hindustani_supporter.email = "this.that@codewithharry.com"
    print(hindustani_supporter.fname)

    del hindustani_supporter.email
    print(hindustani_supporter.email)
    hindustani_supporter.email = "Harry.Perry@codewithharry.com"
    print(hindustani_supporter.email)


#################################################################################################
#Dunder Methods
    class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __repr__(self):
        return f"Employee('{self.name}', {self.salary}, '{self.role}')"

    def __str__(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    emp1 =Employee("Harry", 345, "Programmer")
    # emp2 =Employee("Rohan", 55, "Cleaner")
    print(str(emp1))


#################################################################################################
#virtualenv

    #sudo su   #syatem wide access
    #first install pip3 or upgrade if it is pre installed
    #pip install --upgrade pip
    #pip3 install --upgrade virtualenv

    virtualenv enviroment1
    source enviroment1/bin/activate
    pip freeze > requirements.txt
    pip install -r requirements.txt
    deactivate
    virtualenv --system-site-packages enviroment2
    
    # to upgrade all packages put packages in requirement.txt and put >= instead of ==


#################################################################################################
# Regular Expression

    '''
    .       - Any Character Except New Line
    \d      - Digit (0-9)
    \D      - Not a Digit (0-9)
    \w      - Word Character (a-z, A-Z, 0-9, _)
    \W      - Not a Word Character
    \s      - Whitespace (space, tab, newline)
    \S      - Not Whitespace (space, tab, newline)

    \#b      - Word Boundary
    \B      - Not a Word Boundary
    ^       - Beginning of a String
    $       - End of a String

    []      - Matches Characters in brackets 1 or More
    [^ ]    - Matches Characters NOT in brackets
    |       - Either Or
    ( )     - Group

    Quantifiers:
    *       - 0 or More
    +       - 1 or More
    ?       - 0 or One
    {3}     - Exact Number
    {3,4}   - Range of Numbers (Minimum, Maximum)


    #### Sample Regexs ####

    [a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+

    '''

    # import re
    # pattern = re.compile(r"abc")
    # cache = ""
    # with open("regular_exp/sample.txt", "r") as f:
    #   for x in f:
    #       cache = cache + x
    # matches = pattern.finditer(cache)
    # for match in matches:
    #   print(cache[match.span()[0]:match.span()[1]])


    # import re
    # s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
    # lst = re.findall('\\S+@\\S+', s)
    # print(lst)


#################################################################################################
# Threading






#################################################################################################
# MultiProccesing







#################################################################################################
# Asyncio coroutines







#################################################################################################
# Coroutines
    import time
    def searcher():
        time.sleep(4)
        book="parth sharma"
        print("1")

        while True:
            text = (yield)
            if text in book:
                print("Your text is in the book")
            else:
                print("Text is not in the book")

    search = searcher()
    next(search)
    search.send("parth")
    search.close()



#################################################################################################
# flask

    export FLASK_APP=target
    export FLASK_ENV=development
    flask run



#################################################################################################
# Extras

    print(a//b) #floor quotient
    print(a/b) #divisor
    print(a%b) #remainder
    global i
    #----------------------------------------------------------------------
    v = [None]*3
    pythlist = list(range(3))
    #----------------------------------------------------------------------
    abs()
    #----------------------------------------------------------------------
    import sys
    sys.maxsize
    #----------------------------------------------------------------------
    max(list1)
    #----------------------------------------------------------------------
    list1.count()
    #----------------------------------------------------------------------
    grades=[]
    for i in range(0,3):
        grades+=[int(input())]
    #----------------------------------------------------------------------
    bool(8 in range(7,10))
    #----------------------------------------------------------------------
    print("{:.6f}".format(your value here))
    #----------------------------------------------------------------------
    ##print((5/1).is_integer())
    print(5/2==int(5/2))
    #----------------------------------------------------------------------
    try:
        z = x / y
    except Exception as e:
        z = 0
    #----------------------------------------------------------------------
    px,py,qx,qy=map(int,input().split(" "))
    #----------------------------------------------------------------------
    list1=list(map(int,input().strip().split(" ")))
    #----------------------------------------------------------------------
    sum(i for i in list1)
    #----------------------------------------------------------------------
    for i in reversed(li):
        print(i)
    for i, e in reversed(list(enumerate(a))):
        print(i, e)
    #----------------------------------------------------------------------
    for (a, b, c) in zip(num, color, value):
        print (a, b, c) 
    #----------------------------------------------------------------------
    li = [[ 0 for i in range(llen)] for i in range(llen)]
    li = [[0]*n]*n
    #----------------------------------------------------------------------
    add= lambda x,y:x+y
        print(add(3,4))

    #Map
        list1=[0,1,2,3,4,5,6,7,8,9]
        def func1(n):
            return (n**2)+(2*n)+1
        print(list(map(func1,list1)))

    #Filter
        list1=[0,1,2,3,4,5,6,-2,-3,-1]
        def func1(n):
            if(n>2):
                return True
            else:
                return False	
        print(list(filter(func1,list1)))

    #Reduce
        from functools import reduce
        def func1(a, b):
            return a+b
        print(reduce(func1,[0,1,2,3,4,5,6,7,8,9]))
    #----------------------------------------------------------------------
