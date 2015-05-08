title: Swiping on a touch screen
date: 2015-05-08 16:45:00
category: testing
featured: https://farm6.staticflickr.com/5563/14698379281_0c719d74b3_c.jpg
summary: We had already a few months a problem on the machines touchscreen that our interface behaved differently with a finger swipe as with a mouse drag and drop.


We had already a few months a problem on the machines touchscreen that our interface behaved differently with a finger swipe as with a mouse drag and drop. The problem was that swiping from left to right was navigating to the previous page. And swiping the other way around was taking us to the next page.

Because a customer does not need to know that our interface is in fact a html page, this is unwanted behavior from user testings point of view. In the options of Chrome itself I could not find any options that could explain this behavior.

But there is a solution. Just start chrome or chromium with a command line switch.
<code class="bash"><pre>--overscroll-history-navigation</pre></code>
Did you know that chrome has a lot of command line parameters? Look at [Peter Beverloo’s page](http://peter.sh/experiments/chromium-command-line-switches/) for an overview. 

You see, as a tester you also need to think how we can solve bugs, because not all bugs are code related.
