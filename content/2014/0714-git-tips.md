title: Several git tips
date: 2014-07-14 18:32:00
category: version control
tags: git
Summary: Some nice git tips. What to do if a stash is deleted, or to fast switch between branches. You all can read it in the article of the day.

**Retrieve a deleted stash**

If you delete the stash per accident, and did not want it to be deleted, is is possible to retrieve if it was done recently and the garbage collector was not active yet.
First list all unreachable commits.

<code class="bash"><pre>
$ git stash drop 
Dropped refs/stash@{0} (1392dfcd6418f5b7cb009c24416630597add918f)

$ git fsck --unreachable
Checking object directories: 100% (256/256), done.
unreachable blob 2762d40c58c9ab3601529eb9bbf35f873be605c2
unreachable commit 11d01fc547c3438e24c06ae9a18828e5eaa0b02e
unreachable commit 1392dfcd6418f5b7cb009c24416630597add918f
</pre></code>


This will show you all the commits which are not reachable by a branch or tag and which haven't been garbage collected yet. Look for the ones that say *unreachable commit*, ignore the blobs. The chances are it will be the one closest the top, unless you've performed some other actions which created more unreachables. 

You can examine the commits by doing 'git show <sha>', and this should identify the stash, it'll probably be called 'On master: <your comment>' or similar. Once you've found it, copy the SHA.

To recover this you then do:

<code class="bash"><pre>
$ git show e9fed4e0950aae7ae2943ad0121d2668bd151dbf
</pre></code>

This shows the diff we needed

<code class="bash"><pre>
$ git stash apply e9fed4e0950aae7ae2943ad0121d2668bd151dbf
</pre></code>

Which will bring it back into your working copy.


**Switching branches**

In bash, the command cd - switches to the last directory you were in. You can do the same thing with git to switch to the last branch you were on with **git checkout -**.


<code class="bash"><pre>
$ git checkout -b b1
Switched to a new branch 'b1'

$ git checkout -
Switched to branch 'master'

$ git checkout -
Switched to branch 'b1'
</pre></code>

