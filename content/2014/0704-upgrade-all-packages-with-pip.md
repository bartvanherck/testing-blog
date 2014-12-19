title: Upgrade all packages with pip
tags: windows
Category: python
date: 2014-07-04 21:00:00
Summary: At some time, after installing some python packages, they becomes outdated, because there are new versions available. To upgrade a package it is very simple.

At some time, after installing some python packages, they becomes outdated, because there are new versions available. To upgrade a package it is very simple:

<code class="bash"><pre>
pip install -U <package_name>
</pre></code>

But what if we do not know what packages are needed for upgrade, or we have to many packages to upgrade? Sometimes, we want to upgrade all packages at once. Unfortunately pip does not have an upgrade all option. But we can make use of the pip freeze command. This lists all packages with the version number. This means that we must do a little command line trick.

At linux or in a unix environment it is simple:

<code class="bash"><pre>
pip freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs pip install -U
</pre></code>

In windows however, we use the following:

<code class="bash"><pre>
for /F "delims===" %i in ('pip freeze -l') do pip install -U %i
</pre></code>

This is my tip of today.
