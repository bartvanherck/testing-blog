title: Variable keywords in robot framework
date: 2014-07-17 23:00:42
category: python
Summary: Suppose we have a library for the robotframework with some functions that are more or less the same. For example, there are three keywords 

Suppose we have a library for the robotframework with some functions that are more or less the same. For example, there are three keywords set_parameter_a_in_module_b_to_value, set_parameter_a_in_module_c_to_value, set_parameter_a_in_module_d_to_value. Suppose now that we must set all these functions to a specific value for example the value 3. 

Then in robot framework we define a new keyword Set Parameter A

<code><pre>
\*\*\* keywords \*\*\*
Set Parameter A
    set_parameter_a_in_module_b_to_value  3
    set_parameter_a_in_module_c_to_value  3
    set_parameter_a_in_module_d_to_value  3
</pre></code>
We can now make the value to be set in a variable and input it as a parameter in the keyword

<code><pre>
\*\*\* keywords \*\*\*
Set Parameter A To Value ${Value}
    set_parameter_a_in_module_b_to_value  ${Value}
    set_parameter_a_in_module_c_to_value  ${Value}
    set_parameter_a_in_module_d_to_value  ${Value}
</pre></code>

We call this function in a test like this:

<code><pre>
\*\*\* Test Cases \*\*\*
Test For Setting All Parameters
    Set Parameter A To Value 3
</pre></code>

Ok for so far, but suppose we have more than 3 parameters, lets say 4000. This is a lot more. It is impossible to write everything out. So we must call the set parameter functions dynamically. How to do this? First create an array with the names of the variable part. And call then with a for loop the keywords. 

<code><pre>
\*\*\* Test Cases \*\*\*
Test For Setting All Parameters
    Set Parameter A To Value 3

\*\*\* keywords \*\*\*
Set Parameter A To Value ${Value}
    ${modules}=    Create List    b    c    d
    :FOR    ${module}    IN    ${modules}
    \     set_parameter_a_in_module_${module}_to_value  ${Value}
</pre></code>

This however will not work. We get a No keyword error when running such a test. I did want to have a solution to this problem, because in the current project where I am, there are several objects with more or less the same interfaces and values that needs to be sended to hardware. There was a solution for my problem, so I am very happy now. What is the solution? The keyword Run Keyword is the solution. Here is my solution to my problem: 

<code><pre>
\*\*\* Test Cases \*\*\*
Test For Setting All Parameters
    Set Parameter A To Value 3

\*\*\* keywords \*\*\*
Set Parameter A To Value ${Value}
    ${modules}=    Create List    b    c    d
    :FOR    ${module}    IN    ${modules}
    \     Run Keyword    set_parameter_a_in_module_${module}_to_value  ${Value}
</pre></code>
