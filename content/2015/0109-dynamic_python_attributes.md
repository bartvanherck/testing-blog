title: Dynamic attributes in Python
date: 2015-01-09 18:01:20
tags: python
category: testing
featured: https://farm4.staticflickr.com/3924/14895038696_6988e18b1e_o.jpg
summary: I needed a decent library for my needs, so I wrote them for myself. For that I wanted to have code that looks simple and is easy to use.

I must test some json rpc code. But the libraries I wanted to use did not fulfilled my needs. So time to write my own. There must be a json output like this:
<code class="text"><pre>{
  "method": "my_group.my_plugin.my_method",
  "params": [ 1, 2]
}
</pre></code>
The methods or functions are located inside a plugin. A plugin is located in a group. The parameters are variable too. I wanted to write code in python that looks like this:<code class="python"><pre>my_group.my_plugin.my_method(1,2)</pre></code>
This means that the attributes must be variable. 

I use the getattr function and the call function for this. When an attribute is asked, the getattr function is called. First I tried it with one attribute in one level. Create an instance of class MyRpc and call a attribute that is not yet part of the class.
<code class="python"><pre>A=MyRpc()
A.my_group
</pre></code>
When this code is executed, then the getattr function is called, so it must be implemented. I stored the name of this property in a list, because when a new property is asked, we must know the name of our parent.
<code><pre>class MyRpc(object):
    def \_\_init\_\_(self):
        self.\_\_name = list()
    def \_\_getattr\_\_(self, name):
        self.\_\_name.append(name)
        return self</pre></code>
With this code it is possible to ask endless attributes.
<code class="python"><pre>A=MyRpc()
A.my_group.my_plugin.my_method
</pre></code>
Now we can make a function of it. A function is callable, so make the latest object that we created callable with the call function.
<code><pre>class MyRpc(object):
    def \_\_init\_\_(self):
        self.\_\_name = list()
    def \_\_getattr\_\_(self, name):
        self.\_\_name.append(name)
        return self
    def \_\_call\_\_(self, *args):
        return self.\_\_make\_json\_rpc(args)
    def \_\_make\_json\_rpc(self, params):
        return { 
                   "params": params,
                   "method": self.\_\_method\_name()
               }
    def \_\_method\_name(self):
        return ".".join(self.\_\_name)</pre></code>
The call function, just creates the json and fills in the parameters and the method name. The method name is very simple, because we stored the values already in our list. We can just use the join function to create a correct name.
