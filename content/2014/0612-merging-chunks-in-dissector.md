title: Merging chunks in a dissector
date: 2014-06-12 15:07:00
tags: lua wireshark
category: testing
Summary: In the previous post, I created a basic dissector. It handles all packets one by one and checks them. The problem there is that sometimes it is possible that a packet is to large to fit in one tcp packet. In that case, 

In the previous post, I created a basic dissector. It handles all packets one by one and checks them. The problem there is that sometimes it is possible that a packet is to large to fit in one tcp packet. In that case, the packet is splitted into multiple chunks. For this a dissector has a solution that is a no-brainer.

If we know how many bytes a message contains, it is possible to set the desegment_len field in the pinfo to the value the message still needs. It is also possible thatthe number of bytes is unknown. For that a constant is defined, DESEGMENT_ONE_MORE_SEGMENT

<code class="lua"><pre>
-- The dissector
p_myproto = Proto ("myproto","My Protocol")

function p_myproto.dissector(buffer, pinfo, tree)
    if buffer:len() == 0 then return end
    pinfo.cols.protocol = "myprotocol"
  
    -- SizeOfTheMessage retuns the size of the message that is received
    if buffer:len() == sizeOfTheMessage(buffer) then
        -- The real dissector is in another function to have more readable code
         dissect_message(buffer, pinfo, tree)
    else
        pinfo.desegment_len = DESEGMENT_ONE_MORE_SEGMENT
    end
end
</pre></code>

As you can see, just setting desegment_len to DESEGMENT_ONE_MORE_SEGMENT will hold the buffer and appends the next packet to this buffer. In this case, the different packets are merged into one.

