title: Property based testing
date: 2014-12-29 14:00:00
tags: python, elixir
featured: https://farm8.staticflickr.com/7487/15949873400_3e1fa4636a_b.jpg
category: testing
summary: Property based testing, I discovered it a few days ago and it looks very promising for me. Of course python has a library for it.

What is the purpose of the testing job? Finding bugs? Understand the product we test? I think that both are true. By testing a product, we get a better understanding of what the product does, and as an artefact, we find some issues or bugs.

But finding good test input can be difficult. Even with a lot of unit tests or integration tests, still a lot of bugs get through. Maybe if we did a lot more input, less bugs get through? What if our tests generate input and validate that in our product? Property based testing does this. 

There are a lot of libraries that do a kind of property based testing. Scalacheck is an example. But because I am more interested in python and elixir, I have found other examples: [hypothesis](https://github.com/DRMacIver/hypothesis) for python and [excheck](https://github.com/parroty/excheck) for Elixir.

I did have a look at the examples and it looks very promising. I even created some dummy tests that I can run via unittests in python:
<code class="python"><pre>import unittest
from hypothesis.testdecorators import given


class TestFunctions(unittest.TestCase):
    @given (int, int)
    def test_sum_and_substract(self,x, y):
        assert (x+y) - y == x
    @given (int, int)
    def test_multiply_and_divide(self,x, y):
        if y != 0:
            assert (x*y) / y == x


if __name__ == '__main__':
    unittest.main()
</pre></code>

If this code is run, a lot of tests are injected for those 2 tests. Very handy. I am going to investigate this a little further and will report it later next year if I make progress.
