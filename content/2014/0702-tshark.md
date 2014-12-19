title: tshark
date: 2014-07-02 22:02:01
tags: wireshark
category: testing
Summary: Sometimes in very large traces, it is better to put analysed data in a file, so that that can be opened in a normal text editor. There is where the command tshark becomes a handy tool. The command tshark is normally installed together

Sometimes in very large traces, it is better to put analysed data in a file, so that that can be opened in a normal text editor. There is where the command tshark becomes a handy tool. The command tshark is normally installed together with the wireshark installation. 

I created a dissector for a protocol that I named lb. With tshark, I can filter out all these values in one go.

<code class="bash"><pre>
tshark -2 -R lb -O lb -r myTrace.pcapng > completePipeline.txt
</pre></code>

Here I show all fields of the lb protocol because the option -O is given. This gives a more verbosy output as the normal. Normally only the values that are in the main widget in wireshark are shown. For example:

<code class="bash"><pre>
1   0.001375 172.16.2.185 -> 172.16.2.192 LB 66 Packet ID fcfffc (16580604)
2   0.001483 172.16.2.192 -> 172.16.2.185 LB 66 Packet ID fcfffc (16580604) - Read from 4246 (16966)
3   0.002435 172.16.2.185 -> 172.16.2.192 LB 66 Packet ID fcfffd (16580605)
4   0.002539 172.16.2.192 -> 172.16.2.185 LB 66 Packet ID fcfffd (16580605) - Read from 4247 (16967)
</pre></code>

But with the -O option, suddenly the protocol that was asked for is parsed and displayed on the standard output or in a file, depending if the stdout is redirected to a file or not.

<code class="bash"><pre>
Frame 1: 66 bytes on wire (528 bits), 66 bytes captured (528 bits)
Ethernet II, Src: Hewlett-_18:23:4d (00:22:64:18:23:4d), Dst: Titech_00:0e:d3 (00:2d:76:00:0e:d3)
Internet Protocol Version 4, Src: 172.16.2.185 (172.16.2.185), Dst: 172.16.2.192 (172.16.2.192)
Transmission Control Protocol, Src Port: 54875 (54875), Dst Port: 50001 (50001), Seq: 1, Ack: 4294967285, Len: 12
LB Packet
    ID: 0x00fcfffc (16580604)
    WordSize: 0x0003 (3)
    Command: Read (1)
    Address: 0x00004246 (16966)

Frame 2: 66 bytes on wire (528 bits), 66 bytes captured (528 bits)
Ethernet II, Src: Titech_00:0e:d3 (00:2d:76:00:0e:d3), Dst: Hewlett-_18:23:4d (00:22:64:18:23:4d)
Internet Protocol Version 4, Src: 172.16.2.192 (172.16.2.192), Dst: 172.16.2.185 (172.16.2.185)
Transmission Control Protocol, Src Port: 50001 (50001), Dst Port: 54875 (54875), Seq: 4294967285, Ack: 13, Len: 12
LB Packet
    ID: 0x00fcfffc (16580604)
    WordSize: 0x0003 (3)
    Command: reply (0)
    Read Data: 0x00010000 (65536)
</pre></code>
