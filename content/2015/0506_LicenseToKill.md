title: License To Kill
date: 2015-05-06 16:45:00
category: testing
featured: https://farm4.staticflickr.com/3905/15390247481_b058849b16_c.jpg
summary: Test automation, not simple. Sometimes we testers need to kill some processes. How can we do that? More in this post.

During the process of setting up a protractor test framework, I had some problems about our system. It was again the same problem as I had before. The intension of the test framework is that the testing framework can run on our integration server. So this means after each build or maybe only at night, because this contains end to end tests and running them can take a lot of time in the future.

To run on the GUI, the protractor tests need to start up a backend. That seems logical, isn’t it? Then the tests are running. Afterwards, the backend needs to be shut down. This is where the problems begin. Our system is not setup with automated testing in mind. This means that there is no way of shutting down the backend. How do I shut down or kill that process then?

There seems to be a solution. In windows, there might be a command that is called [taskkill](https://technet.microsoft.com/en-us/library/bb491009.aspx). This program acts like the kill command in unix environments. It is not that good, but it can kill the cronos.exe backend from a batch file when the tests are done.

The command I placed in my scripts are like this:
<code class="bash"><pre>taskkill /F /IM cronos.exe</pre></code>
After that I can run my test script again and again without worrying about remaining processes. 

