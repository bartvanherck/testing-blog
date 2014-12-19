title: angularjs
tags: javascript, nodejs
date: 2014-03-17 18:37:00
category:  testing
summary: I do need to test a new web application that our team is going to write in AngularJS. To start the project, first a kind of environment has to be prepared. [AngularJS](http://angularjs.org/) is a kind of javascript library written by the people of Google if I am correct.


I do need to test a new web application that our team is going to write in AngularJS. To start the project, first a kind of environment has to be prepared. [AngularJS](http://angularjs.org/) is a kind of javascript library written by the people of Google if I am correct.
<div style="float: left">
<img src="http://2.bp.blogspot.com/-nYyfDCzuVvs/UycybvgN1KI/AAAAAAAAAMY/nJ39O14QUYM/s1600/node.JS.png" style="margin: 0px 20px;" />
</div>

There are several tools that we use together with this javascript library. This for making our live easier. We have [grunt](http://gruntjs.com/), [karma](http://karma-runner.github.io/0.10/index.html), [yeoman](http://yeoman.io/), [protractor](https://github.com/angular/protractor) and a lot of more.

Because some of the tools are written as a Node.js application, there is a need to install that Node.js and also the package manager of node.js Because I do not want to install the complete application, I downloaded the binary or executable of node.js and placed that in a file. Afterwards I created a script that changes my PATH variable to the location the node.js binary is located. With that script, I can now use node.js as it was installed.

But the advantage I encounter here is that I can now place my environment in version control and share it with my colleagues or with our build server. If there is a need to install something globally, it is just installed in the directory where node.js is located. Simple and we can not have fun with our project.
