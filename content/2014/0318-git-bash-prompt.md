title: git bash prompt
tags: git
date: 2014-03-18 19:33:00
category: version control
Summary: Even as a tester, we need version control systems. At this moment, personally I use git. When installing git on windows, there is in the shell tab completion as default. This is a nice feature that I wanted to have on all my systems, say it to be mac and linux.


Even as a tester, we need version control systems. At this moment, personally I use git. When installing git on windows, there is in the shell tab completion as default. This is a nice feature that I wanted to have on all my systems, say it to be mac and linux.

I did not had to implement that for myself, because of course it already exist. I did follow a procedure that I explain below. If my command prompt enters a repository, the prompt changes as follows:

<code class="bash"><pre>
[user@localhost projectdir (master)]$
</pre></code>


While rebasing or during a merge process the promtp changes too. Very handy according to me.

<code class="bash"><pre>
[user@localhost projectdir (master|REBASE-i)]$
</pre></code>

To have this nice feature, it is simple. Download some scripts from the net and place the files in a directory on your system. The files itself can be found at following locations:

* [https://raw.github.com/git/git/master/contrib/completion/git-completion.bash](https://raw.github.com/git/git/master/contrib/completion/git-completion.bash)
* [https://raw.github.com/git/git/master/contrib/completion/git-prompt.sh](https://raw.github.com/git/git/master/contrib/completion/git-prompt.sh)

I placed the files in a directory ~/.bash_files on my system. After that, in my ~/.bashrc file (or ~/.bash_profile on my mac) I entered the following commands somewhere at the bottom:

<code class="bash"><pre>
$ source ~/.bash_files/git-completion.sh
$ source ~/.bash_files/git-prompt.sh
$ export PS1='[\u@\h \W$(__git_ps1 " (%s)")]\$ '
</pre></code>

If you followed these instructions, you have tab completion inside your git repositories. Its very nice and handy, that tab key.
