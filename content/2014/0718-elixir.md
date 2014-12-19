title: First usage of elixir
date: 2014-07-18 18:08:43
category: elixir
Summary: I bought a little book of a new programming language named Elixir. The book is called Programming Elixir. I read the first two or three chapters and I must say that it is indeed different from other languages I know. 

<div style="float: right">
<img src="https://farm4.staticflickr.com/3883/14497993749_3bfd4d147d_o.jpg" style="margin: 0px 20px;"/>
</div>
I bought a little book of a new programming language named [Elixir](http://elixir-lang.org/). The book is called Programming Elixir. I read the first two or three chapters and I must say that it is indeed different from other languages I know. It has some elements of Erlang, but not all.

Then I tried to install elixir on my mac. I followed the guidelines on the [official webpage](http://elixir-lang.org/getting_started/1.html#toc_1):

<code class="bash"><pre>
brew update
brew install elixir
</pre></code>

This went fine. I could start the interactive shell with the command iex, like it was in the book.


<code class="bash"><pre>
Erlang/OTP 17 [erts-6.1] [source] [64-bit] [smp:8:8] [async-threads:10] [hipe] [kernel-poll:false] [dtrace]
Interactive Elixir (0.14.3) - press Ctrl+C to exit (type h() ENTER for help)
iex(1)> 
</pre></code>

I could do for example 3 + 4 and I saw :
<code class="bash"><pre>
iex(1)> 3 + 4
7
iex(2)> 
</pre></code>
I tried other examples and then I decided to close the shell. I did not read about a command to close the shell, so because I saw Erlang on the shell, I tried the command q. In Erlang it is q(). Therefore I also tried it as a function, but no luck. 

Aparently there is no command implemented yet to close the interactive shell correctly. What we should do is the following like it is possible in Erlang too:

<code class="bash"><pre>
CTRL-G 
press now q
</pre></code>

My first try with elixir was already ended with a call to google. Nice I would say. Let the explorer in me begin to explore the language.
