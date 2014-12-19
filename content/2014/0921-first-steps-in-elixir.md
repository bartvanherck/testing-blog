title: first steps in elixir
date: 2014-09-21 18:28:43
category: elixir
Summary: Elixir, the language of the future? For me it looks a promising language. I do like the programming language erlang and python, but I assume that elixir can be handy for testing purposes too. The concepts look like erlang according to me. Lets have a first overview of assignments.

Elixir, the language of the future? For me it looks a promising language. I do like the programming language erlang and python, but I assume that elixir can be handy for testing purposes too. The concepts look like erlang according to me. Lets have a first overview of assignments.

Suppose there is a variable and a number must be assigned to it. In any programming language that I know it is something like

<code class="elixir"><pre>
iex(1)> var_a = 5
5
</pre></code>

It seems that is is the same as in python or c, or whatever. But in fact this assignment is like in erlang. It is an evaluation, or just a pattern match. Ask always, what has to be done to evaluate this to be valid mathematically. Right, set the value of var_a to 5. For this the evaluation can be done in the other order, only if var_a has already a value. In case var_a did not have a value, a runtime error is raised.

<code class="elixir"><pre>
iex(1)> var_a = 5
5
iex(2)> var_a
5
iex(3)> 5 = var_a
5
iex(4)> 5 = var_b
** (RuntimeError) undefined function: var_v/0
</pre></code>

If another value is evaluated, for example 3, then a ValueError is raised.

<code class="elixir"><pre>
iex(4)> 3 = value_a    
** (MatchError) no match of right hand side value: 5
</pre></code>

Lists can be bound to a variable:

<code class="elixir"><pre>
iex(6)> lst = [1, 2, 3]
[1, 2, 3]
iex(7)> lst = [a, b, c]
** (RuntimeError) undefined function: b/0    
iex(7)> [a, b, c] = lst
[1, 2, 3]
iex(8)> a
1
iex(9)> b
2
iex(10)> c
3
</pre></code>

Command number 6 stores a list in a variable lst.  Now, place it to another list. This can only be done with variables if the variable is on the left side, otherwise the code seems to think that the variables are functions. A kind of pattern matching occurs. lst is a list containing 3 elements. This can be matched by the list with the three variables a, b and c. So the variables are filled in with the correct values.

In case the list is more complex, this pattern matching is the same:

<code class="elixir"><pre>
iex(11)> lst = [1,[2,3],[3,[4,5]]]  
[1, [2, 3], [3, [4, 5]]]
iex(12)> [a,b,c] = lst
[1, [2, 3], [3, [4, 5]]]
iex(13)> a
1
iex(14)> b
[2, 3]
iex(15)> c
[3, [4, 5]]
</pre></code>

But it is also possible to fill in some values to at the left side.

<code class="elixir"><pre>
iex(17)> lst=[1,3,2]
[1, 3, 2]
iex(18)> [a,3,b] = lst
[1, 3, 2]
iex(19)> a
1
iex(20)> b
2
</pre></code>

This is not too difficult to understand, no? There is also a kind of everything matches operator, or a don’t care. It is just an underscore, like in erlang or in python.

<code class="elixir"><pre>
iex(24)> [1,_,b] = lst
[1, 3, 2]
iex(25)> b
2
iex(26)> [_,_,b] = lst
[1, 3, 2]
iex(27)> [_,_,b] = [1,2,3]
[1, 2, 3]
iex(28)> [_,_,b] = [2,2,3]
[2, 2, 3]
iex(29)> [_,_,b] = [2,2,3]
iex(30)> lst = [1,[2,3],[3,[4,5]]]
[1, [2, 3], [3, [4, 5]]]
iex(31)> [a,b,_] = lst            
[1, [2, 3], [3, [4, 5]]]
iex(32)> a
1
iex(33)> b
[2, 3]
</pre></code>

Here some more complex pattern matches are shown. The command 31 for example shows that it does not matter what is in the last element of the list. It can be a single value, or a list or a list in a list and so on.

There are other concepts in this language that we can handle. A variable can be evaluated or matched only once in one statement. For example

<code class="elixir"><pre>
iex(38)> [a,a] = [1,1]
[1, 1]
iex(39)> a
1
</pre></code>

A last issue that I want to handle is the pin operator. In erlang for example a variable can be set to a value only one time. In elixir it is possible to have that behaviour too, if an ^ is preceeded by a variable name.

<code class="elixir"><pre>
iex(40)> a = 4
4
iex(41)> ^a = 4
4
iex(42)> ^a = 5
** (MatchError) no match of right hand side value: 5
</pre></code>

Value 4 is placed into variable a. If ^a is used, then it can be evaluated if the right side is the same as what was already in the variable a. The variable can not be set a to 5 if a is preceeded by a ^. Some other examples are shown in the next code snippet.

<code class="elixir"><pre>
iex(45)> lst = [1,2,3]
[1, 2, 3]
iex(46)> a=1
1
iex(47)> [^a,b,3] = lst
[1, 2, 3]
iex(48)> a
1
iex(49)> b
2
iex(50)> [^a,b,3] = [2,3,1]
** (MatchError) no match of right hand side value: [2, 3, 1]
</pre></code>
This operator operates inside of lists too. To conclude: the sign = is not an assignment, but an evaluation and the language tries to evaluate to True. This can be done by assigning some values to variables.

In a next post, I am going to cover other aspects of the elixir language.
