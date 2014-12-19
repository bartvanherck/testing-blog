title: classmethods
date: 2014-07-05 20:16:16
category: python
Summary: What is a classmethod in python? It is like a staticmethod but a classmethod has a reference to a class, like a function in a class has a reference to the instantiation of the class, also named as self. Lets have a little example to start with.

What is a classmethod in python? It is like a staticmethod but a classmethod has a reference to a class, like a function in a class has a reference to the instantiation of the class, also named as self. Lets have a little example to start with.

<code class="python"><pre>
class Person(object):
    name = "" 
    given_name = "" 

    def __init__(self, given_name="", name=""):
        self.given_name = given_name
        self.name = name
</pre></code>

Suppose now that we must create a lot of persons, and the information of the names is coming from a string something like "Given_Name - Name". This means that we must create a parsing function that sets the name and given_name variable in the class. There is another way of doing this. We can also create a function that returns an instance of the class person as we create it, so in other languages it is called another constructor. 

Lets extend our example:

<code class="python"><pre>
class Person(object):
    name = "" 
    given_name = "" 

    def __init__(self, given_name="", name=""):
        self.given_name = given_name
        self.name = name

    @classmethod
    def from_str(cls, complete_name):
        name, given = complete_name.split(" - ")
        person1 = cls(given, name)
        return person1

person2 = Person.from_str("Given Name - Other Name")
</pre></code>

In fact we created a kind of factory to create a Person object from other parameters as we expected. The same can be done with a @staticmethod as shown in the code below:

<code class="python"><pre>
class Person(object):
    name = "" 
    given_name = "" 

    def __init__(self, given_name="", name=""):
        self.given_name = given_name
        self.name = name

    @staticmethod
    def from_str_2(complete_name):
        name, given = complete_name.split(" - ")
        return Person(given, name)

person3 = Person.from_str_2("Given Name - Other Name")
</pre></code>

This means that both options are valid in this case. Of course there is a BUT. If you look at the second example, you see that this creates Person objects. What happens if we subclass the Person class. For example we have a class that adds a method to print something?

<code class="python"><pre>
class Person(object):
    name = "" 
    given_name = "" 

    def __init__(self, given_name="", name=""):
        self.given_name = given_name
        self.name = name

    def display(self):
        return "My name is: {0} {1}".format(self.name, self.given_name)

    @staticmethod
    def from_str_2(complete_name):
        given, name = complete_name.split(" - ")
        return Person(given, name)

class OtherPerson(Person):
    def display(self):
        return "My Real name is: {0} {1}".format(self.given_name, self.name)
        

person3 = OtherPerson("John","Doe")
person4 = OtherPerson.from_str_2("John - Doe")

person3.display()    # returns  "My Real name is: John Doe"
person4.display()    # returns  "My Name is: Doe John"
</pre></code>

This is not what we want, we want that also in the second case, the correct display function is addressed. In this case, the @classmethod decorator is what we need to ensure that the creation of the class instance is not hardcoded.

<code class="python"><pre>
class Person(object):
    name = "" 
    given_name = "" 

    def __init__(self, given_name="", name=""):
        self.given_name = given_name
        self.name = name

    def display(self):
        return "My name is: {0} {1}".format(self.name, self.given_name)

    @classmethod
    def from_str_2(cls, complete_name):
        given, name = complete_name.split(" - ")
        return cls(given, name)

class OtherPerson(Person):
    def display(self):
        return "My Real name is: {0} {1}".format(self.given_name, self.name)
        

person3 = OtherPerson("John","Doe")
person4 = OtherPerson.from_str_2("John - Doe")

person3.display()    # returns  "My Real name is: John Doe"
person4.display()    # returns  "My Real name is: John Doe"
</pre></code>

This is the difference between a classmethod and staticmethod.
