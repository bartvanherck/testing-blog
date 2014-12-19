title: wireshark dissector in lua
date: 2014-05-23 07:48:16
tags: lua, wireshark
category: testing
summary: As a tester, sometimes we need to have a look at network traffic. For this, there is a nice tool, called wireshark. To analyse, the application can show the internals of several packets. It even can have a look into the content of a tcp-ip packet. 


As a tester, sometimes we need to have a look at network traffic. For this, there is a nice tool, called [wireshark](http://www.wireshark.org). To analyse, the application can show the internals of several packets. It even can have a look into the content of a tcp-ip packet. For some internals as there is json, it also parses that protocol. The advantage is that we do not have to look at raw data anymore.

If you have a custom protocol you have to analyse the raw data. This is in most cases a very huge effort. Therefore it is possible to create what they call dissectors in wireshark. With a dissector, the protocol can be parsed by wireshark for you. It is possible to create some prototype dissectors in lua. Lets have a look at an example:


    -- create myproto protocol and its fields
    p_myproto = Proto ("myproto","My Protocol")
    local f_command = ProtoField.uint16("myproto.command", "Command", base.HEX)
    local f_data = ProtoField.string("myproto.data", "Data", FT_STRING)
     
    p_myproto.fields = {f_command}
     
    -- myproto dissector function
    function p_myproto.dissector (buf, pkt, root)
      -- validate packet length is adequate, otherwise quit
      if buf:len() == 0 then return end
      pkt.cols.protocol = p_myproto.name
     
      -- create subtree for myproto
      subtree = root:add(p_myproto, buf(0))
      -- add protocol fields to subtree
      subtree:add(f_command, buf(0,2)):append_text(" [Command text]")
     
      -- description of payload
      subtree:append_text(", Command details here or in the tree below")
    end
     
    -- Initialization routine
    function p_myproto.init()
    end
     
    -- register a chained dissector for port 8002
    local tcp_dissector_table = DissectorTable.get("tcp.port")
    dissector = tcp_dissector_table:get_dissector(8002)
      -- you can call dissector from function p_myproto.dissector above
      -- so that the previous dissector gets called
    tcp_dissector_table:add(8002, p_myproto)


**Running the lua script**

Here are the steps required to get the above code running. 

- Edit and save the lua script above to any folder (e.g. c:\myproto) and cal the file myproto.lua
- Open init.lua in the Wireshark installation directory for editing. 
- Add the following lines to init.lua (at the very end):
<pre>
    MYPROTO_SCRIPT_PATH="C:\\myproto\\"
    dofile(MYPROTO_SCRIPT_PATH.."myproto.lua")
</pre>
- Change MYPROTO_SCRIPT_PATH to point to the folder where you saved the script in step 1
- Run Wireshark
- Load a capture file that has the packets of your custom protocol or start a live capture

Now the packets are parsed by wireshark.

