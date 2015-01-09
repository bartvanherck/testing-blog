title: A new year
date: 2015-01-09 18:01:20
tags: python
category: testing
summary: Dynamic attributes
featured: https://farm4.staticflickr.com/3924/14895038696_6988e18b1e_o.jpg

I must test some json rpc code. But the libraries I wanted to use did not fulfilled my needs. So time to write my own. There must be a json output like this:

<code class="json"><pre>{
  "method": "my_group.my_plugin.my_method",
  "params": [ 1, 2]
}
</pre></code>
The methods or functions are located inside a plugin. A plugin is located in a group. The parameters are variable too. I wanted to write code in python that looks like this:
<code class="python"><pre>my_group.my_plugin.my_method(1,2)</pre></code>
This means that the attributes must be variable. 

I use the __getattr__ function and the __call__ function for this. When an attribute is asked, the __getattr_ function is called. First I tried it with one attribute in one level. Create an instance of class MyRpc and call a attribute that is not yet part of the class.
<code class="python"><pre>A=MyRpc()
A.my_group
</pre></code>
When this code is executed, then the __getattr__ function is called, so it must be implemented. I stored the name of this property in a list, because when a new property is asked, we must know the name of our parent.
<code class="python"><pre>class MyRpc(object):
    def __init__(self):
        self.__name = list()

    def __getattr__(self, name):
        self.__name.append(name)
        return self
</pre></code>
With this code it is possible to ask endless attributes.
<code class="python"><pre>A=MyRpc()
A.my_group.my_plugin.my_method
</pre></code>
Now we can make a function of it. A function is callable, so make the latest object that we created callable with the __call__ function.
<code class="python"><pre>class MyRpc(object):
    def __init__(self):
        self.__name = list()

    def __getattr__(self, name):
        self.__name.append(name)
        return self

    def __call__(self, *args):
        return self.__make_json_rpc(args)

    def __make_json_rpc(self, params):
        return { 
                   "params": params,
                   "method": self.__method_name()
               }

    def __method_name(self):
        return ".".join(self.__name)
</pre></code>

The call function, just creates the json and fills in the parameters and the method name. The method name is very simple, because we stored the values already in our list. We can just use the join function to create a correct name.
