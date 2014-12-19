title: Robot framework
tags: robot framework
category: python
date: 2013-04-09 20:32:00


> Robot Framework is a generic test automation framework for acceptance testing and acceptance test-driven development (ATDD).  It has easy-to-use tabular test data syntax and utilizes the keyword-driven testing approach. Its testing capabilities can be extended by test libraries implemented either with Python or Java, and users can create new keywords from existing ones using the same syntax that is used for creating test cases.


These are the words that can be read in the README file from the Robot Framework if you download it via mercurial. I use this framework everyday now to test our code. It is so extensible that I prefer it over other frameworks. The fact that it is written in python is a pro for me.

<div style="float: right"><img src="http://2.bp.blogspot.com/-tdbn8bIW-UY/UWRbjmwGk4I/AAAAAAAAABs/qCLRJ_3lMOI/s200/robotframework.png" /></div>

Because of this, the framework is cross platform. And it is cross platform, I have tested and used it on both linux and windows. There is another plus. It is not needed to install it on your system. This because the python code runs out of the box if the correct PYTHONPATH variable is set.

The robotframework is mirrored in our local version control system. In case the upstream code disappears at some point, you never know, we still have the code. To start testing, a new tester or a developer just clones the robotframework code. Afterwards, the test libraries and test data is checked out, because these are also version controlled. And starts a script to run all Testcases. Our script is called: runAllTestcases.bat or runAllTestcases.sh, depending on the platform you are on.

The script handles the rest. The script runs in fact just the rebot command:


<code class="bash"><pre> 
pybot --name Example path/to/tests/pattern_*.html 
</pre></code>


But that was not enough. The pybot command is everytime on exact the same relative path. For this, the script changes the PATH variable. But changing the PATH variable is not enough, there is also a PYTHONPATH that must be set to the correct path.

In this case, we just can run all our testcases with a simple script. The script can be plugged into our jenkins integration buildserver and we are testing on the fly.
