title: Iterators
date: 2014-09-06 11:58:07
category: python
Summary: We all know that the for loop in python is very handy. We can loop a number of times and do something each time the code is running in the loop.

We all know that the for loop in python is very handy. We can loop a number of times and do something each time the code is running in the loop.
I did try it and came with the following solution:

<code class="python"><pre>
for number in range(30):
    print(number)
</pre></code>

This is a very common code snippet. We also can loop over lists and even over dicts:

<code class="python"><pre>
a = [1,2,4,5]
for item in a:
    print(item)
 
b = { "one":1, "two":2, "three":3}
for key in b:
    print("key {} has value {}".format(key, b[key])
</pre></code>

But, should it not be very handy to loop over some class? Let’s for example create a kind of xrange, but a one that steps by value 2 and not by 1.

<code class="python"><pre>
class myRange(object):
    def __init__(self, max):
        self.number = 0
        self.max = max
 
    def __iter__(self):
        return self
 
    def __next__(self):
        if self.max > self.number:
            num = self.number
            self.number += 2
            return num
        else:
            raise StopIteration()
 
for r in myRange(10):
    print("number {}".format(r))
</pre></code>

This will print the numbers 0,2,4,6,8

As you see, the iterator must have the functions __iter__ and __next__ implemented. The __iter__ function will return the iterator itself, and the __next__ will return the next value, when it is called by the for loop. In case the iterator ends, a StopIteration exception is raised. This exception is silently ignored by the for loop and this exception means that the for loop must end.
