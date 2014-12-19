title: Keeping non unique items in a list
date: 2014-07-31 20:16:16
Category: python
Summary: I tried a new game at http://checkio.org. This is a kind of game for programmers. Learn you programming skills by playing a game. Cool, not? The game contains some kind of problems you need to solve. An interactive programming 

I tried a new game at [http://checkio.org](http://checkio.org). This is a kind of game for programmers. Learn you programming skills by playing a game. Cool, not? The game contains some kind of problems you need to solve. An interactive programming environment is at your service in this game. 
The first problem however was not so simple. I never needed that problem at this point, but it revealed some new things for me.

The problem is simple: I have an array of items. Just delete all items that are not unique in the list and return the other values as a list, with all duplicates in it and in the same order. For example:

<code><pre>
[1, 2, 3, 2, 1] must return [1,2,2,1]
[1, 3, 1, 3, 2, 3] must return [1, 3, 1, 3, 3]
[5, 5, 5, 5, 5, 5] must return [5, 5, 5, 5, 5, 5]
</pre></code>

I did try it and did not have a solution except looping through the array and implementing some obscure algorithm in a function. But I wanted to do this in a small function, preferrable by a list comprehension or maybe 2 of them. Then I discovered iteritems and came to this solution


<code class="python"><pre>
from collections import Counter

def nonuniques(data):
    k = {k for (k,v) in Counter(data).iteritems() if v > 1}
    return [x for x in data if x in k]
</pre></code>

This solution works but was not that optimal because it uses an intermediate set. It could be better, and this I saw in the solutions of the problem:

<code class="python"><pre>
nonuniques=lambda d:[x for x in d if d.count(x)>1]
</pre></code>

There is a count function on a list. I totally forgot that! With this it could be solved as a oneliner that is easier to read as my solution, and is that not where it is all about? To create code that is readable so it contains less bugs.
