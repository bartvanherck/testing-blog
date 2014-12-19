title: Basic Types in Elixir
date: 2014-10-02 18:00:00
category: elixir
Summary: Elixir has like all programming languages some types. Here is an overview of some types.

Elixir has like all programming languages some types.

Integers
--------
There are for example integers. Decimal numbers may contain underscores. It is often used to seperate 3 digits from each other to have better readability. All of the following contains valid examples of integers.

<code class="elixir"><pre>
123
100_000_000
10_0_0
</pre></code>

Atoms
-----
An Atom is a literal, a contant with a name. If you know erlang, it is the same concept, but a different layout though. They must have a leading colon (:). In erlang they must begin with a small letter. But in elixir it does not matter because the colon does identifies an atom. Atoms are used a lot in elixir. Examples:
<code class="elixir"><pre>
:ok
:test
:true
:True
</pre></code>

Tuples
------
A tuple is an ordered collection of values. Once created, a tuple can not be changed anymore. They are written between braces {} and the different elements seperated by a comma.
<code class="elixir"><pre>
{1,2}
{:ok, 1, "next"}
</pre></code>

Lists
-----
The syntax of a list is like arrays in other languages, written between [].
<code class="elixir"><pre>
[1, 2, 3]
[:ok, 2, 3]
[]
</pre></code>
You may think that this is an array, but in fact it is not. This really is a linked data structure. A list is empty or contains a head and a tail. Lists can be easily traversed linearly, but expensive to access in a random order. Like other data structures, a list is immutable. Once created, it can be never changed.

Keyword Lists
-------------
In many cases there is a need for a lists containing a key-value pair. Elixir has a shortcut for this syntax.
<code class="elixir"><pre>
[name: "P1", street: "S1"]
</pre></code>
Elixir converts this to the following:
<code class="elixir"><pre>
[ {:name, "P1"}, {:street, "S1"}]
</pre></code>
This means that the following evaluates without an exception.
<code class="elixir"><pre>
[name: "P1", street: "S1"] = [ {:name, "P1"}, {:street, "S1"}]
</pre></code>
In some cases, the outer brackets can be left out. If it is the last argument in a function call.
<code class="elixir"><pre>
Mymodule.save arg1, [name: "P1", street: "S1"]
</pre></code>
This can be written like this:
<code class="elixir"><pre>
Mymodule.save arg1, name: "P1", street: "S1"
</pre></code>
This syntax is more cleanly to write. But if you do not know this, it can be strange if you look at the source code of the save function.
