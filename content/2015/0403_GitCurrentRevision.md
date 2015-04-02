title: How to show the current revision?
date: 2015-04-03 21:01:20
tags: git
category: other
featured: https://farm8.staticflickr.com/7549/15951252540_de4c241fcf_c.jpg
summary: How can you show the current revision that is checked out in git?


Sometimes I want to know which is the current revision in a repository that I am on. I always did just git log and watched the output. But log has some nice features, it can almost output everything you like it in the way you want.
To show the short revision number, just running
<code class="bash"><pre>
  git log --pretty=foramt:'%h' -n 1 
</pre></code>
is enough. Of course you can create an alias for it:
<code class="bash"><pre>
  git config --global alias.revision "log --pretty=format:'%h' -n 1"
</pre></code>
I hope this is a usefull tip.
