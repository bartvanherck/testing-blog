title: A loop in a batch file
date: 2014-07-03 20:00:00
category: python
Summary: Sometimes we want to have a loop in a windows batch file that executes some ohter command several times. So for example the following python code.

Sometimes we want to have a loop in a windows batch file that executes some ohter command several times. So for example the following python code:

<code class="python"><pre>
for count in range(10):
    do_something()
</pre></code>

The question is now, how can this be done in a batch file? The answer is simple:

<code class="bash"><pre>
ECHO off
SET /A count=0

:loop
IF %count%==10 GOTO end
echo This is iteration %count%
SET /A %count%=%count%+1
GOTO loop

:end
echo "Done"
</pre></code>

A combination of goto and an if statement will do. Note that the set command has the option /A This option is used because otherwise the count value is not a number. Then the count value in the loop will have string values.
