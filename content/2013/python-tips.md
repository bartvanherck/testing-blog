title: Python tips
tags: robot framework
category: python
date: 2013-04-17 15:10:00
Summary: Because the python robot framework does need some additional libraries and our testing needs some simulators, I sometimes have to write python code myself. Here are a few tips that I use and I often forget so that I always have to search for them.

Because the python robot framework does need some additional libraries and our testing needs some simulators, I sometimes have to write python code myself. Here are a few tips that I use and I often forget so that I always have to search for them.

#### Dicts are usefull ####
I create ofthen classes that act like a dict. For this overloading a dict class is a usefull idea.
Example:

<code class="python">
<pre>class MyOwnClass(dict):
    def __init__(self, *args, **kwds):
        super(MyOwnClass,self).__init__(*args, **kwds)
        self.__dict__ = self
</pre>
</code>

Now the class MyOwnClass can be uses as a dict. Nice to know, isn't it?


#### Decoration is nice ####

Sometimes the parameters that comes from the robot framework needs to be converted to other types. Examples are strings must be converted to integers. It is possible to to in the tables itself, but then we always need the __${NUMBER}__ syntax and that is not readable enough for me. For this I decorate the entry functions that needs other types as strings.

<code class="python">
<pre>def convertToSInt(fn):
    def wrapper(self,arg):
        return fn(self,int(arg))
    return wrapper

class OneDummyTestClass(object):
    @convertToInt
    def convertThisStringToInteger(self, number):
        return type(number)
</pre>
</code>

The previous code converts my number to an integer. Of course this is not the correct way, because the decorators can have parameters and it is better to have a decorater that converts more than one paramter at a time. More of this lateron when I need that in my futurre testcases.
