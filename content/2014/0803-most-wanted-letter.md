title: Most Wanted Letter
date: 2014-08-03 10:50:07
category: python
Summary: Again some nice puzzles that I solved and where the solution was much simpler than I expected. The standard libraries of python are very powerfull. We look at a first puzzle.

Again some nice puzzles that I solved and where the solution was much simpler than I expected. The standard libraries of python are very powerfull. We look at a first puzzle:

The description of the problem is as follows:

    You are given a text, which contains different english 
    letters and punctuation symbols. You should find the most 
    frequent letter in the text. The letter returned must 
    be in lower case. While checking for the most wanted letter, 
    casing does not matter, so for the purpose of your search, 
    "A" == "a". Make sure you do not count punctuation symbols, 
    digits and whitespaces, only letters.

    If you have two or more letters with the same frequency, 
    then return the letter which comes first in the latin alphabet. 
    For example -- "one" contains "o", "n", "e" only once 
    for each, thus we choose "e".

I did try it and came with the following solution:

<code class="python"><pre>
def keyf(a):
    return a[1]
    
def checkio(text):
    a = [x.lower() for x in text if x.isalpha()]
    a.sort()
    c=[(l,a.count(l)) for l in a]
    result = max(c,key=keyf)
    
    #replace this for solution
    return result[0]
</pre></code>

But there was a better and smaller solution. Just take all the letters of the alfabeth in lowercase
and take the same max key, but take the count of each letter in the original text and that it is.

<code class="python"><pre>
import string
 
def checkio(text):
    text = text.lower()
    return max(string.ascii_lowercase, key=text.count)
</pre></code>

This are fewer lines of code and make use of the string library.
