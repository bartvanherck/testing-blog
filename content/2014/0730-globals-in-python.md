title: globals in python
date: 2014-07-30 17:58:07
category: python
Summary: Today I am going to have some coding fun as I will call it. The following code was written by me. For the simplicity I just create messages with two characters. A message id character and an optional character.

Today I am going to have some coding fun as I will call it. The following code was written by me. For the simplicity I just create messages with two characters. A message id character and an optional character.

<code class="python"><pre>
class Message(object):
    def __init__(self):
        self.__data = ""
        self.__valid = False

    @property
    def data(self):
        return self.message_id + self.__data

    @data.setter
    def data(self, input):
        if input[0] == self.message_id:
            self.__data = input[1:]
            self.__valid = True
        else:
            self.__valid = False


    @property 
    def valid(self):
        return self.__valid


class MsgRead(Message):
    def __init__(self):
        super(MsgRead, self).__init__()
        self.message_id = "1"


class MsgWrite(Message):
    def __init__(self):
        super(MsgWrite, self).__init__()
        self.message_id = "2"


class GenerateMessage(object):
    @staticmethod
    def create_write(data):
        msg = MsgWrite()
        msg.data = data
        return msg

    @staticmethod
    def create_read(data):
        msg = MsgRead()
        msg.data = data
        return msg

    @staticmethod
    def gen_message(data):
        msg = GenerateMessage.create_read(data)
        if msg.valid:
            return msg
        msg = GenerateMessage.create_write(data)
        if msg.valid:
            return msg

    @staticmethod
    def generate(data):
        msg = GenerateMessage.gen_message(data)
        return msg

g = GenerateMessage()
a = g.generate("1a")
print type(a)
b = g.generate("2b")
print type(b)
</pre></code>

As you can see, there is in the GenerateMessage class more or less duplicated code. Because I do not have only 2 messages, but more than 20, this class will become very large and difficult to maintain lateron. So For this I think I should write the code in a different way. I discovered that the **globals** function will return all objects that the interpreter knows about. It is a dict that represents the current global symbol table. Maybe we can make use of that? And indeed I rewrote my generate function as follows:

<code class="python"><pre>
class GenerateMessage(object):
    @staticmethod
    def create_message_with_name(name, data):
        msg = globals\(\)\[name\]\(\)
        msg.data = data
        return msg

    @staticmethod
    def gen_message(data):
        msg = GenerateMessage.create_message_with_name("MsgRead", data)
        if msg.valid:
            return msg
        msg = GenerateMessage.create_message_with_name("MsgWrite", data)
        if msg.valid:
            return msg
        return None

    @staticmethod
    def generate(data):
        msg = GenerateMessage.gen_message(data)
        return msg
</pre></code>

Now we do not have the enormous bunch of functions anymore. Now the **globals** function will return a dict with all functions that are in the symbol table. Take the name of the class we want to instantiate. And create the wanted class. Is is all in one line, but can be broken into several lines. For me this is readable, so I leave it in one line.
The next thing I would have to get rid of is all the if statements. Can it not be done with a for loop or a list comprehension with a filter ? The list comprehension is not that good I think, because if I have thousands of messages, it will create each time we want to create one message all the messages and that is not the intention. So a for loop that will be stopped if the message is valid will do in this case. Lets have a look at the code:

<code class="python"><pre>
class GenerateMessage(object):
    @staticmethod
    def create_message_with_name(name, data):
        msg = globals\(\)\[name\]\(\)
        msg.data = data
        return msg

    @staticmethod
    def gen_message(data):
        for name in ["MsgWrite", "MsgRead"]:
            msg = GenerateMessage.create_message_with_name(name, data)
            if msg.valid:
                return msg
        return None

    @staticmethod
    def generate(data):
        msg = GenerateMessage.gen_message(data)
        return msg
</pre></code>

This looks a lot simpler, not? Now we use a list with the message names and pass that through a for loop. In case we have a match, the function is returned with the message.
